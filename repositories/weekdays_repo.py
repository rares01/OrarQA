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

    result = [row[0] for row in rows]
    assert all(entry is not None for entry in result)
    return result


def get_id_by_value(name):
    assert name is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM weekday WHERE day=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result


def get_name_by_id(id):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM weekday WHERE id=%s", (id,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[1] for row in rows][0]
    assert result is not None
    return result
