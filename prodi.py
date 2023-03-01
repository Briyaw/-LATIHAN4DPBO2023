class Prodi :
    #access modifier private
    __nama_prodi = "";
    __kode = "";
    __course = "";

    # constructor
    def __init__(self, nama_prodi = "", kode = "", course = ""):
        self.__nama_prodi = nama_prodi
        self.__kode = kode
        self.__course = course

    # penggunaan getter dan setter
    def get_nama_prodi(self):
        return self.__nama_prodi
    
    def set_nama_prodi(self, nama_prodi):
        self.__nama_prodi = nama_prodi

    def get_kode(self):
        return self.__kode
    
    def set_kode(self, kode):
        self.__kode = kode
    
    def get_course(self):
        return self.__course
    
    def set_course(self, course):
        self.__course = course

    #fungsi untuk menambahkan isi array, note: tapi tidak terpakai
    def __str__(self):
        lines = []
        lines.append(f'{self.nama_prodi}, {self.kode}, {self.course}')
        return '\n'.join(lines)
