import sqlite3
import os
from pathlib import Path
from typing import Optional


def add_device_column(db_name: str = 'momox.db', table_name: str = 'nll', 
                      column_name: str = 'Device', default_value: str = 'Drucker') -> bool:
    """
    Add a 'Device' column to the 'nll' table in the 'momox.db' database
    and set the value 'Drucker' (Printer) for all records.
    
    Args:
        db_name: Name of the database file (default: 'momox.db')
        table_name: Name of the table to modify (default: 'nll')
        column_name: Name of the column to add (default: 'Device')
        default_value: Default value to set for all records (default: 'Drucker')
    
    Returns:
        bool: True if operation was successful, False otherwise
    """
    # Get database path in the current directory
    db_path = Path(__file__).parent / db_name
    
    # Verify database file exists
    if not db_path.exists():
        print(f"Error: Database file '{db_path}' not found.")
        return False
    
    try:
        # Use context manager for automatic connection handling
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            
            # Check if the column already exists
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = {column[1] for column in cursor.fetchall()}
            
            if column_name in columns:
                print(f"Column '{column_name}' already exists in table '{table_name}'.")
            else:
                # Add 'Device' column (VARCHAR(20))
                cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} VARCHAR(20)")
                print(f"Column '{column_name}' successfully added to table '{table_name}'.")
            
            # Update all records with the default value
            cursor.execute(f"UPDATE {table_name} SET {column_name} = ?", (default_value,))
            affected_rows = cursor.rowcount
            
            # Changes are automatically committed when exiting the context manager
            print(f"{affected_rows} record(s) updated with '{default_value}'.")
            
            # Display result
            cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} = ?", (default_value,))
            count = cursor.fetchone()[0]
            print(f"Total records with {column_name}='{default_value}': {count}")
            
            return True
        
    except sqlite3.Error as e:
        print(f"Database operation error: {e}")
        return False


if __name__ == "__main__":
    # Execute the function and display success status
    success = add_device_column()
    print(f"\nOperation completed {'successfully' if success else 'with errors'}.")
