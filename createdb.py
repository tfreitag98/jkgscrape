import sqlite3

db = sqlite3.connect('jkgscrapedb.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS lehrer (id text, text text)')
cursor.execute('CREATE TABLE IF NOT EXISTS fach (id text, text text)')
#cursor.execute('CREATE TABLE IF NOT EXISTS stunde (id text, text text)')



fach = (
	('D','Deutsch'),
	('M','Mathe'),
	('Bk','Bildende Kunst'),
	('inf','informatik'),
	('Ek','Erdkunde'),
	('SM','Sport männlich'),
	('SW','Sport Weiblich'),
	('Kstd','Klassenlehrerstunde'),
	('E','Englisch'),
	('G','Geschichte'),
	('F2.','Französisch'),
	('er.','Religion evangelisch'),
	('rk','Religion katholisch'),
	('et','Ethik')
	('AG_D','Debating'),
	('Ph','Physik'),
	('Mu','Musik'),
	('L','Latein')
)
cursor.executemany('INSERT INTO fach(id, text) VALUES (?,?)', fach )

lehrer = (
	('Gb','Gilbert'),
	('Hau','Haumann'),
	('Kh','Kuhnle'),
	('Bes','Besch'),
	('Snr','Schienacher'),
	('Ce','Cebisci'),
	('Gei','Geiselhart'),
	('Key','Keyser'),
	('Btz','Betzner'),
	('Ham','Hampe'),
	('Nas','Nasse'),
	('Btn','Betten'),
	('Hg','Hunger'),
	('Spa','Spanu')
)
cursor.executemany('INSERT INTO lehrer(id, text) VALUES (?,?)', lehrer)
	



db.commit()
db.close()
