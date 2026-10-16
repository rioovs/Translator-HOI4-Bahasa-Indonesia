"""GitHub Release Uploader for Hearts of Iron IV Indonesian Localization Installer."""

import os
import sys
import json
import urllib.request
import urllib.error
import subprocess
from pathlib import Path


def get_github_token() -> str:
    """Retrieves GitHub credential token from Git Credential Manager."""
    p = subprocess.Popen(
        ["git", "credential", "fill"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = p.communicate(input="protocol=https\nhost=github.com\n")
    for line in stdout.splitlines():
        if line.startswith("password="):
            return line.split("=", 1)[1]
    raise ValueError("Token GitHub tidak ditemukan dari Git Credential Manager.")


def create_or_get_release(token: str, owner: str, repo: str, tag: str, name: str, body: str) -> dict:
    """Creates a new release on GitHub, or retrieves it if the tag already exists."""
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "HOI4-Installer-Uploader",
        "Accept": "application/vnd.github.v3+json",
    }

    # Check if release already exists
    get_url = f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}"
    req_get = urllib.request.Request(get_url, headers=headers)
    try:
        with urllib.request.urlopen(req_get) as resp:
            data = json.loads(resp.read().decode())
            print(f"[INFO] Rilis dengan tag '{tag}' sudah ada (ID: {data['id']}).")
            return data
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise

    # Create new release
    post_url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    payload = json.dumps({
        "tag_name": tag,
        "target_commitish": "main",
        "name": name,
        "body": body,
        "draft": False,
        "prerelease": False,
    }).encode("utf-8")

    req_post = urllib.request.Request(post_url, data=payload, headers=headers, method="POST")
    with urllib.request.urlopen(req_post) as resp:
        data = json.loads(resp.read().decode())
        print(f"[INFO] Rilis baru berhasil dibuat: '{name}' (ID: {data['id']})")
        return data


def upload_asset(token: str, upload_url_template: str, asset_path: Path):
    """Uploads a binary asset to a GitHub release."""
    if not asset_path.exists():
        raise FileNotFoundError(f"File asset tidak ditemukan: {asset_path}")

    asset_name = asset_path.name
    # Strip template parameter {?name,label}
    upload_url_base = upload_url_template.split("{")[0]
    upload_url = f"{upload_url_base}?name={asset_name}"

    file_size = asset_path.stat().st_size
    print(f"[INFO] Mengunggah '{asset_name}' ({file_size / (1024 * 1024):.2f} MB)...")

    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "HOI4-Installer-Uploader",
        "Content-Type": "application/octet-stream",
        "Content-Length": str(file_size),
        "Accept": "application/vnd.github.v3+json",
    }

    with open(asset_path, "rb") as f:
        data = f.read()

    req = urllib.request.Request(upload_url, data=data, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req) as resp:
            res = json.loads(resp.read().decode())
            print(f"[SUCCESS] Asset berhasil diunggah!")
            print(f"          Download URL: {res.get('browser_download_url')}")
            return res
    except urllib.error.HTTPError as e:
        error_body = e.read().decode()
        if e.code == 422 and "already_exists" in error_body:
            print(f"[INFO] Asset '{asset_name}' sudah ada di release ini.")
        else:
            raise RuntimeError(f"Gagal mengunggah asset ({e.code}): {error_body}")


def main():
    owner = "rioovs"
    repo = "Translator-HOI4-Bahasa-Indonesia"
    tag = "v1.0.0"
    name = "Hearts of Iron IV - Penginstal Bahasa Indonesia v1.0.0"
    
    body = (
        "## Hearts of Iron IV - Penginstal Bahasa Indonesia v1.0.0\n\n"
        "Aplikasi penginstal mandiri (*standalone executable*) untuk memasang terjemahan Bahasa Indonesia lengkap "
        "ke dalam berkas instalasi game **Hearts of Iron IV**.\n\n"
        "### Fitur Utama:\n"
        "- **208 Berkas Terjemahan**: Mencakup game dasar dan seluruh ekspansi DLC utama.\n"
        "- **Otomatis Deteksi Versi & DLC**: Memeriksa kecocokan versi instalasi game dan status seluruh DLC yang terpasang.\n"
        "- **Integrasi Paradox Launcher (Dowser)**: Otomatis mendaftarkan pilihan `Bahasa Indonesia` di menu pengaturan bahasa game.\n"
        "- **Sistem Pencadangan Aman**: Folder cadangan disimpan di `_hoi4_id_backups/` (terisolasi di luar `localisation/` agar tidak bentrok dengan mesin Clausewitz).\n"
        "- **Antarmuka Minimalis**: Ringkas, bersih, tanpa dependensi Python di komputer pengguna.\n\n"
        "### Panduan Singkat:\n"
        "1. Unduh berkas **`HOI4_Indonesian_Installer.exe`** di bawah.\n"
        "2. Jalankan aplikasi (pilih direktori instalasi Hearts of Iron IV jika tidak terdeteksi otomatis).\n"
        "3. Klik tombol **\"Pasang Terjemahan\"**.\n"
        "4. Buka game atau Paradox Launcher, Bahasa Indonesia siap dimainkan!\n\n"
        "Dikembangkan oleh [@rioovs](https://github.com/rioovs)."
    )

    asset_file = Path("dist") / "HOI4_Indonesian_Installer.exe"

    token = get_github_token()
    print("[1/2] Membuat / mengambil rilis GitHub...")
    release_data = create_or_get_release(token, owner, repo, tag, name, body)

    print("[2/2] Mengunggah file .exe ke aset rilis...")
    upload_url_tmpl = release_data["upload_url"]
    upload_asset(token, upload_url_tmpl, asset_file)

    print("\n" + "=" * 60)
    print("SELESAI! Rilis GitHub telah aktif:")
    print(f"Halaman Rilis: {release_data['html_url']}")
    print("=" * 60)


if __name__ == "__main__":
    main()
