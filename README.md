# skill-laporan-usk

Skill (pengetahuan siap pakai) untuk menulis dan merevisi **dokumen akademik FMIPA
Universitas Syiah Kuala**: Proposal Penelitian, Laporan Tugas Akhir (S1/skripsi),
Proyek Akhir D3, Tesis S2, laporan rekognisi, laporan studi kasus, laporan
magang/kerja praktik, dan laporan praktikum mata kuliah.

Isinya dirangkum dari **_Panduan Tugas Akhir dan Tesis FMIPA USK 2024_** (Bab V
Pedoman Penulisan + Lampiran 7–18) ditambah koreksi & preferensi kerja user.
Semua ditulis dalam Bahasa Indonesia; istilah teknis tetap bahasa Inggris.

## Isi repositori

```
laporan-usk/
├── SKILL.md                          instruksi utama + frontmatter (name & description) — ringkas & prosedural
├── README.md                         cara install & pakai di device baru
├── references/
│   ├── struktur-laporan.md           peta struktur, sistematika bab, jenis dokumen, format halaman pembuka, checklist verifikasi
│   ├── format-penulisan.md           font, margin, spasi, nomor halaman, judul, paragraf, kutipan, tabel/gambar/persamaan, bahasa & PUEBI
│   ├── sitasi-daftar-pustaka.md      sitasi APA dalam teks + 12 jenis entri daftar kepustakaan
│   └── koreksi-dan-preferensi.md     preferensi & koreksi user, aturan "jangan mengarang", daftar perlu konfirmasi
└── templates/                        (template kerangka bab/dokumen)
    ├── kerangka-dokumen.md           kerangka bab/subbab siap salin (TA 5 bab, kajian teoritis 4 bab, proposal, praktikum)
    └── buat_laporan_usk.py           generator kerangka .docx (python-docx) sesuai format panduan
```

## Cara pakai

### 1. Sebagai skill Hermes Agent (otomatis)

Letakkan folder ini di direktori skill profil Hermes:

```
C:\Users\<user>\AppData\Local\hermes\skills\productivity\laporan-usk\
```

### 2. Di device baru (clone dari GitHub)

```bash
git clone https://github.com/Jesenjuansa/skill-laporan-usk.git \
  "$LOCALAPPDATA/hermes/skills/productivity/laporan-usk"
```

Setelah di-clone, agent langsung mengenali skill `laporan-usk` dan memakainya saat
diminta membuat/merevisi laporan, proposal, skripsi, tugas akhir, Proyek Akhir,
tesis, laporan studi kasus, atau laporan praktikum. Tidak ada langkah install lain.

Kalau ingin memperbarui di device lama:

```bash
cd "$LOCALAPPDATA/hermes/skills/productivity/laporan-usk" && git pull
```

### 3. Sebagai panduan manual (tanpa agent)

- `SKILL.md` → aturan inti + prosedur kerja (ringkas).
- `references/struktur-laporan.md` → struktur & sistematika lengkap.
- `references/format-penulisan.md` → aturan format wajib + kaidah bahasa.
- `references/sitasi-daftar-pustaka.md` → cara menulis sitasi & daftar pustaka.
- `references/koreksi-dan-preferensi.md` → hal yang wajib diikuti dan hal yang
  **belum pasti** (jangan dikarang).

### 4. Membuat berkas .docx laporan

```bash
C:/Python314/python.exe templates/buat_laporan_usk.py
```

Skrip itu membuat dokumen contoh lengkap (sampul → abstrak → kata pengantar →
daftar isi → BAB I–V → daftar kepustakaan) dengan margin 3,5/3/3/3 cm, Times New
Roman 12, spasi 1,5, nomor halaman Romawi/Arab, dan field TOC aktif. Contoh
pemakaian tiap fungsi ada di `main()` — ubah `OUT` lalu panggil fungsi yang
dibutuhkan (`sampul()`, `halaman_pengesahan()`, `abstrak()`, `judul_bab()`,
`subjudul()`, `isi()`, `judul_tabel()`, `gambar()`, `keterangan_gambar()`,
`persamaan()`, `entri_pustaka()`).

## Aturan penting

- **Jangan mengarang.** Hal yang belum pasti atau belum pernah diminta user ditandai
  `[PERLU KONFIRMASI]`, dibiarkan titik-titik, lalu ditanyakan ke user.
- **Jangan mengubah berkas draft milik user** — hasil kerja selalu berkas baru.
- **Panduan resmi tetap yang utama**; kalau print-out panduan terbaru berbeda,
  ikuti panduan lalu perbarui berkas di repo ini.
- Repositori bersifat **privat** karena memuat data pribadi (nama, NPM, nama
  pembimbing).

## Sumber

- `_PANDUAN TA-TESIS 2024_Final.pdf` — Panduan Tugas Akhir dan Tesis FMIPA
  Universitas Syiah Kuala 2024 (Dekan FMIPA, 31 Oktober 2024).
- Pengalaman pengerjaan dokumen TA/Proyek Akhir, proposal, presentasi seminar, dan
  laporan praktikum user (NPM <NPM>, D-III Manajemen Informatika
  FMIPA USK).
