"""Hearts of Iron IV - Localization Installer Core Engine.
Handles automatic detection, DLC scanning, version checking, Dowser configuration,
and atomic file deployment.
"""

import os
import sys
import json
import re
import shutil
import datetime
from pathlib import Path

try:
    import winreg
except ImportError:
    winreg = None

from app.dlc_db import get_dlc_display_info

RECOMMENDED_RAW_VERSION = "1.19.3.0"
RECOMMENDED_VERSION_PREFIX = "1.19."


def get_resource_dir() -> Path:
    """Returns the base path for assets/payload, compatible with PyInstaller bundles."""
    if hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    # When running from source repository
    base = Path(__file__).resolve().parent.parent
    return base


def get_source_localisation_dir() -> Path:
    """Locate source localisation/braz_por directory containing the 208 translation files."""
    resource_dir = get_resource_dir()
    candidate = resource_dir / "localisation" / "braz_por"
    if candidate.exists() and any(candidate.glob("*.yml")):
        return candidate

    # Fallback search
    for test_path in [
        Path.cwd() / "localisation" / "braz_por",
        Path(__file__).resolve().parent.parent / "localisation" / "braz_por",
    ]:
        if test_path.exists() and any(test_path.glob("*.yml")):
            return test_path

    raise FileNotFoundError(f"Folder sumber terjemahan tidak ditemukan di: {candidate}")


def get_source_languages_file() -> Path:
    """Locate source languages.yml file."""
    resource_dir = get_resource_dir()
    candidate = resource_dir / "localisation" / "languages.yml"
    if candidate.exists():
        return candidate

    for test_path in [
        Path.cwd() / "localisation" / "languages.yml",
        Path(__file__).resolve().parent.parent / "localisation" / "languages.yml",
    ]:
        if test_path.exists():
            return test_path

    raise FileNotFoundError(f"File languages.yml tidak ditemukan di: {candidate}")


def validate_hoi4_dir(path: Path | str) -> tuple[bool, str]:
    """Validates if the specified directory is a valid Hearts of Iron IV installation."""
    p = Path(path)
    if not p.exists() or not p.is_dir():
        return False, "Folder tidak ditemukan atau bukan merupakan direktori."

    has_exe = (p / "hoi4.exe").exists() or (p / "hoi4").exists()
    has_launcher = (p / "launcher-settings.json").exists()
    has_dlc = (p / "dlc").exists()
    has_loc = (p / "localisation").exists()

    if has_exe or (has_launcher and (has_dlc or has_loc)):
        return True, "Folder instalasi Hearts of Iron IV valid."

    return False, "Folder tidak memiliki file 'hoi4.exe' atau 'launcher-settings.json'."


def find_steam_library_folders() -> list[Path]:
    """Discovers all Steam library folders by parsing libraryfolders.vdf."""
    discovered = []
    if not winreg:
        return discovered

    steam_path = None
    for root in (winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE):
        for sub in (r"SOFTWARE\Valve\Steam", r"SOFTWARE\WOW6432Node\Valve\Steam"):
            try:
                with winreg.OpenKey(root, sub) as key:
                    val, _ = winreg.QueryValueEx(key, "SteamPath")
                    if val and os.path.exists(val):
                        steam_path = Path(val)
                        break
            except Exception:
                pass
        if steam_path:
            break

    # Check default 64-bit and 32-bit Program Files if not in registry
    if not steam_path:
        for default_p in [
            Path(r"C:\Program Files (x86)\Steam"),
            Path(r"C:\Program Files\Steam"),
        ]:
            if default_p.exists():
                steam_path = default_p
                break

    if not steam_path or not steam_path.exists():
        return discovered

    discovered.append(steam_path)

    vdf_file = steam_path / "steamapps" / "libraryfolders.vdf"
    if vdf_file.exists():
        try:
            with open(vdf_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            # Match "path" "\path\to\library"
            paths = re.findall(r'"path"\s+"([^"]+)"', content)
            for p in paths:
                clean_p = Path(p.replace(r"\\", "\\"))
                if clean_p.exists() and clean_p not in discovered:
                    discovered.append(clean_p)
        except Exception:
            pass

    return discovered


def find_hoi4_install_paths() -> list[Path]:
    """Automatically scans registry, Steam libraries, and common directories to locate HOI4."""
    candidates = []

    # 1. Windows Registry uninstall entries for Steam App 394360
    if winreg:
        reg_keys = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 394360",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\Steam App 394360",
        ]
        for rk in reg_keys:
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, rk) as key:
                    val, _ = winreg.QueryValueEx(key, "InstallLocation")
                    if val and os.path.exists(val):
                        p = Path(val)
                        is_valid, _ = validate_hoi4_dir(p)
                        if is_valid and p not in candidates:
                            candidates.append(p)
            except Exception:
                pass

    # 2. Parse Steam library folders
    steam_libraries = find_steam_library_folders()
    for lib in steam_libraries:
        test_path = lib / "steamapps" / "common" / "Hearts of Iron IV"
        is_valid, _ = validate_hoi4_dir(test_path)
        if is_valid and test_path not in candidates:
            candidates.append(test_path)

    # 3. Common fixed drives & folder paths
    common_paths = [
        Path(r"F:\Apps\Hearts_of_Iron_IV\Hearts of Iron IV"),
        Path(r"D:\Games\Hearts of Iron IV"),
        Path(r"E:\Games\Hearts of Iron IV"),
        Path(r"F:\Games\Hearts of Iron IV"),
        Path(r"C:\Games\Hearts of Iron IV"),
        Path(r"C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV"),
        Path(r"D:\SteamLibrary\steamapps\common\Hearts of Iron IV"),
        Path(r"E:\SteamLibrary\steamapps\common\Hearts of Iron IV"),
        Path(r"F:\SteamLibrary\steamapps\common\Hearts of Iron IV"),
        Path(r"G:\SteamLibrary\steamapps\common\Hearts of Iron IV"),
    ]

    # Also check all available Windows drive letters
    drives = [f"{chr(d)}:\\" for d in range(ord("C"), ord("Z") + 1) if os.path.exists(f"{chr(d)}:\\")]
    for d in drives:
        for sub in [
            r"SteamLibrary\steamapps\common\Hearts of Iron IV",
            r"Games\Hearts of Iron IV",
            r"Apps\Hearts of Iron IV",
            r"Hearts of Iron IV",
        ]:
            common_paths.append(Path(d) / sub)

    for cp in common_paths:
        if cp.exists():
            is_valid, _ = validate_hoi4_dir(cp)
            if is_valid and cp not in candidates:
                candidates.append(cp)

    # 4. Check if current running working directory is inside or at HOI4
    cwd = Path.cwd()
    if validate_hoi4_dir(cwd)[0] and cwd not in candidates:
        candidates.append(cwd)
    if validate_hoi4_dir(cwd.parent)[0] and cwd.parent not in candidates:
        candidates.append(cwd.parent)

    return candidates


def get_game_version(game_path: Path | str) -> dict:
    """Extracts and evaluates the Hearts of Iron IV version and compatibility."""
    p = Path(game_path)
    launcher_file = p / "launcher-settings.json"

    raw_version = ""
    version_display = ""
    is_compatible = False
    warning = ""

    if launcher_file.exists():
        try:
            with open(launcher_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            raw_version = data.get("rawVersion", "").strip()
            version_display = data.get("version", "").strip()
        except Exception as e:
            version_display = f"Gagal membaca versi: {e}"

    if not raw_version and not version_display:
        raw_version = "Tidak Diketahui"
        version_display = "Versi Game Tidak Terdeteksi"
        warning = (
            "Peringatan: launcher-settings.json tidak ditemukan. "
            "Kemungkinan versi game berbeda dari versi rekomendasi (1.19.3.0). "
            "Pemasangan tetap dapat dilanjutkan, namun beberapa konten baru mungkin tidak terjemahkan."
        )
        return {
            "raw_version": raw_version,
            "version_display": version_display,
            "is_compatible": False,
            "warning": warning,
        }

    # Check compatibility
    # Baseline tested version is 1.19.3.0
    if raw_version.startswith("1.19.3"):
        is_compatible = True
        warning = ""
    elif raw_version.startswith(RECOMMENDED_VERSION_PREFIX):
        is_compatible = True
        warning = (
            f"Info: Versi terdeteksi ({raw_version}) berada dalam seri 1.19.x. "
            "Terjemahan sepenuhnya dapat dimainkan."
        )
    else:
        is_compatible = False
        warning = (
            f"Peringatan: Versi game yang terdeteksi ({raw_version or version_display}) "
            f"berbeda dari versi yang diuji ({RECOMMENDED_RAW_VERSION}). "
            "Kemungkinan beberapa file atau konten baru tidak terjemahkan."
        )

    return {
        "raw_version": raw_version,
        "version_display": version_display or raw_version,
        "is_compatible": is_compatible,
        "warning": warning,
    }


def scan_dlcs(game_path: Path | str) -> list[dict]:
    """Scans the target game's dlc/ directory, reads metadata, and returns enriched DLC list."""
    p = Path(game_path)
    dlc_dir = p / "dlc"
    if not dlc_dir.exists() or not dlc_dir.is_dir():
        return []

    results = []
    # Scan subdirectories under dlc/
    for item in sorted(dlc_dir.iterdir()):
        if not item.is_dir():
            continue

        dlc_id = item.name
        parsed_name = ""
        parsed_category = ""
        steam_id = ""

        # Search for .dlc metadata file inside directory
        dlc_files = list(item.glob("*.dlc"))
        if dlc_files:
            try:
                with open(dlc_files[0], "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
                m_name = re.search(r'name\s*=\s*"([^"]+)"', content)
                if m_name:
                    parsed_name = m_name.group(1)
                m_cat = re.search(r'category\s*=\s*"([^"]+)"', content)
                if m_cat:
                    parsed_category = m_cat.group(1)
                m_sid = re.search(r'steam_id\s*=\s*"([^"]+)"', content)
                if m_sid:
                    steam_id = m_sid.group(1)
            except Exception:
                pass

        info = get_dlc_display_info(dlc_id, parsed_name, parsed_category)
        info["path"] = str(item)
        info["steam_id"] = steam_id
        results.append(info)

    return results


def patch_dowser_settings_layout(game_path: Path | str) -> tuple[bool, str]:
    """Configures settings-layout.json so Paradox Dowser Launcher displays 'Bahasa Indonesia'."""
    p = Path(game_path)
    layout_file = p / "settings-layout.json"
    if not layout_file.exists():
        return False, "File settings-layout.json tidak ditemukan."

    backup_file = p / "settings-layout.json.bak"
    if not backup_file.exists():
        try:
            shutil.copy2(layout_file, backup_file)
        except Exception as e:
            return False, f"Gagal membuat cadangan settings-layout.json: {e}"

    try:
        with open(layout_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Look for System -> language setting
        patched = False
        if isinstance(data, list):
            for section in data:
                if section.get("category") == "System" or section.get("label") == "System":
                    for setting in section.get("settings", []):
                        if setting.get("name") == "language":
                            options = setting.get("options", [])
                            # Find braz_por option
                            found = False
                            for opt in options:
                                if opt.get("value") == "l_braz_por":
                                    opt["label"] = "Bahasa Indonesia"
                                    opt["valueIso639-1"] = "id"
                                    found = True
                                    patched = True
                                    break
                            if not found:
                                options.insert(1, {
                                    "label": "Bahasa Indonesia",
                                    "value": "l_braz_por",
                                    "valueIso639-1": "id",
                                })
                                patched = True
                            break

        if patched:
            with open(layout_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True, "Berhasil memperbarui settings-layout.json untuk launcher Dowser."
        return False, "Pengaturan 'language' tidak ditemukan di settings-layout.json."

    except Exception as e:
        return False, f"Terjadi kesalahan saat memodifikasi settings-layout.json: {e}"


def patch_user_documents_settings() -> tuple[bool, str]:
    """Updates game documents settings (settings.txt & pdx_settings.txt) to activate Indonesian."""
    user_docs = Path(os.environ.get("USERPROFILE", "")) / "Documents" / "Paradox Interactive" / "Hearts of Iron IV"
    if not user_docs.exists():
        return False, "Folder dokumen pengguna HOI4 tidak ditemukan (belum pernah dijalankan)."

    messages = []
    # 1. Update settings.txt
    settings_file = user_docs / "settings.txt"
    if settings_file.exists():
        try:
            with open(settings_file, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            if re.search(r'language\s*=\s*"[^"]*"', content):
                new_content = re.sub(r'language\s*=\s*"[^"]*"', 'language="l_braz_por"', content)
            else:
                new_content = 'language="l_braz_por"\n' + content

            with open(settings_file, "w", encoding="utf-8") as f:
                f.write(new_content)
            messages.append("settings.txt diperbarui.")
        except Exception as e:
            messages.append(f"Gagal memperbarui settings.txt: {e}")

    # 2. Update pdx_settings.txt
    pdx_file = user_docs / "pdx_settings.txt"
    if pdx_file.exists():
        try:
            with open(pdx_file, "r", encoding="utf-8", errors="ignore") as f:
                pdx_content = f.read()

            if '"System"={' in pdx_content and '"language"={' in pdx_content:
                # Update existing value inside language block
                pdx_new = re.sub(
                    r'("System"=\{[\s\S]*?"language"=\{[\s\S]*?value=)"[^"]*"',
                    r'\1"l_braz_por"',
                    pdx_content,
                )
            else:
                # Append System language block
                sys_block = '\n"System"={\n\t"language"={\n\t\tvalue="l_braz_por"\n\t\tversion=0\n\t}\n}\n'
                pdx_new = pdx_content + sys_block

            with open(pdx_file, "w", encoding="utf-8") as f:
                f.write(pdx_new)
            messages.append("pdx_settings.txt diperbarui.")
        except Exception as e:
            messages.append(f"Gagal memperbarui pdx_settings.txt: {e}")

    return True, ", ".join(messages) if messages else "Pengaturan dokumen HOI4 telah disetel."


def install_translations(
    game_path: Path | str,
    backup: bool = True,
    patch_launcher: bool = True,
    patch_user_doc: bool = True,
    progress_cb=None,
    log_cb=None,
) -> dict:
    """Copies all 208 translation files and languages.yml into the HOI4 game directory with UTF-8 BOM."""
    def log(level: str, msg: str):
        if log_cb:
            log_cb(level, msg)

    def progress(current: int, total: int, filename: str):
        if progress_cb:
            progress_cb(current, total, filename)

    p = Path(game_path)
    is_valid, val_msg = validate_hoi4_dir(p)
    if not is_valid:
        raise ValueError(f"Direktori HOI4 tidak valid: {val_msg}")

    source_dir = get_source_localisation_dir()
    source_files = sorted(list(source_dir.glob("*.yml")))
    if not source_files:
        raise FileNotFoundError("Tidak ada file terjemahan .yml di folder sumber!")

    total_files = len(source_files)
    target_loc_dir = p / "localisation"
    target_braz_por = target_loc_dir / "braz_por"

    log("INFO", f"Memulai pemasangan {total_files} file terjemahan Bahasa Indonesia...")

    # 1. Backup existing files if requested
    backup_path = None
    if backup and target_braz_por.exists():
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = target_loc_dir / f"braz_por_backup_{timestamp}"
        log("INFO", f"Membuat cadangan folder bahasa ke: {backup_path.name}")
        try:
            shutil.copytree(target_braz_por, backup_path)
            log("SUCCESS", f"Cadangan berhasil dibuat di {backup_path.name}")
        except Exception as e:
            log("WARNING", f"Peringatan: Gagal membuat cadangan: {e}")

    # Ensure target directory exists
    target_braz_por.mkdir(parents=True, exist_ok=True)

    # 2. Copy all .yml files ensuring UTF-8 BOM
    copied_count = 0
    utf8_bom = b"\xef\xbb\xbf"

    for idx, src_file in enumerate(source_files, start=1):
        target_file = target_braz_por / src_file.name
        try:
            with open(src_file, "rb") as rf:
                raw_bytes = rf.read()

            # Ensure UTF-8 BOM header
            if not raw_bytes.startswith(utf8_bom):
                raw_bytes = utf8_bom + raw_bytes

            with open(target_file, "wb") as wf:
                wf.write(raw_bytes)

            copied_count += 1
            progress(idx, total_files, src_file.name)
        except Exception as e:
            log("ERROR", f"Gagal menyalin {src_file.name}: {e}")

    log("SUCCESS", f"Berhasil menyalin {copied_count}/{total_files} file dengan format UTF-8 BOM.")

    # 3. Copy languages.yml
    try:
        src_lang = get_source_languages_file()
        target_lang = target_loc_dir / "languages.yml"
        shutil.copy2(src_lang, target_lang)
        log("SUCCESS", "Berhasil menyalin languages.yml (Bahasa Indonesia terdaftar di antarmuka game).")
    except Exception as e:
        log("WARNING", f"Peringatan: Gagal menyalin languages.yml: {e}")

    # 4. Patch Dowser / Launcher
    if patch_launcher:
        suc, msg = patch_dowser_settings_layout(p)
        if suc:
            log("SUCCESS", msg)
        else:
            log("WARNING", msg)

    # 5. Patch User Documents Settings
    if patch_user_doc:
        suc, msg = patch_user_documents_settings()
        if suc:
            log("SUCCESS", msg)
        else:
            log("INFO", msg)

    return {
        "success": True,
        "copied": copied_count,
        "total": total_files,
        "backup_path": str(backup_path) if backup_path else None,
    }


def restore_backup(game_path: Path | str, log_cb=None) -> tuple[bool, str]:
    """Restores the latest backup of braz_por and reverts settings-layout.json."""
    def log(level: str, msg: str):
        if log_cb:
            log_cb(level, msg)

    p = Path(game_path)
    target_loc_dir = p / "localisation"
    target_braz_por = target_loc_dir / "braz_por"

    # Search for latest backup
    backups = sorted(list(target_loc_dir.glob("braz_por_backup_*")), reverse=True)
    if not backups:
        msg = "Tidak ditemukan folder cadangan braz_por_backup_* di dalam direktori localisation/."
        log("WARNING", msg)
        return False, msg

    latest_backup = backups[0]
    log("INFO", f"Memulihkan cadangan dari: {latest_backup.name}...")

    try:
        if target_braz_por.exists():
            shutil.rmtree(target_braz_por)
        shutil.copytree(latest_backup, target_braz_por)
        log("SUCCESS", f"Folder bahasa dipulihkan dari {latest_backup.name}")
    except Exception as e:
        msg = f"Gagal memulihkan file cadangan: {e}"
        log("ERROR", msg)
        return False, msg

    # Revert settings-layout.json.bak
    bak_layout = p / "settings-layout.json.bak"
    layout_file = p / "settings-layout.json"
    if bak_layout.exists():
        try:
            shutil.copy2(bak_layout, layout_file)
            log("SUCCESS", "Pengaturan settings-layout.json dikembalikan ke semula.")
        except Exception as e:
            log("WARNING", f"Gagal mengembalikan settings-layout.json: {e}")

    # Revert user doc settings to English
    user_docs = Path(os.environ.get("USERPROFILE", "")) / "Documents" / "Paradox Interactive" / "Hearts of Iron IV"
    settings_file = user_docs / "settings.txt"
    if settings_file.exists():
        try:
            with open(settings_file, "r", encoding="utf-8", errors="ignore") as f:
                c = f.read()
            c = re.sub(r'language\s*=\s*"[^"]*"', 'language="l_english"', c)
            with open(settings_file, "w", encoding="utf-8") as f:
                f.write(c)
            log("SUCCESS", "Bahasa dokumen disetel kembali ke English.")
        except Exception:
            pass

    return True, f"Berhasil memulihkan cadangan dari {latest_backup.name}."
