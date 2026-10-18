# -*- coding: utf-8 -*-
"""
Kerangka laporan akademik USK FMIPA sesuai _PANDUAN TA-TESIS 2024_Final.pdf (Bab V).

Dipakai sebagai titik awal untuk membuat .docx: margin, font, spasi, halaman pembuka,
judul bab/subjudul/subsubjudul, tabel, gambar, persamaan, TOC, dan daftar kepustakaan
sudah mengikuti aturan panduan.

Jalankan dengan:
    C:/Python314/python.exe buat_laporan_usk.py

Hasil contoh akan ditulis ke berkas OUT di bawah. Untuk tugas sungguhan: ubah OUT,
lalu panggil fungsi-fungsi yang tersedia. Jangan menimpa berkas draft milik user.
"""
import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp', 'contoh-laporan-usk.docx')

# ---------------------------------------------------------------- util XML ----

def _el(tag, **attrs):
    e = OxmlElement(tag)
    for k, v in attrs.items():
        e.set(qn(k), v)
    return e


def set_spacing(p, before=None, after=None, line=None, line_rule=None):
    """w:spacing harus berada sebelum w:ind / w:jc / w:rPr (urutan skema OOXML)."""
    pPr = p._p.get_or_add_pPr()
    sp = pPr.find(qn('w:spacing'))
    if sp is None:
        sp = OxmlElement('w:spacing')
        idx = len(pPr)
        for i, ch in enumerate(pPr):
            if ch.tag in (qn('w:contextualSpacing'), qn('w:ind'), qn('w:jc'), qn('w:rPr'), qn('w:sectPr')):
                idx = i
                break
        pPr.insert(idx, sp)
    for k, v in (('w:before', before), ('w:after', after), ('w:line', line), ('w:lineRule', line_rule)):
        if v is not None:
            sp.set(qn(k), v)
    return sp


def set_page_numbering(section, fmt='decimal', start=None):
    """fmt: 'decimal' (1,2,3) atau 'lowerRoman' (i,ii,iii)."""
    sectPr = section._sectPr
    for old in sectPr.findall(qn('w:pgNumType')):
        sectPr.remove(old)
    pn = OxmlElement('w:pgNumType')
    pn.set(qn('w:fmt'), fmt)
    if start is not None:
        pn.set(qn('w:start'), str(start))
    # pgNumType harus sesudah pgMar dan sebelum cols
    ref = sectPr.find(qn('w:cols'))
    if ref is not None:
        ref.addprevious(pn)
    else:
        sectPr.append(pn)


def footer_page_number(section, posisi='center'):
    """Nomor halaman dari field PAGE, footer 2,0 cm dari bawah."""
    section.footer_distance = Cm(2.0)
    p = section.footer.paragraphs[0]
    p.text = ''
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER if posisi == 'center' else WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run()
    fld = _el('w:fldChar', **{'w:fldCharType': 'begin'})
    instr = OxmlElement('w:instrText')
    instr.set(qn('xml:space'), 'preserve')
    instr.text = ' PAGE '
    end = _el('w:fldChar', **{'w:fldCharType': 'end'})
    run._r.append(fld)
    run._r.append(instr)
    run._r.append(end)
    set_run(run, size=12)


def enable_update_fields(doc):
    """Supaya Word menawarkan/di-set memperbarui field (TOC) saat berkas dibuka."""
    settings = doc.settings.element
    if settings.find(qn('w:updateFields')) is None:
        uf = OxmlElement('w:updateFields')
        uf.set(qn('w:val'), 'true')
        compat = settings.find(qn('w:compat'))
        if compat is not None:
            compat.addprevious(uf)
        else:
            settings.append(uf)


# ------------------------------------------------------------------ teks ------

def set_run(run, bold=False, italic=False, size=12, underline=False, color=None):
    run.font.name = 'Times New Roman'
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.underline = underline
    if color is not None:
        run.font.color.rgb = color
    rPr = run._element.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts')
        rPr.insert(0, rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:cs', 'w:eastAsia'):
        rf.set(qn(a), 'Times New Roman')
    return run


def new_doc():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)      # A4
    sec.left_margin, sec.top_margin = Cm(3.5), Cm(3.0)       # panduan 5.3.1
    sec.right_margin, sec.bottom_margin = Cm(3.0), Cm(3.0)
    st = doc.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(12)
    st.element.rPr.rFonts.set(qn('w:eastAsia'), 'Times New Roman')
    st.paragraph_format.line_spacing = 1.5
    st.paragraph_format.space_after = Pt(0)
    return doc


def para(doc, text='', align=None, bold=False, italic=False, size=12,
         underline=False, first_line=None, left=None, hanging=None,
         line=1.5, space_before=0, space_after=0, color=None, page_break=False):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    pf = p.paragraph_format
    if page_break:
        pf.page_break_before = True
    if first_line is not None:
        pf.first_line_indent = Cm(first_line)
    if left is not None:
        pf.left_indent = Cm(left)
    if hanging is not None:
        pf.left_indent = Cm(hanging)
        pf.first_line_indent = Cm(-hanging)
    set_spacing(p, before=str(int(space_before * 20)), after=str(int(space_after * 20)),
                line=str(int(line * 240)), line_rule='auto')
    if text:
        set_run(p.add_run(text), bold=bold, italic=italic, size=size,
                underline=underline, color=color)
    return p


def judul_bab(doc, nomor, judul, page_break=True):
    """Judul bab: TNR 14 bold kapital, rata tengah, nomor bab 1 spasi di atas judul."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if page_break:
        p.paragraph_format.page_break_before = True
    set_spacing(p, before='0', after='360', line='240', line_rule='auto')  # 1 spasi antar baris
    set_run(p.add_run(nomor.upper()), bold=True, size=14)
    set_run(p.add_run('\n'))
    set_run(p.add_run(judul.upper()), bold=True, size=14)
    # jarak judul bab ke baris pertama isi = 3 x 1,5 spasi
    para(doc, '', line=1.5, space_after=0)
    return p


def subjudul(doc, teks):
    """TNR 12 bold kapital, dari margin kiri, tanpa titik akhir, jarak 3 spasi dari paragraf."""
    p = doc.add_paragraph()
    set_spacing(p, before='540', after='0', line='240', line_rule='auto')
    set_run(p.add_run(teks.upper()), bold=True, size=12)
    return p


def subsubjudul(doc, teks):
    """TNR 12 bold, hanya huruf pertama kata pertama kapital."""
    p = doc.add_paragraph()
    set_spacing(p, before='360', after='0', line='240', line_rule='auto')
    set_run(p.add_run(teks), bold=True, size=12)
    return p


def isi(doc, teks):
    """Paragraf isi: menjorok 1,25 cm, rata kiri-kanan, 1,5 spasi."""
    return para(doc, teks, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_line=1.25)


def daftar(doc, teks, nomor=None):
    """Butir perincian bernomor (1., 2., …) sejajar dengan paragraf isi."""
    t = ('%s. ' % nomor if nomor else '') + teks
    return para(doc, t, align=WD_ALIGN_PARAGRAPH.JUSTIFY, left=1.25, hanging=0.75)


def judul_tabel(doc, nomor, teks):
    """Judul tabel: TNR 12, kecil (kecuali awal), tidak tebal, tanpa titik akhir, DI ATAS tabel."""
    multi = len(teks) > 70          # > sekitar satu baris -> rata kiri
    return para(doc, '%s. %s' % (nomor, teks),
                align=WD_ALIGN_PARAGRAPH.LEFT if multi else WD_ALIGN_PARAGRAPH.CENTER,
                size=12, line=1.0, space_before=18, space_after=3)


def keterangan_gambar(doc, nomor, teks):
    """Keterangan gambar: 1,5 spasi DI BAWAH gambar, satu baris rata tengah."""
    multi = len(teks) > 70
    return para(doc, '%s. %s' % (nomor, teks),
                align=WD_ALIGN_PARAGRAPH.LEFT if multi else WD_ALIGN_PARAGRAPH.CENTER,
                size=12, line=1.0, space_before=9, space_after=9)


def gambar(doc, path, lebar_cm=15.0):
    """Gambar rata tengah; lebar maksimal 15 cm supaya tidak melewati margin 3/3 cm."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(path, width=Cm(lebar_cm))
    return p


def persamaan(doc, teks, nomor):
    """Persamaan + nomor (2.3) rata kanan."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_spacing(p, line='240', line_rule='auto')
    set_run(p.add_run(teks), size=12, italic=True)
    set_run(p.add_run('\t'), size=12)
    set_run(p.add_run('(%s)' % nomor), size=12)
    p.paragraph_format.tab_stops.add_tab_stop(Cm(15.0), WD_TAB_ALIGNMENT.RIGHT)
    return p


def entri_pustaka(doc, teks):
    """Daftar kepustakaan: 1 spasi, baris kedua dst menjorok 1,25 cm."""
    return para(doc, teks, align=WD_ALIGN_PARAGRAPH.JUSTIFY, hanging=1.25,
                line=1.0, space_after=6)


def toc_field(doc, judul='DAFTAR ISI'):
    para(doc, judul, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14,
         line=1.0, space_after=12, page_break=True)
    p = doc.add_paragraph()
    set_spacing(p, line='240', line_rule='auto')
    r = p.add_run()
    b = _el('w:fldChar', **{'w:fldCharType': 'begin'})
    it = OxmlElement('w:instrText')
    it.set(qn('xml:space'), 'preserve')
    it.text = ' TOC \\o "1-3" \\h \\z \\u '
    sep = _el('w:fldChar', **{'w:fldCharType': 'separate'})
    t = OxmlElement('w:t')
    t.text = 'Klik kanan → Update Field untuk memperbarui daftar isi.'
    end = _el('w:fldChar', **{'w:fldCharType': 'end'})
    for e in (b, it, sep, t, end):
        r._r.append(e)
    return p


# ----------------------------------------------------------------- bagian -----

def sampul(doc, judul, jenis='TUGAS AKHIR', kalimat_gelar='memperoleh gelar Ahli Madya',
           nama='NAMA MAHASISWA', npm='000000000', prodi='D-III MANAJEMEN INFORMATIKA',
           departemen='INFORMATIKA', bulan_tahun='OKTOBER 2026', logo=None):
    """Sampul/halaman judul sesuai Lampiran 7 panduan (tanpa nomor halaman)."""
    para(doc, '', line=1.0, space_after=36)
    para(doc, judul.upper(), align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=18, line=1.5)
    para(doc, jenis.upper(), align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=16,
         line=1.0, space_before=36)
    para(doc, 'Diajukan untuk melengkapi tugas-tugas dan memenuhi syarat-syarat guna %s' % kalimat_gelar,
         align=WD_ALIGN_PARAGRAPH.CENTER, size=12, space_before=24)
    para(doc, 'Oleh:', align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_before=24)
    para(doc, nama.upper(), align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14,
         underline=True, line=1.0, space_before=24)
    para(doc, npm, align=WD_ALIGN_PARAGRAPH.CENTER, size=14, line=1.0)
    if logo and os.path.exists(logo):
        p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(logo, width=Cm(3.5))
    else:
        para(doc, '[Logo USK — hitam, center]', align=WD_ALIGN_PARAGRAPH.CENTER,
             italic=True, space_before=36, space_after=36)
    para(doc, 'PROGRAM STUDI %s' % prodi, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True,
         size=14, line=1.0)
    para(doc, 'DEPARTEMEN %s' % departemen, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True,
         size=14, line=1.0)
    para(doc, 'FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM', align=WD_ALIGN_PARAGRAPH.CENTER,
         bold=True, size=14, line=1.0)
    para(doc, 'UNIVERSITAS SYIAH KUALA, BANDA ACEH', align=WD_ALIGN_PARAGRAPH.CENTER,
         bold=True, size=14, line=1.0)
    para(doc, bulan_tahun.upper(), align=WD_ALIGN_PARAGRAPH.CENTER, bold=True,
         size=14, line=1.0)


def halaman_pengesahan(doc, judul, judul_inggris=None, nama='', npm='', prodi='',
                       pembimbing=('', ''), koordinator='', dekan='',
                       kalimat_bawah=''):
    """Pengesahan sesuai Lampiran 8 (judul Inggris wajib untuk Laporan TA/Tesis)."""
    para(doc, 'PENGESAHAN', align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=16,
         line=1.0, space_after=24, page_break=True)
    para(doc, judul.upper(), align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=16, line=1.5)
    if judul_inggris:
        para(doc, judul_inggris.upper(), align=WD_ALIGN_PARAGRAPH.CENTER, bold=True,
             size=14, line=1.5, space_before=12)
    para(doc, 'Oleh', align=WD_ALIGN_PARAGRAPH.CENTER, size=14, space_before=24)
    for label, val in (('Nama', nama), ('NPM', npm), ('Program Studi', prodi)):
        para(doc, '%s\t: %s' % (label, val), left=3.5, hanging=2.5, line=1.5)
    para(doc, '', line=1.0)
    para(doc, 'Menyetujui:', size=12, space_before=12)
    for lbl, nm in (('Pembimbing I,', pembimbing[0]), ('Pembimbing II,', pembimbing[1])):
        para(doc, lbl, size=12)
    para(doc, '', line=1.0)
    para(doc, '', line=1.0)
    for nm in pembimbing:
        para(doc, nm, size=12, underline=True, line=1.0)
        para(doc, 'NIP. ……………………', size=12, line=1.0, space_after=12)
    para(doc, 'Mengetahui:', size=12, space_before=12)
    para(doc, 'Dekan FMIPA\t\t\tKoordinator Program Studi', size=12)
    para(doc, 'Universitas Syiah Kuala,\tUniversitas Syiah Kuala,', size=12)
    para(doc, '', line=1.0)
    para(doc, dekan or '(………………………)', size=12, underline=True, line=1.0)
    para(doc, 'NIP. ……………………', size=12, line=1.0)
    if kalimat_bawah:
        para(doc, kalimat_bawah, align=WD_ALIGN_PARAGRAPH.CENTER, size=12,
             line=1.0, space_before=24)


def abstrak(doc, teks, kata_kunci, judul='ABSTRAK'):
    """Abstrak: maks 250 kata, 1 spasi, halaman sendiri; kata kunci 4-6 kata."""
    jml = len(teks.split())
    if jml > 250:
        raise ValueError('Abstrak %d kata — panduan menetapkan maksimum 250 kata.' % jml)
    para(doc, judul, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14, line=1.0,
         space_after=18, page_break=True)
    para(doc, teks, align=WD_ALIGN_PARAGRAPH.JUSTIFY, line=1.0)
    para(doc, 'Kata kunci: ' + kata_kunci, align=WD_ALIGN_PARAGRAPH.JUSTIFY, line=1.0,
         space_before=12)


def kata_pengantar(doc, paragraf_awal, pihak, paragraf_akhir, kota_tanggal, nama, npm):
    para(doc, 'KATA PENGANTAR', align=WD_ALIGN_PARAGRAPH.CENTER, bold=True, size=14,
         line=1.0, space_after=18, page_break=True)
    for t in paragraf_awal:
        isi(doc, t)
    for n, t in enumerate(pihak, 1):
        daftar(doc, t, n)
    for t in paragraf_akhir:
        isi(doc, t)
    para(doc, kota_tanggal, align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=24)
    para(doc, 'Penyusun,', align=WD_ALIGN_PARAGRAPH.RIGHT)
    para(doc, '', align=WD_ALIGN_PARAGRAPH.RIGHT)
    para(doc, '', align=WD_ALIGN_PARAGRAPH.RIGHT)
    para(doc, nama, align=WD_ALIGN_PARAGRAPH.RIGHT, bold=True, underline=True)
    para(doc, 'NPM. ' + npm, align=WD_ALIGN_PARAGRAPH.RIGHT)


# ------------------------------------------------------------------ demo ------

def main():
    doc = new_doc()
    # --- Bagian Pembuka: nomor Romawi kecil (judul & pengesahan tidak tampil) ---
    set_page_numbering(doc.sections[0], 'lowerRoman', 1)

    sampul(doc, 'CONTOH JUDUL PENELITIAN ANDA', jenis='PROYEK AKHIR',
           kalimat_gelar='memperoleh gelar Ahli Madya',
           nama='<Nama Mahasiswa>', npm='<NPM>')

    halaman_pengesahan(
        doc, 'CONTOH JUDUL PENELITIAN ANDA',
        judul_inggris='ENGLISH TITLE OF YOUR RESEARCH',
        nama='<Nama Mahasiswa>', npm='<NPM>',
        prodi='D-III Manajemen Informatika',
        pembimbing=('<Nama Pembimbing I>',
                    '<Nama Pembimbing II>'),
        koordinator='', dekan='',
        kalimat_bawah='Lulus Sidang Sarjana pada hari ………, ………, ………')

    abstrak(doc, 'Penelitian ini membangun sistem informasi penjualan produk berbasis '
                 'website pada <Nama Usaha>. (contoh isi abstrak — ganti dengan '
                 'ringkasan sungguhan: masalah, tujuan, metode, hasil, manfaat.)',
            kata_kunci='sistem informasi, penjualan, <produk>, framework, website')

    kata_pengantar(
        doc,
        ['Syukur Alhamdulillah dipanjatkan ke hadirat Allah SWT yang telah melimpahkan '
         'rahmat-Nya sehingga Tugas Akhir yang berjudul "…" dapat diselesaikan. '
         'Selawat dan salam disanjungkan kepada Nabi Besar Muhammad SAW. '
         'Tugas Akhir ini merupakan salah satu syarat yang harus dipenuhi untuk '
         'memperoleh gelar Ahli Madya di Program Studi D-III Manajemen Informatika, '
         'FMIPA USK.'],
        ['<Nama Dekan FMIPA>, selaku Dekan FMIPA USK.',
         'Bapak/Ibu Ketua Departemen Informatika FMIPA USK.',
         'Ibu <Nama Pembimbing I>, selaku Ketua Program Studi dan '
         'Pembimbing I.',
         'Ibu <Nama Pembimbing II>, selaku Pembimbing II.',
         'Kedua orang tua dan rekan-rekan D-III Manajemen Informatika.'],
        ['Penulis menyadari laporan ini masih jauh dari sempurna sehingga kritik dan '
         'saran yang membangun sangat diharapkan.'],
        'Banda Aceh, …………………', '<Nama Mahasiswa>', '<NPM>')

    toc_field(doc)

    # --- Bagian Isi: nomor Arab mulai 1, rata kanan bawah ---
    isi_sec = doc.add_section(WD_SECTION.NEW_PAGE)
    set_page_numbering(isi_sec, 'decimal', 1)
    footer_page_number(isi_sec, 'right')

    judul_bab(doc, 'BAB I', 'PENDAHULUAN')
    subjudul(doc, '1.1 Latar Belakang')
    isi(doc, 'Contoh paragraf latar belakang. Ganti dengan uraian sungguhan: hal-hal '
             'yang mendorong penelitian dan argumentasi pentingnya penelitian '
             'dilakukan. Paragraf menjorok 1,25 cm, rata kiri-kanan, spasi 1,5.')
    subjudul(doc, '1.2 Rumusan Masalah')
    isi(doc, 'Rumusan masalah dapat berbentuk pernyataan; tidak wajib berupa '
             'pertanyaan (Panduan 5.2.2.b).')
    subjudul(doc, '1.3 Tujuan Penelitian')
    daftar(doc, 'Membangun sistem informasi penjualan kopi berbasis website.', 1)
    daftar(doc, 'Menguji sistem dengan metode black-box testing.', 2)
    subjudul(doc, '1.4 Manfaat Penelitian')
    isi(doc, 'Contoh manfaat bagi pemilik usaha, pelanggan, dan penulis.')

    judul_bab(doc, 'BAB II', 'TINJAUAN KEPUSTAKAAN')
    subjudul(doc, '2.1 Sistem Informasi')
    isi(doc, 'Contoh isi tinjauan kepustakaan dengan sitasi gaya APA '
             '(Nama, tahun). Contoh: sistem informasi adalah … (Mulyanto, 2009).')
    subsubjudul(doc, '2.1.1 Komponen sistem informasi')
    isi(doc, 'Contoh subsubjudul: hanya huruf pertama kata pertama yang kapital.')
    subjudul(doc, '2.2 Kerangka Pemikiran')
    judul_tabel(doc, 'Tabel 2.1', 'Contoh judul tabel satu baris, rata tengah, '
                                  'tanpa titik akhir')
    t = doc.add_table(rows=2, cols=2)
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for r in range(2):
        for c in range(2):
            cell = t.cell(r, c)
            cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_run(cell.paragraphs[0].add_run('Kolom %d' % (c + 1)), size=11)
            set_spacing(cell.paragraphs[0], line='240', line_rule='auto')
    para(doc, 'Sumber: data penelitian (2026)', size=10, line=1.0, space_before=6)
    persamaan(doc, 'fk = μk · N', '2.1')

    judul_bab(doc, 'BAB III', 'METODE PENELITIAN')
    subjudul(doc, '3.1 Tempat dan Waktu Penelitian')
    isi(doc, 'Contoh: penelitian dilaksanakan di <Nama Usaha> pada bulan '
             'September—Desember 2026.')

    judul_bab(doc, 'BAB IV', 'HASIL DAN PEMBAHASAN')
    subjudul(doc, '4.1 Hasil')
    isi(doc, 'Contoh penyajian hasil. Sisipkan gambar dengan gambar(doc, path) lalu '
             'keterangan_gambar(doc, "Gambar 4.1", "...") di bawahnya.')

    judul_bab(doc, 'BAB V', 'KESIMPULAN DAN SARAN')
    subjudul(doc, '5.1 Kesimpulan')
    isi(doc, 'Contoh kesimpulan yang menjawab rumusan masalah dan tujuan.')
    subjudul(doc, '5.2 Saran')
    isi(doc, 'Contoh saran untuk pengembangan selanjutnya.')

    judul_bab(doc, 'DAFTAR KEPUSTAKAAN', '', page_break=True)
    entri_pustaka(doc, 'Mulyanto, A. (2009). Sistem Informasi Konsep dan Aplikasi. '
                       'Pustaka Pelajar. Yogyakarta.')
    entri_pustaka(doc, 'Pan, Y., Yuan, X., Jiang, L., & Zeng, G. (2018). Recent advances '
                       'in synthesis and photocatalytic applications. Chemical '
                       'Engineering Journal, 354, 407–431.')

    enable_update_fields(doc)
    doc.save(OUT)
    print('SAVED:', OUT)


if __name__ == '__main__':
    main()
