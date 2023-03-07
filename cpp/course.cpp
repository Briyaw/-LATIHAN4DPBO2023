//import library
#include <bits/stdc++.h>
#include "prodi.cpp"
//using standard namespace
using namespace std;
//Human sebagai anak yang diwariskan dari Mahasiswa
class Course : public Prodi
{
    //access modifier private
    private:
        string nama_matakuliah;

    //access modifier publik    
    public:
        //constructor
        Course()
        {
            this->nama_matakuliah = " ";
        }

        //penggunaan getter dan setter
        string get_nama_matakuliah()
        {
            return this->nama_matakuliah;
        }

        void set_nama_matakuliah(string nama_matakuliah)
        {
            this->nama_matakuliah = nama_matakuliah;
        }
        

        //destructor
        ~Course()
        {

        }
};