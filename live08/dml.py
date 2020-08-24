"""
DML - Manipulação de dados

C - create
R - read
U - update
D - delete
"""
import sqlite3


def commit_close(func):
    def decorator(*args):
        con = sqlite3.connect('base.db')
        cur = con.cursor()
        sql = func(*args)
        cur.execute(sql)
        con.commit()
        con.close()
    return decorator
    

@commit_close
def db_insert(name, phone, email):
    return f"""
    INSERT INTO users(name, phone, email)
        VALUES('{name}', '{phone}', '{email}')
    """
 

@commit_close
def db_update(name, email):
    return f"""
    UPDATE users SET name = '{name}' WHERE email = '{email}'
    """


@commit_close
def db_delete(email):
    return f"""
    DELETE FROM users WHERE email = '{email}' 
    """



def db_select(data, field):
    con = sqlite3.connect('base.db')
    cur = con.cursor()
    sql = f"""
    SELECT id, name, phone, email
    FROM users
    WHERE {field}={data}
    """
    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data


