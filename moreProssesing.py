from sets import Set
fileResult = open("result.txt", 'w')

utternaces = {}
nationalities = Set([])
allowedNationalities = ["Hispanohablante","Angloparlante", "nc"]
other = "otro"

for i in range(1,11):
	utternace = {}
	for j in range(0,5):
		file = open( str(i) + "/" + str(j) + "/" + "data.txt",'r')
		point = {}
		for nationality in file:
			nationality = nationality.rstrip()
			if(nationality not in allowedNationalities):
				nationality = other
			nationalities.add(nationality)
			if nationality not in point:
				point[nationality] = 1
			else:
				point[nationality] = point[nationality] + 1
		utternace[j] = point
	utternaces[i] = utternace

nationalities = list(nationalities)
allowedNationalities.append(other)
print allowedNationalities

for i in utternaces.keys():
	fileResult.write("\t")
	for nationality in allowedNationalities:
		fileResult.write("\t" + nationality)
	fileResult.write("\n")
	for j in utternaces[i].keys():
		point = utternaces[i][j]
		print i,"\t",j, "\t",point
		total = sum(point.values())*1.0

		fileResult.write( str(i) + "\t" + str(j))
		for nationality in allowedNationalities:
			if nationality in point:
				fileResult.write("\t" +  str((point[nationality]/total)))
			else:
				fileResult.write("\t" + "0")
		fileResult.write("\n")