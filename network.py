def Detect_network(num):
	"""
	docstring, network, we detect network through taking the first 3 numbers of each tel number
	to detect which network a given number belongs to. if the number is not in the network scope,
	it will return others. And invalid if un usual chacters are typed  
	"""
	if num.isdigit():
		if num.startswith("077") or num.startswith("078"):
			return "MTN"
		if num.startswith("075") or num.startswith("070"):
			return"Airtel"
		if num.startswith("079"):
			return "Africel"
		if num.startswith("074"):
			return "Smart"
		if num.startswith("071"):
			return "UTL"
		if num.startswith("073"):
			return "K2"	
		else:
			return "Others"	
	else:
		return "Invalid"		

#print Detect_network("0785667777")       

	