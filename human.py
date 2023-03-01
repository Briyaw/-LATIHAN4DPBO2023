class Human:
    
    #access modifier private
    __nik = "";
    __nama = "";
    __jenis_kelamin = '';

    # constructor
    def __init__(self, nik = "", nama = "", jenis_kelamin = ''):
        self.__nik = nik
        self.__nama = nama
        self.__jenis_kelamin
       

    # penggunaan getter dan setter
    def get_nik(self):
        return self.__nik
    
    def set_nik(self, nik):
        self.__nik = nik

    def get_nama(self):
        return self.__nama
    
    def set_nama(self, nama):
        self.__nama = nama
    
    def get_jenis_kelamin(self):
        return self.__jenis_kelamin
    
    def set_jenis_kelamin(self, jenis_kelamin):
        self.__jenis_kelamin = jenis_kelamin

    #output list nama campuran dosen dan mahasiswa, note:belum selesai pengerjaan
    def listNama(self, names):
        for name in names:
            print(name.get_nama)
            print(name.get_jenis_kelamin)
            print(name.get_nik)