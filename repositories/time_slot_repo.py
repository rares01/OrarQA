from dbcontext import connection


def get_time_slot_values():
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()

    cur.execute("SELECT * FROM timeslot")
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    start_hour = [row[1] for row in rows]
    end_hour = [row[2] for row in rows]

    return [f"{start_hour[i]}-{end_hour[i]}" for i in range(len(start_hour))]


def get_id_by_value(start_hour, end_hour):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()
    cur.execute("SELECT id FROM timeslot WHERE start_hour=%s AND end_hour=%s", (start_hour, end_hour))
    rows = cur.fetchall()

    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    return [row[0] for row in rows][0]


def get_timeslot_by_id(id):
    conn = connection()
    assert conn is not None, "Connection unstable"
    cur = conn.cursor()
    cur.execute("SELECT * FROM timeslot WHERE id=%s", (id, ))
    rows = cur.fetchall()

    start_hour = [row[1] for row in rows][0]
    end_hour = [row[2] for row in rows][0]
    cur.close()
    conn.close()
    assert conn.closed == 1, "Connection is not closed"

    return str(start_hour) + ":00-" + str(end_hour) + ":00"
