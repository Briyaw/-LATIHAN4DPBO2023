from dosen import Dosen
from mahasiswa import Mahasiswa
from prodi import Prodi

#Pengisian beberapa data mahasiswa dan dosen
siswa = [Mahasiswa("Muhammad Febriansyah Firdaus", "2005202", 'L', "MIPA"), Mahasiswa("Ghiyats Al-Kadzim","2005453", 'P', "MIPA")]
dosen = [Dosen("Rosa Ariani Sukamto, M.T.", "2882921", 'P', "MIPA", "S2", "Ngoding"), Dosen("Herbert, S.Kom., M.T.", "2132132", 'L', "MIPA", "S2", "Interface")]
#array baris 2 sengaja tidak di set datanya untuk test case pengisian data Prodi
siswa[0].matkul =Prodi("Ilkom", "22A", "DPBO")

#Menampilkan data mahasiswa
print("List Mahasiswa")
print("==============")

i=0
for obj in siswa :
    print(str(i+1) + ". Nama : " + siswa[i].get_nama())
    print("   NIM : " + siswa[i].get_nim())
    print("   Gender : " +siswa[i].get_jenis_kelamin())
    print("   Fakultas : " +siswa[i].get_fakultas())
    #jika kita mengeset data Prodi
    if obj.matkul :
        print("   Prodi : " +siswa[i].matkul.get_nama_prodi())
        print("   Kode : " +siswa[i].matkul.get_kode())
        print("   Course : " +siswa[i].matkul.get_course())
    i = i + 1

    print('')

#Menampilkan data dosen
print("List Dosen")
print("==============")
i=0
for obj in dosen :
    print(str(i+1) + ". Nama : " + dosen[i].get_nama())
    print("   NIP : " + dosen[i].get_nip())
    print("   Gender : " +dosen[i].get_jenis_kelamin())
    print("   Fakultas : " +dosen[i].get_fakultas())
    print("   Pend. Teakhir : " +dosen[i].get_pend_terakhir())
    print("   Keahlian : " +dosen[i].get_keahlian())
    i = i + 1

    print('')


#Saya Muhammad Febriansyah Firdaus mengerjakan Latihan4 dalam mata kuliah
#DPBO untuk keberkahanNya maka saya tidak
#melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.