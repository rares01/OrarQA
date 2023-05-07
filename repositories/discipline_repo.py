from dbcontext import connection
from entities.discipline import Discipline


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
        disciplines.append(discipline)

    return disciplines


def add_discipline(name):
    conn = connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO discipline (name) VALUES (%s)",
        name)
    conn.commit()

    print("Discipline added!")

    cur.close()
    conn.close()
