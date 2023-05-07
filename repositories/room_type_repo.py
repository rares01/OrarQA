from dbcontext import connection


def get_room_type_values():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM roomtype")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]



