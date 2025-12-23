#!/usr/bin/env python
"""
Kopiert Daten aus einer SQLite-Datenbanktabelle in eine andere SQLite-Datenbanktabelle.
"""

import sqlite3
from pathlib import Path
from typing import List, Tuple, Optional


def get_table_columns(cursor: sqlite3.Cursor, table_name: str) -> List[str]:
    """
    Ruft die Spaltennamen einer Tabelle ab.
    
    Args:
        cursor: Datenbank-Cursor
        table_name: Name der Tabelle
        
    Returns:
        Liste der Spaltennamen
    """
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [row[1] for row in cursor.fetchall()]
    return columns


def copy_table_data(
    source_db: str,
    target_db: str,
    source_table: str,
    target_table: str,
    where_clause: Optional[str] = None,
    column_mapping: Optional[dict] = None
) -> int:
    """
    Kopiert Daten von einer Quelltabelle in eine Zieltabelle.
    
    Args:
        source_db: Pfad zur Quelldatenbank
        target_db: Pfad zur Zieldatenbank
        source_table: Name der Quelltabelle
        target_table: Name der Zieltabelle
        where_clause: Optionale WHERE-Bedingung für Quelldaten (z.B. "id > 100")
        column_mapping: Optionales Dictionary für Spaltenzuordnung {quell_spalte: ziel_spalte}
        
    Returns:
        Anzahl der kopierten Datensätze
    """
    try:
        # Verbindung zur Quelldatenbank
        source_conn = sqlite3.connect(source_db)
        source_cursor = source_conn.cursor()
        
        # Verbindung zur Zieldatenbank
        target_conn = sqlite3.connect(target_db)
        target_cursor = target_conn.cursor()
        
        # Spaltennamen der Quelltabelle abrufen
        source_columns = get_table_columns(source_cursor, source_table)
        
        # Spaltennamen der Zieltabelle abrufen
        target_columns = get_table_columns(target_cursor, target_table)
        
        # Spaltenzuordnung bestimmen
        if column_mapping:
            # Verwende benutzerdefinierte Zuordnung
            columns_to_copy = []
            target_cols = []
            for src_col, tgt_col in column_mapping.items():
                if src_col in source_columns and tgt_col in target_columns:
                    columns_to_copy.append(src_col)
                    target_cols.append(tgt_col)
        else:
            # Automatische Zuordnung: Nur gemeinsame Spaltennamen
            columns_to_copy = [col for col in source_columns if col in target_columns]
            target_cols = columns_to_copy.copy()
        
        if not columns_to_copy:
            print("Keine übereinstimmenden Spalten gefunden!")
            return 0
        
        print(f"Zu kopierende Spalten: {', '.join(columns_to_copy)}")
        
        # Daten aus Quelltabelle lesen
        query = f"SELECT {', '.join(columns_to_copy)} FROM {source_table}"
        if where_clause:
            query += f" WHERE {where_clause}"
        
        source_cursor.execute(query)
        rows = source_cursor.fetchall()
        
        if not rows:
            print("Keine Daten zum Kopieren gefunden.")
            return 0
        
        # Daten in Zieltabelle einfügen
        placeholders = ', '.join(['?' for _ in target_cols])
        insert_query = f"INSERT INTO {target_table} ({', '.join(target_cols)}) VALUES ({placeholders})"
        
        target_cursor.executemany(insert_query, rows)
        target_conn.commit()
        
        copied_count = len(rows)
        print(f"{copied_count} Datensätze erfolgreich kopiert.")
        
        return copied_count
        
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        raise
        
    finally:
        if 'source_conn' in locals():
            source_conn.close()
        if 'target_conn' in locals():
            target_conn.close()


def copy_table_data_with_attach(
    source_db: str,
    target_db: str,
    source_table: str,
    target_table: str,
    where_clause: Optional[str] = None
) -> int:
    """
    Kopiert Daten mittels ATTACH DATABASE (alternative Methode).
    Diese Methode ist effizienter für große Datenmengen.
    
    Args:
        source_db: Pfad zur Quelldatenbank
        target_db: Pfad zur Zieldatenbank
        source_table: Name der Quelltabelle
        target_table: Name der Zieltabelle
        where_clause: Optionale WHERE-Bedingung
        
    Returns:
        Anzahl der kopierten Datensätze
    """
    try:
        # Verbindung zur Zieldatenbank
        conn = sqlite3.connect(target_db)
        cursor = conn.cursor()
        
        # Quelldatenbank anhängen
        cursor.execute(f"ATTACH DATABASE '{source_db}' AS source_db")
        
        # Spaltennamen ermitteln
        cursor.execute(f"PRAGMA source_db.table_info({source_table})")
        source_columns = [row[1] for row in cursor.fetchall()]
        
        cursor.execute(f"PRAGMA table_info({target_table})")
        target_columns = [row[1] for row in cursor.fetchall()]
        
        # Gemeinsame Spalten finden
        common_columns = [col for col in source_columns if col in target_columns]
        
        if not common_columns:
            print("Keine übereinstimmenden Spalten gefunden!")
            return 0
        
        print(f"Zu kopierende Spalten: {', '.join(common_columns)}")
        
        # Daten kopieren
        columns_str = ', '.join(common_columns)
        query = f"""
            INSERT INTO {target_table} ({columns_str})
            SELECT {columns_str} FROM source_db.{source_table}
        """
        
        if where_clause:
            query += f" WHERE {where_clause}"
        
        cursor.execute(query)
        copied_count = cursor.rowcount
        
        conn.commit()
        
        # Quelldatenbank trennen
        cursor.execute("DETACH DATABASE source_db")
        
        print(f"{copied_count} Datensätze erfolgreich kopiert.")
        
        return copied_count
        
    except sqlite3.Error as e:
        print(f"Datenbankfehler: {e}")
        raise
        
    finally:
        if 'conn' in locals():
            conn.close()


def main():
    """
    Beispiel-Hauptprogramm.
    """
    # Pfade zu den Datenbanken
    base_path = Path(__file__).parent
    source_db = base_path / "quelle.db"
    target_db = base_path / "ziel.db"
    
    print("=" * 60)
    print("SQLite Daten-Kopier-Tool")
    print("=" * 60)
    
    # Beispiel 1: Einfaches Kopieren aller Daten
    print("\n--- Methode 1: Zwei separate Verbindungen ---")
    try:
        count = copy_table_data(
            source_db=str(source_db),
            target_db=str(target_db),
            source_table="lieferanten",
            target_table="lieferanten"
        )
        print(f"✓ {count} Datensätze kopiert")
    except Exception as e:
        print(f"✗ Fehler: {e}")
    
    # Beispiel 2: Kopieren mit WHERE-Bedingung
    print("\n--- Methode 2: Mit ATTACH DATABASE (effizienter) ---")
    try:
        count = copy_table_data_with_attach(
            source_db=str(source_db),
            target_db=str(target_db),
            source_table="lager",
            target_table="lager",
            where_clause="reserviert = 0"
        )
        print(f"✓ {count} Datensätze kopiert")
    except Exception as e:
        print(f"✗ Fehler: {e}")
    
    # Beispiel 3: Kopieren mit Spaltenzuordnung
    print("\n--- Methode 3: Mit benutzerdefinierter Spaltenzuordnung ---")
    try:
        column_mapping = {
            "kundennummer": "id",
            "name": "kundenname",
            "anschrift": "adresse"
        }
        count = copy_table_data(
            source_db=str(source_db),
            target_db=str(target_db),
            source_table="kunden",
            target_table="kunden_kopie",
            column_mapping=column_mapping
        )
        print(f"✓ {count} Datensätze kopiert")
    except Exception as e:
        print(f"✗ Fehler: {e}")
    
    print("\n" + "=" * 60)
    print("Fertig!")


if __name__ == "__main__":
    main()
