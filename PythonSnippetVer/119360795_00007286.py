for key, group in groupby(things, lambda x: x[0]):
	listOfThings = " and ".join([thing[1] for thing in group])
	print key + "s:  " + listOfThings + "."