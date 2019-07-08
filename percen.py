def dis_perc(a,b):

	if not((type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)):
		return "Invalid arguments"
	elif (a <= 0):
		return ("Total amount cannot be zero")
	else:
		d = (b/a) * 100
		return d
