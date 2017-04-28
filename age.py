import datetime
import math
def Date_of_birth(Age):
	""" doc string this function calculates a persons year of birth if the person provides their Age
	it gets the current date and reduces the persons age from it
	"""
 today = datetime.datetime.now().year
 dob = today - int(Age)
 return dob

#print Date_of_birth('27')


