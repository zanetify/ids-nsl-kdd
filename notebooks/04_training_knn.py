# ============================================
# SKRIPSI - Sistem Deteksi Intrusi (IDS)
# File 04: Training Model KNN
# ============================================

import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import time
import joblib

# Load data hasil preprocessing
print("Loading data preprocessing...")
X_train = np.load('D:/Skripsi/models/X_train.npy')
X_test = np.load('D:/Skripsi/models/X_test.npy')
y_train = pd.read_csv('D:/Skripsi/models/y_train.csv')['kategori']
y_test = pd.read_csv('D:/Skripsi/models/y_test.csv')['kategori']

print(f"Data siap: {X_train.shape[0]} training, {X_test.shape[0]} testing")

# Training model KNN
print("\nTraining KNN... (mohon tunggu, lebih lama dari RF)")
start = time.time()

knn_model = KNeighborsClassifier(
    n_neighbors=5,
    n_jobs=-1
)
knn_model.fit(X_train, y_train)

durasi = time.time() - start
print(f"Training selesai dalam {durasi:.2f} detik")

# Prediksi
print("Prediksi data testing...")
y_pred = knn_model.predict(X_test)

# Evaluasi
akurasi = accuracy_score(y_test, y_pred)
print(f"\nAkurasi KNN: {akurasi*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred,
     labels=['Normal', 'DoS', 'Probe', 'R2L', 'U2R'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=['Normal', 'DoS', 'Probe', 'R2L', 'U2R'],
            yticklabels=['Normal', 'DoS', 'Probe', 'R2L', 'U2R'])
plt.title('Confusion Matrix - KNN')
plt.ylabel('Aktual')
plt.xlabel('Prediksi')
plt.tight_layout()
plt.savefig('D:/Skripsi/results/confusion_matrix_knn.png', dpi=150)
plt.show()

# Simpan model
joblib.dump(knn_model, 'D:/Skripsi/models/knn_model.pkl')
print("\nModel KNN tersimpan!")