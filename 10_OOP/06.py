"""Utwórz klasę Pracownik.

    Pracownik ma stanowisko, wynagrodzenie, imie, nazwisko, staz pracy.

    Pracownik powinen miec roczne podwyżki wg. dowolnie wymyślonego
     sposobu liczenia. Pracownik powinen odprowadzać podatek o wysokoci
     zależnej od swoich zarobków oraz minimalną składkę zdrowotną.

    Pracownik powinien mieć pole typu boolowskiego zawierające status
    studenta. Jeśli pracownik jest studentem jego składka zdrowotna
    wynosi 0%.

    Wszyscy pracownicy mają wspólną nazwę firmy. Spółgłoski imienia
    i nazwiska wraz z nazwą firmy .com tworzą adres mailowy. Np.

    Adam Kowalski Love Python Company

    email -> smkwlsk@lovepythoncompany.com
"""


class Employee:
    def __init__(self, position, payment, name, surname, seniority, is_student):
        self.position = position
        self.payment = payment
        self.name = name
        self.surname = surname
        self.seniority = seniority
        self.is_student = is_student

    def annual_raise(self, annual_procent):
        self.payment += self.payment * (annual_procent / 100)

    def calculate_tax(self):
        if self.is_student:
            return 0
        else:
            if self.payment > 10000:
                return self.payment * 0.1
            else:
                return 0

    def calculate_health_insurance(self):
        if self.is_student:
            return 0
        else:
            return max(20, self.payment * 0.01)

    def generate_email(self, company_name):
        import re

        imie_bez_spacji = re.sub(r"\s+", "", self.name)
        nazwisko_bez_spacji = re.sub(r"\s+", "", self.surname)

        spolgloski_imie = re.findall(r"[^aeiouy]+", imie_bez_spacji, re.IGNORECASE)
        spolgloski_nazwisko = re.findall(r"[^aeiouy]+", nazwisko_bez_spacji, re.IGNORECASE)

        adres_email = spolgloski_imie[0] + spolgloski_nazwisko[0] + "@" + company_name.lower() + ".com"
        return adres_email

def main():

    employee1 = Employee("Programista", 10000, "Adam", "Kowalski", 3, False)
    employee1.annual_raise(5)
    print(f'wypłata po rocznej podwyżce wyniesie: {employee1.payment}')

    tax = employee1.calculate_tax()
    print(f'podatek wyniesie: {tax}')

    health_insurance = employee1.calculate_health_insurance()
    print(f'składka zdrowotna wyniesie: {health_insurance}')

    adres_email = employee1.generate_email("LovePythonCompany")
    print(f'nowy adres email pracownika: {adres_email}')

if __name__ == '__main__':
    main()