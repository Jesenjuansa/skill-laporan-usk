# Koreksi, Preferensi, dan Hal "Perlu Konfirmasi"

Ketentuan kerja dari user (termasuk larangannya), konvensi nama berkas, data identitas, aturan "jangan mengarang", daftar hal yang perlu konfirmasi, serta daftar yang sudah dikonfirmasi. **Baca ini lebih dulu sebelum mengerjakan tugas.**

## BAGIAN 1 — Preferensi & koreksi yang wajib diikuti

Bagian ini adalah hasil koreksi/permintaan langsung dari user. **Baca lebih dulu
sebelum mengerjakan tugas dokumentasi apa pun** untuk dia.

### Aturan yang tidak boleh dilanggar

1. **Jangan mengubah berkas miliknya tanpa izin.** Draft, laporan lama, dan berkas
   referensi tidak boleh ditimpa ("jangan ganggu file lain"). Semua hasil harus
   **berkas BARU** dengan nama yang jelas. Kalau memang harus menyunting berkasnya,
   buat cadangan dulu dan beri tahu dia.
2. **Deliverable disimpan di folder tugas yang bersangkutan**, bukan di Downloads:
   - Proyek Akhir / TA → `D:\PROYEK AKHIR`
   - Praktikum Pemrograman Game → `D:\lab game`
   - Kelas Data Sains → `D:\kelas data sains` (UTS: `D:\DATA SAINS\uts`)
   - Kalau tidak ada folder tugas → `C:\Users\Lenovo\Downloads`
3. **Satu berkas gabungan, bukan dipecah-pecah.** Dia pernah menegur:
   "jangan di bedain, 1 file aja".
4. **Sitasi hanya dari PDF referensi jurnal miliknya** dan harus bisa ditelusuri
   ke berkasnya. Jangan mengarang sumber.
5. **Gambar/diagram harus tetap terbaca setelah ditempel di Word** (area teks
   ± 16 cm) dan harus disertai **berkas sumber** (mis. `.drawio`). Diagram dibuat
   manual via matplotlib + ekspor drawio karena di komputer ini tidak ada
   graphviz/mermaid/inkscape/soffice.
6. **Presentasi (sempro/semhas):** ikuti susunan dan format dari contoh yang dia
   berikan; isinya tetap dari proposal miliknya. Template harus bagus karena
   **dia akan mengedit isinya sendiri nanti** (nama pembimbing/penguji, tanggal).
   Data yang belum ada (NIP, penguji, tanggal) → biarkan titik-titik, jangan
   dikarang.
7. **Bahasa:** seluruh dokumen dan jawaban dalam **Bahasa Indonesia**; istilah
   teknis boleh tetap bahasa Inggris. Di terminal, jawab dengan **teks polos tanpa
   markdown**.
8. **Penjelasan untuk dia** harus sederhana/non-teknis, sebutkan **alasan** tiap
   keputusan, dan beri komentar yang jelas di dalam skrip.

### Kebiasaan teknis di komputer ini

- Skrip Office dijalankan dengan `C:/Python314/python.exe`; venv hermes tidak
  punya pip. Path argumen untuk exe native Windows wajib gaya `C:/...`
  (MSYS merusak `/c/...`).
- python-docx tersedia; python-pptx juga. Tidak ada LibreOffice/soffice/pdftoppm/
  graphviz.
- **Berkas yang sedang terbuka di Word/PowerPoint terkunci**: simpan gagal
  `PermissionError`, `mv` gagal "Device or resource busy". Solusi: simpan ke nama
  baru dulu, rapikan setelah Office ditutup (cek berkas `~$*.docx`, proses WINWORD /
  POWERPNT). Untuk mengecek/menutup, jangan mengambil risiko menghilangkan
  pekerjaannya yang belum tersimpan.
- Script scratch di `$LOCALAPPDATA/Temp` bisa dihapus Windows di tengah sesi —
  tulis dan jalankan skrip dalam batch yang sama.
- Untuk ekspor PDF dan update field Word, pakai PowerShell COM
  (`New-Object -ComObject Word.Application`) hanya bila Word tidak sedang berjalan.

### Konvensi nama berkas

- Laporan praktikum mata kuliah: `LAPORAN <N>.docx` + PDF `<NPM> <NAMA> LAPORAN <N>.pdf`
  (pola nama, isi `<NPM>`/`<NAMA>` sesuai milik user).
- Dokumen TA / Proyek Akhir: pakai nama deskriptif yang sudah dipakai user + penanda
  versi baru (mis. `<nama berkas> (revisi <tanggal>).docx`). Jangan menimpa berkas lama.

### Data identitas — tidak disimpan di repo ini

Data pribadi **tidak ditulis di skill ini** (aturan user 18 Okt 2026: jangan memasukkan
data pribadi ke repo). Yang perlu diisi di dokumen:

| Isi | Diambil dari |
|---|---|
| Nama lengkap & NPM | berkas/proposal milik user di komputer lokal |
| Program studi / departemen / fakultas | berkas lokal (D-III Manajemen Informatika · Departemen Informatika · FMIPA USK) |
| Judul penelitian | draft/proposal milik user |
| Nama Pembimbing I & II | surat penetapan pembimbing / dokumen user |
| **NIP semua pihak** | `[PERLU KONFIRMASI]` — selalu dikosongkan (`NIP. ………………`), jangan dikarang |
| Nama & NIP dosen penguji, tanggal seminar | `[PERLU KONFIRMASI]` — dikosongkan |
| Nomor HP, email, alamat | tidak pernah dipakai di naskah |

Cara cepat mengambil identitas: lihat berkas proposal/laporan terakhir milik user
(mis. di `D:\PROYEK AKHIR`), atau tanyakan langsung.

### Cara melaporkan hasil (gaya yang dia harapkan)

- Sebutkan **path lengkap** setiap berkas yang dibuat.
- Ringkas isi/struktur dokumen, sebutkan halaman/jumlah bagian penting.
- Sebutkan **apa yang perlu dia periksa/isi sendiri** (tanggal, NIP, keterangan
  gambar).
- Kalau ada hal yang tidak bisa diverifikasi (mis. tidak ada alat render), katakan
  terus terang, jangan mengarang hasil.


## BAGIAN 2 — Aturan "jangan mengarang" & daftar perlu konfirmasi

Aturan user (dinyatakan langsung): *"Jika ada hal yang belum pasti atau belum pernah
saya ajarkan, JANGAN mengarang. Tandai sebagai 'perlu konfirmasi' dan tanyakan ke
saya."*

Berkas ini punya dua bagian: **(A) hal yang masih perlu konfirmasi** dan
**(B) hal yang sudah dikonfirmasi user** (jangan ditanyakan lagi).

### Cara pakai penanda

| Penanda | Arti | Sikap |
|---|---|---|
| `[PANDUAN]` | Tertulis di _Panduan TA/Tesis FMIPA USK 2024_ | Boleh dinyatakan sebagai aturan |
| `[USER]` | Preferensi/koreksi langsung dari user | Ikuti |
| `[UMUM]` | Praktik/kebiasaan dari berkas miliknya — bukan aturan | Sebut sebagai kebiasaan, jangan sebagai ketentuan |
| `[PERLU KONFIRMASI]` | Tidak ada rujukan & belum dipastikan | **Jangan diisi sendiri.** Tandai, lalu tanyakan ke user |

**Prosedur wajib bila menemukan hal `[PERLU KONFIRMASI]`:**

1. Jangan isi, jangan tebak, jangan mengambil dari laporan/dokumen orang lain.
2. Biarkan titik-titik (`………`) di dokumen hasil; tulis penanda
   `[perlu konfirmasi]` pada laporan hasil ke user (bukan di dalam naskah resmi).
3. **Tanyakan ke user** (bisa sekaligus beberapa pertanyaan).
4. Setelah dijawab: isi sesuai jawaban, pindahkan item ke bagian (B) di berkas ini
   beserta tanggalnya, dan catat keputusannya di `koreksi-dan-preferensi.md`.

---

### (A) Yang masih PERLU KONFIRMASI

| # | Hal | Catatan / pertanyaan yang harus diajukan |
|---|---|---|
| 1 | **Rincian format laporan studi kasus** | Panduan tidak memakai istilah "studi kasus". Kerangka 5-bab versi kasus di `struktur-laporan.md` masih **usulan** — tanyakan bila user benar-benar dapat tugas ini (user belum pernah dapat tugas studi kasus) |
| 2 | **Rincian format laporan magang / kerja praktik / PKL** | Sama seperti di atas: tidak diatur panduan; kerangka di `05` usulan. Tanyakan bila tugasnya muncul |
| 3 | **Nama & NIP dosen penguji, tanggal seminar/sidang** | Data orang lain — selalu kosongkan (titik-titik) dan minta user mengisi |
| 4 | **Isi laporan UTS/ujian praktikum** | Belum pernah dijelaskan (lihat catatan di `struktur-laporan.md`; laporan praktikum biasa sudah ada polanya) |
| 5 | **Batas minimal jumlah kata per bab / jumlah minimum rujukan** | Panduan hanya menetapkan abstrak maks 250 kata & kata kunci 4–6 kata. Jangan mengarang batas lain |
| 6 | **Ambang kemiripan/plagiarisme (mis. Turnitin)** | Panduan hanya menyebut pernyataan bebas plagiasi, tanpa ambang persen |
| 7 | **Isi lampiran yang wajib** | Panduan: lampiran "jika ada", harus berhubungan langsung dengan isi |
| 8 | **Kalau dosen mata kuliah memberi aturan format lain** | Aturan dosen yang menang; konfirmasi ke user saat itu terjadi |

Catatan: user pernah ditanya (18 Oktober 2026) soal template laporan studi
kasus/magang → jawabannya **"cukup dicatat di skill saja, belum perlu template"**.

---

### (B) Yang SUDAH DIKONFIRMASI user

| # | Hal | Keputusan | Tanggal |
|---|---|---|---|
| 1 | **Tanda titik pada nomor subbab** | Pakai **`1.1` tanpa titik** (mengikuti badan naskah panduan, bukan contoh Daftar Isi Lampiran 13) | 18 Okt 2026 |
| 2 | **NIP Dosen Pembimbing I** | **Kosongkan saja** — jangan pakai angka dari slide contoh orang lain; selalu titik-titik `NIP. ………………` | 18 Okt 2026 |
| 3 | **NIP Dosen Pembimbing II** | **Kosongkan saja** (titik-titik) | 18 Okt 2026 |
| 4 | **Aturan khusus Proyek Akhir D3** | Prodi D-III Manajemen Informatika **tidak punya aturan/template sendiri** → **ikuti panduan FMIPA** seperti sekarang (5 bab bentuk empiris, sampul `PROYEK AKHIR`, gelar Ahli Madya) | 18 Okt 2026 |
| 5 | **Judul tabel/gambar** | Pakai `Tabel 2.1.` / `Gambar 2.1.` sesuai panduan 5.3.8 (titik setelah nomor bab dan setelah nomor urut) | 18 Okt 2026 |
| 6 | **Visibilitas repo GitHub skill ini** | **Privat** | 18 Okt 2026 |
| 7 | **Data identitas yang boleh diisi otomatis** | Nama, NPM, program studi, departemen, fakultas, judul Proyek Akhir, nama pembimbing (tanpa NIP) | 18 Okt 2026 |

---

### Aturan sikap (berlaku umum)

1. **Jangan mengarang.** Tidak ada di panduan dan belum pernah diminta user →
   tandai `[PERLU KONFIRMASI]` dan tanyakan. Jangan diam-diam mengisi.
2. **Jangan mengisi data pribadi/orang lain** (NIP, nama penguji, tanggal, nomor
   surat) dengan tebakan — biarkan titik-titik.
3. **Jangan menyalin isi laporan orang lain** ke dokumen user lalu menyajikannya
   sebagai karya user tanpa memberi tahu. Sebutkan sumbernya dan tawarkan penulisan
   ulang (parafrase) dengan gaya user.
4. **Jangan menyatakan sesuatu "sudah benar" tanpa bukti.** Kalau tidak bisa
   diverifikasi (mis. render gambar, nomor halaman), katakan apa adanya.
5. Kalau user memberi jawaban/koreksi baru: **langsung perbarui skill** (pindahkan
   item ke bagian B berkas ini + catat di `koreksi-dan-preferensi.md`).
