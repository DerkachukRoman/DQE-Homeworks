import sqlite3 
from csv import reader
from os import getcwd


def create_tables(cursor):
    query = """
            CREATE TABLE IF NOT EXISTS Project
            (
                Name TEXT NOT NULL,
                Description TEXT,
                Deadline DATE,
                UNIQUE (Name, Deadline)
            );

            CREATE TABLE IF NOT EXISTS Tasks
            (
                ID INTEGER PRIMARY KEY,
                Priority INTEGER,
                Details TEXT,
                Status TEXT,
                Deadline DATE,
                Completed DATE,
                Project TEXT NOT NULL
            )
    """
    cursor.executescript(query)
    return


def populate_project(cursor, data_file):
    
    data = []

    with open(data_file) as f:
        f_csv = reader(f)
        headers = next(f_csv)
        values = f_csv

        for row in values:
            data.append(tuple(row))

    query = """
        INSERT OR REPLACE INTO Project
        VALUES (?,?,?)
    """

    cursor.executemany(query, data)
    return 


def populate_tasks(cursor, data_file):

    data = []

    with open(data_file) as f:
        f_csv = reader(f)
        headers = next(f_csv)
        values = f_csv

        for row in values:
            data.append(tuple(row))

    query = """
        INSERT OR REPLACE INTO Tasks
        VALUES (?,?,?,?,?,?,?)
    """

    cursor.executemany(query, data)
    return


def tasks_of_project(cursor, project_name):
    query = """
        SELECT * 
        FROM Tasks
        WHERE Project = ? 
    """

    cursor.execute(query, tuple([project_name]))

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("There are no tasks for {}".format(project_name))
    else:
        for row in rows:
            print(row)

    return



if __name__ == "__main__":
    conn = sqlite3.connect("mybase.db")
    cur = conn.cursor()

    projects_file = getcwd() + "\\projects.csv"
    tasks_file = getcwd() + "\\tasks.csv"

    project = input("Input name of project:")

    create_tables(cur)
    populate_project(cur, projects_file)
    populate_tasks(cur, tasks_file)

    conn.commit()

    tasks_of_project(cur, project)

    conn.close()