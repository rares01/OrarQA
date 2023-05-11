from dbcontext import connection
from entities.discipline import Discipline
from repositories.study_year_repo import get_value_by_id, get_id_by_value
from repositories.teacher_repo import get_teacher_full_name_by_id, get_teacher_id_by_full_name


def get_disciplines():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM discipline")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    disciplines = []
    for row in rows:
        discipline = Discipline(*row)
        discipline.teacher_full_name = get_teacher_full_name_by_id(row[3])
        discipline.study_year = get_value_by_id(row[2])
        disciplines.append(discipline)

    return disciplines


def get_disciplines_value():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM discipline")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    disciplines = [row[1] for row in rows]

    return disciplines


def add_discipline(name, year, teacher):
    conn = connection()
    cur = conn.cursor()

    year_id = get_id_by_value(year)
    teacher_id = get_teacher_id_by_full_name(teacher)

    cur.execute(
        "INSERT INTO discipline (name, study_year_id, teacher_id) VALUES (%s,%s,%s)",
        (name, year_id, teacher_id,))
    conn.commit()

    print("Discipline added!")

    cur.close()
    conn.close()


def delete_discipline(id):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM discipline WHERE id=%s", (id,))
    conn.commit()

    print("Discipline removed!")

    cur.close()
    conn.close()


def get_discipline_id_by_value(name):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM discipline WHERE name=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]


def get_discipline_by_id(id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM discipline WHERE id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[1] for row in rows][0]
