import psycopg2
import psycopg2.extras

def get_animals(age=None, name=None):
    # Replace with your actual PostgreSQL credentials
    conn = psycopg2.connect(
        dbname="your_db_name",
        user="your_username",
        password="your_password",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    query = "SELECT * FROM animals WHERE 1=1"
    params = []

    if age:
        query += " AND ageString ILIKE %s"
        params.append(f"%{age}%")  # partial match e.g., "1 Year"

    if name:
        query += " AND name ILIKE %s"
        params.append(f"%{name}%")  # partial match e.g., "Spoofer"

    cur.execute(query, params)
    results = cur.fetchall()

    cur.close()
    conn.close()

    return [dict(row) for row in results]
