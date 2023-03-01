from human import Human
# Kelas Dosen sebagai child dari kelas Human
class Dosen(Human) :

    #access modifier private
    __nip ="";
    __nama ="";
    __jenis_kelamin ='';
    __fakultas ="";
    __pend_terakhir ="";
    __keahlian ="";
    
    # constructor
    def __init__(self,  nama = "", nip = "", jenis_kelamin = '', fakultas = "", pend_terakhir = "", keahlian = "" ):
        self.__nip = nip
        self.__nama = nama
        self.__jenis_kelamin = jenis_kelamin
        self.__fakultas = fakultas
        self.__pend_terakhir = pend_terakhir
        self.__keahlian = keahlian
        self.univ = None

    # getter and setter
    def get_nip(self):
        return self.__nip
    
    def set_nip(self, nip):
        self.__nip = nip

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

    def get_pend_terakhir(self):
        return self.__pend_terakhir
    
    def set_pend_terakhir(self, pend_terakhir):
        self.__pend_terakhir = pend_terakhir

    def get_keahlian(self):
        return self.__keahlian
    
    def set_keahlian(self, keahlian):
        self.__keahlian = keahlian