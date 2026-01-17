from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Einfache Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f4f4f4;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            h1 {
                color: #333;
            }
            form {
                margin-top: 20px;
            }
            input[type="text"] {
                padding: 8px;
                width: 70%;
                font-size: 16px;
            }
            button {
                padding: 8px 20px;
                background-color: #007bff;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #0056b3;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                background-color: #e9ecef;
                border-radius: 4px;
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Willkommen zur Flask Web-App!</h1>
            <p>Dies ist eine einfache Web-Anwendung mit Flask.</p>
            
            <form method="POST" action="/greet">
                <label for="name">Dein Name:</label><br><br>
                <input type="text" id="name" name="name" placeholder="Gib deinen Namen ein" required>
                <button type="submit">Grüßen</button>
            </form>
            
            <h2>Weitere Seiten:</h2>
            <ul>
                <li><a href="/about">Über die App</a></li>
                <li><a href="/info">Informationen</a></li>
            </ul>
        </div>
    </body>
    </html>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Gast')
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gruß</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .greeting {{
                font-size: 24px;
                color: #28a745;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="greeting">Hallo, {name}! 👋</div>
            <p>Schön, dich hier zu sehen!</p>
            <a href="/">← Zurück zur Startseite</a>
        </div>
    </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Über die App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f4f4f4;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Über diese App</h1>
            <p>Dies ist eine einfache Web-Anwendung, die mit Flask entwickelt wurde.</p>
            <p>Flask ist ein leichtgewichtiges Python Web-Framework für die Erstellung von Web-Anwendungen.</p>
            <a href="/">← Zurück zur Startseite</a>
        </div>
    </body>
    </html>
    '''

@app.route('/info')
def info():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Informationen</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 600px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f4f4f4;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            .info-box {
                background-color: #e7f3ff;
                padding: 15px;
                border-left: 4px solid #2196F3;
                margin: 15px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Informationen</h1>
            <div class="info-box">
                <strong>Framework:</strong> Flask (Python)
            </div>
            <div class="info-box">
                <strong>Version:</strong> 1.0
            </div>
            <div class="info-box">
                <strong>Funktion:</strong> Einfache Web-Anwendung mit mehreren Seiten
            </div>
            <a href="/">← Zurück zur Startseite</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
