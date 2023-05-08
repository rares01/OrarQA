from dbcontext import connection
from entities.student import Student
from repositories.semi_year_repo import get_id_by_value as get_id_semi_year
from repositories.student_group_repo import get_id_by_value as get_id_student_group
from repositories.study_year_repo import get_id_by_value as get_id_study_year
from repositories.semi_year_repo import get_value_by_id as get_value_semi_year
from repositories.student_group_repo import get_value_by_id as get_value_student_group
from repositories.study_year_repo import get_value_by_id as get_value_study_year


def get_students():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    students = []
    for row in rows:
        student = Student(*row)
        student.study_year = get_value_study_year(row[3])
        student.semi_year = get_value_semi_year(row[4])
        student.student_group = get_value_student_group(row[5])
        students.append(student)

    return students


def add_student(first_name, last_name, study_year, semi_year, student_group):
    conn = connection()
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
