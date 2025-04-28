import decimal
import sys

print("Madzia")
print('Madzia')

print(type('madzia'))  # <class 'str'>
print('39')
print(39)
print(type(39))  # <class 'int'>
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)
# ctrl / - automatyczny komentarz
# print("59" + 90) # TypeError: can only concatenate str (not "int") to str
print("59"+"90")  # 5990
print(59 * "*")  # ***********************************************************
print(59 * "9")  # 99999999999999999999999999999999999999999999999999999999999

print(int("59"))
print("59" + str("90"))
print(type(3.99))  # <class 'float'>
print(sys.float_info)  # sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1+0.5) # 0.6
print(0.1 + 0.2)  # 0.30000000000000004
# problem z przechowywaniem odwzorowania
# decimal - obejscie problemu zaokrąglen
# zmienna - pudełko na dane
a = decimal.Decimal("10")
print(a)

# ctrl d - powielanie linii
a = decimal.Decimal("1.2345")
b = decimal.Decimal("2.3456")
print(a+b)  # 3.5801
precyzja = decimal.Decimal("0.00")
print((a+b).quantize(precyzja))  # 3.58

# typ logiczny
# prawda fałsz
# True False

print(True)
print(False)

print(int(True))   # 1
print(int(False))  # 0

print(bool(1))  # True
print(bool(0))  # False
print(bool(100))  # True

print(bool(None))  # False
print(bool(""))  # False

print("###############")

tekst = 'Radek'
tekst.upper()  #  """ Return a copy of the string converted to uppercase. """
print(tekst)
print(tekst.upper())  # RADEK
zm = tekst.upper()
print(zm)  # RADEK

# kolekcje - przechowuje wiele elementów
# lista, krotka (tupla), zbior (set), słownik (dict)

lista = [3, 6, 7, 8, 9]
print (lista)  # [3, 6, 7, 8, 9] nie zmienia  kolejnosci

lista2 = lista # kopia referencji, adres w pamieci
print(lista2)  # [3, 6, 7, 8, 9]
print (lista)  # [3, 6, 7, 8, 9]
lista_copy = lista.copy()
lista.clear() # kasowanie elementow z listy
print (lista) # []
print (lista2)  # []
print(lista_copy)  # [3, 6, 7, 8, 9]
print("1###############")
krotka = tuple(lista_copy)  # <class 'tuple'>
print(type(krotka))  # lista do odczytu, pozwala efektywniej zarzadzac pamiecia
print(krotka)  # (3, 6, 7, 8, 9)  nawiasy okragle

zbior = {5, 6, 5, 6, 6, 7,8 ,9, 0}
print(zbior)  # {0, 5, 6, 7, 8, 9} przechowuje unikalne wartości
# nie zachowuje kolejności przy dodawaniu elementów

# słownik
# odwzorowanie json
#{'name' : "Radek", 'age' : 45}
slownik = {'name' : "Radek", 'age' : 45}
print(type(slownik))  # <class 'dict'>
print(slownik)  # {'name': 'Radek', 'age': 45}


print("2###############")

slownik = {'name': ["Radek", "Tomek", "Marek"], "age": 45}
print(slownik["name"])

