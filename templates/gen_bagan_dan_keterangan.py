# -*- coding: utf-8 -*-
"""
Dokumen Word berdiri sendiri: BAGAN (gambar bersih) + keterangan tugas tiap jabatan.

Dipakai saat user minta "gambar bagan + keterangan di bawahnya, buat di Word".
Isi keterangan diambil dari sumbernya (LKP/skripsi bab struktur organisasi) lalu
ditulis sebagai daftar bernomor 1..n dengan sub-butir a/b/c dan 1/2/3.

Jalankan:  C:/Python314/python.exe gen_bagan_dan_keterangan.py
Ubah GAMBAR dan KETERANGAN dulu. Jangan menimpa draf user (simpan nama baru).

Dua hal yang WAJIB diperhatikan:
  1. Lebar gambar = lebar area teks PERSIS. Margin 2,5/2,5 -> 16,0 cm;
     kalau memakai margin USK (3,5/3,0) -> 14,5 cm, jangan 16 cm.
     Gambar +/- 1 mm sudah menghindari pembulatan Word sehingga tidak turun
     ke halaman berikutnya.
  2. Keterangan gambar di bawah gambar + keep_with_next (lihat gen_bab3_laporan.py).
"""

import os
from docx import Document
from docx.shared import Pt, Cm, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn

GAMBAR = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp',
                      'Bagan_Struktur_Organisasi_polos.png')
OUT = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp',
                   'Struktur_Organisasi.docx')

JUDUL = ['STRUKTUR ORGANISASI', 'PT. BANK ACEH SYARIAH CABANG SIGLI']
KETERANGAN_GAMBAR = ['Gambar 2.1', 'Struktur Organisasi PT. Bank Aceh Syariah Cabang Sigli']
SUMBER = 'Sumber: PT. Bank Aceh Syariah Cabang Sigli'

# (nomor, teks pembuka jabatan, [(huruf, teks), ...], [(nomor, teks), ...])
KETERANGAN = [
    (1, 'Kepala Cabang/Pimpinan, yaitu orang yang mengawasi, memeriksa secara '
        'terperinci transaksi yang terjadi di bank serta mengelola semua kegiatan '
        'yang berlangsung pada PT. Bank Aceh Syariah Cabang Sigli. Tugas pokok:',
     [('a', 'Mengkoordinir, mengarahkan, membina serta mengawasi seluruh kegiatan '
             'personil dari kantor cabang dan bertanggung jawab langsung kepada direksi.'),
      ('b', 'Melaksanakan segala peraturan/ketentuan dan prosedur kegiatan operasional '
             'yang telah digariskan oleh Bank Indonesia.')], []),
    (2, 'Wakil Pemimpin (Wapim), yaitu unsur pimpinan atau pembantu pimpinan yang '
        'membantu tugas-tugas pemimpin cabang.', [], []),
]


def susun():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.5)
    sec.top_margin = sec.bottom_margin = Cm(2.5)
    area = Emu(sec.page_width - sec.left_margin - sec.right_margin)
    lebar_gambar = Cm(round(area.cm, 2) - 0.08)      # -0,8 mm: hindari pembulatan

    st = doc.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(12)
    rPr = st.element.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        from docx.oxml import OxmlElement
        rf = OxmlElement('w:rFonts')
        rPr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):
        rf.set(qn(a), 'Times New Roman')
    pf = st.paragraph_format
    pf.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    pf.space_before = Pt(0)
    pf.space_after = Pt(0)

    def par(teks='', *, align=WD_ALIGN_PARAGRAPH.JUSTIFY, kiri=0, gantung=None,
            bold=False, italic=False, before=0, after=0):
        p = doc.add_paragraph()
        p.alignment = align
        f = p.paragraph_format
        f.left_indent = Cm(kiri)
        if gantung:
            f.first_line_indent = Cm(-gantung)
        f.space_before = Pt(before)
        f.space_after = Pt(after)
        f.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
        if teks:
            r = p.add_run(teks)
            r.bold = bold
            r.italic = italic
        return p

    for t in JUDUL:
        par(t, align=WD_ALIGN_PARAGRAPH.CENTER, bold=True)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(GAMBAR, width=lebar_gambar)

    for t in KETERANGAN_GAMBAR:
        par(t, align=WD_ALIGN_PARAGRAPH.CENTER, before=6)
    par(SUMBER, align=WD_ALIGN_PARAGRAPH.CENTER, italic=True, after=12)

    par('Keterangan:', align=WD_ALIGN_PARAGRAPH.LEFT, before=6, after=2)
    for no, judul, huruf, angka in KETERANGAN:
        par('%d. %s' % (no, judul), kiri=0.75, gantung=0.75, before=8)
        for lr, teks in huruf:
            par('%s. %s' % (lr, teks), kiri=1.4, gantung=0.6)
        for nmr, teks in angka:
            par('%s. %s' % (nmr, teks), kiri=2.0, gantung=0.6)

    doc.save(OUT)
    print('TERSIMPAN:', OUT, '| lebar gambar', round(lebar_gambar.cm, 2), 'cm')


if __name__ == '__main__':
    susun()
