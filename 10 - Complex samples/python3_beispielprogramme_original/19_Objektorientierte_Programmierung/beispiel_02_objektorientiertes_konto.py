#!/usr/bin/env python

class Konto:
    def __init__(self, inhaber, kontonummer, kontostand, max_tagesumsatz=1500):
        self.inhaber = inhaber
        self.kontonummer = kontonummer
        self.kontostand = kontostand
        self.max_tagesumsatz = max_tagesumsatz
        self.umsatz_heute = 0

    def geldtransfer(self, ziel, betrag):
        # Hier erfolgt der Test, ob der Transfer möglich ist
        if (betrag < 0 or self.umsatz_heute + betrag > self.max_tagesumsatz or ziel.umsatz_heute + betrag > ziel.max_tagesumsatz):
            # Transfer unmöglich
            return False
        else:
            # Alles OK - Auf geht's
            self.kontostand -= betrag
            self.umsatz_heute += betrag
            ziel.kontostand += betrag
            ziel.umsatz_heute += betrag
            return True

    def einzahlen(self, betrag):
        if betrag < 0 or self.umsatz_heute + betrag > self.max_tagesumsatz:
            # Tageslimit überschritten oder ungültiger Betrag
            return False
        else:
            self.kontostand += betrag
            self.umsatz_heute += betrag
            return True

    def auszahlen(self, betrag):
        if betrag < 0 or self.umsatz_heute + betrag > self.max_tagesumsatz:
            # Tageslimit überschritten oder ungültiger Betrag
            return False
        else:
            self.kontostand -= betrag
            self.umsatz_heute += betrag
            return True

    def zeige(self):
        print("Konto von {}".format(self.inhaber))
        print("Aktueller Kontostand: {:.2f} Euro".format(self.kontostand))
        print("(Heute schon {:.2f} von {} Euro umgesetzt)".format(self.umsatz_heute, self.max_tagesumsatz))


if __name__ == "__main__":
    k1 = Konto("Heinz Meier", 567123, 12350.0)
    k2 = Konto("Erwin Schmidt", 396754, 15000.0)
    k1.geldtransfer(k2, 160)
    k2.geldtransfer(k1, 1000)
    k2.geldtransfer(k1, 500)
    k2.einzahlen(500)
    k1.zeige()
    k2.zeige()
