from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

# Connect to MySQL
connection = pymysql.connect(
    host="mysql",
    user="root",
    password="root123",
    autocommit=True
)

cursor = connection.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS flaskdb")

# Select Database
connection.select_db("flaskdb")

# Create Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS aws_services(
    id INT AUTO_INCREMENT PRIMARY KEY,
    service_name VARCHAR(100),
    service_type VARCHAR(100),
    region VARCHAR(100),
    status VARCHAR(50)
)
""")

# Home Page
@app.route('/', methods=['GET', 'POST'])
def home():

    # Insert data into MySQL
    if request.method == 'POST':

        service_name = request.form['service_name']
        service_type = request.form['service_type']
        region = request.form['region']
        status = request.form['status']

        cursor.execute("""
        INSERT INTO aws_services(service_name, service_type, region, status)
        VALUES(%s,%s,%s,%s)
        """, (service_name, service_type, region, status))

        connection.commit()

    # Fetch all data
    cursor.execute("SELECT * FROM aws_services")

    services = cursor.fetchall()

    return render_template("index.html", services=services)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)