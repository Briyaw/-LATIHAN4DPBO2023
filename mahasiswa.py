from human import Human
# kelas Mahasiswa sebagai anak yang diwariskan dari kelas Human
class Mahasiswa(Human):
    # access modifier private
    __nim = "";
    __nama = "";
    __jenis_kelamin = '';
    __fakultas = "";

    # constructor
    def __init__(self,  nama = "", nim = "",jenis_kelamin = '', fakultas = ""):
        self.__nama = nama
        self.__nim = nim
        self.__jenis_kelamin = jenis_kelamin
        self.__fakultas = fakultas
        self.matkul = None #komoditas dari kelas Prodi
        self.univ = None #komoditas dari kelas SivitasAkademik

    # penggunaan getter dan setter
    def get_nim(self):
        return self.__nim
    
    def set_nim(self, nim):
        self.__nim = nim

    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama  

    def get_jenis_kelamin(self):
        return self.__jenis_kelamin
    
    def set_jenis_kelamin(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin

    def get_fakultas(self):
        return self.__fakultas
    
    def set_fakultas(self, fakultas):
        self.__fakultas = fakultas      

    