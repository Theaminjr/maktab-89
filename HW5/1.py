class King:
    instance = None

    def __new__(cls,*args):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance


class Vazir(King):
    def __new__(cls, *args):
        return object.__new__(cls)
    def __init__(self,name) -> None:
        self.name = name



cyrus = King()
koorosh = King()
print(type(koorosh))
print(cyrus is koorosh)

amirkabir = Vazir("amir")
ali = Vazir("ali")
print(ali is amirkabir)
print(type(amirkabir))



