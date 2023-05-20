from dbcontext import connection


def get_room_type_values():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT name FROM roomtype")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed() == 1, "Connection is not closed"

    return [row[0] for row in rows]


def get_id_by_value(name):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM roomtype WHERE name=%s", (name,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    assert conn.closed() == 1, "Connection is not closed"

    return [row[0] for row in rows][0]


