from dbcontext import connection


def get_room_type_values():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT name FROM roomtype")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows]
    assert all(roomtype[0] is not None and roomtype[1] is not None for roomtype in result)
    return result


def get_id_by_value(name):
    assert name is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM roomtype WHERE name=%s", (name,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result
