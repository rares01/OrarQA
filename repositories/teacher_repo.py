from dbcontext import connection
from entities.teacher import Teacher


def get_teacher_full_name_by_id(id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM teacher where id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    values = rows[0]
    return values[0] + " " + values[1]


def get_teacher_full_names():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM teacher")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    teachers = []
    for row in rows:
        teachers.append(row[0] + " " + row[1])

    return teachers


def get_teacher_id_by_full_name(full_name):
    first_name, last_name = full_name.split()
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM teacher WHERE first_name=%s AND last_name=%s", (first_name, last_name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]


def get_teachers():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM teacher")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    teachers = []
    for row in rows:
        teacher = Teacher(*row)
        teachers.append(teacher)

    return teachers


def get_full_teachers():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM teacher")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    teachers = []
    for row in rows:
        teacher = Teacher(*row)
        teachers.append(teacher)

    return teachers


def add_teacher(first_name, last_name):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO teacher (first_name, last_name) VALUES (%s,%s)",
        (first_name, last_name))
    conn.commit()

    print("Teacher added!")

    cur.close()
    conn.close()
