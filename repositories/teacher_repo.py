from dbcontext import connection
from entities.teacher import Teacher


def get_teacher_full_name_by_id(id):
    assert id is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM teacher where id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    values = rows[0]
    result = values[0] + " " + values[1]
    assert result is not " "
    return result


def get_teacher_full_names():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM teacher")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    teachers = []
    for row in rows:
        teachers.append(row[0] + " " + row[1])

    assert len(teachers) is not None
    return teachers


def get_teacher_id_by_full_name(full_name):
    assert full_name is not None
    first_name, last_name = full_name.split()
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM teacher WHERE first_name=%s AND last_name=%s", (first_name, last_name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result


def get_teachers():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM teacher")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    teachers = []
    for row in rows:
        teacher = Teacher(*row)
        teachers.append(teacher)

    assert all(
        entry.id is not None and entry.first_name is not None and entry.last_name is not None for entry in teachers)
    return teachers


def get_full_teachers():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM teacher")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    teachers = []
    for row in rows:
        teacher = Teacher(*row)
        teachers.append(teacher)

    assert all(
        entry.id is not None and entry.first_name is not None and entry.last_name is not None for entry in teachers)
    return teachers


def add_teacher(first_name, last_name):
    assert first_name is not None
    assert last_name is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO teacher (first_name, last_name) VALUES (%s,%s)",
        (first_name, last_name))
    conn.commit()

    print("Teacher added!")

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"
