import psycopg2

# Trying to connect database using library psycopg2.



def add_user(usr, password, nm):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "INSERT INTO account (username, passwd, owner_name) VALUES(%s,%s,%s)"
    cursor.execute(SQL_query, (usr, password, nm))
    conn.commit()
    cursor.close()
    conn.close()


def fetch_user_info(usr):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM account WHERE username = %s"
    cursor.execute(SQL_query, (usr,))
    conn.commit()
    res = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return res


def delete_user(usr):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "DELETE FROM account WHERE username = %s"
    cursor.execute(SQL_query,(usr,))
    conn.commit()
    cursor.close()
    conn.close()

def add_food(nm, price):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "INSERT INTO food (name, price) VALUES(%s,%s)"
    cursor.execute(SQL_query, (nm, price))
    conn.commit()
    cursor.close()
    conn.close()


def delete_food(item):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "DELETE FROM food WHERE name = %s"
    cursor.execute(SQL_query, (item,))
    conn.commit()
    cursor.close()
    conn.close()


def add_coffee(nm, price):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "INSERT INTO coffee (name, price) VALUES(%s,%s)"
    cursor.execute(SQL_query, (nm, price))
    conn.commit()
    cursor.close()
    conn.close()


def delete_coffee(item):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "DELETE FROM coffee WHERE name = %s"
    cursor.execute(SQL_query, (item,))
    conn.commit()
    cursor.close()
    conn.close()


def add_milk_tea( nm, price):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "INSERT INTO milk_tea (name, price) VALUES(%s,%s)"
    cursor.execute(SQL_query, (nm, price))
    conn.commit()
    cursor.close()
    conn.close()


def delete_milk_tea(item):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "DELETE FROM milk_tea WHERE name = %s"
    cursor.execute(SQL_query, (item,))
    conn.commit()
    cursor.close()
    conn.close()

def fetch_food(item_name):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM food WHERE name = %s "
    cursor.execute(SQL_query, (item_name,))
    conn.commit()
    res = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return res


def fetch_milk_tea(item_name):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM milk_tea WHERE name = %s "
    cursor.execute(SQL_query, (item_name,))
    conn.commit()
    res = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return res


def fetch_coffee(item_name):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM coffee WHERE name = %s "
    cursor.execute(SQL_query, (item_name,))
    conn.commit()
    res = cursor.fetchall()[0]
    cursor.close()
    conn.close()
    return res


def check_passwd(usr, pw):
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT passwd FROM account WHERE username = %s"
    cursor.execute(SQL_query, (usr,))
    res = cursor.fetchone()
    if res is None:
        return False
    else:
        if res[0] == pw:
            return True
        else:
            return False


def fetch_all_reg():
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM account"
    cursor.execute(SQL_query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def fetch_all_food():
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM food"
    cursor.execute(SQL_query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res


def fetch_all_coffee():
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM coffee"
    cursor.execute(SQL_query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res

def fetch_all_milktea():
    conn = psycopg2.connect(host="localhost", user="postgres", password="19971031xs", dbname="postgres")
    cursor = conn.cursor()
    SQL_query = "SELECT * FROM milk_tea"
    cursor.execute(SQL_query)
    res = cursor.fetchall()
    cursor.close()
    conn.close()
    return res



