import sqlite3, ui
from datetime import datetime


stundenplan_george = (
	('Montag', ('D', 'D', 'Ek', 'Ek', 'inf', 'inf', '', 'M','M')),
	('Dienstag', ('Bk', 'Bk', 'SM', 'SM', 'KStd', 'E', '', 'G', 'G')),
	('Mittwoch', ( 'M', 'M', 'F2', 'F2','E')),
	('Donnerstag', ('E', 'E', 'D', 'D', 'er.', 'er', '', 'AG_D', 'AG_D')),
	('Freitag', ('Ph', 'Ph', 'Mu', 'Mu', 'F2', 'F2'))
)

db = sqlite3.connect('jkgscrapedb.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = db.cursor()
cursor.execute('''select * from rawdata''')
rawdata = cursor.fetchall()



print(rawdata)

db.close()