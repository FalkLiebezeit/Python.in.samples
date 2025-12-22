#!/usr/bin/env python
"""
Erstellt die SQLite-Datenbankstruktur für die Lagerverwaltung.
"""

import sqlite3
from pathlib import Path


def create_database(db_path: str = r"C:\Users\Falk\source\repos\Python.in.samples\14 - Databases\Momox\falk.db") -> None:
    """
    Erstellt die Datenbanktabellen für die Lagerverwaltung.
    
    Args:
        db_path: Pfad zur Datenbankdatei
    """
    try:
        with sqlite3.connect(db_path) as con:
            cursor = con.cursor()
            
            # Fremdschlüssel aktivieren
            cursor.execute("PRAGMA foreign_keys = ON")
            
            # Tabelle für Lieferanten erstellen
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS lieferanten (
                    kurzname TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    telefonnummer TEXT
                )
            """)
            
            # Tabelle für Kunden erstellen
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS kunden (
                    kundennummer INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    anschrift TEXT
                )
            """)
            
            # Tabelle für Lager erstellen
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS lager (
                    fachnummer INTEGER PRIMARY KEY,
                    seriennummer INTEGER NOT NULL,
                    komponente TEXT NOT NULL,
                    lieferant TEXT,
                    reserviert INTEGER DEFAULT 0,
                    FOREIGN KEY (lieferant) REFERENCES lieferanten(kurzname),
                    CHECK (reserviert IN (0, 1))
                )
            """)
            
            con.commit()

            print(f"Tabellen erfolgreich erstellt: {Path(db_path).absolute()}")
            
    except sqlite3.Error as e:
        print(f"Fehler beim Erstellen der Tabellen: {e}")
        raise


if __name__ == "__main__":
    create_database()


