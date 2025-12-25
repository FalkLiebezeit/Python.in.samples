"""
Flask Web App to display all data from the Tags table in the momox.db database.
Optimized version with better error handling and resource management.
"""

from flask import Flask, render_template, jsonify
import sqlite3
import os
from contextlib import contextmanager

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # Support for non-ASCII characters in JSON

# Database path configuration
DB_PATH = os.path.join(os.path.dirname(__file__), 'momox.db')


@contextmanager
def get_db_connection():
    """Context manager for database connections to ensure proper resource cleanup."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Enable column access by name
    try:
        yield conn
    finally:
        conn.close()


@app.route('/')
def index():
    """Main page - displays all tags from the database in a formatted table."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tags')
            tags = cursor.fetchall()
            column_names = [description[0] for description in cursor.description] if cursor.description else []
        
        return render_template('tags.html', tags=tags, columns=column_names)
    
    except sqlite3.Error as e:
        error_msg = f"""
        <h1>Database Error</h1>
        <p>Error accessing the database: {str(e)}</p>
        <p>Please ensure that the 'momox.db' file exists in the same directory as the application.</p>
        <p><a href="/">Try Again</a></p>
        """
        return error_msg, 500
    except Exception as e:
        return f"<h1>Error</h1><p>An unexpected error occurred: {str(e)}</p><p><a href='/'>Return Home</a></p>", 500


@app.route('/api/tags')
def api_tags():
    """API endpoint - returns tags data as JSON for programmatic access."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tags')
            tags = cursor.fetchall()
            column_names = [description[0] for description in cursor.description] if cursor.description else []
        
        # Convert rows to dictionaries
        tags_list = [dict(zip(column_names, row)) for row in tags]
        
        return jsonify({
            'success': True,
            'count': len(tags_list),
            'columns': column_names,
            'data': tags_list
        })
    
    except sqlite3.Error as e:
        return jsonify({
            'success': False,
            'error': f'Database error: {str(e)}'
        }), 500


@app.route('/raw')
def raw_data():
    """Displays raw data as a simple list."""
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Tags')
            tags = cursor.fetchall()
        
        result = "<h1>Tags - Raw Data</h1>"
        result += f"<p>Number of entries: {len(tags)}</p>"
        result += "<ul style='font-family: monospace;'>"
        for tag in tags:
            result += f"<li>{dict(tag)}</li>"
        result += "</ul>"
        result += '<br><a href="/">← Back to formatted view</a> | <a href="/api/tags">View as JSON</a>'
        
        return result
    
    except sqlite3.Error as e:
        return f"<h1>Database Error</h1><p>{str(e)}</p>", 500


@app.errorhandler(404)
def not_found(error):
    """Custom 404 error handler."""
    return "<h1>404 - Page Not Found</h1><p><a href='/'>Return Home</a></p>", 404


if __name__ == '__main__':
    # Check if database exists on startup
    if not os.path.exists(DB_PATH):
        print(f"⚠️  WARNING: Database '{DB_PATH}' not found!")
        print("Please ensure that 'momox.db' exists in the same directory.")
    else:
        print(f"✓ Database found: {DB_PATH}")
    
    print("\n🚀 Starting Flask server...")
    print("📍 Access the app at: http://localhost:5000")
    print("📊 API endpoint available at: http://localhost:5000/api/tags\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
