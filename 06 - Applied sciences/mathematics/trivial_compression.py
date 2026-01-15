# trivial_compression.py
# Aus "Algorithmen in Python", Kapitel 1
# Copyright 2018 David Kopec
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1  # Mit Sentinel starten
        for nucleotide in gene.upper():
            self.bit_string <<= 2  # Zwei Bit nach links verschieben
            if nucleotide == "A":  # Letzte zwei Bits in 00 ändern
                self.bit_string |= 0b00
            elif nucleotide == "C":  # Letzte zwei Bits in 01 ändern
                self.bit_string |= 0b01
            elif nucleotide == "G":  # Letzte zwei Bits in 10 ändern
                self.bit_string |= 0b10
            elif nucleotide == "T":  # Letzte zwei Bits in 11 ändern
                self.bit_string |= 0b11
            else:
                raise ValueError("Ungültiges Nukleotid:{}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2):  # - 1, um Sentinel auszuschließen
            bits: int = self.bit_string >> i & 0b11  # Nur 2 relevante Bits lesen
            if bits == 0b00:  # A
                gene += "A"
            elif bits == 0b01:  # C
                gene += "C"
            elif bits == 0b10:  # G
                gene += "G"
            elif bits == 0b11:  # T
                gene += "T"
            else:
                raise ValueError("Ungültige Bits:{}".format(bits))
        return gene[::-1]  # [::-1] kehrt String durch Rückwärts-Slicing um

    def __str__(self) -> str:  # String-Darstellung für formatierte Ausgabe
        return self.decompress()


if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
    print("Original: {} Byte".format(getsizeof(original)))
    compressed: CompressedGene = CompressedGene(original)  # Komprimieren
    print("Komprimiert: {} Byte".format(getsizeof(compressed.bit_string)))
    print(compressed)  # Dekomprimiert
    print("Originaldaten und dekomprimierte Daten sind identisch: {}".format(original == compressed.decompress()))
