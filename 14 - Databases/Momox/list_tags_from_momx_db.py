#!/usr/bin/env python
"""
Lists all data from the 'tags' table in the momox.db database.
"""

import sqlite3
from pathlib import Path
from typing import List, Tuple


def list_tags(database_path: str) -> List[Tuple]:
    """
    Retrieves and displays all data from the tags table.
    
    Args:
        database_path: Path to the falk.db database
        
    Returns:
        List of tuples containing all rows from the tags table
    """
    try:
        # Connect to the database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        
        # Get column names
        cursor.execute("PRAGMA table_info(tags)")
        columns_info = cursor.fetchall()
        column_names = [col[1] for col in columns_info]
        
        # Fetch all data from tags table
        cursor.execute("SELECT * FROM tags")
        rows = cursor.fetchall()
        
        # Display results
        print("=" * 80)
        print(f"Tags Table - Total Records: {len(rows)}")
        print("=" * 80)
        
        if not rows:
            print("No data found in the tags table.")
            return []
        
        # Print column headers
        header = " | ".join([f"{name:15}" for name in column_names])
        print(header)
        print("-" * len(header))
        
        # Print rows
        for row in rows:
            row_str = " | ".join([f"{str(val):15}" for val in row])
            print(row_str)
        
        print("=" * 80)
        
        return rows
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
        
    except Exception as e:
        print(f"Error: {e}")
        return []
        
    finally:
        if 'conn' in locals():
            conn.close()


def get_table_info(database_path: str, table_name: str = "tags"):
    """
    Displays detailed information about the table structure.
    
    Args:
        database_path: Path to the database
        table_name: Name of the table (default: tags)
    """
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        
        print(f"\nTable Structure: {table_name}")
        print("-" * 80)
        
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()
        
        print(f"{'Column ID':<12} {'Name':<20} {'Type':<15} {'Not Null':<10} {'Default':<15} {'Primary Key'}")
        print("-" * 80)
        
        for col in columns:
            col_id, name, col_type, not_null, default_val, pk = col
            print(f"{col_id:<12} {name:<20} {col_type:<15} {not_null:<10} {str(default_val):<15} {pk}")
        
        conn.close()
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")


def main():
    """
    Main program.
    """
    # Path to the database
    base_path = Path(__file__).parent
    database_path = base_path / "momox.db"
    
    # Check if database exists
    if not database_path.exists():
        print(f"Error: Database not found at {database_path}")
        print("Please ensure 'momox.db' exists in the same directory as this script.")
        return
    
    print(f"\nDatabase: {database_path}")
    
    # Display table structure
    get_table_info(str(database_path), "tags")
    
    # List all tags
    print("\n")
    tags = list_tags(str(database_path))
    
    # Summary
    print(f"\nTotal records retrieved: {len(tags)}")


if __name__ == "__main__":
    main()
