//import library
#include <bits/stdc++.h>
#include "mahasiswa.cpp"
#include "dosen.cpp"

//using standard namespace
using namespace std;


int main()
{
    Mahasiswa siswa[2];
    siswa[0] = Mahasiswa("Muhammad Febriansyah Firdaus", "2005202", "L", "MIPA");
    siswa[1] = Mahasiswa("Ghiyats Al-Kadzim","2005453", "P", "MIPA");
    Dosen dosen[2];
    dosen[0] = Dosen("Rosa Ariani Sukamto, M.T.", "2882921", "P", "MIPA", "S2", "Ngoding");
    dosen[1] = Dosen("Herbert, S.Kom., M.T.", "2132132", 'L', "MIPA", "S2", "Interface");

    siswa[0].matkul = Prodi("Ilkom", "22A", "DPBO");
    siswa[1].matkul = Prodi("Pilkom", "31B", "Web");

    cout<<"List Mahasiswa"<<endl;
    cout<<"=============="<<endl;

    for(int i=0; i<=2; i++){
        cout << i+1 <<". Nama : " << siswa[i].get_nama() << endl;
        cout << "   NIM : " << siswa[i].get_nim() << endl;
        cout << "   Gender : " << siswa[i].get_jenis_kelamin() << endl;
        cout << "   Fakultas : " << siswa[i].get_fakultas() << endl;
        cout << "   Prodi : " << siswa[i].matkul.get_nama_prodi() << endl;
        cout << "   Kode : " << siswa[i].matkul.get_kode() << endl;
        cout << "   Course : " << siswa[i].matkul.get_course() << endl;
    }
    return 0;
}