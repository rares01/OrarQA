from dbcontext import connection
from entities.student_group import StudentGroup


def get_student_groups():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM studentgroup")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    student_groups = []
    for row in rows:
        student_group = StudentGroup(*row)
        student_groups.append(student_group)

    assert all(
        entry.id is not None and entry.number is not None for
        entry in student_groups)
    return student_groups


def get_student_groups_values():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT number FROM studentgroup")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows]
    assert all(entry is not None for entry in result)
    return result


def get_id_by_value(number):
    assert number is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM studentgroup WHERE number=%s", (number,))
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

    cur.execute("SELECT number FROM studentgroup WHERE id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result
