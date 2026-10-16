"""Hearts of Iron IV - Indonesian Localization Installer GUI.
Clean, restrained desktop UI designed under Anti-Slop principles.
"""

import os
import sys
import threading
import subprocess
import webbrowser
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from app.core import (
    find_hoi4_install_paths,
    validate_hoi4_dir,
    get_game_version,
    scan_dlcs,
    install_translations,
    restore_backup,
    RECOMMENDED_RAW_VERSION,
)
from app import __version__

# Palette: Controlled dark neutral surfaces with a single primary accent
BG_MAIN = "#0f1218"
BG_HEADER = "#151922"
BG_CARD = "#151922"
BG_CARD_BORDER = "#222938"
BG_INPUT = "#0c0e14"
BG_INPUT_BORDER = "#252d3d"

FG_MAIN = "#f1f5f9"
FG_MUTED = "#8e9bb0"
FG_DIM = "#57657a"

COLOR_PRIMARY = "#1e40af"
COLOR_PRIMARY_HOVER = "#1d4ed8"
COLOR_PRIMARY_TEXT = "#ffffff"

COLOR_BTN_SEC = "#1f2633"
COLOR_BTN_SEC_HOVER = "#2a3345"
COLOR_BTN_SEC_BORDER = "#2d3748"

COLOR_SUCCESS = "#16a34a"
COLOR_SUCCESS_BG = "#052e16"
COLOR_SUCCESS_TEXT = "#bbf7d0"

COLOR_WARNING = "#ca8a04"
COLOR_WARNING_BG = "#422006"
COLOR_WARNING_TEXT = "#fef08a"

COLOR_ERROR = "#dc2626"
COLOR_ERROR_BG = "#450a0a"
COLOR_ERROR_TEXT = "#fecaca"

FONT_FAMILY = "Segoe UI"
FONT_MONO = "Consolas"
CREDIT_URL = "https://github.com/rioovs"


class AntiSlopButton(tk.Button):
    """Button with explicit states, clean flat borders, and no gratuitous effects."""

    def __init__(self, master, text, bg=COLOR_BTN_SEC, fg=FG_MAIN, hover_bg=None, command=None, **kwargs):
        self.default_bg = bg
        self.hover_bg = hover_bg or (COLOR_BTN_SEC_HOVER if bg == COLOR_BTN_SEC else bg)
        btn_font = kwargs.pop("font", (FONT_FAMILY, 9))
        padx = kwargs.pop("padx", 14)
        pady = kwargs.pop("pady", 6)

        super().__init__(
            master,
            text=text,
            bg=self.default_bg,
            fg=fg,
            activebackground=self.hover_bg,
            activeforeground=fg,
            relief="flat",
            bd=0,
            cursor="hand2",
            command=command,
            font=btn_font,
            padx=padx,
            pady=pady,
            **kwargs,
        )
        self.bind("<Enter>", lambda e: self.configure(bg=self.hover_bg))
        self.bind("<Leave>", lambda e: self.configure(bg=self.default_bg))


class HOI4InstallerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"Hearts of Iron IV - Penginstal Bahasa Indonesia v{__version__}")
        self.root.geometry("820x720")
        self.root.minsize(760, 640)
        self.root.configure(bg=BG_MAIN)

        self.selected_path = tk.StringVar()
        self.backup_opt = tk.BooleanVar(value=True)
        self.dowser_opt = tk.BooleanVar(value=True)
        self.user_doc_opt = tk.BooleanVar(value=True)

        self.detected_version = {}
        self.detected_dlcs = []
        self.is_installing = False

        self._setup_styles()
        self._build_ui()
        self._auto_detect()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TProgressbar",
            thickness=10,
            troughcolor=BG_INPUT,
            background=COLOR_PRIMARY_HOVER,
            bordercolor=BG_CARD_BORDER,
            lightcolor=COLOR_PRIMARY_HOVER,
            darkcolor=COLOR_PRIMARY_HOVER,
        )

        style.configure(
            "TCheckbutton",
            background=BG_CARD,
            foreground=FG_MAIN,
            font=(FONT_FAMILY, 9),
        )
        style.map(
            "TCheckbutton",
            background=[("active", BG_CARD)],
            foreground=[("active", FG_MAIN)],
        )

    def _build_ui(self):
        # 1. Header Bar
        header = tk.Frame(self.root, bg=BG_HEADER, padx=24, pady=16, highlightthickness=1, highlightbackground=BG_CARD_BORDER)
        header.pack(fill="x")

        title_box = tk.Frame(header, bg=BG_HEADER)
        title_box.pack(side="left", fill="both")

        lbl_title = tk.Label(
            title_box,
            text="Hearts of Iron IV - Penginstal Bahasa Indonesia",
            font=(FONT_FAMILY, 13, "bold"),
            fg=FG_MAIN,
            bg=BG_HEADER,
        )
        lbl_title.pack(anchor="w")

        lbl_sub = tk.Label(
            title_box,
            text="Pemasangan berkas terjemahan langsung ke direktori instalasi game",
            font=(FONT_FAMILY, 9),
            fg=FG_MUTED,
            bg=BG_HEADER,
        )
        lbl_sub.pack(anchor="w", pady=(2, 0))

        badge_box = tk.Frame(header, bg=BG_HEADER)
        badge_box.pack(side="right", anchor="e")

        lbl_ver = tk.Label(
            badge_box,
            text=f"Versi {__version__}",
            font=(FONT_FAMILY, 8),
            bg=COLOR_BTN_SEC,
            fg=FG_MUTED,
            padx=8,
            pady=4,
        )
        lbl_ver.pack(side="right")

        # Main Body Container
        content = tk.Frame(self.root, bg=BG_MAIN, padx=20, pady=12)
        content.pack(fill="both", expand=True)

        # 2. Section: Game Directory Selector
        dir_frame = tk.LabelFrame(
            content,
            text=" Direktori Instalasi Game ",
            font=(FONT_FAMILY, 9, "bold"),
            bg=BG_CARD,
            fg=FG_MAIN,
            bd=1,
            relief="solid",
            padx=12,
            pady=10,
        )
        dir_frame.pack(fill="x", pady=(0, 10))

        dir_box = tk.Frame(dir_frame, bg=BG_CARD)
        dir_box.pack(fill="x")

        self.txt_path = tk.Entry(
            dir_box,
            textvariable=self.selected_path,
            font=(FONT_FAMILY, 9),
            bg=BG_INPUT,
            fg=FG_MAIN,
            insertbackground=FG_MAIN,
            relief="solid",
            bd=1,
            highlightthickness=0,
        )
        self.txt_path.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 8))

        btn_auto = AntiSlopButton(
            dir_box,
            text="Cari Otomatis",
            bg=COLOR_BTN_SEC,
            hover_bg=COLOR_BTN_SEC_HOVER,
            command=self._auto_detect,
        )
        btn_auto.pack(side="left", padx=(0, 6))

        btn_browse = AntiSlopButton(
            dir_box,
            text="Pilih Folder...",
            bg=COLOR_BTN_SEC,
            hover_bg=COLOR_BTN_SEC_HOVER,
            command=self._browse_dir,
        )
        btn_browse.pack(side="left")

        # 3. Section: Status Cards (Version & DLC)
        status_row = tk.Frame(content, bg=BG_MAIN)
        status_row.pack(fill="x", pady=(0, 10))

        # 3a. Card Status Versi
        self.card_ver = tk.LabelFrame(
            status_row,
            text=" Status Versi Game ",
            font=(FONT_FAMILY, 9, "bold"),
            bg=BG_CARD,
            fg=FG_MAIN,
            bd=1,
            relief="solid",
            padx=12,
            pady=8,
        )
        self.card_ver.pack(side="left", fill="both", expand=True, padx=(0, 6))

        self.lbl_ver_display = tk.Label(
            self.card_ver,
            text="Memeriksa versi...",
            font=(FONT_FAMILY, 9),
            fg=FG_MAIN,
            bg=BG_CARD,
            anchor="w",
            justify="left",
        )
        self.lbl_ver_display.pack(fill="x", anchor="w")

        self.lbl_ver_badge = tk.Label(
            self.card_ver,
            text="Menunggu deteksi",
            font=(FONT_FAMILY, 8),
            bg=COLOR_BTN_SEC,
            fg=FG_MUTED,
            padx=8,
            pady=3,
        )
        self.lbl_ver_badge.pack(anchor="w", pady=(6, 0))

        # 3b. Card Status DLC
        self.card_dlc = tk.LabelFrame(
            status_row,
            text=" Ekspansi & Konten (DLC) ",
            font=(FONT_FAMILY, 9, "bold"),
            bg=BG_CARD,
            fg=FG_MAIN,
            bd=1,
            relief="solid",
            padx=12,
            pady=8,
        )
        self.card_dlc.pack(side="right", fill="both", expand=True, padx=(6, 0))

        self.lbl_dlc_display = tk.Label(
            self.card_dlc,
            text="Memindai DLC...",
            font=(FONT_FAMILY, 9),
            fg=FG_MAIN,
            bg=BG_CARD,
            anchor="w",
            justify="left",
        )
        self.lbl_dlc_display.pack(fill="x", anchor="w")

        dlc_action_row = tk.Frame(self.card_dlc, bg=BG_CARD)
        dlc_action_row.pack(fill="x", pady=(6, 0))

        self.lbl_dlc_badge = tk.Label(
            dlc_action_row,
            text="0 DLC",
            font=(FONT_FAMILY, 8),
            bg=COLOR_BTN_SEC,
            fg=FG_MUTED,
            padx=8,
            pady=3,
        )
        self.lbl_dlc_badge.pack(side="left")

        btn_view_dlc = AntiSlopButton(
            dlc_action_row,
            text="Rincian DLC",
            bg=COLOR_BTN_SEC,
            hover_bg=COLOR_BTN_SEC_HOVER,
            command=self._show_dlc_popup,
            padx=10,
            pady=3,
        )
        btn_view_dlc.pack(side="right")

        # 3c. Warning Banner (Hidden by default, shown if version differs)
        self.warn_banner = tk.Frame(
            content,
            bg=COLOR_WARNING_BG,
            bd=1,
            relief="solid",
            padx=12,
            pady=8,
        )
        self.lbl_warn = tk.Label(
            self.warn_banner,
            text="",
            font=(FONT_FAMILY, 8),
            fg=COLOR_WARNING_TEXT,
            bg=COLOR_WARNING_BG,
            wraplength=740,
            justify="left",
        )
        self.lbl_warn.pack(anchor="w")

        # 4. Section: Options
        opt_card = tk.LabelFrame(
            content,
            text=" Opsi Pemasangan ",
            font=(FONT_FAMILY, 9, "bold"),
            bg=BG_CARD,
            fg=FG_MAIN,
            bd=1,
            relief="solid",
            padx=12,
            pady=8,
        )
        opt_card.pack(fill="x", pady=(0, 10))

        c1 = ttk.Checkbutton(
            opt_card,
            text="Konfigurasi Paradox Dowser Launcher (menambahkan label Bahasa Indonesia)",
            variable=self.dowser_opt,
        )
        c1.pack(anchor="w", pady=2)

        c2 = ttk.Checkbutton(
            opt_card,
            text="Atur Bahasa Indonesia sebagai bahasa default di dokumen pemain (settings.txt)",
            variable=self.user_doc_opt,
        )
        c2.pack(anchor="w", pady=2)

        c3 = ttk.Checkbutton(
            opt_card,
            text="Cadangkan folder bahasa asli sebelum proses pemasangan",
            variable=self.backup_opt,
        )
        c3.pack(anchor="w", pady=2)

        # 5. Action Buttons
        action_row = tk.Frame(content, bg=BG_MAIN)
        action_row.pack(fill="x", pady=(0, 10))

        self.btn_install = AntiSlopButton(
            action_row,
            text="Pasang Bahasa Indonesia",
            bg=COLOR_PRIMARY,
            hover_bg=COLOR_PRIMARY_HOVER,
            fg=COLOR_PRIMARY_TEXT,
            command=self._start_install,
            font=(FONT_FAMILY, 10, "bold"),
            pady=8,
        )
        self.btn_install.pack(side="left", fill="x", expand=True, padx=(0, 8))

        self.btn_restore = AntiSlopButton(
            action_row,
            text="Pulihkan Cadangan",
            bg=COLOR_BTN_SEC,
            hover_bg=COLOR_BTN_SEC_HOVER,
            command=self._start_restore,
            pady=8,
        )
        self.btn_restore.pack(side="left", padx=(0, 8))

        self.btn_play = AntiSlopButton(
            action_row,
            text="Jalankan Game",
            bg=COLOR_BTN_SEC,
            hover_bg=COLOR_BTN_SEC_HOVER,
            command=self._launch_game,
            pady=8,
        )
        self.btn_play.pack(side="left")

        # 6. Section: Status & Log
        log_card = tk.LabelFrame(
            content,
            text=" Log Aktivitas ",
            font=(FONT_FAMILY, 9, "bold"),
            bg=BG_CARD,
            fg=FG_MAIN,
            bd=1,
            relief="solid",
            padx=10,
            pady=6,
        )
        log_card.pack(fill="both", expand=True)

        self.progress_bar = ttk.Progressbar(log_card, style="TProgressbar", orient="horizontal", mode="determinate")
        self.progress_bar.pack(fill="x", pady=(2, 6))

        self.lbl_status = tk.Label(
            log_card,
            text="Status: Siap memasang.",
            font=(FONT_FAMILY, 8),
            fg=FG_MUTED,
            bg=BG_CARD,
            anchor="w",
        )
        self.lbl_status.pack(fill="x", anchor="w", pady=(0, 4))

        log_frame = tk.Frame(log_card, bg=BG_INPUT)
        log_frame.pack(fill="both", expand=True)

        self.txt_log = tk.Text(
            log_frame,
            bg=BG_INPUT,
            fg="#cbd5e1",
            insertbackground="#ffffff",
            font=(FONT_MONO, 8),
            wrap="word",
            bd=0,
            padx=8,
            pady=6,
        )
        scroll = tk.Scrollbar(log_frame, command=self.txt_log.yview)
        self.txt_log.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.txt_log.pack(side="left", fill="both", expand=True)

        # Syntax Color Tags
        self.txt_log.tag_config("INFO", foreground="#38bdf8")
        self.txt_log.tag_config("SUCCESS", foreground="#4ade80")
        self.txt_log.tag_config("WARNING", foreground="#facc15")
        self.txt_log.tag_config("ERROR", foreground="#f87171")

        # 7. Footer with Clickable Credit Link
        footer = tk.Frame(self.root, bg=BG_HEADER, padx=20, pady=8, highlightthickness=1, highlightbackground=BG_CARD_BORDER)
        footer.pack(fill="x", side="bottom")

        lbl_foot_left = tk.Label(
            footer,
            text="Hearts of Iron IV Indonesian Localization • Lisensi MIT",
            font=(FONT_FAMILY, 8),
            fg=FG_DIM,
            bg=BG_HEADER,
        )
        lbl_foot_left.pack(side="left")

        # Clickable Credit Container
        credit_box = tk.Frame(footer, bg=BG_HEADER)
        credit_box.pack(side="right")

        lbl_credit_prefix = tk.Label(
            credit_box,
            text="Pengembang: ",
            font=(FONT_FAMILY, 8),
            fg=FG_DIM,
            bg=BG_HEADER,
        )
        lbl_credit_prefix.pack(side="left")

        lbl_credit_link = tk.Label(
            credit_box,
            text="rioovs",
            font=(FONT_FAMILY, 8, "underline"),
            fg="#38bdf8",
            bg=BG_HEADER,
            cursor="hand2",
        )
        lbl_credit_link.pack(side="left")
        lbl_credit_link.bind("<Button-1>", lambda e: webbrowser.open_new_tab(CREDIT_URL))
        lbl_credit_link.bind("<Enter>", lambda e: lbl_credit_link.configure(fg="#7dd3fc"))
        lbl_credit_link.bind("<Leave>", lambda e: lbl_credit_link.configure(fg="#38bdf8"))

    def log(self, level: str, message: str):
        """Appends a color-tagged log message."""
        def _append():
            self.txt_log.insert("end", f"[{level}] ", level)
            self.txt_log.insert("end", f"{message}\n")
            self.txt_log.see("end")
        self.root.after(0, _append)

    def set_status(self, text: str):
        self.root.after(0, lambda: self.lbl_status.configure(text=f"Status: {text}"))

    def _auto_detect(self):
        """Scans for game path and refreshes status."""
        self.log("INFO", "Mencari direktori Hearts of Iron IV secara otomatis...")
        paths = find_hoi4_install_paths()
        if paths:
            selected = str(paths[0])
            self.selected_path.set(selected)
            self.log("SUCCESS", f"Folder game ditemukan: {selected}")
            self._analyze_selected_dir(selected)
        else:
            self.log("WARNING", "Hearts of Iron IV tidak terdeteksi otomatis. Silakan gunakan tombol Pilih Folder.")
            self.lbl_ver_display.configure(text="Belum terdeteksi")
            self.lbl_dlc_display.configure(text="Belum terdeteksi")

    def _browse_dir(self):
        path = filedialog.askdirectory(title="Pilih Direktori Instalasi Hearts of Iron IV")
        if path:
            self.selected_path.set(path)
            self._analyze_selected_dir(path)

    def _analyze_selected_dir(self, dir_path: str):
        """Checks game version, scans DLCs, and updates GUI status cards."""
        p = Path(dir_path)
        is_valid, msg = validate_hoi4_dir(p)
        if not is_valid:
            self.log("ERROR", f"Direktori tidak valid: {msg}")
            self.lbl_ver_display.configure(text="Folder Tidak Valid", fg=COLOR_ERROR_TEXT)
            self.lbl_ver_badge.configure(text="Tidak Valid", bg=COLOR_ERROR_BG, fg=COLOR_ERROR_TEXT)
            self.warn_banner.pack_forget()
            return

        # 1. Version Analysis
        ver_info = get_game_version(p)
        self.detected_version = ver_info
        raw_v = ver_info["raw_version"]
        display_v = ver_info["version_display"]

        self.lbl_ver_display.configure(text=f"{display_v}", fg=FG_MAIN)
        if ver_info["is_compatible"]:
            self.lbl_ver_badge.configure(text="Kompatibel (1.19.3.x)", bg=COLOR_SUCCESS_BG, fg=COLOR_SUCCESS_TEXT)
            self.warn_banner.pack_forget()
            self.log("SUCCESS", f"Versi game kompatibel: {display_v} ({raw_v})")
        else:
            self.lbl_ver_badge.configure(text="Perlu Perhatian", bg=COLOR_WARNING_BG, fg=COLOR_WARNING_TEXT)
            warn_text = ver_info["warning"]
            self.lbl_warn.configure(text=warn_text)
            self.warn_banner.pack(fill="x", pady=(0, 10), after=self.card_ver.master)
            self.log("WARNING", warn_text)

        # 2. DLC Analysis
        dlcs = scan_dlcs(p)
        self.detected_dlcs = dlcs
        total_dlc = len(dlcs)
        expansions = [d for d in dlcs if "ekspansi" in d["category"].lower() or "country pack" in d["category"].lower()]

        self.lbl_dlc_display.configure(text=f"{total_dlc} DLC Terdeteksi ({len(expansions)} Ekspansi Utama)", fg=FG_MAIN)
        self.lbl_dlc_badge.configure(text=f"{total_dlc} DLC Didukung", bg=COLOR_SUCCESS_BG, fg=COLOR_SUCCESS_TEXT)
        self.log("INFO", f"Memindai DLC: {total_dlc} DLC terdeteksi di folder game.")

    def _show_dlc_popup(self):
        """Displays modal list of all detected DLCs with categories."""
        if not self.detected_dlcs:
            messagebox.showinfo("Daftar DLC", "Belum ada DLC yang terdeteksi.")
            return

        win = tk.Toplevel(self.root)
        win.title("Daftar DLC Terdeteksi")
        win.geometry("640x500")
        win.configure(bg=BG_MAIN)
        win.transient(self.root)

        header = tk.Frame(win, bg=BG_HEADER, padx=16, pady=12, highlightthickness=1, highlightbackground=BG_CARD_BORDER)
        header.pack(fill="x")
        tk.Label(header, text="Daftar DLC Terdeteksi", font=(FONT_FAMILY, 11, "bold"), fg=FG_MAIN, bg=BG_HEADER).pack(anchor="w")
        tk.Label(
            header,
            text=f"Total: {len(self.detected_dlcs)} DLC terdeteksi. Seluruh konten tercakup dalam berkas terjemahan.",
            font=(FONT_FAMILY, 8),
            fg=FG_MUTED,
            bg=BG_HEADER,
        ).pack(anchor="w", pady=(2, 0))

        body = tk.Frame(win, bg=BG_MAIN, padx=12, pady=10)
        body.pack(fill="both", expand=True)

        list_box = tk.Frame(body, bg=BG_CARD)
        list_box.pack(fill="both", expand=True)

        tree = ttk.Treeview(list_box, columns=("category", "title", "status"), show="headings", height=15)
        tree.heading("category", text="Kategori")
        tree.heading("title", text="Nama DLC")
        tree.heading("status", text="Status")

        tree.column("category", width=140, anchor="w")
        tree.column("title", width=360, anchor="w")
        tree.column("status", width=100, anchor="center")

        scroll = ttk.Scrollbar(list_box, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        tree.pack(side="left", fill="both", expand=True)

        for d in self.detected_dlcs:
            tree.insert("", "end", values=(d["category"], d["title"], "Tersedia"))

        btn_close = AntiSlopButton(win, text="Tutup", bg=COLOR_BTN_SEC, hover_bg=COLOR_BTN_SEC_HOVER, command=win.destroy)
        btn_close.pack(pady=10)

    def _start_install(self):
        """Runs the installation process in a worker thread."""
        path = self.selected_path.get().strip()
        if not path:
            messagebox.showwarning("Peringatan", "Silakan pilih direktori game Hearts of Iron IV terlebih dahulu.")
            return

        is_valid, msg = validate_hoi4_dir(path)
        if not is_valid:
            messagebox.showerror("Error", f"Folder tidak valid: {msg}")
            return

        if self.detected_version and not self.detected_version.get("is_compatible", False):
            ver_warn = self.detected_version.get("warning", "")
            confirm = messagebox.askyesno(
                "Peringatan Kompatibilitas Versi",
                f"{ver_warn}\n\nApakah Anda ingin tetap melanjutkan pemasangan?",
            )
            if not confirm:
                return

        self.is_installing = True
        self.btn_install.configure(state="disabled")
        self.btn_restore.configure(state="disabled")
        self.progress_bar["value"] = 0

        thread = threading.Thread(target=self._worker_install, args=(path,), daemon=True)
        thread.start()

    def _worker_install(self, path: str):
        try:
            self.set_status("Memasang berkas terjemahan...")

            def on_progress(cur, total, fname):
                pct = int((cur / total) * 100)
                self.root.after(0, lambda: self.progress_bar.configure(value=pct))
                self.set_status(f"Menyalin ({cur}/{total}): {fname}")

            res = install_translations(
                game_path=path,
                backup=self.backup_opt.get(),
                patch_launcher=self.dowser_opt.get(),
                patch_user_doc=self.user_doc_opt.get(),
                progress_cb=on_progress,
                log_cb=self.log,
            )

            self.root.after(0, lambda: self.progress_bar.configure(value=100))
            self.set_status("Pemasangan selesai.")
            self.log("SUCCESS", "Pemasangan berkas terjemahan Bahasa Indonesia selesai.")
            self.log("INFO", "Game siap dijalankan melalui launcher atau berkas hoi4.exe.")

            self.root.after(0, lambda: messagebox.showinfo(
                "Pemasangan Berhasil",
                f"Terjemahan Bahasa Indonesia ({res['copied']} berkas) berhasil dipasang ke dalam Hearts of Iron IV.\n\n"
                "Pilihan bahasa di Dowser Launcher telah diperbarui ke Bahasa Indonesia.",
            ))

        except Exception as e:
            self.log("ERROR", f"Terjadi kesalahan saat instalasi: {e}")
            self.set_status("Gagal.")
            self.root.after(0, lambda: messagebox.showerror("Gagal Memasang", f"Kesalahan: {e}"))
        finally:
            self.is_installing = False
            self.root.after(0, lambda: self.btn_install.configure(state="normal"))
            self.root.after(0, lambda: self.btn_restore.configure(state="normal"))

    def _start_restore(self):
        """Restores the backup files."""
        path = self.selected_path.get().strip()
        if not path:
            messagebox.showwarning("Peringatan", "Pilih folder game terlebih dahulu.")
            return

        confirm = messagebox.askyesno(
            "Konfirmasi Pemulihan",
            "Apakah Anda yakin ingin memulihkan folder bahasa dari cadangan terakhir?",
        )
        if not confirm:
            return

        self.set_status("Memulihkan cadangan...")
        suc, msg = restore_backup(path, log_cb=self.log)
        if suc:
            messagebox.showinfo("Pemulihan Berhasil", msg)
            self.set_status("Cadangan berhasil dipulihkan.")
        else:
            messagebox.showerror("Gagal Memulihkan", msg)
            self.set_status("Gagal memulihkan cadangan.")

    def _launch_game(self):
        """Launches dowser.exe or hoi4.exe from the game directory."""
        path = self.selected_path.get().strip()
        if not path:
            messagebox.showwarning("Peringatan", "Pilih direktori game terlebih dahulu.")
            return

        p = Path(path)
        dowser = p / "dowser.exe"
        hoi4 = p / "hoi4.exe"

        target_exe = None
        if dowser.exists():
            target_exe = dowser
        elif hoi4.exists():
            target_exe = hoi4

        if target_exe:
            try:
                subprocess.Popen([str(target_exe)], cwd=str(p))
                self.log("INFO", f"Meluncurkan: {target_exe.name}")
            except Exception as e:
                self.log("ERROR", f"Gagal menjalankan game: {e}")
                messagebox.showerror("Error", f"Gagal meluncurkan game: {e}")
        else:
            messagebox.showerror("Error", "dowser.exe atau hoi4.exe tidak ditemukan di direktori tersebut.")


def run_gui():
    root = tk.Tk()
    app = HOI4InstallerApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
