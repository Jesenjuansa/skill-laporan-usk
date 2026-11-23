# -*- coding: utf-8 -*-
"""
Buat bagan struktur organisasi bersih (PNG + SVG) dari data teks, tanpa watermark.

Dipakai saat user minta "versi polosan" dari bagan yang diambil dari skripsi/LKP
orang lain: bagan digambar ulang dari struktur yang sama, sumbernya tetap dicantumkan
sebagai "Sumber: <instansi>, diolah penulis, <tahun>".

Kenapa skrip, bukan menggambar manual: ukuran kanvas harus PAS dengan area teks Word
dan geometri garis penghubung gampang salah (garis melayang, kotak terpotong).

Jalankan:  C:/Python314/python.exe buat_bagan_organisasi.py

Yang sudah diperhitungkan di sini (pitfall yang pernah memakan waktu):
  1. `ax.set_aspect('auto')` + `subplots_adjust(0..1)` -> rasio PIKsel == rasio inci
     (tanpa ini, koordinat crop hasil bolak-balik dan teks jadi lonjong).
  2. Garis siku staf: batang vertikal di KIRI kotak, ujung garis horizontal dihitung
     `x - SW/2` dan `spine = x - SW/2 - jarak` -> tidak ada garis melayang/menembus.
  3. Semua kotak staf memakai satu `STEP` yang sama supaya kolom sejajar.
  4. Baris terpanjang (kolom dengan staf terbanyak) menentukan batas bawah kanvas.
  5. Simpan dua format: PNG 400 dpi (untuk Word) + SVG (untuk Edit di Word/Inkscape).
"""

import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# ---- kanvas: LEbar 16 cm = tinggi 29,7 - 2,5 - 2,5 (margin skripsi lain) ----
# Untuk laporan USK FMIPA pakai area teks 14,5 cm -> FIG_W = 5.71 inci.
FIG_W = 6.30
FIG_H = 4.30
DPI = 400
OUT_DIR = os.path.join(os.environ.get('LOCALAPPDATA', '.'), 'Temp')
NAMA = 'Bagan_Struktur_Organisasi'

# ---------------------------------------------------------------- data bagan
PUNCAK = 'Pemimpin'
WAKIL = 'Wakil Pemimpin'
# (judul kepala seksi, [petugas dari atas ke bawah])
SEKSI = [
    ('Kepala Seksi\nPembiayaan', ['Account\nOfficer', 'Petugas\nPembiayaan']),
    ('Kepala Seksi\nOperasional', ['Petugas\nMIS/Haji', 'Customer\nService', 'Teller']),
    ('Kepala Seksi\nUmum/SDI', ['Petugas SDI', 'Petugas Umum', 'Office Boy',
                                'Supir', 'Security']),
    ('Kepala Seksi\nLegal/PA', ['Petugas\nLegal']),
]

# ---------------------------------------------------------------- geometri
LW = 1.15          # tebal garis (pt) - samakan kotak & penghubung
FS = 7.4           # ukuran teks kotak
BH = 9.0           # tinggi kotak
KW, SW = 19.5, 16.5   # lebar kotak kepala seksi / kotak staf
STEP = 10.4        # jarak vertikal antar kotak staf
STUB = 2.8         # jarak batang vertikal staf dari tepi kiri kotak
MARGIN = 8.0       # margin kanvas (unit 0-100)


def gambar_bagan(path_png, path_svg):
    fig, ax = plt.subplots(figsize=(FIG_W, FIG_H), dpi=DPI)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')

    def box(cx, cy, w, h, teks, fs=FS):
        ax.add_patch(Rectangle((cx - w / 2, cy - h / 2), w, h, facecolor='white',
                               edgecolor='black', linewidth=LW, zorder=3))
        ax.text(cx, cy, teks, ha='center', va='center', fontsize=fs,
                family='serif', color='black', zorder=4, linespacing=1.2)

    def V(x, y1, y2):
        ax.plot([x, x], [min(y1, y2), max(y1, y2)], color='black', lw=LW,
                solid_capstyle='butt', zorder=2)

    def H(x1, x2, y):
        ax.plot([min(x1, x2), max(x1, x2)], [y, y], color='black', lw=LW,
                solid_capstyle='butt', zorder=2)

    n = len(SEKSI)
    isi = 100 - 2 * MARGIN
    lebar_kolom = isi / n
    cx = [MARGIN + lebar_kolom * (i + 0.5) for i in range(n)]

    max_staf = max(len(s[1]) for s in SEKSI)
    total = BH * 2 + STEP * (max_staf - 1) + BH + 3 * (BH / 2 + 3.0)
    skala = isi / total

    def Y(y):                       # unit desain -> 0..100
        return 100 - MARGIN - y * skala

    yP = Y(BH / 2)
    yW = Y(BH + 3.0 + BH / 2)
    yK = Y(BH + 3.0 + BH + 3.0 + BH / 2)
    yS0 = Y(BH + 3.0 + BH + 3.0 + BH + 3.0 + BH / 2)

    box(50, yP, 20, BH * skala, PUNCAK)
    box(50, yW, 24, BH * skala, WAKIL)
    V(50, yP - BH * skala / 2, yW + BH * skala / 2)

    bus_y = (yW - BH * skala / 2 + yK + BH * skala / 2) / 2
    V(50, yW - BH * skala / 2, bus_y)
    H(cx[0], cx[-1], bus_y)
    for x in cx:
        V(x, bus_y, yK + BH * skala / 2)

    for x, (judul, staf) in zip(cx, SEKSI):
        box(x, yK, KW, BH * skala, judul)
        ys = [yS0 - j * STEP * skala for j in range(len(staf))]
        atas = yS0 + BH * skala / 2
        V(x, yK - BH * skala / 2, atas)
        if len(staf) > 1:
            spine = x - SW / 2 - STUB
            V(spine, ys[-1], atas)
            for y in ys:
                H(spine, x - SW / 2, y)
        for y, t in zip(ys, staf):
            box(x, y, SW, BH * skala, t)

    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)
    for ext, path in (('png', path_png), ('svg', path_svg)):
        fig.savefig(path, dpi=DPI, facecolor='white')
    plt.close(fig)
    print('TERSIMPAN:', path_png)
    print('TERSIMPAN:', path_svg)


if __name__ == '__main__':
    gambar_bagan(os.path.join(OUT_DIR, NAMA + '_polos.png'),
                 os.path.join(OUT_DIR, NAMA + '_polos.svg'))
