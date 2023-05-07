from dbcontext import connection


def get_student_groups_values():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT number FROM studentgroup")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]


def get_id_by_value(number):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM studentgroup WHERE number=%s", (number,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]
