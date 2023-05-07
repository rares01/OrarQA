from dbcontext import connection
from repositories.semi_year_repo import get_id_by_value as get_id_semi_year
from repositories.student_group_repo import get_id_by_value as get_id_student_group
from repositories.study_year_repo import get_id_by_value as get_id_study_year


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
