"""1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi na
 funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią
 wartość
 (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru."""


import random


def bmi_calculator(w, h):
    BMI = w / (h ** 2)
    return BMI



def BMI_informations(info):
    if BMI > 18.5 < 24.99:
        print("waga normalna")
    elif BMI > 25.0 < 29.9:
        print("nadwaga")
    elif BMI > 30.0 < 34.99:
        print("nadwaga")
    elif BMI > 35.0:
        print("otyłość")
    else:
        print("niedowaga")


w = float(input("podaj wagę w kg:"))
h = float(input("podaj wzrost w m:"))



your_bmi = bmi_calculator(w, h)
print("twoje BMI wynosi:", BMI)

print("Ocena BMI wynosi:", BMI_informations(your_bmi))



