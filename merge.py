import json
import codecs
import csv
import unicodedata


f = codecs.open("votacao_impeachment.csv", "r", encoding="utf-8")
votacao_impeachment = f.readlines()[1:]
f.close()

f = codecs.open("df_ids.csv", "r", encoding="utf-8")
df_ids = f.readlines()[1:]
f.close()

out = open("votacao_impeachment_id.csv", "w")
out.write('id_dep;deputado;IMPEACHMENT;nome\n')

for item in df_ids:
	item = item.split(";")

	nome = item[0].rstrip()
	
	id = item[1].rstrip()

	for row in votacao_impeachment:
		row = row.split(";")

		nome_completo = row[0].rstrip()
		imp = row[1].rstrip()
		nome_sem_espaco = row[2].rstrip()
		
		if nome_sem_espaco == nome:
			print "equals ok"
			id = [id]
			line = id + row
			out.write(';'.join(line))



out.close()





