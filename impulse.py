#!/usr/bin/env python

import sqlite3

try:
	db = sqlite3.connect('db/impulse')
	cursor = db.cursor()
	cursor.execute('''CREATE TABLE IF NOT EXISTS
			hosts(id INTEGER PRIMARY KEY AUTOINCREMENT, host TEXT, status INTEGER)''')
	db.commit()

except Exception as e:
	db.rollback()
	raise e

finally:
	db.close()
