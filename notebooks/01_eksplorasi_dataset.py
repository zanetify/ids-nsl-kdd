# ============================================
# SKRIPSI - Sistem Deteksi Intrusi (IDS)
# File 01: Eksplorasi Dataset NSL-KDD
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Nama kolom dataset NSL-KDD
kolom = [
    'duration', 'protocol_type', 'service', 'flag', 'src_bytes',
    'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot',
    'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell',
    'su_attempted', 'num_root', 'num_file_creations', 'num_shells',
    'num_access_files', 'num_outbound_cmds', 'is_host_login',
    'is_guest_login', 'count', 'srv_count', 'serror_rate',
    'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
    'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count',
    'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
    'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate',
    'dst_host_serror_rate', 'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
    'dst_host_srv_rerror_rate', 'label', 'difficulty'
]

# Load dataset
print("Loading dataset...")
df_train = pd.read_csv('D:/Skripsi/nsl-kdd/KDDTrain+.txt', 
                        names=kolom, header=None)
df_test = pd.read_csv('D:/Skripsi/nsl-kdd/KDDTest+.txt', 
                       names=kolom, header=None)

print(f"✅ Dataset Training: {df_train.shape[0]} baris, {df_train.shape[1]} kolom")
print(f"✅ Dataset Testing : {df_test.shape[0]} baris, {df_test.shape[1]} kolom")

# Lihat 5 baris pertama
print("\n--- 5 Baris Pertama Dataset ---")
print(df_train.head())

# Lihat distribusi label (jenis traffic)
print("\n--- Distribusi Label Training ---")
print(df_train['label'].value_counts())
# ============================================
# VISUALISASI - Distribusi Jenis Serangan
# ============================================

# Sederhanakan label menjadi 4 kategori utama
def kategorisasi(label):
    if label == 'normal':
        return 'Normal'
    elif label in ['neptune', 'back', 'land', 'pod', 'smurf', 'teardrop']:
        return 'DoS'
    elif label in ['ipsweep', 'nmap', 'portsweep', 'satan']:
        return 'Probe'
    elif label in ['ftp_write', 'guess_passwd', 'imap', 'multihop', 
                   'phf', 'spy', 'warezclient', 'warezmaster']:
        return 'R2L'
    else:
        return 'U2R'

df_train['kategori'] = df_train['label'].apply(kategorisasi)

# Hitung distribusi kategori
distribusi = df_train['kategori'].value_counts()
print("\n--- Distribusi Kategori Serangan ---")
print(distribusi)

# Buat grafik
plt.figure(figsize=(8, 5))
sns.barplot(x=distribusi.index, y=distribusi.values, palette='Blues_d')
plt.title('Distribusi Kategori Traffic Jaringan - NSL-KDD', fontsize=14)
plt.xlabel('Kategori')
plt.ylabel('Jumlah Data')
plt.tight_layout()
plt.savefig('D:/Skripsi/results/distribusi_kategori.png', dpi=150)
plt.show()
print("Grafik tersimpan di D:/Skripsi/results/")