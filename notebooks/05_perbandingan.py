# ============================================
# SKRIPSI - Sistem Deteksi Intrusi (IDS)
# File 05: Perbandingan RF vs KNN
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import time

# Load data
print("Loading data...")
X_train = np.load('D:/Skripsi/models/X_train.npy')
X_test = np.load('D:/Skripsi/models/X_test.npy')
y_train = pd.read_csv('D:/Skripsi/models/y_train.csv')['kategori']
y_test = pd.read_csv('D:/Skripsi/models/y_test.csv')['kategori']

# Load model
rf_model = joblib.load('D:/Skripsi/models/random_forest_model.pkl')
knn_model = joblib.load('D:/Skripsi/models/knn_model.pkl')

# Evaluasi kedua model
hasil = {}
for nama, model in [('Random Forest', rf_model), ('KNN', knn_model)]:
    start = time.time()
    y_pred = model.predict(X_test)
    durasi = time.time() - start
    
    hasil[nama] = {
        'Akurasi'  : accuracy_score(y_test, y_pred) * 100,
        'Precision': precision_score(y_test, y_pred, average='weighted') * 100,
        'Recall'   : recall_score(y_test, y_pred, average='weighted') * 100,
        'F1-Score' : f1_score(y_test, y_pred, average='weighted') * 100,
        'Waktu (s)': round(durasi, 2)
    }

# Tampilkan tabel perbandingan
df_hasil = pd.DataFrame(hasil).T
print("\n===== PERBANDINGAN HASIL =====")
print(df_hasil.round(2).to_string())

# Grafik perbandingan
metrik = ['Akurasi', 'Precision', 'Recall', 'F1-Score']
x = np.arange(len(metrik))
width = 0.35

fig, ax = plt.subplots(figsize=(10, 6))
bars1 = ax.bar(x - width/2, 
               [hasil['Random Forest'][m] for m in metrik], 
               width, label='Random Forest', color='steelblue')
bars2 = ax.bar(x + width/2, 
               [hasil['KNN'][m] for m in metrik], 
               width, label='KNN', color='seagreen')

ax.set_ylabel('Nilai (%)')
ax.set_title('Perbandingan Performa Random Forest vs KNN')
ax.set_xticks(x)
ax.set_xticklabels(metrik)
ax.set_ylim(0, 110)
ax.legend()

# Tambah nilai di atas bar
for bar in bars1:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=9)
for bar in bars2:
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.5,
            f'{bar.get_height():.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('D:/Skripsi/results/perbandingan_rf_knn.png', dpi=150)
plt.show()
print("\nGrafik perbandingan tersimpan!")