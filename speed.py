import speedtest
import json

import mysql.connection

config = {
  'user': 'user',
  'password': 'password',
  'host': 'host',
  'database':'db',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

servers = []

s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
s.results.share()

results = s.results.dict()

add_results = ("INSERT INTO speed-test-results"
				"(download,upload,ping,timestamp)"
				"VALUES(%(download)s,%(upload)s,%(ping)s,%(timestamp)s)")

cursor.execute(add_results,results)

cnx.commit()

cursor.close()
cnx.close()
print(results)
