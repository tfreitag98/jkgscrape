import urllib3, sqlite3
from bs4 import BeautifulSoup
from datetime import date, datetime

url = 'http://www.jkg-stuttgart.de/jkgdata/vertretungsplan/sa3_7a.htm'
http = urllib3.PoolManager()
response = http.request('GET', url)
created_at = datetime.now()

soup = BeautifulSoup(response.data, 'html.parser')

table = soup.find('table', attrs = {'rules': 'all'})

data = []
rows = table.find_all('tr')
for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	cols = [created_at] + cols
	data.append(cols)

#print(data)
data = data[1:] #header entfernen

db = sqlite3.connect('jkgscrapedb.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cursor = db.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS rawdata (created_at timestamp, tag text, klassen text, fach text, stunde text, lehrer text, raum text, grund, text, vertretungs_text text, art text, verlegt_von text, ndruck text)')


cursor.executemany("INSERT INTO rawdata(created_at, tag, klassen, fach, stunde, lehrer, raum, grund, vertretungs_text, art, verlegt_von, ndruck) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", data)

db.commit()
db.close()