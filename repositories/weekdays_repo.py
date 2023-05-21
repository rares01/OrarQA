from dbcontext import connection


def get_weekdays_values():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT day FROM weekday")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    return [row[0] for row in rows]


def get_id_by_value(name):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM weekday WHERE day=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    return [row[0] for row in rows][0]


def get_name_by_id(id):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM weekday WHERE id=%s", (id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    return [row[1] for row in rows][0]
