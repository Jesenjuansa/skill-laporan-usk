# Format & Tata Cara Penulisan USK

Aturan format wajib (Panduan TA/Tesis FMIPA USK 2024 bagian 5.3), aturan tabel, gambar, dan persamaan, serta kaidah bahasa/ejaan (5.5 + PUEBI).

## BAGIAN 1 — Ketentuan umum, halaman, judul, paragraf, kutipan

### 5.3.1 Ketentuan umum

- Kertas **A4 (210 × 297 mm) 80 gsm**, putih, seluruh lembar harus sama warna dan
  kualitasnya.
- **Huruf: Times New Roman 12 pt** untuk seluruh Bagian Pembuka, Isi, dan Penutup.
  Pengecualian: **judul bab**, teks pada **tabel**, **grafik/ilustrasi** lain boleh
  memakai huruf/ukuran sesuai kebutuhan.
- **Margin**:
  - kiri = **3,50 cm**
  - atas = **3,00 cm**
  - kanan = **3,00 cm**
  - bawah = **3,00 cm**
- **Spasi**: seluruh Bagian Isi **1,5 spasi**. Pengecualian:

| Bagian | Spasi |
|---|---|
| Abstrak (Indonesia & Inggris) | 1 spasi |
| Daftar isi | 1 spasi, **antar bab 2 spasi** |
| Judul tabel / keterangan gambar lebih dari satu baris | 1 spasi |
| Isi tabel / isi lampiran | 1–1,5 spasi |
| Nomor bab dengan judul bab | 1 spasi |
| Judul bab dengan baris pertama / subjudul | **3 × 1,5 spasi** |
| Subjudul / subsubjudul lebih dari satu baris | 1 spasi |
| Baris terakhir paragraf dengan subjudul baru | **2 × 1,5 spasi** |
| Baris terakhir keterangan tabel/gambar dengan paragraf di bawahnya | **2 × 1,5 spasi** |
| Kutipan lebih dari 5 baris | 1 spasi |
| Sumber bacaan pada Daftar Kepustakaan | 1 spasi, indensi 1,25 cm pada baris kedua dst. |

### 5.3.2 Penomoran halaman

- **Bagian Pembuka**: angka **Romawi kecil** (i, ii, iii, …).
  - Halaman **judul** dan **pengesahan** tidak mencantumkan nomor (tetap dihitung).
  - Nomor pertama yang tampak = halaman abstrak / kata pengantar, sesuai posisinya
    dihitung dari halaman judul.
  - Letak: **tengah bawah**, footer **2,0 cm**.
- **Bagian Isi dan Penutup**: angka **Arab** (1, 2, 3, …).
  - Letak: **kanan bawah**, footer **2,0 cm**.
  - BAB I mulai dari **1** (restart), bukan melanjutkan nomor Romawi.
- Sampul tidak bernomor.

### 5.3.3 Judul bab

- TNR **14 pt**, **kapital**, **tebal**.
- Nomor bab dan judul bab berjarak **1 spasi**.
- Judul bab dengan baris pertama/subjudul berjarak **3 × 1,5 spasi**.
- Di dokumen Word: nomor bab dan judul bab biasanya satu paragraf
  (`BAB I` + baris baru + `PENDAHULUAN`), rata tengah, spasi tunggal di antaranya.

### 5.3.4 Subjudul

- TNR **12 pt**, **kapital**, **tebal**.
- Penomoran angka Arab `bab.nomor` (contoh `1.1`, `2.3`), **tanpa titik di akhir**.
  `[USER]` dikonfirmasi 18 Okt 2026: pakai **`1.1` TANPA titik** pada nomornya
  (mengikuti badan naskah panduan; contoh Daftar Isi Lampiran 13 yang menulis
  `1.1.` tidak dipakai).
- Dimulai dari **margin kiri** (bukan menjorok).
- Bila lebih dari satu baris: baris kedua 1 spasi, mulai di bawah huruf pertama baris
  di atasnya.
- Jarak ke paragraf bawahnya 1,5 spasi; jarak dari baris terakhir paragraf
  sebelumnya 3 spasi.
- Istilah/nama asing di subjudul mengikuti aturan penulisan yang berlaku (miring).

### 5.3.5 Subsubjudul

- TNR **12 pt**, **tebal**.
- **Hanya huruf pertama kata pertama** yang kapital, kecuali ada kata yang memang
  harus berkapital sesuai ketentuan.
- Penomoran `bab.subjudul.subsubjudul` (contoh `2.3.1`), **tanpa titik di akhir**.
- Mulai dari margin kiri; baris lanjutan 1 spasi; jarak ke paragraf bawahnya 1,5
  spasi; jarak dari paragraf sebelumnya 1,5 spasi.

### 5.3.6 Paragraf baru

- Baris pertama paragraf menjorok **1,25 cm** dari margin kiri.
- Jarak antar paragraf = **1,5 spasi**.
- Rata **kiri-kanan (justify)**.
- **Hindari paragraf yang hanya terdiri dari satu kalimat.**

### 5.3.7 Kutipan atau rujukan

- **Kutipan > 5 baris**: diketik **1 spasi**, seluruh baris menjorok **1,25 cm**
  (setentang awal paragraf baru), tanpa tanda petik. Jarak baris akhir paragraf
  sebelumnya dan paragraf sesudahnya tetap 1,5 spasi.
- **Kutipan < 5 baris** dianggap rujukan dalam teks:
  - `Menurut Guenther (1999) persyaratan minimum …`
  - `Persyaratan minimum … (Guenther, 1999).`
- Aturan penulisan rujukan (nama akhir + tahun):

| Jumlah penulis | Contoh |
|---|---|
| Satu | Kim (2002) / (Kim, 2002) |
| Dua | Kim and Lee (2002) / (Kim and Lee, 2002) |
| Tiga atau lebih | Miller et al. (2002) / (Miller et al., 2002) |
| Penulis sama, tahun sama | Smith et al. (2002a) / Smith et al. (2002b) |

Catatan: setiap kutipan harus jelas sumbernya sehingga pembaca mudah menelusuri.

### 5.3.8 Ilustrasi (ringkasan)

Ilustrasi = tabel, grafik, diagram alir, foto, atau gambar. Detail lengkap di
`format-penulisan.md`.

### Setelan Word yang memenuhi aturan ini

Kalau membangun .docx dengan python-docx (lihat `templates/buat_laporan_usk.py`):

```
section.page_width  = Cm(21.0); section.page_height = Cm(29.7)
section.left_margin = Cm(3.5)
section.top_margin = section.right_margin = section.bottom_margin = Cm(3.0)
style = doc.styles['Normal']; style.font.name = 'Times New Roman'; style.font.size = Pt(12)
style.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')   # WAJIB
style.paragraph_format.line_spacing = 1.5
style.paragraph_format.space_after = Pt(0)
```

- Judul bab: paragraf rata tengah, 2 baris (`BAB I` / `PENDAHULUAN`), 14 pt bold,
  spasi dalam paragraf 1,0 (nomor bab–judul bab 1 spasi), sebelum judul diberi jarak
  dan `page_break_before = True` supaya tiap bab mulai halaman baru.
- Subjudul/subsubjudul: 1 spasi antar baris kalau lebih dari satu baris.
- Footer: bagian pembuka `PgNumType fmt=lowerRoman`, bagian isi `fmt=decimal start=1`;
  posisi nomor tengah bawah vs kanan bawah diatur lewat tab pada footer.
- Hati-hati: section BAB berikutnya **jangan** diberi `pgNumType start=…` warisan,
  karena nomor halaman akan mengulang.


## BAGIAN 2 — Tabel, gambar, dan persamaan

Ilustrasi = tabel, grafik, diagram alir, foto, atau gambar. Ilustrasi yang baik
menyajikan informasi lebih efektif dan mengurangi kalimat panjang.

### Penomoran (berlaku sama untuk tabel & gambar)

- Angka **Arab**, dimulai dengan **nomor bab** + **titik**, lalu **nomor urut** + **titik** → contoh: `Tabel 2.1.`, `Gambar 3.2.`
  `[PANDUAN]` Catatan PUEBI di bagian 3 file ini: angka penomoran deret ilustrasi
  ditulis **tanpa titik di belakang** (`Gambar 2.1`), dan subjudul pun `[USER]` tanpa
  titik. Kalau menemukan captions sumber (LKP/skripsi lain) berbentuk `Gambar 2.1`
  tanpa titik, itu konsisten dengan PUEBI — jangan "membetulkan" jadi bertitik; ikuti
  bentuk yang dipakai naskah user sendiri, dan tanyakan bila belum ada contohnya.
- Tabel/gambar pertama di Bab II = `Tabel 2.1.` / `Gambar 2.1.`
- Nomor di Daftar Tabel/Daftar Gambar harus sama dengan yang di teks.

### Tabel

- **Judul tabel di ATAS tabel.**
- Huruf **kecil** kecuali huruf awal, **tidak dicetak tebal**, **tidak diakhiri
  tanda titik**.
- Judul **satu baris** → rata **tengah**; judul **lebih dari satu baris** → rata
  **kiri**, baris lanjutan 1 spasi dimulai di bawah huruf awal judul.
- Jarak paragraf terakhir teks sebelum judul tabel = **3 spasi**; jarak baris
  terakhir tabel dengan paragraf di bawahnya = **3 spasi**.
- **Isi tabel** boleh memakai huruf dan spasi bervariasi (1–1,5 spasi), biasanya
  sedikit lebih kecil dari teks (mis. 11 pt).
- **Sumber/keterangan** ditulis **di bawah tabel**, 1 spasi, **Times New Roman 10 pt**.
- Contoh judul: `Tabel 2.1. Desain dan analisis ortogonal hidrolisis asam sekam jagung
  pada variasi konsentrasi asam, rasio serat jagung: asam sulfat, waktu, dan
  temperatur (dimodifikasi dari Xiao et al., 2018)`
- Tabel yang dimodifikasi dari rujukan berbahasa asing: tambahkan kata
  **"dimodifikasi dari"** pada judulnya.
- Penempatan: boleh di halaman tersendiri **setelah** halaman teks yang
  memperkenalkannya, atau di halaman yang sama dengan teks sebelumnya. Di halaman
  tersendiri: posisi di tengah halaman, jarak sama dari margin kiri/kanan, tidak
  melewati margin.
- Tabel kecil: boleh lebih dari satu tabel dalam satu halaman.
- Tabel boleh membujur/melintang sesuai ukuran.
- Bila tidak muat satu halaman: lanjutan di halaman berikutnya **mengulang judul
  kolom**.

### Gambar

- **Judul gambar + keterangan di BAWAH gambar, jarak 1,5 spasi.**
- Huruf **kecil** kecuali huruf awal, **tidak tebal**, **tanpa titik akhir**.
- Judul/keterangan **lebih dari satu baris** → mulai dari **margin kiri**, 1 spasi,
  baris kedua di bawah huruf awal judul.
- Judul/keterangan **satu baris** → rata **tengah** halaman.
- Sumber gambar dari pihak lain **wajib disebutkan di akhir keterangan** di dalam
  **tanda kurung**, boleh ditambah **"dimodifikasi dari"**.
- Gambar boleh ditempatkan di halaman sendiri, terpisah dari teks.
- Beberapa data tidak perlu di Bagian Isi, cukup di **Lampiran**.
- **Keterangan tidak boleh terpisah halamannya dari gambar.** Set `keep_with_next`
  pada paragraf gambar dan `keep_together` agar gambar tidak dipecah antar halaman.
- **Satu tangkapan layar antarmuka = satu nomor Gambar**, bukan digabung beberapa
  halaman ke satu nomor dan bukan ditempel jadi satu gambar gabungan. Urutan bloknya:
  paragraf penjelas → gambar → keterangan di bawahnya.

### Persamaan

- Nomor persamaan memakai angka Arab dalam tanda kurung, mengikuti nomor bab:
  `(2.3)` = persamaan **ketiga** yang ditulis pada **Bab II**.
- Nomor ditempatkan **di ujung kanan** baris persamaan (rata kanan), sejajar dengan
  baris persamaan.
- **Keterangan simbol** ditulis di bawah persamaan, tiap simbol dijelaskan
  (satu per baris), contoh:

```
        fk = μk · N                                   (2.3)

dengan
fk : gaya gesekan kinetik (N)
μk : koefisien gesekan kinetik
N  : gaya normal (N)
```

### Praktik di Word (python-docx / Word COM)

- Tabel: `doc.add_table(rows, cols)`, set gaya garis, judul tabel sebagai paragraf
  terpisah **sebelum** tabel, centang; bila lewat satu baris → rata kiri.
- Gambar: `run.add_picture(path, width=Cm(...))` dalam paragraf rata tengah. Lebar
  maksimal **14 cm** — area teks dengan margin kiri 3,5 cm dan kanan 3,0 cm hanya
  **14,5 cm**, jadi 15 cm sudah melewati margin. Jangan memperbesar melebihi ukuran
  asli tangkapan layar (hasilnya blur). Contoh lengkap: `templates/gen_bab3_laporan.py`.
  Hitung lebar dari section, jangan dihafal: `Emu(sec.page_width - sec.left_margin -
  sec.right_margin).cm`, lalu kurangi ~0,8 mm agar pembulatan Word tidak memindahkan
  gambar ke halaman berikutnya. Dokumen berdiri sendiri dengan margin 2,5 cm boleh
  memakai bagan selebar **16 cm**; naskah USK tetap 14 cm.
- Kotak penanda untuk gambar yang belum ada: tabel 1×1 bergaris putus-putus, tetapi
  lebarnya harus dipaksa di level tabel (`w:tblW`, `w:tblLayout type="fixed"`,
  `w:gridCol`), bukan hanya `cell.width`, kalau tidak kotaknya meluber ke margin.
- Nomor `Tabel 2.1.`/`Gambar 2.1.` ditulis manual (bukan caption otomatis Word)
  supaya konsisten dengan format panduan dan mudah diatur.


## BAGIAN 3 — Kaidah bahasa & ejaan (PUEBI)

### Dasar

- Bahasa yang dipakai adalah **bahasa tulis yang baku**. Kebakuan terlihat pada
  ketepatan, kelugasan, kelengkapan unsur, dan kecermatan penggunaan ejaan.
- Bahasa harus **efisien dan efektif**: mengikuti kaidah baku, hemat kata dan
  ungkapan.
- Harus terlihat **hubungan antar kalimat yang logis**: sebab-akibat, kesejajaran,
  dan penjelasan terhadap suatu pernyataan.
- Ejaan mengikuti **PUEBI** (Permendikbud 50/2015) — panduan mencantumkan PUEBI
  lengkap sebagai Lampiran 18 (huruf kapital, penulisan kata, angka & bilangan,
  tanda baca, unsur serapan).

### Ciri tulisan yang dinilai benar (dari rubrik penilaian panduan)

Kriteria bahasa pada rubrik: "Menggunakan bahasa tulis yang baku, lugas, efisien,
dan efektif; menggunakan ejaan, perhurufan, dan tanda baca dengan benar; memilih
kata dan istilah dengan tepat."

### Aturan PUEBI yang paling sering muncul (ringkas)

**Huruf kapital** dipakai untuk huruf pertama awal kalimat, nama orang/agama/Tuhan,
gelar kehormatan, nama lembaga/geografi; **tidak** dipakai untuk nama jenis/satuan
ukur (mis. `ikan mujair`, `5 ampere`) atau kata tugas dalam nama.

**Kata depan** (`di`, `ke`, `dari`) ditulis **terpisah**; awalan `di-`/`ke-` menempel
pada kata kerja (mis. `di dalam lemari` vs `disimpan`).

**Bentuk ulang** memakai tanda hubung: `anak-anak`, `terus-menerus`. Bentuk ulang
gabungan kata mengulang unsur pertama: `surat kabar` → `surat-surat kabar`.

**Gabungan kata** yang lazim (kata majemuk/istilah khusus) dipisah: `duta besar`,
`rumah sakit jiwa`, `simpan empat`. Gabungan kata yang sudah padu diserangkaikan:
`beasiswa`, `kacamata`, `olahraga`, `sukarela`.

**Angka dan bilangan**:
- Bilangan yang dapat dinyatakan dengan satu atau dua kata ditulis dengan huruf,
  kecuali dipakai berurutan dalam perincian. Bilangan pada awal kalimat ditulis
  dengan huruf (kalau terlalu panjang, susunan kalimatnya diubah).
- Angka dipakai untuk ukuran panjang/berat/luas/isi/waktu dan nilai uang
  (`0,5 cm`, `Rp5.000,00`), nomor alamat, dan nomor bagian karangan.
- **Tanda titik tidak dipakai** di belakang angka penomoran deret digital pada
  judul tabel/bagan/grafik/gambar (`Tabel 1.1`, `Gambar 1.1`).
- Koma dipakai sebagai tanda desimal (`12,5 m`); titik untuk ribuan yang
  menunjukkan jumlah (`13.000`).

**Tanda baca penting**:
- Titik dua untuk perincian yang merupakan penjelasan/pemerian.
- Titik koma memisahkan rincian yang berupa klausa atau perincian yang sudah
  memakai koma.
- Koma sebelum kata penghubung setara (`tetapi`, `melainkan`, `sedangkan`) dan di
  belakang ungkapan penghubung antarkalimat (`oleh karena itu`, `jadi`).
- Tanda petik ( `"…"` ) untuk petikan langsung dan judul artikel/bab; **tidak** untuk
  judul buku (judul buku pakai huruf miring).
- Tanda elipsis didahului dan diikuti spasi; di akhir kalimat jadi empat titik.

**Unsur serapan**: kata/istilah asing yang miring mengikuti ejaan aslinya
(mis. *de facto*, *force majeur*); istilah yang sudah diserap ditulis sesuai kaidah
Indonesia. Nama Latin spesies ditulis miring.

### Rambu praktis menulis isi laporan

> **[USULAN — bukan dari dokumen Anda]** Bagian ini adalah saran praktis umum, bukan aturan dari panduan FMIPA maupun permintaan user. Pakai hanya bila user setuju; kalau ragu, tanyakan dulu.


1. **Kalimat efektif**: satu gagasan pokok per kalimat; hindari kalimat bertele-tele
   dan kata mubazir ("adalah merupakan", "agar supaya", "di mana" sebagai penghubung).
2. **Kalimat pasif** sering lebih tepat untuk laporan ("sistem dibangun dengan
   Laravel", "data dianalisis menggunakan…"), tetapi jangan sampai menghilangkan
   pelaku yang penting.
3. **Kesejajaran bentuk** dalam perincian (semua frasa kerja atau semua nomina).
4. **Konsistensi istilah** — sekali memakai satu istilah (mis. "antarmuka"), pakai
   istilah itu seterusnya, jangan berganti-ganti.
5. **Istilah teknis** yang belum baku: tulis miring pada penyebutan pertama,
   sertakan padanan Indonesia dalam tanda kurung, mis. *black-box testing*
   (pengujian kotak hitam).
6. Hindari **bahasa lisan** ("gitu", "banget", "kayak"), **singkatan tidak baku**
   ("dgn", "yg", "dll" ditulis "dan lain-lain" bila di dalam kalimat resmi),
   dan **angka di awal kalimat**.
7. Rujuk tabel/gambar dari dalam teks ("… ditunjukkan pada Tabel 2.1") sebelum
   tabel/gambar itu muncul.
8. Jangan mengulang seluruh isi tabel/gambar dalam bentuk kalimat; cukup bahas
   hal pentingnya.

### Cara menyesuaikan untuk user

- Tulis **Bahasa Indonesia baku**, tetapi saat menjelaskan sesuatu **kepadanya**
  (bukan di dalam laporan) pakai bahasa sederhana dan sebutkan alasan setiap
  keputusan.
- Jangan memakai markdown pada jawaban di terminal — teks polos.

## BAGIAN 4 — Pola tulisan yang dipakai user (diambil dari berkasnya)

Pola-pola ini muncul berulang di laporan/proposal user, jadi aman diikuti
(penanda `[UMUM]` = kebiasaan dari berkas, bukan aturan panduan):

1. **Paragraf isi 3–6 kalimat**, diawali penanda hubungan yang eksplisit:
   "Berdasarkan kondisi tersebut, …", "Selain itu, …", "Sejalan dengan hal tersebut, …",
   "Akibatnya, …", "Dengan demikian, …". Hindari paragraf satu kalimat.
2. **Rumusan masalah bisa berbentuk pernyataan** ("Belum tersedianya …"), asal
   jumlahnya sejajar dengan jumlah tujuan dan manfaat. Sering 4 poin di proposal,
   2–3 poin di laporan praktikum.
3. **Setiap butir tujuan/manfaat dimulai kata kerja** (Merancang, Memusatkan,
   Memfasilitasi, Membantu) dan menjawab butir rumusan masalah yang sama nomornya.
4. **Latar belakang praktikum** berisi: pentingnya bagian yang dibuat → apa yang
   akan dibuat → hasil yang diharapkan. Cukup 1–2 paragraf.
5. **Bab II praktikum** hanya memuat konsep dasar yang benar-benar dipakai di Bab III
   (bukan teori panjang); 1 subbab = 1 konsep, masing-masing 2–4 kalimat.
6. **Langkah di Bab III ditulis perintah kerja** ("Klik kanan → 3D Object → Cylinder,
   beri nama Player, atur posisi …"), memakai istilah menu asli aplikasi.
7. **Kode program**: blok lengkap, diawali nama berkas, memakai nama variabel/fungsi
   berbahasa Indonesia (mis. `kecepatan`, `koinTerkumpul`, `PerbaruiTeks`).
8. **Kesimpulan** menjawab rumusan masalah satu per satu, biasanya 2–4 paragraf pendek.
9. **Saran** 1 paragraf, berupa rencana pengembangan lanjutan yang konkret.

### Cacat yang pernah terjadi di berkas user (jangan diulang)

| Cacat | Berkas | Perbaikan |
|---|---|---|
| Subbab ada di daftar isi tetapi bab kosong | LAPORAN UTS | daftar isi harus sama dengan isi |
| NPM semua anggota kelompok sama | LAPORAN UTS | tiap anggota NPM sendiri |
| Judul di kata pengantar tidak sama dengan judul sampul | LAPORAN UTS | samakan |
| Daftar pustaka tidak ada padahal memakai aplikasi | LAPORAN 1–3 | cantumkan sumber resmi |
| Keterangan gambar tidak konsisten (titik/strip) | LAPORAN 1–4 | pakai satu gaya (gaya Laporan VI) |
| Bagian "3.2 Jebakan dan player berkedip…" isinya soal koin | LAPORAN 3 | judul subbab harus sesuai isi |

## CEK-CEPAT SEBELUM SERAH (jalankan skrip ini)

```python
# cek_cepat.py — C:/Python314/python.exe cek_cepat.py "D:/lab game/LAPORAN X.docx"
import sys, re, docx
from docx.oxml.ns import qn
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
d = docx.Document(sys.argv[1])
els = list(d.element.body)
img = cap = tanpa_cap = 0
for i, el in enumerate(els):
    if el.tag == W + 'p' and el.find('.//' + W + 'drawing') is not None:
        img += 1
        nxt = ''.join(t.text or '' for t in els[i + 1].iter(W + 't')).strip() if i + 1 < len(els) else ''
        if not re.match(r'(Gambar|Sumber)', nxt):
            tanpa_cap += 1
ps = [p.text.strip() for p in d.paragraphs]
cap = len([p for p in ps if re.match(r'Gambar\s*\d', p)])
satu = [p for p in ps if len(p.split()) > 8 and p.endswith('.')
        and len([s for s in re.split(r'(?<=[.!?])\s+', p) if s]) == 1]
s = d.sections[0]
print('margin   %.2f/%.2f/%.2f/%.2f cm' % (s.left_margin.cm, s.top_margin.cm,
                                           s.right_margin.cm, s.bottom_margin.cm))
print('gambar   %d | keterangan %d | gambar tanpa keterangan %d' % (img, cap, tanpa_cap))
print('paragraf 1 kalimat: %d' % len(satu))
print('daftar pustaka ada:', any('DAFTAR PUSTAKA' in p.upper() for p in ps))
print('kode program (using/public class):', sum(1 for p in ps if p.startswith(('using ', 'public '))))
```

Target lulus: **gambar tanpa keterangan = 0**, **paragraf 1 kalimat = 0**,
margin 3,50/3,00/2,50/3,00 cm (atau sesuai permintaan user), daftar pustaka ada.
