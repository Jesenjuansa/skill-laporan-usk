# Kerangka Dokumen — siap salin

Kerangka bab/subbab untuk dipakai langsung. Ganti teks dalam `<...>` dengan isi
penelitian. Aturan format (font, margin, spasi, penomoran halaman) ada di
`references/format-penulisan.md`; struktur lengkap per jenis dokumen di
`references/struktur-laporan.md`. Bagian yang ditandai **[perlu konfirmasi]**
jangan diisi sendiri — tanyakan dulu ke user.

---

## A. Laporan Tugas Akhir / Proyek Akhir (bentuk empiris — 5 bab)

**Halaman pembuka (urutannya tetap):** Sampul → Halaman Judul → Pengesahan →
Pernyataan Bebas Plagiasi → Deklarasi (jika ada) → Abstrak (250 kata) + Abstract →
Kata Pengantar → Daftar Isi → Daftar Tabel → Daftar Gambar → Daftar Lampiran.

```
BAB I  PENDAHULUAN
1.1  Latar Belakang            <alasan & argumentasi pentingnya penelitian>
1.2  Rumusan Masalah           <jelas, dibatasi; boleh bukan pertanyaan>
1.3  Tujuan Penelitian         <pernyataan singkat tujuan>
1.4  Hipotesis (jika ada)      <hanya kalau penelitian menguji dugaan>
1.5  Manfaat Penelitian        <bagi objek, pembaca, dan penulis>

BAB II  TINJAUAN KEPUSTAKAAN
2.1  <konsep/teori utama>      <sertai sitasi APA dari referensi milik user>
2.2  <teori pendukung>
2.3  <penelitian terdahulu>
2.4  <kerangka pemikiran>      <boleh tabel/gambar bila perlu>

BAB III  METODE PENELITIAN
3.1  Tempat dan Waktu Penelitian
3.2  Alat dan Bahan
3.3  Metode Kerja              <perencanaan → desain → implementasi → pengujian>
3.4  Teknik Pengujian          <mis. black-box testing>

BAB IV  HASIL DAN PEMBAHASAN
4.1  Hasil                     <sajikan data/sistem yang dibangun>
4.2  Pembahasan                <analisis + kaitkan dengan teori/penelitian terdahulu>
4.3  Pengujian                 <tabel hasil uji + penjelasan>

BAB V  KESIMPULAN DAN SARAN
5.1  Kesimpulan                <jawab rumusan masalah/tujuan>
5.2  Saran                     <lanjutan pengembangan>

DAFTAR KEPUSTAKAAN             <alfabetis, APA, 1 spasi, menjorok 1,25 cm>
LAMPIRAN                       <kode program, dokumentasi, data pendukung>
BIODATA MAHASISWA
```

## B. Kajian teoritis / studi literatur (4 bab — tanpa bab Metode)

```
BAB I    PENDAHULUAN (1.1 Latar Belakang, 1.2 Rumusan Masalah, 1.3 Tujuan,
         1.4 Hipotesis jika ada, 1.5 Manfaat)
BAB II   TINJAUAN KEPUSTAKAAN
BAB III  HASIL DAN PEMBAHASAN
BAB IV   KESIMPULAN DAN SARAN
```

## C. Proposal Penelitian (yang beda dari laporan)

- Tidak dipakai: sampul khusus, pernyataan bebas plagiasi, deklarasi, abstrak.
- Bab metode **wajib** memuat jadwal pelaksanaan dan **perkiraan biaya penelitian**.
- Halaman pengesahan: cukup tanda tangan Koordinator Prodi (tanda tangan Dekan tidak
  diperlukan).
- Isi BAB I–III sebagian besar akan menjadi BAB I–III laporan akhir nanti.

## D. Laporan studi kasus **[perlu konfirmasi]**

Belum ada aturan resminya di panduan. Kerangka usulan (5 bab):

```
BAB I    PENDAHULUAN        <latar belakang kasus, batasan kasus, rumusan masalah, tujuan, manfaat>
BAB II   TINJAUAN KEPUSTAKAAN <teori yang dipakai menganalisis kasus>
BAB III  METODE              <jenis studi kasus, lokus/subjek, sumber data, teknik analisis>
BAB IV   HASIL DAN PEMBAHASAN <profil objek, kondisi nyata, analisis, temuan>
BAB V    KESIMPULAN DAN SARAN <simpulan kasus + rekomendasi>
```

## E. Laporan magang / kerja praktik / PKL **[perlu konfirmasi]**

Kerangka usulan: BAB I Pendahuluan → BAB II Profil Instansi → BAB III Pelaksanaan
Kegiatan (uraian kerja, jadwal, kendala) → BAB IV Simpulan dan Saran → Lampiran
(surat tugas, log book/kartu bimbingan, dokumentasi) → Biodata.

## F. Laporan praktikum mata kuliah (gaya contoh laporan mahasiswa)

```
Sampul            : Laporan <I/II/III/IV> Pratikum <Mata Kuliah> + judul + nama/NPM
KATA PENGANTAR    : diawali Bismillahirrahmanirrahim…, diakhiri tempat/tanggal + Penyusun
DAFTAR ISI        : titik-titik + nomor halaman (KATA PENGANTAR ii, DAFTAR ISI iii, bab dari 1)
BAB I  PENDAHULUAN    (1.1 Latar Belakang, 1.2 Rumusan Masalah, 1.3 Tujuan, 1.4 Manfaat)
BAB II LANDASAN TEORI
BAB III PROSES DAN HASIL   <langkah praktikum + Gambar 3.x di bawah tiap langkah>
BAB IV PENUTUP        (4.1 Kesimpulan, 4.2 Saran)
DAFTAR PUSTAKA
```

## G. Daftar isi kosong (format titik-titik)

> **[USULAN — bukan dari dokumen Anda]** Bagian ini adalah saran praktis umum, bukan aturan dari panduan FMIPA maupun permintaan user. Pakai hanya bila user setuju; kalau ragu, tanyakan dulu.


```
KATA PENGANTAR ..................................................... ii
DAFTAR ISI ......................................................... iii
BAB I PENDAHULUAN .................................................... 1
1.1 Latar Belakang ................................................... 1
1.2 Rumusan Masalah .................................................. 1
...
DAFTAR KEPUSTAKAAN ................................................... <n>
```

## H. Laporan praktikum versi rapi (pola Laporan VI — paling direkomendasikan)

```
Sampul
  Laporan <I/II/III/IV/VI> Pratikum Pemrograman Game
  JUDUL SINGKAT KAPITAL (mis. MEMBUAT PLAYER, KOIN, PERANGKAP, DAN TAMPILAN MENANG atau KALAH)
  Disusun untuk memenuhi / tugas mata kuliah Pemrograman Game
  Oleh: <NAMA> / <NPM>
  PROGRAM STUDI DIII MANAJEMEN INFORMATIKA · JURUSAN INFORMATIKA
  FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM UNIVERSITAS SYIAH KUALA
  BANDA ACEH, <BULAN> <TAHUN>

KATA PENGANTAR  (3 paragraf pendek: pembuka doa · isi laporan · penutup + kritik/saran)
                 diakhiri: Banda Aceh, <tanggal> / Penyusun, / NAMA / NPM : ...

DAFTAR ISI      (tab leader, halaman; memuat subsubbab 3.x.y)

BAB I PENDAHULUAN
  1.1 Latar Belakang       (1–2 paragraf: bagian game itu penting → apa yang dibuat → hasil)
  1.2 Rumusan Masalah      (2 poin bernomor: "Bagaimana membuat …?", "Bagaimana …?")
  1.3 Tujuan Praktikum     (2 poin, sejajar rumusan masalah)
  1.4 Manfaat Praktikum    (2 poin: bagi penulis, bagi pembaca)

BAB II LANDASAN TEORI      (satu subbab = satu konsep dasar yang dipakai di Bab III)
  2.1 <GameObject dan Component>
  2.2 <Transform, Rigidbody, dan Collider>
  2.3 <Trigger>
  2.4 <Skrip C# dan MonoBehaviour>
  2.5 <Canvas dan UI>

BAB III PROSES DAN HASIL PRAKTIKUM
  3.1 <Persiapan Proyek>            (versi engine, nama proyek, scene awal, lantai/cahaya)
       → Gambar 3.1  <judul>
  3.2 <Bagian utama 1>
      3.2.1 <langkah 1>             teks 2–4 kalimat + Gambar 3.2
      3.2.2 <langkah 2>             teks + Gambar 3.3
      3.2.3 <langkah skrip>         teks + blok kode (nama berkas.cs) + Gambar
  3.3 <Bagian utama 2>  3.3.1 … 3.3.2 … 3.3.3 …
  3.4 <Bagian utama 3>  3.4.1 … 3.4.2 … 3.4.3 …
  3.5 <Bagian utama 4>  3.5.1 … (Canvas, teks, panel, skrip pengatur)
  3.6 Hasil Akhir        (permainan dicoba: apa yang terjadi) → Gambar
  3.7 Struktur Berkas    (letak skrip/scene) → Gambar

BAB IV PENUTUP
  4.1 Kesimpulan    (per bagian: player / koin & perangkap / tampilan — masing-masing 1 paragraf;
                     menjawab rumusan masalah)
  4.2 Saran         (1 paragraf: animasi, nilai dari Inspector, suara, tombol panel)

DAFTAR PUSTAKA      (dokumentasi resmi engine + sumber lain; 2–5 entri, gaya APA)
```

Aturan wajib pada versi ini: **setiap gambar bernomor + berjudul**, **tidak ada
paragraf isi satu kalimat**, **kode program ditulis utuh**, **kesimpulan per bagian**.
