---
name: laporan-usk
description: Use when diminta membuat/merevisi laporan, proposal, skripsi, tugas akhir (TA), Proyek Akhir D3, atau tesis USK FMIPA — termasuk laporan studi kasus, laporan magang, dan laporan praktikum. Mengatur struktur, format wajib, sitasi APA, aturan tabel/gambar/persamaan, serta preferensi penulisan yang sudah ditetapkan pemilik skill.
---

# Laporan USK (FMIPA Universitas Syiah Kuala)

Aturan penulisan dokumen akademik FMIPA USK dari *Panduan TA/Tesis FMIPA USK 2024*
(Bab V + Lampiran 7–18), ditambah koreksi & preferensi user.

## Aturan #1 — JANGAN MENGARANG

Kalau ada hal yang belum pasti atau belum pernah diajarkan/diminta user:
**jangan diisi dengan asumsi**. Tandai **`[PERLU KONFIRMASI]`**, biarkan titik-titik
(`………`) di dokumen hasil, lalu **tanyakan ke user**. Berlaku juga untuk data
pribadi/orang lain (NIP, nama penguji, tanggal). Daftar lengkapnya ada di
`references/koreksi-dan-preferensi.md`.

Penanda yang dipakai di seluruh skill: `[PANDUAN]` aturan resmi · `[USER]`
ketentuan user · `[UMUM]` kebiasaan dari berkasnya (bukan aturan) ·
`[PERLU KONFIRMASI]` tidak boleh diisi sendiri.

## Kapan dipakai

- Membuat/merevisi/memeriksa Proposal Penelitian, Laporan Tugas Akhir (S1),
  Proyek Akhir D3, Tesis S2, laporan rekognisi.
- Menyusun bagian dokumen: sampul, pengesahan, plagiasi, deklarasi, abstrak,
  kata pengantar, daftar isi/tabel/gambar/lampiran, BAB I–V, daftar kepustakaan.
- Laporan studi kasus, laporan magang/kerja praktik, laporan praktikum mata kuliah.
- Memeriksa format naskah sebelum diserahkan ke pembimbing/penguji/seminar.

Sumber otoritatif: `D:\PROYEK AKHIR\_PANDUAN TA-TESIS 2024_Final.pdf`. Kalau ada
perbedaan dengan berkas ini, panduan yang menang.

## Aturan inti (ringkas — rincian di references/)

`[PANDUAN]` A4 · **Times New Roman 12 pt** · margin **kiri 3,5 cm**, atas/kanan/bawah
3,0 cm · spasi **1,5** (abstrak & daftar kepustakaan 1 spasi; daftar isi 1 spasi,
antar bab 2 spasi) · paragraf menjorok **1,25 cm**, rata kiri-kanan ·
**judul bab** TNR 14 pt kapital tebal rata tengah (nomor bab–judul 1 spasi) ·
**subjudul** TNR 12 pt kapital tebal bernomor `1.1` (**tanpa titik** — `[USER]`) ·
**subsubjudul** `1.1.1` hanya huruf awal kapital ·
nomor halaman: Pembuka **Romawi kecil** (tengah bawah), Isi & Penutup **angka Arab**
mulai 1 (kanan bawah), footer 2,0 cm · setiap bab mulai halaman baru.

`[PANDUAN]` Sitasi gaya **APA**: `(Kim, 2002)`, dua penulis `(Kim and Lee, 2002)`,
≥3 penulis `(Miller et al., 2002)`; kutipan > 5 baris = 1 spasi menjorok 1,25 cm.
Daftar kepustakaan alfabetis, 1 spasi, baris kedua menjorok 1,25 cm.

`[PANDUAN]` Penomoran ilustrasi `Tabel 2.1.` dan `Gambar 2.1.`; judul tabel **di atas**
tabel, keterangan gambar **1,5 spasi di bawah** gambar; huruf kecil kecuali huruf awal,
tidak tebal, tanpa titik akhir; satu baris rata tengah, lebih dari satu baris rata
kiri. Persamaan bernomor `(2.3)` rata kanan + keterangan simbol di bawahnya.

## Prosedur mengerjakan tugas laporan

1. Baca `references/koreksi-dan-preferensi.md` lebih dulu (larangan & kebiasaan user,
   daftar perlu konfirmasi).
2. Lihat contoh/format yang diberikan user (laporan sebelumnya, sample, panduan).
3. Tentukan jenis dokumen & bentuknya → `references/struktur-laporan.md`.
4. Bangun dokumen dari `templates/` (JANGAN mengubah berkas draft milik user; hasil
   harus berkas baru) → generator: `templates/buat_laporan_usk.py`, kerangka teks:
   `templates/kerangka-dokumen.md`.
5. Tulis isi mengikuti `references/format-penulisan.md`; sitasi hanya dari folder
   referensi jurnal user dan harus bisa ditelusuri
   (`references/sitasi-daftar-pustaka.md`).
6. Verifikasi dengan checklist di `references/struktur-laporan.md` (bagian 5); kalau
   memungkinkan ekspor PDF lewat Word COM sebagai bukti.
7. Laporkan hasil: path berkas lengkap + apa yang perlu user isi sendiri
   (NIP, tanggal, nama penguji).

## Berkas skill ini

| Berkas | Isi |
|---|---|
| `references/struktur-laporan.md` | Peta & struktur: urutan bagian, sistematika bab per bentuk/jenis dokumen, format halaman pembuka, checklist verifikasi |
| `references/format-penulisan.md` | Font, margin, spasi, nomor halaman, judul/paragraf/kutipan, tabel–gambar–persamaan, kaidah bahasa & PUEBI |
| `references/sitasi-daftar-pustaka.md` | Sitasi APA dalam teks + 12 jenis entri daftar kepustakaan |
| `references/koreksi-dan-preferensi.md` | Preferensi & koreksi user, aturan "jangan mengarang", daftar perlu konfirmasi & yang sudah dikonfirmasi |
| `templates/kerangka-dokumen.md` | Kerangka bab/subbab siap salin (TA 5 bab, kajian teoritis 4 bab, proposal, praktikum) |
| `templates/buat_laporan_usk.py` | Generator kerangka .docx (margin, font, spasi, halaman pembuka, TOC) |

## Pitfall yang sudah pernah terjadi

- Berkas .docx/.pptx yang sedang terbuka di Word/PowerPoint **terkunci** →
  `PermissionError` / `mv: Device or resource busy`. Simpan ke nama baru dulu, rapikan
  setelah Office ditutup (cek `~$*.docx`, proses WINWORD/POWERPNT).
- `python-docx` tidak memvalidasi skema: urutan elemen `w:pPr` harus benar
  (`w:spacing` sebelum `w:ind`/`w:jc`/`w:rPr`; `w:sectPr` paling akhir) — salah urutan
  → Word mengeluh "unreadable content".
- Set font juga untuk `eastAsia`, kalau tidak huruf jatuh ke Calibri.
- Nomor halaman bisa mengulang kalau `w:pgNumType` warisan tidak dibersihkan pada
  section bab berikutnya.
- Daftar isi berbasis field TOC: sertakan `<w:updateFields w:val="true"/>` di
  `word/settings.xml` atau update lewat Word COM.
- Tidak ada LibreOffice/soffice/pdftoppm di komputer ini; pakai Word lewat PowerShell
  COM untuk cek dokumen + ekspor PDF (pastikan WINWORD tidak sedang dipakai user).
- Skrip Office dijalankan dengan `C:/Python314/python.exe` (venv hermes tanpa pip).
