# -*- coding: utf-8 -*-
"""
Contoh lengkap SATU BAB (BAB III Metode Penelitian) untuk laporan/proposal USK FMIPA.

Kenapa skrip, bukan atur manual di Word: margin, spasi, indentasi, penomoran
Tabel/Gambar, dan posisi nomor halaman harus konsisten dan bisa dicek ulang.

Yang dicontohkan di sini (semua bagian yang paling sering salah):
  1. Judul bab 14 pt tebal rata tengah + jarak 3 x 1,5 spasi ke isi.
  2. Subjudul `3.1` / subsubjudul `3.3.2` - nomor & teks dijalankan (tab), bold,
     tanpa titik di akhir nomor.
  3. Tabel: judul DI ATAS tabel, rata tengah, tanpa titik akhir, header berulang
     antar halaman (`w:tblHeader`).
  4. Gambar: satu antarmuka = satu nomor Gambar + keterangan DI BAWAH gambar,
     dan gambar + keterangannya dipaksa satu halaman (`keep_with_next`).
     Ini yang mencegah keterangan "yatim" di puncak halaman berikutnya.
  5. Kotak penanda untuk gambar yang belum tersedia (lebar tabel dipaksa).
  6. Nomor halaman kanan bawah, angka Arab mulai 1.

Jalankan:  C:/Python314/python.exe gen_bab3_laporan.py
Ubah SS/OUT sebelum dipakai untuk tugas sungguhan. Jangan menimpa draf user.
"""

import os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SS = 'folder-tangkapan-layar'      # ganti ke folder gambar tugas yang dikerjakan
OUT = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp', 'contoh-bab3.docx')

LEBAR_GAMBAR = Cm(14.0)   # area teks = 21 - 3,5 - 3,0 = 14,5 cm; jangan lebih
TEKS = 1.5
TB = 'Tabel 3.{}'
GB = 'Gambar 3.{}'

# (nomor gambar, judul keterangan, nama berkas atau None kalau belum ada)
ANTARMUKA = [
    (6, 'Halaman booking jadwal konsultasi', None),
    (7, 'Halaman lacak dokumen', None),
]


def new_doc():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
    sec.left_margin = Cm(3.5)
    sec.right_margin = sec.top_margin = sec.bottom_margin = Cm(3.0)
    sec.footer_distance = Cm(2.0)          # panduan: footer 2,0 cm
    st = doc.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(12)
    rPr = st.element.get_or_add_rPr()
    rf = rPr.find(qn('w:rFonts'))
    if rf is None:
        rf = OxmlElement('w:rFonts')
        rPr.append(rf)
    for a in ('w:ascii', 'w:hAnsi', 'w:eastAsia', 'w:cs'):   # eastAsia wajib
        rf.set(qn(a), 'Times New Roman')
    st.paragraph_format.line_spacing = TEKS
    st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.space_after = Pt(0)
    return doc


def par(doc, text='', *, indent=True, spacing=TEKS, bold=False, size=12,
        align=None, before=0, after=0, justify=True):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = spacing
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    if indent:
        pf.first_line_indent = Cm(1.25)
    p.alignment = align or (WD_ALIGN_PARAGRAPH.JUSTIFY if justify
                            else WD_ALIGN_PARAGRAPH.LEFT)
    if text:
        r = p.add_run(text)
        r.bold = bold
        r.font.size = Pt(size)
    return p


def bab_title(doc, nomor, judul):
    """BAB III / METODE PENELITIAN: 14 pt tebal, 1 spasi antar baris, halaman baru."""
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.page_break_before = True
    pf.line_spacing = 1.0
    r = p.add_run(nomor.upper() + chr(10) + judul.upper())
    r.bold = True
    r.font.size = Pt(14)
    for _ in range(4):            # 3 x 1,5 spasi ke baris pertama isi
        par(doc, '', indent=False, justify=False)


def subjudul(doc, teks):
    par(doc, '', indent=False, justify=False)     # 2 x 1,5 spasi dari paragraf atas
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(teks)          # contoh: '3.1' + tab + judul
    r.bold = True
    r.font.size = Pt(12)


def subsubjudul(doc, teks):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run(teks)
    r.bold = True
    r.font.size = Pt(12)
    par(doc, '', indent=False, justify=False)


def caption(doc, text, before=6, after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.line_spacing = TEKS
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    p.add_run(text).font.size = Pt(12)
    return p


def gambar(doc, berkas, judul):
    """Gambar + keterangan DI BAWAHNYA, dipaksa satu halaman.

    keep_with_next pada paragraf gambar = keterangan ikut pindah halaman.
    keep_together pada paragraf gambar = gambar tidak dipecah antar halaman.
    """
    if berkas:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        pf = p.paragraph_format
        pf.line_spacing = 1.0
        pf.space_before = Pt(6)
        pf.space_after = Pt(0)
        pf.keep_with_next = True
        pf.keep_together = True
        p.add_run().add_picture(os.path.join(SS, berkas), width=LEBAR_GAMBAR)
        caption(doc, judul)
        return
    # belum ada tangkapan layar -> kotak penanda; lebar tabel HARUS dipaksa
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    for tag, attrs in (('w:tblW', {'w:w': str(int(14.0 / 2.54 * 1440)),
                                   'w:type': 'dxa'}),
                       ('w:tblLayout', {'w:type': 'fixed'})):
        el = OxmlElement(tag)
        for k, v in attrs.items():
            el.set(qn(k), v)
        tblPr.append(el)
    borders = OxmlElement('w:tblBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        el = OxmlElement('w:' + edge)
        el.set(qn('w:val'), 'dashed')
        el.set(qn('w:sz'), '6')
        el.set(qn('w:color'), '808080')
        borders.append(el)
    tblPr.append(borders)
    grid = t._tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for gc in grid.findall(qn('w:gridCol')):
            gc.set(qn('w:w'), str(int(14.0 / 2.54 * 1440)))
    trPr = t.rows[0]._tr.get_or_add_trPr()
    h = OxmlElement('w:trHeight')
    h.set(qn('w:val'), str(int(7.0 / 2.54 * 1440)))
    h.set(qn('w:hRule'), 'atLeast')
    trPr.append(h)
    cell = t.cell(0, 0)
    cell.width = Cm(14.0)
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.line_spacing = 1.0
    r = p.add_run('[ TEMPATKAN TANGKAPAN LAYAR DI SINI ]' + chr(10) + chr(10) +
                  'Hapus kotak ini, lalu sisipkan gambar dengan Insert > Pictures '
                  '(lebar maksimal 14 cm).')
    r.font.size = Pt(10)
    r.italic = True
    r.font.color.rgb = RGBColor(0x80, 0x80, 0x80)
    cap = caption(doc, judul)
    cap.paragraph_format.keep_with_next = True


def tabel_kop(doc, header, rows, widths, font_size=10):
    """Tabel bergaris dengan baris judul berulang antar halaman."""
    t = doc.add_table(rows=1, cols=len(header))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]
        c.text = ''
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.0
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(font_size)
    t.rows[0]._tr.get_or_add_trPr().append(OxmlElement('w:tblHeader'))
    for data in rows:
        cells = t.add_row().cells
        for i, val in enumerate(data):
            cells[i].text = ''
            p = cells[i].paragraphs[0]
            p.paragraph_format.line_spacing = 1.0
            p.paragraph_format.space_before = Pt(1)
            p.paragraph_format.space_after = Pt(1)
            p.alignment = (WD_ALIGN_PARAGRAPH.CENTER if i == 0
                           else WD_ALIGN_PARAGRAPH.LEFT)
            p.add_run(str(val)).font.size = Pt(font_size)
    for row in t.rows:
        for i, w in enumerate(widths):
            row.cells[i].width = Cm(w)
    return t


def nomor_halaman(sec):
    """Angka Arab, kanan bawah. Jangan set w:start pada section bab berikutnya."""
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    fp.paragraph_format.line_spacing = 1.0
    run = fp.add_run()
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    run._r.addnext(fld)
    pn = sec._sectPr.find(qn('w:pgNumType'))
    if pn is None:
        pn = OxmlElement('w:pgNumType')
        sec._sectPr.append(pn)
    pn.set(qn('w:fmt'), 'decimal')


def main():
    doc = new_doc()
    nomor_halaman(doc.sections[0])

    bab_title(doc, 'BAB III', 'METODE PENELITIAN')

    subjudul(doc, '3.1\tWaktu dan Tempat Penelitian')
    par(doc, 'Paragraf isi: menjorok 1,25 cm, rata kiri-kanan, spasi 1,5. '
             'Sebutkan lokasi objek penelitian dan lokasi pengembangan, '
             'lalu jangka waktu penelitian.')
    par(doc, 'Paragraf kedua. Rujuk tabel/gambar dari dalam teks sebelum '
             'ilustrasinya muncul, mis. "... ditunjukkan pada Tabel 3.1."')

    caption(doc, TB.format(1) + ' Jadwal penelitian')
    tabel_kop(doc,
              ['No', 'Uraian kegiatan', 'Okt 2026', 'Nov 2026', 'Des 2026'],
              [['1', 'Pengumpulan data dan studi literatur', 'v', 'v', ''],
               ['2', 'Analisis kebutuhan sistem', '', 'v', 'v']],
              widths=[1.0, 8.4, 1.6, 1.6, 1.6])
    par(doc, 'Keterangan: v = kegiatan dilaksanakan pada bulan tersebut',
        indent=False, justify=False, spacing=1.0, size=10, before=4)

    subjudul(doc, '3.2\tAlat dan Bahan')
    par(doc, 'Sebutkan perangkat keras dan perangkat lunak yang benar-benar dipakai. '
             'Jangan menyalin spesifikasi milik mahasiswa lain.')

    subjudul(doc, '3.3\tMetode Kerja')
    par(doc, 'Jelaskan jenis penelitian, pendekatan, dan metode pengembangan '
             '(mis. Waterfall) beserta alasan pemilihannya.')

    subsubjudul(doc, '3.3.1\tAnalisis Kebutuhan')
    par(doc, 'Data dikumpulkan melalui tiga cara sebagai berikut.')
    for no, teks in (('a.', 'Wawancara, yaitu ...'),
                     ('b.', 'Observasi, yaitu ...'),
                     ('c.', 'Studi pustaka, yaitu ...')):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.line_spacing = TEKS
        pf.left_indent = Cm(1.25)
        pf.first_line_indent = Cm(-0.5)
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.add_run(no + '\t' + teks).font.size = Pt(12)
        pf.tab_stops.add_tab_stop(Cm(1.25))

    subjudul(doc, '3.3.2\tPerancangan Sistem')
    par(doc, 'Perancangan digambarkan dengan flowchart, use case diagram, activity '
             'diagram, dan ERD.')
    subsubjudul(doc, '3.3.2.1\tFlowchart Alur Sistem')
    par(doc, 'Jelaskan alur pengunjung dan alur admin, lalu rujuk gambarnya.')
    gambar(doc, None, GB.format(1) + ' Flowchart alur sistem')

    subsubjudul(doc, '3.3.2.2\tRancangan Antarmuka (UI)')
    par(doc, 'Setiap halaman dijelaskan satu per satu, masing-masing dengan satu '
             'nomor Gambar dan satu keterangan sendiri.')
    for no, judul, berkas in ANTARMUKA:
        par(doc, 'Penjelasan untuk halaman ini. Sebutkan kolom/field yang ada, '
                 'siapa penggunanya, dan apa yang bisa dilakukan di halaman itu. '
                 'Tampilan halaman ini ditunjukkan pada ' + GB.format(no) + '.')
        gambar(doc, berkas, GB.format(no) + ' ' + judul)

    subsubjudul(doc, '3.3.3\tImplementasi')
    par(doc, 'Penerapan rancangan menjadi aplikasi: migration/tabel, routing, '
             'view, dan hasil di kedua sisi pengguna.')

    subsubjudul(doc, '3.3.4\tPengujian')
    par(doc, 'Jelaskan metode pengujian (mis. black box testing), data uji valid '
             'dan tidak valid, lalu rujuk tabel skenario pengujian.')
    caption(doc, TB.format(2) + ' Rencana pengujian fungsional (black box testing)')
    tabel_kop(doc,
              ['No', 'Fitur yang diuji', 'Skenario pengujian', 'Hasil yang diharapkan'],
              [['1', 'Booking jadwal', 'Mengisi formulir dengan data lengkap',
                'Data tersimpan dan kode booking terbentuk'],
               ['2', 'Pelacakan dokumen', 'Memasukkan kode yang tidak terdaftar',
                'Muncul pesan kode tidak ditemukan']],
              widths=[0.9, 3.6, 5.1, 5.4])

    doc.save(OUT)
    print('TERSIMPAN:', OUT)


if __name__ == '__main__':
    main()
