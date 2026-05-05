# ============================================
# SKRIPSI - Sistem Deteksi Intrusi (IDS)
# File 06: Summary Report
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns

# Load data
X_train = np.load('D:/Skripsi/models/X_train.npy')
X_test  = np.load('D:/Skripsi/models/X_test.npy')
y_train = pd.read_csv('D:/Skripsi/models/y_train.csv')['kategori']
y_test  = pd.read_csv('D:/Skripsi/models/y_test.csv')['kategori']

rf_model  = joblib.load('D:/Skripsi/models/random_forest_model.pkl')
knn_model = joblib.load('D:/Skripsi/models/knn_model.pkl')

y_pred_rf  = rf_model.predict(X_test)
y_pred_knn = knn_model.predict(X_test)

labels = ['Normal', 'DoS', 'Probe', 'R2L', 'U2R']

# Buat figure dengan 4 panel
fig = plt.figure(figsize=(16, 12))
fig.suptitle('Laporan Hasil IDS - Random Forest vs KNN\nGema Rajab Fauzan | Teknik Informatika', 
             fontsize=14, fontweight='bold', y=0.98)

gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.4, wspace=0.3)

# Panel 1: Confusion Matrix RF
ax1 = fig.add_subplot(gs[0, 0])
cm_rf = confusion_matrix(y_test, y_pred_rf, labels=labels)
sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=ax1,
            xticklabels=labels, yticklabels=labels)
ax1.set_title('Confusion Matrix - Random Forest')
ax1.set_ylabel('Aktual')
ax1.set_xlabel('Prediksi')

# Panel 2: Confusion Matrix KNN
ax2 = fig.add_subplot(gs[0, 1])
cm_knn = confusion_matrix(y_test, y_pred_knn, labels=labels)
sns.heatmap(cm_knn, annot=True, fmt='d', cmap='Greens', ax=ax2,
            xticklabels=labels, yticklabels=labels)
ax2.set_title('Confusion Matrix - KNN')
ax2.set_ylabel('Aktual')
ax2.set_xlabel('Prediksi')

# Panel 3: Bar chart perbandingan
ax3 = fig.add_subplot(gs[1, 0])
metrik = ['Akurasi', 'Precision', 'Recall', 'F1-Score']
rf_vals  = [
    accuracy_score(y_test, y_pred_rf)*100,
    precision_score(y_test, y_pred_rf, average='weighted')*100,
    recall_score(y_test, y_pred_rf, average='weighted')*100,
    f1_score(y_test, y_pred_rf, average='weighted')*100
]
knn_vals = [
    accuracy_score(y_test, y_pred_knn)*100,
    precision_score(y_test, y_pred_knn, average='weighted')*100,
    recall_score(y_test, y_pred_knn, average='weighted')*100,
    f1_score(y_test, y_pred_knn, average='weighted')*100
]
x = np.arange(len(metrik))
w = 0.35
ax3.bar(x - w/2, rf_vals,  w, label='Random Forest', color='steelblue')
ax3.bar(x + w/2, knn_vals, w, label='KNN',           color='seagreen')
ax3.set_xticks(x)
ax3.set_xticklabels(metrik)
ax3.set_ylim(0, 110)
ax3.set_ylabel('Nilai (%)')
ax3.set_title('Perbandingan Metrik Evaluasi')
ax3.legend()
for i, (rv, kv) in enumerate(zip(rf_vals, knn_vals)):
    ax3.text(i - w/2, rv + 1, f'{rv:.1f}%', ha='center', fontsize=8)
    ax3.text(i + w/2, kv + 1, f'{kv:.1f}%', ha='center', fontsize=8)

# Panel 4: Tabel ringkasan
ax4 = fig.add_subplot(gs[1, 1])
ax4.axis('off')
tabel_data = [
    ['Metrik', 'Random Forest', 'KNN', 'Winner'],
    ['Akurasi',   f'{rf_vals[0]:.2f}%', f'{knn_vals[0]:.2f}%', 'RF'],
    ['Precision', f'{rf_vals[1]:.2f}%', f'{knn_vals[1]:.2f}%', 'RF'],
    ['Recall',    f'{rf_vals[2]:.2f}%', f'{knn_vals[2]:.2f}%', 'RF'],
    ['F1-Score',  f'{rf_vals[3]:.2f}%', f'{knn_vals[3]:.2f}%', 'RF'],
    ['Waktu Prediksi', '0.04 detik', '4.60 detik', 'RF'],
]
tabel = ax4.table(cellText=tabel_data[1:], colLabels=tabel_data[0],
                  loc='center', cellLoc='center')
tabel.auto_set_font_size(False)
tabel.set_fontsize(10)
tabel.scale(1.2, 1.8)
ax4.set_title('Ringkasan Hasil', fontweight='bold')

plt.savefig('D:/Skripsi/results/summary_report.png', dpi=150, bbox_inches='tight')
plt.show()
print("Summary report tersimpan di D:/Skripsi/results/summary_report.png")