from dbcontext import connection
from entities.student import Student
from repositories.semi_year_repo import get_id_by_value as get_id_semi_year
from repositories.semi_year_repo import get_value_by_id as get_value_semi_year
from repositories.student_group_repo import get_id_by_value as get_id_student_group
from repositories.student_group_repo import get_value_by_id as get_value_student_group
from repositories.study_year_repo import get_id_by_value as get_id_study_year
from repositories.study_year_repo import get_value_by_id as get_value_study_year


def get_students():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    students = []
    for row in rows:
        student = Student(*row)
        student.study_year = get_value_study_year(row[3])
        student.semi_year = get_value_semi_year(row[4])
        student.student_group = get_value_student_group(row[5])
        students.append(student)

    assert all(
        entry.id is not None and entry.first_name is not None and entry.last_name is not None and entry.student_group is
        not None and entry.semi_year is not None and entry.study_year is not None for entry in students)
    return students


def add_student(first_name, last_name, study_year, semi_year, student_group):
    assert first_name is not None
    assert last_name is not None
    assert student_group is not None
    assert semi_year is not None
    assert study_year is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    study_year_id = get_id_study_year(study_year)
    semi_year_id = get_id_semi_year(semi_year)
    student_group_id = get_id_student_group(student_group)

    cur.execute(
        "INSERT INTO student (first_name, last_name, study_year_id, semi_year_id, student_group_id) VALUES (%s, %s, "
        "%s, %s, %s)",
        (first_name, last_name, str(study_year_id), str(semi_year_id), str(student_group_id)))
    conn.commit()

    print("Student added!")

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"


def delete_student(id):
    assert id is not None
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM student WHERE id=%s", (id,))
    conn.commit()

    print("Student removed!")

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"
