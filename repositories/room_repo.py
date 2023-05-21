from dbcontext import connection
from repositories.room_type_repo import get_id_by_value


def get_room_values():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT name FROM room")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows]
    assert all(room[0] is not None and room[1] is not None and room[2] is not None for room in result)
    return result


def get_rooms_by_room_type(room_type):
    assert room_type is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()
    room_type_id = get_id_by_value(room_type)
    cur.execute("SELECT name FROM room WHERE room_type_id=%s", (room_type_id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows]
    assert all(room[0] is not None and room[1] is not None and room[2] is not None for room in result)
    return result


def get_id_by_value(name):
    assert name is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM room WHERE name=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result


def get_value_by_id(id):
    assert id is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT name FROM room WHERE id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result
