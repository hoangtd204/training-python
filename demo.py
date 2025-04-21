class PhuongTien():
    def __init__(self, name, velocity):
        self.name = name
        self.velocity = velocity

    def dichuyen(self):
        print(f"{self.name} dang di chuyen voi van toc {self.velocity} km/h")


class Oto(PhuongTien):
    def __init__(self, name, velocity, socho):
        super().__init__(name, velocity)
        self.socho = socho

    def dichuyen(self):
        print(f"OTO {self.name} cho {self.socho} dang chay {self.velocity} km/h")


class Xemay(PhuongTien):
    def __init__(self, name, velocity, loaixe):
        super().__init__(name, velocity)
        self.loaixe = loaixe

    def dichuyen(self):
        print(
            f"Xe may {self.name} loai {self.loaixe} dang chay {self.velocity}km/h")


transList = [Xemay("HonDa", 60, "xe_so"),
             Oto("Toyota", 60, "6 cho"),
             Oto("Kia", 60, "4 cho"),
             Xemay("vision", 80, "xe_ga")
             ]


def Tuychon(listpt):
    for loaipt in listpt:
        loaipt.dichuyen()


Tuychon(transList)
