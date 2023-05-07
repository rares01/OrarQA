from dbcontext import connection


def get_time_slot_values():
    conn = connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM timeslot")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    start_hour = [row[1] for row in rows]
    end_hour = [row[2] for row in rows]

    return [f"{start_hour[i]}-{end_hour[i]}" for i in range(len(start_hour))]


print(get_time_slot_values())


