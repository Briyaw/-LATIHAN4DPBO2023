from prodi import Prodi
# Kelas Course sebagai child dari kelas Prodi
class Course(Prodi) :
    #access modifier private
    __nama_matakuliah =""; #nama_matakuliah isinya sama dengan course jadi saya bingung di bagian situ untuk menentukan kelasnya sebagai komposit atau pewarisan

    # constructor
    def __init__(self, nama_matakuliah = ""):
        self.__nama_matakuliah = nama_matakuliah

    # getter and setter
    def get_nama_matakuliah(self):
        return self.__nama_matakuliah
    
    def set_nama_matakuliah(self, nama_matakuliah):
        self.__nama_matakuliah = nama_matakuliah
