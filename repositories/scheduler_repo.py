from dbcontext import connection


def add_entry(id):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("INSERT INTO scheduler (id) VALUES (%s)", (id,))

    conn.commit()

    cur.close()
    conn.close()
    assert conn.closed() == 1, "Connection is not closed"


# add_entry(1)
