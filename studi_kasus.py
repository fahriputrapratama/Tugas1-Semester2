# DATA PEGAWAI
nama_karyawan = str(input('nama karyawan : '))
jam_kerja = int(input('jam kerja perhari : '))
tarif = int(input('tarif perjam : '))

# PERGITUNGAN PERHARI
gaji_perhari = jam_kerja*tarif
print(f'gaji {nama_karyawan} perhari adalah : Rp{gaji_perhari:,}')

# PERHITUNGAN PERBULAN
hari_perbulan = int(input('Berapa hari bekerja dalam sebulan : ')) 
gaji_perbulan = gaji_perhari*hari_perbulan
print(f'gaji {nama_karyawan} perbulan adalah : Rp{gaji_perbulan:,}')