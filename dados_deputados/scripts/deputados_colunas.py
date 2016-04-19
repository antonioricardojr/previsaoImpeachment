import re

f = open("deputados_votacao.csv", "r")


rows = f.readlines()

f.close()


out = open("deputados.csv", "w")

cols = 'id_dep;nome;partido;UF;tema_10;tema_11;tema_12;tema_13;tema_14;tema_15;tema_16;tema_17;tema_18;tema_19;tema_1;tema_2;tema_3;tema_4;tema_5;tema_6;tema_7;tema_8;tema_9;'
cols = cols.split(";")



out.write(";".join(cols) + '\n')


def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)


lines_resp = []


for row in rows:
	
	row = row.split(";")


	temas = []
	info = []

	for item in row:
		
		if len(item.split(" ")) > 1:
			item = '"' + item + '"'

		if item[0].isdigit() and item[1] == "_":
			temas.append(item)
		else:
			info.append(item)


	temas = natural_sort(temas)
	# print temas

	info = info + temas

	info = ';'.join(info)

	lines_resp.append(info)



lines_resp = '\n'.join(lines_resp)


out.writelines(lines_resp)

out.close()



