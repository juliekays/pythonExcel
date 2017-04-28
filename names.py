def Gender_detector(Surname):
	""" docstring, here we detect someones sex through taking first 2 letters
	of their surnames. 
	"""
	Surname=Surname.upper()
	if Surname.startswith("NA") or Surname.startswith("KE"):
		return "F"

	else:
		return "M"

#print Gender_detector("kayizzi")			
