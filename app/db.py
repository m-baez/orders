import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='mbaez',
    password='noloseman',
    database='pedidos'
)
cursor = db.cursor()

time_zone = cursor.execute('SET lc_time_names = "es_MX"')
