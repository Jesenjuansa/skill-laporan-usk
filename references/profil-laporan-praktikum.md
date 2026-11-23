# Profil Laporan Praktikum (gaya Jesen Juansa) — hasil baca Laporan I–VI

Berkas ini merangkum **pola nyata laporan praktikum yang Anda buat sendiri** (Laporan
I, II, III, IV, VI, dan Tugas Pemrograman Game di `D:\lab game`). Dipakai kalau
tugasnya laporan mata kuliah/praktikum — **bukan** Laporan TA/Proyek Akhir (untuk itu
pakai `struktur-laporan.md`).

Penanda: `[USER]` pola dari berkas Anda · `[KOREKSI]` hal yang ternyata belum sesuai
panduan/bermasalah dan harus diperbaiki · `[PERLU KONFIRMASI]` belum pasti.

## 1. Pola sampul `[USER]`

Berkas: `LAPORAN <N>.docx`, PDF `<NPM> <NAMA> LAPORAN <N>.pdf`.

```
Laporan <I/II/III/IV/V/VI> Pratikum Pemrograman Game      ← baris pembuka (catatan: "Pratikum" memang ejaan di berkas Anda)
<JUDUL BESAR KAPITAL, tebal>                              ← isi sesuai topik praktikum
Disusun untuk memenuhi
tugas mata kuliah Pemrograman Game
Oleh:
<NAMA>                                                    ← tebal, bergaris bawah
<NPM>
<logo USK>
PROGRAM STUDI DIII MANAJEMEN INFORMATIKA
JURUSAN INFORMATIKA
FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM UNIVERSITAS SYIAH KUALA
BANDA ACEH, <BULAN> <TAHUN>
```

Judul tiap laporan yang sudah dipakai (untuk menjaga sambungan antar laporan):
- Laporan II — *Implementasi Fitur Gameplay pada Game Platformer Menggunakan Construct 3*
- Laporan III — *Implementasi Fitur Gameplay pada Game Platformer Menggunakan Construct 3*
- Laporan IV — *Instalasi Unity untuk Pengembangan Game*
- Laporan VI — *Membuat Player, Koin, Perangkap, dan Tampilan Menang atau Kalah* (Unity)

## 2. Halaman depan `[USER]`

| Halaman | Isi |
|---|---|
| KATA PENGANTAR | diawali `Bismillahirrahmanirrahim.` → 1 paragraf syukur + judul laporan → 1 paragraf isi laporan → 1 paragraf kritik & saran → `Banda Aceh, <tanggal>` → `Penyusun,` → NAMA → `NPM : <NPM>` |
| DAFTAR ISI | manual (bukan field TOC), format: `KATA PENGANTAR\tii`, `DAFTAR ISI\tiii`, `BAB I PENDAHULUAN\t1`, `1.1  Latar Belakang\t1` …; nomor halaman depan angka Romawi kecil |

## 3. Susunan bab `[USER]`

Bentuk ringkas (Laporan II–IV):
```
BAB I   PENDAHULUAN      1.1 Latar Belakang · 1.2 Rumusan Masalah · 1.3 Tujuan Praktikum · 1.4 Manfaat Praktikum
BAB II  LANDASAN TEORI   2.1 … · 2.2 … (teori yang dipakai di praktikum, 3–5 subbab)
BAB III PROSES DAN HASIL PRAKTIKUM   langkah kerja + gambar tiap langkah
BAB IV  PENUTUP          4.1 Kesimpulan · 4.2 Saran
DAFTAR PUSTAKA
```

Bentuk rinci (Laporan VI — dipakai kalau praktikumnya bertahap/berlapis):
```
BAB III PROSES DAN HASIL PRAKTIKUM
3.1 <persiapan proyek>
3.2 <bagian 1>   3.2.1 · 3.2.2 · 3.2.3 (satu subsubbab per langkah kecil)
3.3 <bagian 2>   3.3.1 · 3.3.2 …
3.x <hasil akhir: uji coba + tampilan game>
3.y <struktur berkas>
BAB IV PENUTUP
```

Ciri penulisan `[USER]`: Bahasa Indonesia lugas, memakai kata "saya", kalimat
langkah berbentuk perintah ("Klik kanan di jendela Hierarchy, pilih 3D Object →
Cylinder, lalu beri nama Player"), setiap langkah diikuti satu gambar
(`Gambar 3.x  <keterangan singkat>`), dan Bab III ditutup dengan hasil uji coba.

## 4. Format dokumen `[USER]` + `[KOREKSI]`

| Hal | Yang dipakai di berkas Anda | Status |
|---|---|---|
| Ukuran kertas | A4 | sesuai |
| Font | Times New Roman 12 pt | sesuai |
| Spasi isi | 1,5 | sesuai |
| Paragraf | menjorok ~1,25 cm, rata kiri-kanan | sesuai |
| Judul bab | 14 pt tebal, rata tengah, `BAB I` lalu `PENDAHULUAN` di baris berikut | sesuai |
| Subjudul | 12 pt tebal, nomor `1.1` (Laporan VI menulis `1.1  Latar Belakang` dengan dua spasi) | sesuai (pakai satu spasi) |
| Subsubjudul | `3.2.1` tebal | sesuai |
| Margin | Laporan VI: kiri/atas/kanan/bawah **3,00 cm** semua. Laporan IV & proposal: kiri 3,50, kanan **2,50** | `[KOREKSI]` panduan FMIPA: kiri 3,50 cm, atas/kanan/bawah 3,00 cm → **kanan harus 3,00**, bukan 2,50 |
| Nomor halaman | ada di footer | `[KOREKSI]` pastikan: halaman depan angka Romawi kecil (ii, iii), isi mulai 1, dan sampul tidak bernomor |
| Judul bab mulai halaman baru | ya | sesuai |

## 5. Kesalahan yang harus dicek pada laporan praktikum `[KOREKSI]`

Diambil dari masalah yang benar-benar ada di berkas/laporan yang dikerjakan:

1. **Gambar milik orang lain.** Laporan IV pertama memakai 12 tangkapan layar dari
   laporan teman (Naima). Hanya boleh dipakai kalau user mengizinkan; sisanya
   diambil dari komputer sendiri atau dikosongkan.
2. **Gambar tidak diberi keterangan / keterangan tidak cocok dengan isinya.** Setiap
   gambar WAJIB punya keterangan `Gambar <bab>.<nomor>` dan isinya harus sesuai
   langkahnya.
3. **Sitasi tidak ada padahal daftar pustaka ada.** Laporan VI punya 5 entri daftar
   pustaka tetapi **0 sitasi** di dalam teks. Kalau daftar pustaka dicantumkan,
   minimal rujuk sumbernya di teks (mis. `(Unity Technologies, 2022)`).
4. **Daftar pustaka tidak urut abjad** (Laporan VI: Unity Manual, Rigidbody,
   Collider, Canvas, lalu Microsoft). Harus alfabetis: Microsoft dulu, baru Unity.
5. **Sumber non-teks tanpa penjelasan** (Tugas Pemrograman Game berisi 2 halaman
   gambar saja, tanpa teks). Kalau tugasnya berupa gambar, beri keterangan minimal.
6. **Data pribadi di dalam laporan** (nama, NPM, nama pembimbing) — wajar di naskah,
   tapi **jangan** dimasukkan ke skill/repo.
7. **Versi perangkat tidak konsisten** antar laporan (Naima menulis Unity
   `2022.3.62f2`, komputer Anda memasang `2022.3.62f3`). Tulis versi yang benar-benar
   dipakai; cek di Unity Hub menu Installs.
8. **Angka/ukuran di langkah harus sama dengan yang dipakai** (posisi objek, skala,
   nama variabel skrip). Jangan menyalin angka dari laporan lain.

## 6. Daftar pustaka laporan praktikum `[USER]`

Format yang dipakai di Laporan VI (dianggap paling rapi dari berkas Anda):
```
Unity Technologies. (2022). Unity Manual 2022.3 (LTS). Diakses dari https://docs.unity3d.com/2022.3/Documentation/Manual/index.html
Microsoft. (2024). C# documentation. Diakses dari https://learn.microsoft.com/en-us/dotnet/csharp/
```
Urutkan alfabetis, satu spasi, baris kedua menjorok 1,25 cm.

## 7. Kalau praktikumnya memakai Unity `[USER]`

Pola Laporan VI yang bisa diikuti:
- sebutkan versi Unity dan nama proyek di awal Bab III;
- tampilkan skrip C# utuh dengan nama berkasnya (`PlayerGerak.cs`), lalu jelaskan
  fungsi tiap bagian;
- tambahkan tabel/daftar singkat "objek yang dibuat + komponennya" kalau banyak;
- akhiri Bab III dengan hasil uji coba (tombol yang dipakai, apa yang terjadi) dan
  struktur folder (`Assets/Scripts`, `Assets/Scenes`).

## 8. Belum perlu dikarang `[PERLU KONFIRMASI]`

- Apakah dosen meminta daftar gambar/tabel untuk laporan praktikum (di Laporan I–VI
  tidak ada). Tanyakan bila jumlah gambar banyak.
- Apakah laporan praktikum perlu halaman pengesahan (di berkas Anda tidak ada).
