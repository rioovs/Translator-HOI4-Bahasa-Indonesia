"""Hearts of Iron IV - Indonesian Localization Installer
Main Entry Point.
"""

import sys
import argparse
from pathlib import Path

# Enable High-DPI awareness on Windows for crisp rendering
if sys.platform == "win32":
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        try:
            import ctypes
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass

from app.core import (
    find_hoi4_install_paths,
    validate_hoi4_dir,
    get_game_version,
    scan_dlcs,
    install_translations,
)
from app.gui import run_gui


def cli_install(target_path: str = None, no_backup: bool = False):
    """Headless CLI installation mode."""
    print("=== Hearts of Iron IV - Penginstal Bahasa Indonesia (CLI) ===")
    if not target_path:
        paths = find_hoi4_install_paths()
        if not paths:
            print("[ERROR] Tidak dapat menemukan folder HOI4 otomatis. Tentukan --path.")
            sys.exit(1)
        target_path = str(paths[0])

    p = Path(target_path)
    is_valid, msg = validate_hoi4_dir(p)
    if not is_valid:
        print(f"[ERROR] Direktori tidak valid: {msg}")
        sys.exit(1)

    print(f"[INFO] Folder target: {p}")
    ver = get_game_version(p)
    print(f"[INFO] Versi game: {ver['version_display']} (Kompatibel: {ver['is_compatible']})")
    if ver["warning"]:
        print(f"[WARNING] {ver['warning']}")

    dlcs = scan_dlcs(p)
    print(f"[INFO] {len(dlcs)} DLC terdeteksi.")

    def log_cb(lvl, m):
        print(f"[{lvl}] {m}")

    def progress_cb(cur, tot, f):
        if cur % 20 == 0 or cur == tot:
            print(f"  -> Menyalin ({cur}/{tot}): {f}")

    res = install_translations(
        game_path=p,
        backup=not no_backup,
        patch_launcher=True,
        patch_user_doc=True,
        progress_cb=progress_cb,
        log_cb=log_cb,
    )
    print(f"[SUCCESS] Pemasangan berhasil: {res['copied']} file terpasang!")


def main():
    parser = argparse.ArgumentParser(description="Hearts of Iron IV Indonesian Localization Installer")
    parser.add_argument("--cli", action="store_true", help="Jalankan dalam mode baris perintah (CLI)")
    parser.add_argument("--path", type=str, help="Path ke folder instalasi Hearts of Iron IV")
    parser.add_argument("--no-backup", action="store_true", help="Jangan buat cadangan file asli")

    args = parser.parse_args()

    if args.cli or args.path:
        cli_install(args.path, args.no_backup)
    else:
        run_gui()


if __name__ == "__main__":
    main()
