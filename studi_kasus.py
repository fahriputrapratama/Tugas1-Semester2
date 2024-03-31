# DATA PEGAWAI
nama_karyawan = str(input('nama karyawan : '))
jam_kerja = int(input('jam kerja perhari : '))
tarif = int(input('tarif perjam : '))

# PERGITUNGAN PERHARI
gaji_perhari = jam_kerja*tarif

# PERHITUNGAN PERBULAN
hari_perbulan = 20 
gaji_perbulan = gaji_perhari*hari_perbulan
print(f'gaji {nama_karyawan} perbulan adalah : {gaji_perbulan:,}')
