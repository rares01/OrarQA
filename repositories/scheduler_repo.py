from dbcontext import connection


def add_entry(id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO scheduler (id) VALUES (%s)", (id,))

    conn.commit()

    cur.close()
    conn.close()


# add_entry(1)
