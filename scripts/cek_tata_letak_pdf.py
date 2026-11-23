# -*- coding: utf-8 -*-
"""Cek tata letak hasil ekspor PDF laporan (.docx -> PDF lewat Word COM).

Ekspor PDF saja tidak membuktikan tata letak benar. Skrip ini memeriksa tiga hal
yang paling sering salah dan sulit dilihat manual di dokumen ratusan halaman:

  1. Keterangan gambar "yatim": label `Gambar n.m` yang tidak berada pada halaman
     yang sama dengan gambarnya.
  2. Blok teks yang melewati margin kanan area teks.
  3. Nomor halaman per halaman (memastikan bab baru mulai dari 1, bukan melanjutkan).

Pakai:
    C:/Python314/python.exe cek_tata_letak_pdf.py hasil.pdf

Catatan: A4 = 595,3 pt. Margin kiri 3,5 cm = 99 pt, kanan 3,0 cm = 85 pt,
sehingga area teks berakhir di x = 510 pt.
"""

import re
import sys

import pymupdf

KIRI = 96.0          # toleransi di bawah 3,5 cm
KANAN = 512.0        # toleransi di atas batas margin kanan


def main(path):
    d = pymupdf.open(path)
    print(f'berkas: {path} | halaman: {len(d)}')

    label = re.compile(r'(Gambar|Tabel)\s+(\d+\.\d+)')
    halaman_label = {}
    halaman_gambar = {}
    for i, page in enumerate(d):
        teks = page.get_text()
        for kind, num in label.findall(teks):
            halaman_label.setdefault((kind, num), set()).add(i + 1)
        # gambar pada halaman: objek gambar yang benar-benar ada di halaman itu
        if page.get_images():
            halaman_gambar.setdefault(i + 1, True)

    print('\n== Keterangan gambar tanpa gambar di halaman yang sama ==')
    masalah = 0
    for (kind, num), pages in sorted(halaman_label.items()):
        if kind != 'Gambar':
            continue
        if not any(p in halaman_gambar for p in pages):
            print(f'  [WARN] Gambar {num}: label di halaman {sorted(pages)}, '
                  f'tidak ada gambar di halaman itu')
            masalah += 1
    if not masalah:
        print('  tidak ada (semua label Gambar berada di halaman bergambar)')

    print('\n== Blok teks melewati margin ==')
    lewat = 0
    for i, page in enumerate(d):
        for b in page.get_text('blocks'):
            x0, _, x1, _ = b[:4]
            if x0 < KIRI or x1 > KANAN:
                cuplik = b[4].strip().replace(chr(10), ' ')[:60]
                print(f'  [WARN] hal {i + 1}: x=({x0:.0f}..{x1:.0f}) -> {cuplik}')
                lewat += 1
    if not lewat:
        print('  tidak ada')

    print('\n== Nomor halaman pertama tiap halaman ==')
    for i, page in enumerate(d):
        teks = page.get_text().strip().split(chr(10))
        print(f'  hal {i + 1}: {teks[0][:50] if teks else "(kosong)"}')

    print(f'\nringkasan: {masalah} label gambar yatim, {lewat} blok lewat margin')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('pakai: cek_tata_letak_pdf.py <berkas.pdf>')
    main(sys.argv[1])
