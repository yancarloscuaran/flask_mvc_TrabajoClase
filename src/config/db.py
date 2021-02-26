import mariadb

config ={
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'flask_mvc'
}

#** para accionar todos los elementos del diccionario config
DB = mariadb.connect(**config)
DB.autocommit = True