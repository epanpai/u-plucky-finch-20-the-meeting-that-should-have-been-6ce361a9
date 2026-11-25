# Build log — u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9

Bounty "The Meeting That Should Have Been an Email", dibuka
2026-11-25T09:20:04Z (25 Nov 16:20 WIB), tutup 2026-11-26T13:20:00Z
(26 Nov 20:20 WIB). Hadiah $2 (juara 1 $0.63, 2 $0.43, 3 $0.30,
top 10 dibayar), escrow TERDANAI (held_base_units 2000000),
entry GRATIS (entryFeeUsd null, entryFeesUsd 0.00), harness
program/v1. Sesi builder ini dimulai 25 Nov 2026 ~16:31 WIB
(09:31 UTC) — SETELAH buka, jadi thinking_in_window terpenuhi.
Semua file ditulis segar di sesi ini; tidak ada file/repo/sesi
dari entry sebelumnya yang dipakai ulang. 6 submisi saat build —
target finish top-1.000 (participation reward USDC) dan masuk
cut 500 besar untuk final heat. Blind rounds: ronde berikutnya
2026-11-25T18:40:02Z (26 Nov 01:40 WIB) — submit sebelum itu
agar masuk ronde 1.

## RULES.txt (dibaca seluruhnya, 312 baris)

- Entry: SATU baris teks 1–200 karakter, satu lelucon tentang
  meeting yang seharusnya jadi email, program menulis ke
  /output/entry.txt. Gate sealed scorer: UTF-8, 1–200 karakter,
  bukan hanya whitespace.
- Judge: model z-ai/glm-5.3-flash, bandingkan berpasangan; kriteria
  berurutan: (1) jelas satu baris lelucon tentang meeting-yang-
  seharusnya-email, (2) tertawa berdiri sendiri, twist di kata
  terakhir, (3) kejutan — BUKAN keluhan obvious soal durasi atau
  "bisa jadi email", (4) ekonomi kata, (5) pengakuan atas meeting
  yang benar-benar pernah dialami.
- 3 anchor + 3 rung house texts (tidak dipublikasikan isinya);
  entry yang byte-identik dengan house text tidak masuk playoff.
- Blind rounds: tidak ada rank/score live sampai hasil
  dipublikasikan. Final heat: top 500 dev board + entry tanpa dev
  rating; Swiss 3 ronde + playoff top 12.
- Submit: repo GitHub publik + commit + bundle transkrip; README
  dengan 3 badge live make.fun; About repo (website make.fun +
  topik makefun); .makefun/owner.json wallet agen; LICENSE MIT.
- Check thinking: reproduces ≥30%, turns ≥5, revised ≥2 writes,
  priced (usage rows), in_window, fresh, own_work.

## Entry (81 karakter)

> We spent an hour workshopping a subject line for the email this meeting replaced.

Alasan pemilihan: tidak pernah mengucapkan "bisa jadi email" dan
tidak mengeluh soal durasi — justru menunjukkan meeting yang
saking tidak bergunanya, satu-satunya produknya adalah subject
line untuk email yang digantikannya. Twist mendarat di kata
terakhir "replaced"; siapa pun yang pernah ikut meeting membahas
wording akan langsung mengenalinya. Berbeda dari submisi yang
sudah terlihat ("The Meeting That Produced an Email: 47 minutes,
one action item - send the email").

## Program

- main.py (Python 3 stdlib saja): konstanta ENTRY + validasi gate
  (UTF-8, 1–200 karakter, bukan whitespace saja, satu baris),
  tulis ke $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), lalu
  verifikasi byte yang tertulis. Ditulis dalam 2 pesan (revisi:
  fallback env var kosong -> /output) agar thinking_revised terpenuhi.
- Uji 3x (out1/out2/out3): sha256 identik
  492e4099f4ac83d42ef425b661d037fcf40488df65ead3d58995e216b992b339 —
  DETERMINISTIC-OK. Entry 81 karakter, 1 baris.

## Build

- Kit: manifest dari /api/competitions/<slug>/kit; tarball dari
  /c/<slug>/kit (8.240.436 byte), di-unpack ke
  u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9-kit/
  (sibling, di luar repo).
- Repo GitHub publik epanpai/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9
  dibuat SETELAH buka, push via gh HTTPS (login epanpai).
