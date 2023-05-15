from dbcontext import connection
from entities.scheduler_entry import SchedulerEntry
from repositories.weekdays_repo import get_id_by_value as get_weekday_id
from repositories.weekdays_repo import get_name_by_id as get_weekday_name
from repositories.time_slot_repo import get_id_by_value as get_time_slot_id, get_timeslot_by_id as get_time_slot
from repositories.teacher_repo import get_teacher_id_by_full_name as get_teacher_id, get_teacher_full_name_by_id \
    as get_teacher_full_name
from repositories.discipline_repo import get_discipline_id_by_value as get_discipline_id, \
    get_discipline_by_id as get_discipline_name
from repositories.study_year_repo import get_id_by_value as get_study_year_id, get_value_by_id as get_study_year_number
from repositories.semi_year_repo import get_id_by_value as get_semi_year_id, get_value_by_id as get_semi_year_name
from repositories.student_group_repo import get_id_by_value as get_student_group_id, \
    get_value_by_id as get_student_group_name


def add_entry(weekday, start_hour, end_hour, teacher, discipline, study_year, semi_year, student_group, scheduler_id):
    conn = connection()
    cur = conn.cursor()

    weekday_id = get_weekday_id(weekday)
    time_slot_id = get_time_slot_id(start_hour, end_hour)
    teacher_id = get_teacher_id(teacher)
    discipline_id = get_discipline_id(discipline)
    study_year_id = get_study_year_id(study_year)
    semi_year_id = get_semi_year_id(semi_year)
    student_group_id = get_student_group_id(student_group)

    cur.execute(
        "INSERT INTO schedulerentry (weekday_id, time_slot_id, teacher_id, discipline_id, study_year_id,"
        " semi_year_id, student_group_id, scheduler_id) VALUES (%s, %s, "
        "%s, %s, %s, %s, %s, %s)",
        (weekday_id, time_slot_id, teacher_id, discipline_id, study_year_id, semi_year_id, student_group_id,
         scheduler_id))

    conn.commit()

    cur.close()
    conn.close()


def get_entry_by_id(entry_id):
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT id FROM timeslot WHERE entry_id=%s", (entry_id,))

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows][0]


def fetch_rows(rows):
    entries = []
    for row in rows:
        id = row[0]
        weekday = get_weekday_name(row[1])
        time_slot = get_time_slot(row[2])
        teacher = get_teacher_full_name(row[3])
        discipline = get_discipline_name(row[4])
        study_year = get_study_year_number(row[5])
        semi_year = get_semi_year_name(row[6])
        student_group = get_student_group_name(row[7])
        entries.append((id, weekday, time_slot, teacher, discipline, study_year, semi_year, student_group))

    return entries


def get_entries():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM schedulerentry")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return fetch_rows(rows)


print(get_entries())


def fetch_rows_with_entity(rows):
    entries = []
    for row in rows:
        id = row[0]
        weekday = get_weekday_name(row[1])
        time_slot = get_time_slot(row[2])
        teacher = get_teacher_full_name(row[3])
        discipline = get_discipline_name(row[4])
        study_year = get_study_year_number(row[5])
        semi_year = get_semi_year_name(row[6])
        student_group = get_student_group_name(row[7])
        scheduler_entry = SchedulerEntry(id, weekday, time_slot, teacher, discipline, study_year, semi_year,
                                         student_group, 1)
        entries.append(scheduler_entry)

    return entries


def get_entries_with_entity():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM schedulerentry")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return fetch_rows_with_entity(rows)
