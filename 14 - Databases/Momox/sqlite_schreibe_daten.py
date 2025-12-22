#!/usr/bin/env python
"""
Füllt die Lagerverwaltungsdatenbank mit Beispieldaten.
Fügt Testdaten für Lagerartikel, Lieferanten und Kunden ein.
"""

import sqlite3
from typing import Tuple


def insert_sample_data(db_path: str = "lagerverwaltung.db") -> None:
    """
    Fügt Beispieldaten in die Datenbanktabellen ein.
    
    Args:
        db_path: Pfad zur Datenbankdatei
        
    Raises:
        sqlite3.Error: Bei Datenbankfehlern
    """
    try:
        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            
            # Lieferanten zuerst einfügen (wegen Foreign Key Constraint)
            lieferanten = (
                ("FC", "FiboComputing Inc.", "011235813"),
                ("LPE", "LettgenPetersErnesti", "026741337"),
                ("GC", "Golden Computers", "016180339")
            )
            cursor.executemany(
                "INSERT OR IGNORE INTO lieferanten VALUES (?,?,?)", 
                lieferanten
            )
            print(f"{len(lieferanten)} Lieferanten eingefügt")
            
            # Kunden einfügen
            kunden = (
                (12, "Heinz Elhurg", "Turnhallenstr. 1, 3763 Sporthausen"),
                (57, "Markus Altbert", "Kämperweg 24, 2463 Duisschloss"),
                (64, "Steve Apple", "Podmacstr 2, 7467 Iwarhausen")
            )
            cursor.executemany(
                "INSERT OR IGNORE INTO kunden VALUES (?,?,?)", 
                kunden
            )
            print(f"{len(kunden)} Kunden eingefügt")
            
            # Lagerartikel einfügen
            # Format: (fachnummer, seriennummer, komponente, lieferant, reserviert)
            lagerartikel = (
                (1, "2607871987", "Grafikkarte Typ 1", "FC", 0),
                (2, "19870109", "Prozessor Typ 13", "LPE", 57),
                (10, "06198823", "Netzteil Typ 3", "FC", 0),
                (25, "11198703", "LED-Lüfter", "FC", 57),
                (26, "19880105", "Festplatte 10 TB", "LPE", 12)
            )
            cursor.executemany(
                "INSERT OR IGNORE INTO lager VALUES (?,?,?,?,?)", 
                lagerartikel
            )
            print(f"{len(lagerartikel)} Lagerartikel eingefügt")
            
            # Änderungen speichern
            con.commit()
            print(f"\nAlle Daten erfolgreich in '{db_path}' gespeichert")
            
    except sqlite3.IntegrityError as e:
        print(f"Integritätsfehler: {e}")
        print("Hinweis: Einige Daten existieren bereits oder verletzten Constraints")
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        raise


if __name__ == "__main__":
    insert_sample_data()
