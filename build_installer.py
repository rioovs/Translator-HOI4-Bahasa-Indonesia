"""Build Script for Hearts of Iron IV Indonesian Localization Installer.
Packages the entire Python GUI application and 208 translation files into a standalone .exe.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
LOCALISATION_DIR = BASE_DIR / "localisation" / "braz_por"
LANGUAGES_FILE = BASE_DIR / "localisation" / "languages.yml"
DIST_DIR = BASE_DIR / "dist"
BUILD_DIR = BASE_DIR / "build"


def check_prerequisites():
    """Validates that all payload files are present prior to compilation."""
    print("[1/4] Memeriksa kelengkapan file payload terjemahan...")
    if not LOCALISATION_DIR.exists():
        raise FileNotFoundError(f"Folder terjemahan tidak ditemukan: {LOCALISATION_DIR}")

    files = list(LOCALISATION_DIR.glob("*.yml"))
    print(f"      -> Ditemukan {len(files)} file .yml di localisation/braz_por.")
    if len(files) < 200:
        raise ValueError(f"Jumlah file terjemahan tidak lengkap (hanya {len(files)} file).")

    if not LANGUAGES_FILE.exists():
        raise FileNotFoundError(f"File languages.yml tidak ditemukan: {LANGUAGES_FILE}")
    print("      -> languages.yml valid.")


def clean_previous_builds():
    """Cleans up previous PyInstaller output directories."""
    print("[2/4] Membersihkan folder build sebelumnya...")
    for d in [DIST_DIR, BUILD_DIR]:
        if d.exists():
            try:
                shutil.rmtree(d)
                print(f"      -> Menghapus: {d.name}")
            except Exception as e:
                print(f"      -> Peringatan: Tidak dapat menghapus {d.name}: {e}")


def build_executable():
    """Runs PyInstaller to compile the standalone .exe."""
    print("[3/4] Mengompilasi aplikasi menjadi file executable standalone...")

    # Data arguments for PyInstaller: source;target
    add_data_braz_por = f"{LOCALISATION_DIR};localisation/braz_por"
    add_data_languages = f"{LANGUAGES_FILE};localisation"

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--onefile",
        "--windowed",
        "--name",
        "HOI4_Indonesian_Installer",
        "--add-data",
        add_data_braz_por,
        "--add-data",
        add_data_languages,
        "--hidden-import",
        "tkinter",
        "--hidden-import",
        "tkinter.ttk",
        "--hidden-import",
        "tkinter.filedialog",
        "--hidden-import",
        "tkinter.messagebox",
        "--hidden-import",
        "winreg",
        "main.py",
    ]

    print("      -> Menjalankan PyInstaller...")
    print(f"      -> Command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=str(BASE_DIR))

    if result.returncode != 0:
        raise RuntimeError(f"PyInstaller gagal dengan exit code: {result.returncode}")

    target_exe = DIST_DIR / "HOI4_Indonesian_Installer.exe"
    if not target_exe.exists():
        raise FileNotFoundError(f"File executable tidak ditemukan di {target_exe}")

    size_mb = target_exe.stat().st_size / (1024 * 1024)
    print(f"[4/4] SUKSES! File .exe berhasil dibuat:")
    print(f"      -> Lokasi: {target_exe}")
    print(f"      -> Ukuran: {size_mb:.2f} MB")


def main():
    try:
        check_prerequisites()
        clean_previous_builds()
        build_executable()
        print("\n========================================================")
        print("  HOI4 Indonesian Localization Installer Siap Digunakan!")
        print("========================================================\n")
    except Exception as e:
        print(f"\n[ERROR] Kompilasi gagal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
