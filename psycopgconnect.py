import psycopg2


def create():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Ayush123' host='localhost' port='5000'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='Ayush123' host='localhost' port='5000'")
    cur = conn.cursor()
    # cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item, quantity, price))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity, price, item):
    conn = psycopg2.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()

create()
# delete("Wine glass")
# update(15, 3.5, "Coffee mug")
# print(view())
# insert("Banana", 12, 40.0)
