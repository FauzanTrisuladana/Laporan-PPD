# 1. Membuat folder terpisah (latihan & tugas) dan menyalin aset yang dipakai
mkdir -p latihan/create_model latihan/web tugas/create_model tugas/web/artifacts tugas/web/templates
cp create_model/tabular/hcvdat0.csv latihan/create_model/hcvdat0.csv
cp -r web/tabular_v2/static web/tabular_v2/templates latihan/web/
cp -r web/tabular_v2/static tugas/web/
rm -rf create_model web .gitattributes

# 2. Memeriksa struktur direktori hasil penataan proyek
find . -maxdepth 3 -not -path './.git*' -not -path './.venv*' | sort 2>&1 | tee docs/output/01-setup-structure.txt
