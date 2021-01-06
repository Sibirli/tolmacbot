import psycopg2

class Database:

    def __init__(self, database):

        self.conn = psycopg2.connect(database)
        self.cursor = self.conn.cursor()
        self.cursor.execute("select exists(select * from information_schema.tables where table_name=%s)", ('profile',))
        if not self.cursor.fetchone()[0]:
            self.cursor.execute(open("database.sql", "r").read())

    def insert(self, chat_id, username, first_name, last_name, date):
        with self.conn:
            self.cursor.execute('INSERT INTO profile (chat_id, username, first_name, last_name, date) '
                                'VALUES (%s,%s,%s,%s,%s)', (chat_id, username, first_name, last_name, date))
            self.conn.commit()

    def get_id(self, chat_id):
        with self.conn:
            self.cursor.execute('SELECT id FROM profile WHERE chat_id = %s;', (chat_id,))
            return self.cursor.fetchone()

    def get_all(self):
    	with self.conn:
    		self.cursor.execute('SELECT chat_id FROM profile')
    		return self.cursor.fetchall()
