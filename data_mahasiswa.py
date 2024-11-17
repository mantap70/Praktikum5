data_mahasiswa = []

while True:
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai_tugas = float(input("Nilai Tugas: "))
    nilai_uts = float(input("Nilai UTS: "))
    nilai_uas = float(input("Nilai UAS: "))
    
    nilai_akhir = (nilai_tugas * 0.3) + (nilai_uts * 0.35) + (nilai_uas * 0.35)
    
    data_mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": nilai_tugas,
        "UTS": nilai_uts,
        "UAS": nilai_uas,
        "Nilai Akhir": nilai_akhir
    })
    
    tambah = input("Tambah data(y/t)? ")
    if tambah.lower() == 't':
        break

print("\nDaftar Mahasiswa:")
print("="*60)
print(f"{'No':<3} {'Nama':<15} {'NIM':<10} {'Tugas':<6} {'UTS':<6} {'UAS':<6} {'Akhir':<6}")
print("="*60)
for i, mhs in enumerate(data_mahasiswa, start=1):
    print(f"{i:<3} {mhs['Nama']:<15} {mhs['NIM']:<10} {mhs['Tugas']:<6.2f} {mhs['UTS']:<6.2f} {mhs['UAS']:<6.2f} {mhs['Nilai Akhir']:<6.2f}")
print("="*60)