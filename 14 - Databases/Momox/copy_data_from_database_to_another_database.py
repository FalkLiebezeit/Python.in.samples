#!/usr/bin/env python
"""
Copies data from one SQLite database table to another SQLite database table.
"""

import sqlite3
from pathlib import Path
from typing import List, Tuple, Optional


def get_table_columns(cursor: sqlite3.Cursor, table_name: str) -> List[str]:
    """
    Retrieves the column names of a table.
    
    Args:
        cursor: Database cursor
        table_name: Name of the table
        
    Returns:
        List of column names
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
    Copies data from a source table to a target table.
    
    Args:
        source_db: Path to the source database
        target_db: Path to the target database
        source_table: Name of the source table
        target_table: Name of the target table
        where_clause: Optional WHERE condition for source data (e.g., "id > 100")
        column_mapping: Optional dictionary for column mapping {source_column: target_column}
        
    Returns:
        Number of copied records
    """
    try:
        # Connect to source database
        source_conn = sqlite3.connect(source_db)
        source_cursor = source_conn.cursor()
        
        # Connect to target database
        target_conn = sqlite3.connect(target_db)
        target_cursor = target_conn.cursor()
        
        # Retrieve column names from source table
        source_columns = get_table_columns(source_cursor, source_table)
        
        # Retrieve column names from target table
        target_columns = get_table_columns(target_cursor, target_table)
        
        # Determine column mapping
        if column_mapping:
            # Use user-defined mapping
            columns_to_copy = []
            target_cols = []
            for src_col, tgt_col in column_mapping.items():
                if src_col in source_columns and tgt_col in target_columns:
                    columns_to_copy.append(src_col)
                    target_cols.append(tgt_col)
        else:
            # Automatic mapping: Only common column names
            columns_to_copy = [col for col in source_columns if col in target_columns]
            target_cols = columns_to_copy.copy()
        
        if not columns_to_copy:
            print("No matching columns found!")
            return 0
        
        print(f"Columns to copy: {', '.join(columns_to_copy)}")
        
        # Read data from source table
        query = f"SELECT {', '.join(columns_to_copy)} FROM {source_table}"
        if where_clause:
            query += f" WHERE {where_clause}"
        
        source_cursor.execute(query)
        rows = source_cursor.fetchall()
        
        if not rows:
            print("No data to copy found.")
            return 0
        
        # Insert data into target table
        placeholders = ', '.join(['?' for _ in target_cols])
        insert_query = f"INSERT INTO {target_table} ({', '.join(target_cols)}) VALUES ({placeholders})"
        
        target_cursor.executemany(insert_query, rows)
        target_conn.commit()
        
        copied_count = len(rows)
        print(f"{copied_count} records successfully copied.")
        
        return copied_count
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
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
    Copies data using ATTACH DATABASE (alternative method).
    This method is more efficient for large datasets.
    
    Args:
        source_db: Path to the source database
        target_db: Path to the target database
        source_table: Name of the source table
        target_table: Name of the target table
        where_clause: Optional WHERE condition
        
    Returns:
        Number of copied records
    """
    try:
        # Connect to target database
        conn = sqlite3.connect(target_db)
        cursor = conn.cursor()
        
        # Attach source database
        cursor.execute(f"ATTACH DATABASE '{source_db}' AS source_db")
        
        # Determine column names
        cursor.execute(f"PRAGMA source_db.table_info({source_table})")
        source_columns = [row[1] for row in cursor.fetchall()]
        
        cursor.execute(f"PRAGMA table_info({target_table})")
        target_columns = [row[1] for row in cursor.fetchall()]
        
        # Find common columns
        common_columns = [col for col in source_columns if col in target_columns]
        
        if not common_columns:
            print("No matching columns found!")
            return 0
        
        print(f"Columns to copy: {', '.join(common_columns)}")
        
        # Copy data
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
        
        # Detach source database
        cursor.execute("DETACH DATABASE source_db")
        
        print(f"{copied_count} records successfully copied.")
        
        return copied_count
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        raise
        
    finally:
        if 'conn' in locals():
            conn.close()


def main():
    """
    Example main program.
    """
    # Paths to the databases
    base_path = Path(__file__).parent
    source_db = base_path / "nfcdb.db"
    target_db = base_path / "falk.db"
    
    print("=" * 60)
    print("SQLite Data Copy Tool")
    print("=" * 60)
    
    # Example 1: Simple copying of all data
    print("\n--- Method 1: Two separate connections ---")
    try:
        count = copy_table_data(
            source_db=str(source_db),
            target_db=str(target_db),
            source_table="tags",
            target_table="tag"
        )
        print(f"✓ {count} records copied")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Example 2: Copying with WHERE condition
    print("\n--- Method 2: Using ATTACH DATABASE (more efficient) ---")
    try:
        count = copy_table_data_with_attach(
            source_db=str(source_db),
            target_db=str(target_db),
            source_table="lager",
            target_table="lager",
            where_clause="reserviert = 0"
        )
        print(f"✓ {count} records copied")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    # Example 3: Copying with column mapping
    print("\n--- Method 3: With custom column mapping ---")
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
        print(f"✓ {count} records copied")
    except Exception as e:
        print(f"✗ Error: {e}")
    
    print("\n" + "=" * 60)
    print("Done!")


if __name__ == "__main__":
    main()
