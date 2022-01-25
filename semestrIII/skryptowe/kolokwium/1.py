import datetime


class PESEL:
    def __init__(self, pesel: str, birthDate: str, sex: str) -> None:
        if (len(pesel) != 11 or not pesel.isnumeric() or sex not in "mf" or birthDate[2] != ":" or birthDate[5] != ":" or
                not birthDate[3:5].isnumeric() or not birthDate[0:2].isnumeric() or not birthDate[-4:].isnumeric()):
            raise Exception("Źle podane dane")
        if (int(birthDate[3:5]) > 12 or int(birthDate[0:2]) > 31 or int(birthDate[-4:]) > 2999):
            raise Exception("zła data urodzenia")
        self.pesel = pesel
        # DD:MM:YYYY
        self.birthDate = birthDate
        self.sex = sex
        self.intPesel = [int(x) for x in self.pesel]
        self.controlSum = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    def check(self):
        return "Pesel poprawny" if (self.pesel[0:2] == self.birthDate[-2:])\
            and (self.pesel[2:4] == self.birthDate[3:5])\
            and (self.pesel[4:6] == self.birthDate[0:2])\
            and (self.intPesel[9] % 2 == 1 and self.sex == "m") or (
            self.intPesel[9] % 2 == 0 and self.sex == "f")\
            and ((10-(sum([self.intPesel[x] * self.controlSum[x]
                           for x in range(len(self.controlSum))]) % 10)) % 10)\
            else "Pesel niepoprawny"


def main():
    try:
        p = PESEL("99010118713", "01:01:1999", "m")
        print(p.check())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
