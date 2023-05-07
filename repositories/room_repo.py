from dbcontext import connection
from repositories.room_type_repo import get_id_by_value


def get_room_values():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM room")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]


def get_rooms_by_room_type(room_type):
    conn = connection()
    cur = conn.cursor()
    room_type_id = get_id_by_value(room_type)
    cur.execute("SELECT name FROM room WHERE room_type_id=%s", (room_type_id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]


def get_id_by_value(name):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM room WHERE name=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]


def get_value_by_id(id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM room WHERE id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]



