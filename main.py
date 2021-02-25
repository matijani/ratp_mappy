import os
if __name__ == "__main__":
	file_name = input("Donner le nom du fichier log : \n") 
	try:
		file =  open(file_name, "r")
		lines = file.readlines()
		result = [["",0,[]]]
		for line in lines:
			line_fields = line.split("\t")
			if len(line_fields) == 2 and "/map/1.0/slab/" in line_fields[1]:
				tuile=line_fields[1]
				tuile_fields = tuile.split("/map/1.0/slab/")[1].split("/")
				viewmode, zoom_level = tuile_fields[0], tuile_fields[2]
				if result[-1][0] == viewmode:
					result[-1][1] += 1
					result[-1][2].append(zoom_level)
				else:
					result.append([viewmode, 1, [zoom_level]])
		for row in result[1:]:
			print(row[0]+"\t" + str(row[1])+"\t"+','.join(sorted(set(row[2]))))
	except FileNotFoundError as e:
		print(e)
		pass
