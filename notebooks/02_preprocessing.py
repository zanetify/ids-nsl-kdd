# ============================================
# SKRIPSI - Sistem Deteksi Intrusi (IDS)
# File 02: Preprocessing Data
# ============================================

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Nama kolom
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
df_train = pd.read_csv('D:/Skripsi/nsl-kdd/KDDTrain+.txt', names=kolom, header=None)
df_test = pd.read_csv('D:/Skripsi/nsl-kdd/KDDTest+.txt', names=kolom, header=None)

# Kategorisasi label
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
df_test['kategori'] = df_test['label'].apply(kategorisasi)

# Hapus kolom yang tidak diperlukan
df_train = df_train.drop(['label', 'difficulty'], axis=1)
df_test = df_test.drop(['label', 'difficulty'], axis=1)

# Encode kolom kategorikal
print("Encoding kolom kategorikal...")
le = LabelEncoder()
for col in ['protocol_type', 'service', 'flag']:
    df_train[col] = le.fit_transform(df_train[col])
    df_test[col] = le.fit_transform(df_test[col])

# Pisahkan fitur dan label
X_train = df_train.drop('kategori', axis=1)
y_train = df_train['kategori']
X_test = df_test.drop('kategori', axis=1)
y_test = df_test['kategori']

# Normalisasi fitur
print("Normalisasi data...")
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(f"\nShape X_train : {X_train.shape}")
print(f"Shape X_test  : {X_test.shape}")
print(f"Kategori      : {y_train.unique()}")
print("\nPreprocessing selesai!")

# Simpan hasil preprocessing
np.save('D:/Skripsi/models/X_train.npy', X_train)
np.save('D:/Skripsi/models/X_test.npy', X_test)
y_train.to_csv('D:/Skripsi/models/y_train.csv', index=False)
y_test.to_csv('D:/Skripsi/models/y_test.csv', index=False)
print("Data tersimpan di folder models!")