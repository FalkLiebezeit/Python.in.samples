#!/usr/bin/env python
"""
Liest und zeigt Daten aus der Datenbank.
Demonstriert verschiedene SELECT-Abfragen mit JOINs.
"""

import sqlite3
from typing import List, Tuple


def query_items_by_supplier_phone(
    db_path: str = r"C:\Users\Falk\source\repos\Python.in.samples\14 - Databases\Momox\falk.db", 
    phone: str = "011235813"
) -> List[Tuple]:
    """
    Fragt alle Lagerartikel eines Lieferanten anhand der Telefonnummer ab.
    
    Args:
        db_path: Pfad zur Datenbankdatei
        phone: Telefonnummer des Lieferanten
        
    Returns:
        Liste von Tupeln mit (fachnummer, komponente, lieferantenname)
    """
    try:
        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            
            # SQL-Abfrage mit INNER JOIN (moderne Syntax)
            # Findet alle Artikel vom Lieferanten mit gegebener Telefonnummer
            sql = """
                SELECT 
                    l.fachnummer, 
                    l.komponente, 
                    lf.name AS lieferant
                FROM lager l
                INNER JOIN lieferanten lf ON l.lieferant = lf.kurzname
                WHERE lf.telefonnummer = ?
                ORDER BY l.fachnummer
            """
            
            cursor.execute(sql, (phone,))
            results = cursor.fetchall()
            
            return results
            
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        return []


def display_items(items: List[Tuple]) -> None:
    """
    Zeigt die Lagerartikel formatiert an.
    
    Args:
        items: Liste von Tupeln mit Artikeldaten
    """
    if not items:
        print("Keine Artikel gefunden.")
        return
    
    print(f"\nGefundene Artikel: {len(items)}")
    print("-" * 70)
    print(f"{'Fachnr':<8} {'Komponente':<30} {'Lieferant':<30}")
    print("-" * 70)
    
    for fachnr, komponente, lieferant in items:
        print(f"{fachnr:<8} {komponente:<30} {lieferant:<30}")
    
    print("-" * 70)


def query_all_items_with_details(db_path: str = "lagerverwaltung.db") -> None:
    """
    Zeigt alle Lagerartikel mit vollständigen Details an.
    
    Args:
        db_path: Pfad zur Datenbankdatenbank
    """
    try:
        with sqlite3.connect(db_path) as con:
            # Row Factory für dict-ähnlichen Zugriff
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            
            # Umfassende Abfrage mit LEFT JOINs
            sql = """
                SELECT 
                    l.fachnummer,
                    l.seriennummer,
                    l.komponente,
                    lf.name AS lieferant_name,
                    lf.telefonnummer AS lieferant_tel,
                    k.name AS kunde_name,
                    CASE 
                        WHEN l.reserviert > 0 THEN 'Ja'
                        ELSE 'Nein'
                    END AS ist_reserviert
                FROM lager l
                LEFT JOIN lieferanten lf ON l.lieferant = lf.kurzname
                LEFT JOIN kunden k ON l.reserviert = k.kundennummer
                ORDER BY l.fachnummer
            """
            
            cursor.execute(sql)
            
            print("\n" + "=" * 100)
            print("ALLE LAGERARTIKEL MIT DETAILS")
            print("=" * 100)
            
            for row in cursor.fetchall():
                print(f"\nFach {row['fachnummer']}: {row['komponente']}")
                print(f"  Seriennummer: {row['seriennummer']}")
                print(f"  Lieferant: {row['lieferant_name']} ({row['lieferant_tel']})")
                print(f"  Reserviert: {row['ist_reserviert']}", end="")
                if row['kunde_name']:
                    print(f" für {row['kunde_name']}")
                else:
                    print()
            
            print("=" * 100)
            
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")


if __name__ == "__main__":
    # Beispiel 1: Artikel eines bestimmten Lieferanten
    print("BEISPIEL 1: Artikel von FiboComputing Inc.")
    items = query_items_by_supplier_phone()
    display_items(items)
    
    # Beispiel 2: Alle Artikel mit vollständigen Details
    print("\n\nBEISPIEL 2: Alle Artikel mit Details")
    query_all_items_with_details()

