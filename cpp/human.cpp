//import library
#include <iostream>
#include <string>
#include <bits/stdc++.h>
//using standard namespace
using namespace std;
//Human sebagai anak yang diwariskan dari Mahasiswa
class Human
{
    //access modifier private
    private:
        string nik;
        string nama;
        string jenis_kelamin;

    //access modifier publik    
    public:
        //constructor
        Human()
        {
            this->nik = " ";
            this->nama = " ";
            this->jenis_kelamin = " ";
        }

        //penggunaan getter dan setter
        string get_nik()
        {
            return this->nik;
        }

        void set_nik(string nik)
        {
            this->nik = nik;
        }
        
        string get_nama()
        {
            return this->nama;
        }

        void set_nama(string nama)
        {
            this->nama = nama;
        }

        char get_jenis_kelamin()
        {
            return this->jenis_kelamin;
        }

        void set_jenis_kelamin(string jenis_kelamin)
        {
            this->jenis_kelamin = jenis_kelamin;
        }

        //destructor
        ~Human()
        {

        }
};