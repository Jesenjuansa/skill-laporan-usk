# -*- coding: utf-8 -*-
"""Generator BAB HASIL (BAB IV) laporan magang / kerja praktik USK FMIPA.

Kenapa skrip dan bukan atur manual di Word: nomor subbab, nomor tabel, header tabel
berulang, dan jumlah hari pada tabel rekapitulasi harus konsisten dengan data kartu
kendali. Semua dihitung dari satu sumber data di bawah.

Yang dicontohkan:
  1. Subbab 4.1 rincian kegiatan harian -> Tabel 4.1 (header berulang antar halaman).
  2. Narasi yang dibaca dari data, bukan dari ingatan: jumlah hari kerja, hari tanpa
     kegiatan, rentang tanggal.
  3. Subbab 4.2 rekapitulasi jenis kegiatan -- jumlah hari dihitung dari daftar
     tanggal, diurutkan dari yang terbanyak.
  4. Subbab 4.3 kendala & solusi (butir a/b/c/d).
  5. Subbab 4.4 pembahasan yang merujuk balik ke bagan di bab profil
     ("... pada Gambar 2.1") -- nomor gambar milik bab tempat bagan berada.

Isi KEGIATAN dan JENIS di bawah adalah CONTOH BENTUK. Ganti dengan data kartu kendali
user; jangan memakai isi contoh ini sebagai isi laporan siapa pun.

Jalankan:  C:/Python314/python.exe gen_bab_hasil_kegiatan.py
"""

import os
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

OUT = r"C:/Users/Lenovo/Downloads"          # ganti ke folder tugas (mis. D:/MAGANG)
NAMA_BERKAS = "BAB IV <nama laporan> (revisi).docx"
TEKS, TAB, FS_TAB = 1.5, 1.0, 11
LEBAR_GAMBAR = Cm(14.0)      # area teks 14,5 cm; jangan lebih

# ---- sumber data: satu baris per hari kerja, apa adanya dari kartu kendali ----
# Urutkan kronologis di sini; kartu kendali sering menaruh baris tambahan di bawah.
KEGIATAN = [
    ("1 Juli 2026",  "Melakukan orientasi lingkungan kerja dan menerima arahan tugas"),
    ("2 Juli 2026",  "Membantu pengisian formulir administrasi sesuai ketentuan"),
    ("3 Juli 2026",  "Melakukan pengecekan kelengkapan formulir"),
    ("6 Juli 2026",  "Membantu pemberian stempel pengesahan dokumen"),
    ("7 Juli 2026",  "Melakukan penyortiran dokumen berdasarkan kategori pelayanan"),
    ("8 Juli 2026",  "Menyusun dokumen administrasi berdasarkan urutan tanggal"),
    ("9 Juli 2026",  "Sakit"),
    ("10 Juli 2026", "Membantu kegiatan administrasi harian"),
]

# ---- rekapitulasi: nama jenis kegiatan + daftar tanggal pelaksanaannya ----
# Jumlah hari SELALU dihitung dari len(tanggal), jangan diketik manual.
JENIS = [
    ("Pengisian formulir administrasi", ["2 Juli"]),
    ("Pemberian stempel pengesahan dokumen", ["6 Juli"]),
    ("Pengecekan kelengkapan formulir", ["3 Juli"]),
    ("Penyortiran dokumen berdasarkan kategori", ["7 Juli"]),
    ("Penataan dan penyusunan dokumen", ["8 Juli"]),
    ("Orientasi lingkungan kerja", ["1 Juli"]),
]

HARI_TANPA_KEGIATAN = "Sakit"      # isi = apa adanya dari kartu kendali


# ===================== helper dokumen (sama untuk semua bab) =====================
def new_doc():
    doc = Document()
    s = doc.sections[0]
    s.page_width, s.page_height = Cm(21.0), Cm(29.7)
    s.left_margin = Cm(3.5)
    s.top_margin = s.right_margin = s.bottom_margin = Cm(3.0)
    s.footer_distance = Cm(2.0)
    st = doc.styles["Normal"]
    st.font.name = "Times New Roman"
    st.font.size = Pt(12)
    rPr = st.element.get_or_add_rPr()
    rf = rPr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts"); rPr.append(rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), "Times New Roman")     # eastAsia wajib
    st.paragraph_format.line_spacing = TEKS
    st.paragraph_format.space_before = Pt(0)
    st.paragraph_format.space_after = Pt(0)
    return doc


def par(doc, text="", *, indent=True, spacing=TEKS, align=WD_ALIGN_PARAGRAPH.JUSTIFY,
        left=None, before=0, after=0, size=12, keep_next=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.line_spacing = spacing
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if left is not None:
        pf.left_indent = Cm(left)
    if indent:
        pf.first_line_indent = Cm(1.25)
    if keep_next:
        pf.keep_with_next = True
    p.alignment = align
    if text:
        p.add_run(text).font.size = Pt(size)
    return p


def judul_bab(doc, nomor, judul):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.page_break_before = True; pf.line_spacing = 1.0
    r = p.add_run(nomor.upper() + "\n" + judul.upper())
    r.bold = True; r.font.size = Pt(14)


def subjudul(doc, nomor, judul, page_break=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf = p.paragraph_format
    pf.line_spacing = 1.0
    if page_break:
        pf.page_break_before = True
    pf.keep_with_next = True
    r = p.add_run(nomor + "\t" + judul.upper())
    r.bold = True; r.font.size = Pt(12)
    par(doc, "", indent=False, align=WD_ALIGN_PARAGRAPH.LEFT)


def butir(doc, label, text, left=1.25, hang=0.6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    pf = p.paragraph_format
    pf.line_spacing = TEKS
    pf.left_indent = Cm(left); pf.first_line_indent = Cm(-hang)
    pf.tab_stops.add_tab_stop(Cm(left))
    p.add_run(label + "\t" + text).font.size = Pt(12)


def cell_text(cell, text, bold=False, align=WD_ALIGN_PARAGRAPH.LEFT):
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = align
    pf = p.paragraph_format
    pf.line_spacing = TAB; pf.space_before = Pt(1); pf.space_after = Pt(1)
    r = p.add_run(str(text)); r.bold = bold; r.font.size = Pt(FS_TAB)


def tabel(doc, header, rows, widths, align_col=()):
    t = doc.add_table(rows=1, cols=len(header))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    tblPr = t._tbl.tblPr
    w = OxmlElement("w:tblW")
    w.set(qn("w:w"), str(int(sum(widths) / 2.54 * 1440))); w.set(qn("w:type"), "dxa")
    tblPr.append(w)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    for i, h in enumerate(header):
        cell_text(t.rows[0].cells[i], h, bold=True, align=WD_ALIGN_PARAGRAPH.CENTER)
    t.rows[0]._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))  # ulang header
    for data in rows:
        cells = t.add_row().cells
        for i, v in enumerate(data):
            cell_text(cells[i], v,
                      align=WD_ALIGN_PARAGRAPH.CENTER if i in align_col
                      else WD_ALIGN_PARAGRAPH.LEFT)
    grid = t._tbl.find(qn("w:tblGrid"))
    if grid is not None:
        for gc, wd in zip(grid.findall(qn("w:gridCol")), widths):
            gc.set(qn("w:w"), str(int(wd / 2.54 * 1440)))
    for row in t.rows:
        for i, wd in enumerate(widths):
            row.cells[i].width = Cm(wd)
    return t


def caption(doc, text, before=12, after=6, keep_next=False):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    pf = p.paragraph_format
    pf.line_spacing = 1.0 if len(text) > 95 else TEKS
    pf.space_before = Pt(before); pf.space_after = Pt(after)
    if keep_next:
        pf.keep_with_next = True
    p.add_run(text).font.size = Pt(12)
    return p


def sumber(doc, teks):
    par(doc, teks, indent=False, spacing=1.0, size=10, before=4,
        align=WD_ALIGN_PARAGRAPH.LEFT)


def nomor_halaman(sec):
    fp = sec.footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    fp.paragraph_format.line_spacing = 1.0
    fld = OxmlElement("w:fldSimple"); fld.set(qn("w:instr"), "PAGE")
    fp._p.append(fld)
    pn = sec._sectPr.find(qn("w:pgNumType"))
    if pn is None:
        pn = OxmlElement("w:pgNumType"); sec._sectPr.append(pn)
    pn.set(qn("w:fmt"), "decimal")


# ============================== isi bab ==============================
def main():
    doc = new_doc()
    nomor_halaman(doc.sections[0])

    judul_bab(doc, "BAB IV", "HASIL DAN PEMBAHASAN")
    par(doc, "", indent=False, size=6, spacing=1.0)

    total = len(KEGIATAN)
    kosong = sum(1 for _, k in KEGIATAN if k.strip().lower() == HARI_TANPA_KEGIATAN.lower())
    aktif = total - kosong

    # ---------- 4.1 ----------
    subjudul(doc, "4.1", "Rincian Kegiatan Kerja Praktik")
    par(doc, "Kegiatan Kerja Praktik dilaksanakan penulis di <nama instansi> mulai "
             "tanggal %s sampai dengan %s dengan jumlah kehadiran %d hari kerja dan "
             "%d hari tanpa kegiatan. Rincian kegiatan harian penulis disajikan pada "
             "Tabel 4.1." % (KEGIATAN[0][0], KEGIATAN[-1][0], aktif, kosong))
    par(doc, "Selama pelaksanaan Kerja Praktik, penulis ditempatkan pada bagian "
             "administrasi dan operasional. Pekerjaan yang paling sering dilakukan "
             "adalah pengisian formulir, pengecekan kelengkapan berkas, pemberian "
             "stempel, serta penataan dokumen.")

    caption(doc, "Tabel 4.1 Rincian kegiatan harian pelaksanaan Kerja Praktik",
            before=12, after=6, keep_next=True)
    tabel(doc, ["No", "Hari/Tanggal", "Kegiatan"],
          [(i + 1, t, k) for i, (t, k) in enumerate(KEGIATAN)],
          widths=[1.0, 3.3, 10.0], align_col={0})
    sumber(doc, "Sumber: Kartu Kendali Kerja Praktek <nama instansi> (tahun)")

    par(doc, "Berdasarkan Tabel 4.1, kegiatan penulis pada minggu pertama diawali "
             "dengan orientasi lingkungan kerja, kemudian dilanjutkan dengan pekerjaan "
             "administrasi rutin. Kegiatan tersebut dilaksanakan berulang setiap hari "
             "kerja dengan tingkat tanggung jawab yang meningkat seiring bertambahnya "
             "pemahaman penulis terhadap prosedur kantor.", before=12)
    par(doc, "Terdapat %d hari kerja yang tidak terisi kegiatan, yaitu pada saat "
             "penulis %s. Dengan demikian, dari %d hari kerja yang tercatat pada kartu "
             "kendali, penulis melaksanakan kegiatan pada %d hari kerja."
             % (kosong, HARI_TANPA_KEGIATAN.lower(), total, aktif))

    # ---------- 4.2 ----------
    subjudul(doc, "4.2", "Rekapitulasi Kegiatan", page_break=True)
    par(doc, "Jenis kegiatan yang dilaksanakan penulis beserta jumlah hari "
             "pelaksanaannya disajikan pada Tabel 4.2. Satu hari kerja dapat memuat "
             "lebih dari satu jenis kegiatan, sehingga jumlah hari pada seluruh jenis "
             "kegiatan lebih besar daripada jumlah hari kerja.")
    caption(doc, "Tabel 4.2 Rekapitulasi jenis dan jumlah hari pelaksanaan kegiatan",
            before=12, after=6, keep_next=True)
    rekap = sorted(JENIS, key=lambda x: -len(x[1]))       # dihitung, bukan diketik
    tabel(doc, ["No", "Jenis Kegiatan", "Jumlah Hari Pelaksanaan"],
          [(i + 1, n, "%d hari" % len(t)) for i, (n, t) in enumerate(rekap)],
          widths=[1.0, 10.5, 3.0], align_col={0, 2})
    sumber(doc, "Sumber: Kartu Kendali Kerja Praktek <nama instansi> (tahun)")
    par(doc, "Berdasarkan Tabel 4.2, kegiatan yang paling sering dilaksanakan adalah "
             "%s, yaitu pada %d hari kerja."
             % (rekap[0][0].lower(), len(rekap[0][1])), before=12)

    # ---------- 4.3 ----------
    subjudul(doc, "4.3", "Kendala dan Solusi")
    par(doc, "Selama melaksanakan Kerja Praktik, penulis menghadapi beberapa kendala "
             "beserta cara mengatasinya sebagai berikut.")
    for lbl, isi in [
        ("a.", "Kendala pada ketelitian pengisian dan pengecekan formulir. Solusinya "
               "adalah melakukan pengecekan ulang sebelum formulir diserahkan kepada "
               "petugas."),
        ("b.", "Kendala pada penyusunan dokumen yang berasal dari beberapa jenis "
               "pelayanan. Solusinya adalah mengelompokkan dokumen berdasarkan tanggal, "
               "jenis dokumen, dan jenis pelayanan."),
        ("c.", "Kendala pada penyesuaian diri di awal kegiatan. Solusinya adalah "
               "mengikuti orientasi, bertanya kepada pembimbing lapangan, dan "
               "mempelajari contoh dokumen yang sudah ada.")]:
        butir(doc, lbl, isi)

    # ---------- 4.4 ----------
    subjudul(doc, "4.4", "Pembahasan")
    par(doc, "Kegiatan Kerja Praktik yang dilaksanakan penulis berada pada bagian "
             "administrasi dan operasional. Berdasarkan struktur organisasi pada "
             "Gambar 2.1, pekerjaan tersebut merupakan bagian dari tugas Operation "
             "Office dan Back Office, yang bertanggung jawab meneliti kembali "
             "transaksi yang telah dilakukan pada bagian pelayanan.")
    par(doc, "Berdasarkan Tabel 4.2, pekerjaan administratif yang dilakukan penulis "
             "lebih banyak berupa kegiatan yang sifatnya berulang. Hal ini menunjukkan "
             "bahwa kelancaran pelayanan sangat bergantung pada ketertiban administrasi, "
             "sehingga dokumen mudah ditemukan kembali ketika dibutuhkan.")
    par(doc, "Pelaksanaan pekerjaan administrasi tersebut juga berkaitan dengan prinsip "
             "kehati-hatian. Kelengkapan data pada formulir merupakan bagian dari upaya "
             "memastikan identitas dan keabsahan data nasabah sebelum diproses lebih "
             "lanjut, sehingga pengecekan ulang bukan sekadar kegiatan tambahan "
             "melainkan bagian dari prosedur pengendalian internal.")

    path = os.path.join(OUT, NAMA_BERKAS)
    doc.save(path)
    print("TERSIMPAN:", path, os.path.getsize(path))


if __name__ == "__main__":
    main()
