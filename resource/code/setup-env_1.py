# 1. Membuat virtual environment Python 3.12 dan menginstal dependensi
uv venv --seed --python 3.12 .venv
.venv/bin/pip install flask numpy scikit-learn pandas joblib

# 2. Verifikasi versi Python dan daftar paket terpasang
(.venv/bin/python --version && .venv/bin/pip list) 2>&1 | tee docs/output/01-verify-env.txt
