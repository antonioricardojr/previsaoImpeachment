import unicodedata
import codecs
import json
import csv

f = codecs.open("temas.json", "r", encoding ="utf-8")
temas = f.read()
f.close()


out = open("temas.csv", "w")
out.write('id_tema\ttema\tpergunta\tdescr\n')

parsed_json = json.loads(temas)


id_tema = 0

for tema in parsed_json:
	row = []
	t = tema["Tema"]
	t = str(unicodedata.normalize('NFKD', t).encode('utf-8','ignore'))
	
	pergunta  = tema["Pergunta"]
	pergunta = str(unicodedata.normalize('NFKD', pergunta).encode('utf-8','ignore'))

	descr = tema["descr"]
	descr = str(unicodedata.normalize('NFKD', descr).encode('utf-8','ignore'))

	id_tema += 1

	row.append(str(id_tema))
	row.append(t)
	row.append(pergunta)
	row.append(descr)


	row = '\t'.join(row) + '\n'
	
	out.write(row)


out.close()