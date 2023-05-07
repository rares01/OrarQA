from dbcontext import connection


def get_semi_years_values():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM semiyear")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]


def get_id_by_value(name):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM semiyear WHERE name=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]


def get_value_by_id(id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT name FROM semiyear WHERE id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]
