from dbcontext import connection
from entities.discipline import Discipline
from repositories.study_year_repo import get_value_by_id, get_id_by_value
from repositories.teacher_repo import get_teacher_full_name_by_id, get_teacher_id_by_full_name


def get_disciplines():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM discipline")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"
    disciplines = []
    for row in rows:
        discipline = Discipline(*row)
        discipline.teacher_full_name = get_teacher_full_name_by_id(row[3])
        discipline.study_year = get_value_by_id(row[2])
        disciplines.append(discipline)

    assert all(
        entry.teacher_full_name is not None and entry.id is not None and entry.study_year is not None and entry.name for
        entry in disciplines)
    return disciplines


def get_disciplines_value():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM discipline")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"
    disciplines = [row[1] for row in rows]
    assert all(
        entry is not None for entry in disciplines)

    return disciplines


def add_discipline(name, year, teacher):
    assert name is not None
    assert year is not None
    assert teacher is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
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
    assert conn.closed == 1, "Connection is not closed"


def delete_discipline(id):
    assert id is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM discipline WHERE id=%s", (id,))
    conn.commit()

    print("Discipline removed!")

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"


def get_discipline_id_by_value(name):
    assert name is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT id FROM discipline WHERE name=%s", (name,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[0] for row in rows][0]
    assert result is not None
    return result


def get_discipline_by_id(id):
    assert id is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM discipline WHERE id=%s", (id,))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    result = [row[1] for row in rows][0]
    assert result is not None
    return result
