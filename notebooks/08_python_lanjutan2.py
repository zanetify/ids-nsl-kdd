# ============================================
# BELAJAR PYTHON LANJUTAN - PART 2
# Topik: List Comprehension, Lambda, Pandas
# ============================================

import pandas as pd
import numpy as np

# ── PART 1: LIST COMPREHENSION ──
# Cara singkat membuat list — lebih Pythonic!

print("=" * 50)
print("PART 1: LIST COMPREHENSION")
print("=" * 50)

# Cara lama (Java style)
angka_biasa = []
for i in range(1, 11):
    angka_biasa.append(i * 2)
print(f"Cara lama : {angka_biasa}")

# Cara Python (List Comprehension)
angka_python = [i * 2 for i in range(1, 11)]
print(f"Cara Python: {angka_python}")

# Contoh dengan kondisi — filter data serangan
semua_label = ['normal', 'neptune', 'normal', 'DoS', 'normal', 'probe', 'DoS']
hanya_serangan = [label for label in semua_label if label != 'normal']
print(f"\nSemua label  : {semua_label}")
print(f"Hanya serangan: {hanya_serangan}")

# List comprehension dengan transformasi
label_upper = [label.upper() for label in semua_label]
print(f"Label uppercase: {label_upper}")


# ── PART 2: LAMBDA FUNCTION ──
# Fungsi singkat tanpa nama — cocok untuk operasi sederhana

print("\n" + "=" * 50)
print("PART 2: LAMBDA FUNCTION")
print("=" * 50)

# Fungsi biasa
def kuadrat_biasa(x):
    return x ** 2

# Lambda equivalent
kuadrat_lambda = lambda x: x ** 2

print(f"Kuadrat 5 (biasa) : {kuadrat_biasa(5)}")
print(f"Kuadrat 5 (lambda): {kuadrat_lambda(5)}")

# Lambda dengan map — terapkan fungsi ke semua elemen
angka = [1, 2, 3, 4, 5]
hasil_kuadrat = list(map(lambda x: x ** 2, angka))
print(f"\nAngka asal  : {angka}")
print(f"Setelah map : {hasil_kuadrat}")

# Lambda dengan filter — filter elemen
hasil_filter = list(filter(lambda x: x > 3, angka))
print(f"Filter > 3  : {hasil_filter}")

# Contoh nyata: sorting data berdasarkan nilai akurasi
hasil_model = [
    {'model': 'Random Forest', 'akurasi': 72.65},
    {'model': 'KNN', 'akurasi': 70.44},
    {'model': 'SVM', 'akurasi': 74.20},
]
hasil_sorted = sorted(hasil_model, key=lambda x: x['akurasi'], reverse=True)
print(f"\nRanking model berdasarkan akurasi:")
for i, h in enumerate(hasil_sorted, 1):
    print(f"  {i}. {h['model']}: {h['akurasi']}%")


# ── PART 3: PANDAS LANJUTAN ──
print("\n" + "=" * 50)
print("PART 3: PANDAS LANJUTAN")
print("=" * 50)

# Buat DataFrame simulasi hasil deteksi IDS
data = {
    'koneksi_id': range(1, 11),
    'protocol'  : ['tcp', 'udp', 'tcp', 'tcp', 'udp', 'tcp', 'udp', 'tcp', 'tcp', 'udp'],
    'src_bytes' : [491, 146, 0, 232, 199, 1000, 50, 800, 300, 100],
    'label'     : ['normal', 'normal', 'DoS', 'normal', 'DoS', 'Probe', 'normal', 'DoS', 'normal', 'Probe'],
    'prediksi'  : ['normal', 'normal', 'DoS', 'normal', 'normal', 'Probe', 'normal', 'DoS', 'DoS', 'Probe']
}
df = pd.DataFrame(data)
print("\nDataset simulasi IDS:")
print(df.to_string(index=False))

# Groupby — analisis per kategori
print("\n--- Jumlah per label aktual ---")
print(df.groupby('label')['koneksi_id'].count())

# Filtering data
print("\n--- Hanya koneksi DoS ---")
dos = df[df['label'] == 'DoS']
print(dos[['koneksi_id', 'protocol', 'src_bytes', 'label']].to_string(index=False))

# Tambah kolom baru — apakah prediksi benar?
df['prediksi_benar'] = df['label'] == df['prediksi']
akurasi = df['prediksi_benar'].mean() * 100
print(f"\n--- Evaluasi Prediksi ---")
print(df[['koneksi_id', 'label', 'prediksi', 'prediksi_benar']].to_string(index=False))
print(f"\nAkurasi manual: {akurasi:.1f}%")

# Statistik deskriptif
print("\n--- Statistik src_bytes ---")
print(df['src_bytes'].describe())

print("\nSelesai! Kamu baru saja belajar List Comprehension, Lambda, dan Pandas lanjutan!")