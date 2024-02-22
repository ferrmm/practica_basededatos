from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Connect to SQLite database
    connection = sqlite3.connect('estudiantes.db')
    cursor = connection.cursor()

    # Execute a query to fetch data from the 'estudiantes' table
    cursor.execute("SELECT * FROM estudiantes")
    estudiantes = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Render the HTML template with the fetched data
    return render_template('index.html', estudiantes=estudiantes)

if __name__ == '__main__':
    app.run(debug=True)
