import sqlite3

import pyTalkManager as tm


class DB:
    """The DB module provides an interface to the project's SQLite3 database."""


    def get_path():
        """Returns the path of the database located in config.ini"""
        return tm.configGet('DB', 'location')


    def DbInit():
        """Initialize SQLite database

        This method runs when the user is running pyTalkManager for the first time
        or when the user wants to initialize a new database. The method crates a
        new SQLite database with all the needed tables and fields used by PyTalkManager.
        """

        conn = sqlite3.connect(DB.get_path())
        c = conn.cursor()

        c.execute('''CREATE TABLE Assignment (
                                              id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                              speaker INTEGER NOT NULL,
                                              talk INTEGER NOT NULL,
                                              congregation INTEGER NOT NULL,
                                              chairman INTEGER NOT NULL,
                                              hospitality INTEGER NOT NULL,
                                              date DATETIME NOT NULL,
                                              FOREIGN KEY(speaker) REFERENCES Brother(id),
                                              FOREIGN KEY(talk) REFERENCES Talk(id),
                                              FOREIGN KEY(congregation) REFERENCES Congregation(id),
                                              FOREIGN KEY(chairman) REFERENCES Brother(id),
                                              FOREIGN KEY(hospitality) REFERENCES Hospitality(id)
                                              )''')

        c.execute('''CREATE TABLE Brother (
                                           id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                           first_name TEXT NOT NULL,
                                           middle_name TEXT,
                                           last_name TEXT NOT NULL,
                                           email TEXT,
                                           phone TEXT NOT NULL,
                                           congregation NUMERIC NOT NULL,
                                           responsibility TEXT NOT NULL,
                                           speaker BOOL NOT NULL DEFAULT 0,
                                           chairman BOOL NOT NULL DEFAULT 0,
                                           coordinator BOOL NOT NULL DEFAULT 0,
                                           note BLOB,
                                           FOREIGN KEY(congregation) REFERENCES Congregation(id)
                                           )''')

        c.execute('''CREATE TABLE Congregation (
                                           id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                           name TEXT NOT NULL,
                                           phone TEXT,
                                           email TEXT,
                                           street TEXT NOT NULL,
                                           city TEXT NOT NULL,
                                           state TEXT NOT NULL,
                                           zip NUMERIC NOT NULL,
                                           long NUMERIC,
                                           lat NUMERIC,
                                           note BLOB
                                           )''')

        c.execute('''CREATE TABLE Hospitality (
                                               id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                               name TEXT NOT NULL,
                                               note TEXT
                                               )''')

        c.execute('''CREATE TABLE SpeakerTalk (
                                               id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                               title INTEGER NOT NULL,
                                               speaker INTEGER NOT NULL,
                                               FOREIGN KEY(title) REFERENCES Talk(id)
                                               FOREIGN KEY(speaker) REFERENCES Brother(id)
                                               )''')

        c.execute('''CREATE TABLE Talk (
                                        id INTEGER PRIMARY KEY NOT NULL UNIQUE,
                                        title TEXT NOT NULL,
                                        subject TEXT
                                        )''')

        conn.close()


    def add_item(self, table, column, value):
        """Takes an item and adds it to the database.

        Known Problems:
            The value list that is passed into the method is automatically
            converted into a string regardless if it's another data type
            such as an int, float, or bool.

        :arguments
        table - a string with the table that will be written to
        column - a list with the the column(s) that will be written in
        value - a list with the value(s) that will be written.

        """

        list_column = ', '.join(column)
        list_value = "', '".join(value)  # Converts each value into a string.

        command = "INSERT INTO {table}({column}) VALUES('{values}')".format(table=table,  # adds ' ' to values.
                                                                            column=list_column,
                                                                            values=list_value)

        DB.commit_sql(None, command)


    def return_pass_sql(self, sql):
        """
        Returns the item the user requested.

        """

        command = "{}".format(sql)

        data = DB.return_sql(None, command)
        return data


    def delete_data(self):
        """Deletes data from the database"""
        pass


    def edit_item(self, table, item):
        """Edits data in the database"""
        pass


    def commit_sql(self, sql):
        """Takes the SQL commands and commits it to SQLite

        :param sql: the SQL command that needs to be passed
                       to SQLite.

        """

        conn = sqlite3.connect(DB.get_path())
        c = conn.cursor()

        c.execute("PRAGMA foreign_keys = ON")
        c.execute(sql)
        conn.commit()
        conn.close()

    def return_sql(self, sql):
        """
        Returns data from the SQLite database.

        :param sql: the SQL command to pass to SQLite
        :return data: returns a list with each row in a tuple.

        """

        comm = sqlite3.connect(DB.get_path())
        c = comm.cursor()

        c.execute("PRAGMA foreign_keys = ON")
        c.execute(sql)
        data = c.fetchall()
        c.close()

        return data