
# #ZAD1
# lista = [x for x in range(0,31)]
# print(lista)
# lista2 = [x*2 for x in lista]
# plik = open('zadanie1.txt','w')
# plik.writelines(str(lista2))
# plik.close()

#ZAD2
# plik = open('zadanie1.txt','r')
# print(plik.readline())

#ZAD3
# pierwsza = "w moich snach wciaz Warszawa\n"
# druga = "Pelna, ulic, placow, drzew\n"
# with open('zadanie3.txt','w+') as plik:
#     plik.write(pierwsza)
#     plik.write(druga)
#
# with open('zadanie3.txt','r') as plik:
#     for line in plik:
#         print(line)
#ZAD4
# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         print("Nazwa: ", self.nazwa_produktu)
#         print("ilosc: ",self.ilosc)
#         print("Jednostka: ",self.jednostka_miary)
#         print("Cena: ",self.cena_jed)
#
#     def ile_produktu(self):
#         print("Ile produktu:",self.ilosc, self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         print("Cena za wszystko: ",self.cena_jed * self.ilosc)
#
# produkt = NaZakupy("Ziemniaki", 3, "kg", 2)
# produkt.wyswietl_produkt()
# produkt.ile_produktu()
# produkt.ile_kosztuje()

#ZAD5
#ZAD6


