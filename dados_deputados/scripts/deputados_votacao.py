import json
import codecs
import csv
import unicodedata



# f = codecs.open("deputados_votacao.json", "r", "UTF-8")
f = codecs.open("deputados_votacao.json", "r", encoding="utf-8")
dados_votos_deputados = f.read()
f.close()

f = open("temas.csv", "r")
temas_csv = f.readlines()[1:]

out = open("deputados_votacao.csv", "w")

# print dados

lines_resp = []
parsed_json = json.loads(dados_votos_deputados)

for item in parsed_json:
	row = []
	partido = item["partido"]
	partido = str(unicodedata.normalize('NFKD', partido).encode('utf-8','ignore'))

	nome = item["nome"]
	nome = str(unicodedata.normalize('NFKD', nome).encode('utf-8','ignore'))
	
	uf = item["uf"]
	uf = str(unicodedata.normalize('NFKD', uf).encode('utf-8','ignore'))
	
	id_dep = item["id_dep"]
	id_dep = str(unicodedata.normalize('NFKD', id_dep).encode('utf-8','ignore'))


	row.append(id_dep)
	row.append(nome)
	row.append(partido)
	row.append(uf)


	for t in temas_csv:
		t = t.split("\t")
		
		id_tema = t[0]

		for tema in item["temas"]:

			nome_tema = tema["tema"]
			nome_tema = str(unicodedata.normalize('NFKD', nome_tema).encode('utf-8','ignore'))

			if nome_tema == t[1]:
				voto = tema["value_name"]

				voto = str(unicodedata.normalize('NFKD', voto).encode('utf-8','ignore'))

				


				voto = id_tema + "_" + voto.replace(" ", "_")


				print voto

				row.append(voto)

	print row
	row = ';'.join(row) + '\n'

	lines_resp.append(row)

out.seek(0, 2)
out.writelines(lines_resp)
			


# value_name = tema["value_name"]
	# value = tema["value"]
	# tema = tema["tema"]
	# id_tema += id_tema

	# row.append(id_tema)
	# row.append(tema)
	# row.append(value_name)
	# row.append(value)

	# row = ';'.join(row)
f.close()
out.close()