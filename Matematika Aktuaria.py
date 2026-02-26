# ============================================
# SOAL NOMOR 9
# Diketahui dari suatu tabel mortalita, jumlah penduduk yang hidup 
# Diketahui dari suatu tabel mortalita, jumlah penduduk yang hidup 
# pada usia tepat 20 tahun (𝑙20) adalah 98.567 jiwa, dan yang hidup 
# pada usia tepat 21 tahun (𝑙21) adalah 98.432 jiwa. Hitunglah jumlah 
# penduduk yang diprediksi hidup pada usia 20 tahun dan 8 bulan 
# (𝑙20,6667) dengan menggunakan asumsi Uniform Distribution of 
# Deaths (UDD). 
# ============================================

# Data diketahui
l20 = 98567
l21 = 98432
s = 0.6667  # 8 bulan = 0.6667 tahun

# Rumus UDD
l20_6667 = l20 - s * (l20 - l21)

# Tampilkan hasil
print(f"Jumlah penduduk yang hidup pada usia 20,6667 tahun (l20.6667) = {l20_6667:.4f} jiwa")

# ============================================
# SOAL NOMOR 10
# Sebuah perusahaan asuransi memiliki data bahwa probabilitas 
# kematian antara usia 40 tahun hingga 41 tahun (𝑞40) adalah 
# 0,0025. Hitunglah probabilitas seseorang yang berusia tepat 40 
# tahun 3 bulan (𝑥 + 𝑠 = 40,25) akan meninggal dalam satu tahun ke 
# depan (𝑞40,25) dengan asumsi UDD.
# ============================================

# Data diketahui
q40 = 0.0025  
s = 0.25      # 3 bulan = 0,25 tahun

# Asumsi UDD
q40_25 = q40 / (1 - s * q40)

# Tampilkan hasil
print(f"Probabilitas meninggal pada usia 40,25 (q40.25) = {q40_25:.8f}")

# ============================================
# SOALNOMOR 11
# Diketahui bahwa force of mortality (𝜇𝑥) adalah konstan pada 
# interval usia 50-51 tahun sebesar 0,005. Hitunglah probabilitas 
# seseorang yang berusia tepat 50 tahun 6 bulan (𝑥 + 𝑠 = 50,5) akan 
# bertahan hidup hingga usia 51 tahun 6 bulan (𝑝50,5) berdasarkan 
# asumsi CFM.
# ============================================

import math

# Data diketahui
mu_x = 0.005      # force of mortality konstan
t = 1.0           # dari usia 50,5 ke 51,5 tahun = 1 tahun

# Rumus probabilitas bertahan hidup dengan asumsi CFM
p50_5 = math.exp(-mu_x * t)

# Tampilkan hasil dengan format seperti contoh
print(f"Probabilitas bertahan hidup dari usia 50,5 hingga 51,5 tahun (p50.5) = {p50_5:.8f}")

# ============================================
# SOALNOMOR 12
# Dengan data yang sama (𝜇𝑥 = 0,005 pada interval usia 50-51 
# tahun), hitunglah probabilitas seseorang yang berusia tepat 50 
# tahun 6 bulan (𝑥 + 𝑠 = 50,5) akan meninggal dalam satu tahun ke 
# depan (𝑞50,5) sebelum mencapai usia 51 tahun 6 bulan. 
# ============================================

import math

# Data diketahui
mu_x = 0.005      # force of mortality konstan
t = 1.0           # selang waktu 1 tahun (dari 50,5 ke 51,5)

# Rumus probabilitas meninggal (CFM)
q50_5 = 1 - math.exp(-mu_x * t)

# Tampilkan hasil
print(f"Probabilitas meninggal dalam satu tahun ke depan pada usia 50,5 tahun (q50.5) = {q50_5:.8f}")
