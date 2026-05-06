# ============================================
# BELAJAR PYTHON LANJUTAN
# Topik: OOP (Object Oriented Programming)
# ============================================

# ── PART 1: CLASS & OBJECT ──
# Bayangkan kamu membuat "cetakan" untuk objek jaringan

class NetworkConnection:
    """Merepresentasikan sebuah koneksi jaringan"""
    
    # Constructor - dipanggil saat objek dibuat
    def __init__(self, src_ip, dst_ip, protocol, label):
        self.src_ip   = src_ip
        self.dst_ip   = dst_ip
        self.protocol = protocol
        self.label    = label  # 'normal' atau jenis serangan
    
    # Method - fungsi yang dimiliki objek
    def is_attack(self):
        return self.label != 'normal'
    
    def info(self):
        status = "SERANGAN" if self.is_attack() else "Normal"
        return f"{self.src_ip} → {self.dst_ip} | {self.protocol} | Status: {status}"


# Buat beberapa objek koneksi
conn1 = NetworkConnection("192.168.1.1", "10.0.0.1", "TCP", "normal")
conn2 = NetworkConnection("192.168.1.2", "10.0.0.1", "UDP", "neptune")
conn3 = NetworkConnection("192.168.1.3", "10.0.0.2", "TCP", "portsweep")

print("=" * 50)
print("PART 1: CLASS & OBJECT")
print("=" * 50)
print(conn1.info())
print(conn2.info())
print(conn3.info())
print(f"\nApakah conn2 serangan? {conn2.is_attack()}")


# ── PART 2: INHERITANCE (PEWARISAN) ──
# Class anak mewarisi semua dari class induk

class AttackConnection(NetworkConnection):
    """Koneksi yang sudah diidentifikasi sebagai serangan"""
    
    def __init__(self, src_ip, dst_ip, protocol, label, severity):
        # Panggil constructor parent
        super().__init__(src_ip, dst_ip, protocol, label)
        self.severity = severity  # 'low', 'medium', 'high'
    
    def alert(self):
        return f"[ALERT-{self.severity.upper()}] {self.info()}"


print("\n" + "=" * 50)
print("PART 2: INHERITANCE")
print("=" * 50)
attack = AttackConnection("10.0.0.5", "192.168.1.1", "TCP", "DoS", "high")
print(attack.alert())


# ── PART 3: ERROR HANDLING ──
# Menangani error dengan elegan

print("\n" + "=" * 50)
print("PART 3: ERROR HANDLING")
print("=" * 50)

def bagi_traffic(total, normal):
    try:
        persentase = (normal / total) * 100
        return f"Traffic normal: {persentase:.1f}%"
    except ZeroDivisionError:
        return "Error: Total traffic tidak boleh 0!"
    except TypeError:
        return "Error: Input harus berupa angka!"
    finally:
        print("Fungsi selesai dijalankan.")

print(bagi_traffic(125973, 67343))
print(bagi_traffic(0, 100))
print(bagi_traffic("abc", 100))


# ── PART 4: FILE HANDLING ──
# Baca dan tulis file - berguna untuk logging sistem IDS

print("\n" + "=" * 50)
print("PART 4: FILE HANDLING")
print("=" * 50)

# Tulis log
with open('D:/Skripsi/results/ids_log.txt', 'w') as f:
    f.write("=== IDS Log File ===\n")
    f.write(f"{conn1.src_ip} -> {conn1.dst_ip} | {conn1.protocol} | Status: Normal\n")
    f.write(f"{conn2.src_ip} -> {conn2.dst_ip} | {conn2.protocol} | Status: SERANGAN\n")
    f.write(f"{conn3.src_ip} -> {conn3.dst_ip} | {conn3.protocol} | Status: SERANGAN\n")
    f.write(f"[ALERT-HIGH] {attack.src_ip} -> {attack.dst_ip} | Status: SERANGAN\n")

print("Log berhasil ditulis!")

# Baca log
with open('D:/Skripsi/results/ids_log.txt', 'r') as f:
    isi = f.read()
    print("\nIsi log file:")
    print(isi)

print("\nSelesai! Kamu baru saja belajar OOP, Inheritance, Error Handling, dan File Handling!")