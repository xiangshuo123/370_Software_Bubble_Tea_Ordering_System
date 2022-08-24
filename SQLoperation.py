import SQLconnector as sql
import psycopg2

def addTable():

    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "DROP TABLE IF EXISTS coffee, food, milk_tea, account"
    cursor.execute(SQL_query)
    SQL_query = "CREATE TABLE coffee(name VARCHAR (50) PRIMARY KEY UNIQUE,price VARCHAR (50))"
    cursor.execute(SQL_query)
    SQL_query = "CREATE TABLE food AS SELECT * FROM coffee"
    cursor.execute(SQL_query)
    SQL_query = "CREATE TABLE milk_tea AS SELECT * FROM coffee"
    cursor.execute(SQL_query)
    SQL_query = "CREATE TABLE account(username VARCHAR (50) PRIMARY KEY ,passwd VARCHAR (50),owner_name VARCHAR (50))"
    cursor.execute(SQL_query)
    conn.commit()
    cursor.close()
    conn.close()
    sql.add_coffee("Cappuccino", "4.5")
    sql.add_coffee("Latte", "4.5")
    sql.add_coffee("Mocha", "4.5")
    sql.add_coffee("Americano", "2.9")
    sql.add_coffee("Caramel Macchiato", "4.5")

    sql.add_food("Takoyaki","4.99")
    sql.add_food("Bubble Waffle", "7.99")
    #
    sql.add_milk_tea("Blueberry Cheese Storm","6.49")
    sql.add_milk_tea("Brown Sugar Milk Tea","4.99")
    #
    sql.add_user("cmpt370","123456","Kayla")

    # print(sql.fetch_all_milktea(), sql.fetch_all_coffee())