# Mencari & mengekstrak gambar referensi (bagan, struktur organisasi, skema)

Dipakai saat user minta gambar pendukung laporan (struktur organisasi mitra,
bagan kerja, skema) yang harus **bisa ditelusuri ke sumbernya**.

## 1. Jangan mulai dari mesin pencari gambar

Gambar bagan organisasi instansi kecil (cabang bank, kantor, sekolah) hampir tidak
pernah terindeks di Google/Bing Images. Pencarian gambar justru mengembalikan hasil
tak berhubungan (mesin mengabaikan kutip/frasa) — tidak layak dibuang waktu.

Mulai dari **pencarian teks web** dengan kata kunci dokumen, bukan dengan kata kunci gambar:

```
"<nama instansi>" "struktur organisasi" cabang <lokasi> pdf
"<nama instansi>" "<lokasi>" skripsi repository
"Gambar 4.1" "struktur organisasi" "<nama instansi>" cabang
```

Tambahan kata `skripsi`, `laporan kerja praktik`, `LKP`, `repository`, `pdf` sangat
membantu: bagan itu biasanya ada sebagai **Gambar 2.1 / 4.1** di skripsi/LKP
mahasiswa lain yang meneliti instansi yang sama. Repository kampus terbuka
(mis. `repository.ar-raniry.ac.id`) cocok untuk instansi di Aceh.

Cek deskripsi hasil untuk pola `Gambar X.Y Struktur Organisasi ... Sumber: ...`.

## 2. Ekstrak gambar dari PDF, jangan screenshot

Screenshot browser = resolusi layar, miring, terpotong kotak lain. Render halaman
langsung dari PDF dengan `pymupdf` (400 dpi minimum untuk bagan dengan teks kecil):

```python
import pymupdf
doc = pymupdf.open("lkp.pdf")
p = doc[31]                                   # indeks halaman = nomor cetak - 1 (kurangi halaman depan)
pix = p.get_pixmap(dpi=400, clip=pymupdf.Rect(x0, y0, x1, y1))   # satuan POIN, bukan piksel
pix.save("bagan.png")
```

### Menentukan batas crop yang tepat

Jangan menebak koordinat dari hasil crop sebelumnya (biasanya sisi kanan/bawah
terpotong). Ambil dari objek PDF-nya:

```python
for x0, y0, x1, y1, txt, *_ in p.get_text("blocks"):   # kotak teks = kotak bagan
    print(round(x0,1), round(y0,1), round(x1,1), round(y1,1), txt.strip()[:40])
for b in p.get_drawings():                             # garis penghubung/kotak
    print(b["rect"], b["type"])
```

Batas bagan = min `x0`/`y0` dan max `x1`/`y1` dari blok teks + garis, lalu beri
margin ~8–12 pt. **Kotak terakhir di kolom terpanjang** (mis. `Security` di bawah
`Umum/SDI`) menentukan batas bawah — berhenti **sebelum** blok caption
(`Gambar 2.1 ...`), jangan ikut terpotong setengah.

Bagain bercaption bawah sering tumpang tindih: blok caption mulai lebih tinggi
dari garis bawah kotak terakhir. Periksa dengan daftar semua kata berkoordinat
di zona itu:

```python
for w in p.get_text("words"):
    if y_min - 2 < w[1] < y_max + 10: print([round(v,1) for v in w[:4]], w[4])
```

Simpan juga **halaman utuh** (dpi 200) yang memuat caption + keterangan jabatan:
itu bukti sumber untuk user dan bahan tabel "tugas tiap jabatan".

## 3. Verifikasi crop secara visual sebelum menyerahkan

`vision_analyze` hasil PNG-nya dengan pertanyaan tertutup (ya/tidak), bukan
"jelaskan gambar": *apakah semua kotak utuh termasuk sisi kanan kotak terakhir dan
garis bawah kotak paling bawah, apakah ada caption yang ikut?* Model vision sering
menebak tepi gambar — kalau jawabannya ragu ("mungkin"), daerah zoom-kan
(`region=[...]`) atau ulangi crop, jangan diteruskan ke user apa adanya.

**Jangan percaya vision untuk satu kotak yang mepet tepi bawah.** Model berulang kali
menyatakan "kotak Security sudah punya garis bawah" padahal belum. Ambil angka dari
objek PDF, bukan dari mata: kotak staf di PDF adalah drawing bertipe `fs` (fill+stroke),
jadi `rect`-nya = kotak penuh. Batas bawah bagan = `max(rect.y1)` dari drawing `fs`,
dan crop berhenti beberapa poin di bawah angka itu (jangan pakai `max(y1)` semua
drawing: ada garis bus selebar halaman jauh di bawah bagan).

## 4. Kalau user minta versi "polosan" — gambar ulang, jangan bersihkan watermark

Menghapus watermark dari gambar orang lain = mengubah karya orang; hasilnya juga
berkualitas rendah (watermark menembus di belakang teks berswara kertas). Gambar
ulang dari struktur yang sama.

Pakai `scripts/buat_bagan_organisasi.py` (isi `SEKSI` sesuai sumber, ukuran kanvas
sudah disetel ke area teks Word). Aturan gambar ulang:

- **Struktur & label dipertahankan sama**, termasuk urutan kotak. Koreksi yang boleh
  dan sebaiknya dilakukan: salah ketik jelas (`Costumer Service` -> `Customer
  Service`). Perubahan yang lebih dari koreksi ejaan (`Supir` -> `Sopir`, mengubah
  kalimat keterangan yang tidak gramatika) **sebutkan ke user di jawaban** supaya
  bisa ditolak — jangan diam-diam.
- Kanvas = lebar area teks Word, rasio 1,55–1,60 (bukan persegi panjang sembarang),
  supaya bagan besar dan tidak mengecil saat ditempel.
- Selalu simpan **PNG 400 dpi** (untuk Word) **dan SVG** (untuk disunting Word/
  Inkscape). Skripnya sudah mengeset `ax.set_aspect('auto')` + `subplots_adjust(0..1)`;
  tanpa itu koordinat hasil tidak cocok dengan inci kanvas dan teks jadi lonjong.
- Peringatan yang tetap disampaikan: struktur bisa sudah berubah (jabatan/pimpinan
  berganti) — untuk laporan, konfirmasikan ke instansi saat penelitian; sumber versi
  redraw ditulis `Sumber: <Instansi> <Cabang>, diolah penulis, <tahun>`.

## 5. Serahkan bagan + keterangan jabatan sebagai SATU berkas Word

User biasanya tidak mau gambar terpisah dari teks keterangannya. Susun dokumen:
judul -> gambar (lebar = area teks) -> keterangan (`Gambar 2.1` / judul / Sumber) ->
`Keterangan:` + daftar jabatan 1..n dengan sub-butir a/b/c dan 1/2/3. Generator +
format sudah ada di `templates/gen_bagan_dan_keterangan.py`.

Keterangan jabatan **diambil dari halaman sumber yang sama** (LKP/skripsi itu)
dan ditulis ulang kalimatnya bila rusak tata bahasanya; jangan mengarang tugas
jabatan yang tidak tertulis di sumber.

## 6. Menyerahkan ke user

- Letakkan di folder tugasnya (Proyek Akhir: `D:\PROYEK AKHIR\GAMBAR REFERENSI\`),
  nama berkas deskriptif: `Struktur_Organisasi_<Instansi>_<Cabang>.png`.
- Sertakan **halaman sumber utuh** sebagai lampiran bukti.
- Sebut sumber lengkap (penulis, judul karya, institusi, nomor halaman, URL) di chat,
  dan tampilkan isi bagan sebagai tabel di jawaban supaya bisa dipakai tanpa buka gambar.
- **Selalu beri peringatan penggunaan** (aturan user: tidak boleh menyerupai karya
  orang lain):
  - bagan dari skripsi/LKP orang lain punya watermark kampus dan bukan milik user →
    tawarkan **gambar ulang bersih** dari struktur yang sama, atau minta salinan resmi
    ke instansi saat penelitian.
  - kalau memakai versi nilai: sumber ditulis `Sumber: <Instansi> <Cabang>, diolah
    penulis, <tahun>` — bukan mengaku milik sendiri.
  - data bisa sudah berubah (staf/pimpinan berganti) → sebut bahwa nama pejabat di
    dokumen lama belum tentu berlaku, jangan ditambahkan ke laporan tanpa konfirmasi.
    Tahun LKP-nya juga sebutkan (mis. "data 2019") supaya user tahu batas kesegarannya.
