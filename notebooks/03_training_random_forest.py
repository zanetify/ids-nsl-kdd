# ============================================
# SKRIPSI - Sistem Deteksi Intrusi (IDS)
# File 03: Training Model Random Forest
# ============================================

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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

# Training model
print("\nTraining Random Forest... (mohon tunggu)")
start = time.time()

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
rf_model.fit(X_train, y_train)

durasi = time.time() - start
print(f"Training selesai dalam {durasi:.2f} detik")

# Prediksi
y_pred = rf_model.predict(X_test)

# Evaluasi
akurasi = accuracy_score(y_test, y_pred)
print(f"\nAkurasi Random Forest: {akurasi*100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
plt.figure(figsize=(8, 6))
cm = confusion_matrix(y_test, y_pred, 
     labels=['Normal', 'DoS', 'Probe', 'R2L', 'U2R'])
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['Normal', 'DoS', 'Probe', 'R2L', 'U2R'],
            yticklabels=['Normal', 'DoS', 'Probe', 'R2L', 'U2R'])
plt.title('Confusion Matrix - Random Forest')
plt.ylabel('Aktual')
plt.xlabel('Prediksi')
plt.tight_layout()
plt.savefig('D:/Skripsi/results/confusion_matrix_rf.png', dpi=150)
plt.show()

# Simpan model
joblib.dump(rf_model, 'D:/Skripsi/models/random_forest_model.pkl')
print("\nModel tersimpan!")