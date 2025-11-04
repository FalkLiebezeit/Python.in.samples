#!/usr/bin/env python

class KontostandException(Exception):
    def __init__(self, kontostand, betrag):
        super().__init__(kontostand, betrag)
        self.kontostand = kontostand
        self.betrag = betrag

    def __str__(self):
        return "Kontostand zu niedrig: Es werden {}€ mehr benötigt".format(self.betrag - self.kontostand)


class Konto:
    def __init__(self, betrag):
        self.kontostand = betrag

    def abheben(self, betrag):
        if betrag > self.kontostand:
            raise KontostandException(self.kontostand, betrag)
        self.kontostand -= betrag


if __name__ == "__main__":
    k = Konto(1000)
    try:
        k.abheben(2000)
    except KontostandException as e:
        print("Kontostand: {}€".format(e.kontostand))
        print("Abheben von {}€ nicht möglich.".format(e.betrag))

    k.abheben(2000)
