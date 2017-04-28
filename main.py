import openpyxl
from age import* 
from network import *
from names import *
from read1 import*
from write1 import*
excel_sheet='julikayi.xlsx'
sheet1_name='INPUT'
sheet2_name='RESULTS'
#copy and write to coln 1 names
sheet1_coln1=read_xl_column(excel_sheet,sheet1_name,1)
write_xl_col(sheet1_coln1,excel_sheet,sheet2_name,1)
#copy and write to coln 2 names
sheet1_coln2=read_xl_column(excel_sheet,sheet1_name,2)
write_xl_col(sheet1_coln2,excel_sheet,sheet2_name,2)
#detect gender from column2 sheet2 secondgend

gender=[]
del sheet1_coln1[0]
for name in sheet1_coln2:
	sex=Gender_detector(name)
	gender.append(sex)
gender.insert(0,'Gender')
#write gender to coln 3 sheet2
write_xl_col(gender,excel_sheet,sheet2_name,3)

#copy and write age to sheet2
sheet1_coln3=read_xl_column(excel_sheet,sheet1_name,3)
write_xl_col(sheet1_coln3,excel_sheet,sheet2_name,4)
#from age detect year of birth

Year_Of_birth=[]
del sheet1_coln3[0]
for age in sheet1_coln3:
	age=int(age)
	if type(age)==int:
		year=Date_of_birth(age)
		Year_Of_birth.append(year)	
Year_Of_birth.insert(0,'YearOfBirth')
write_xl_col(Year_Of_birth,excel_sheet,sheet2_name,5)	

#copy and write telnumber

sheet1_coln4=read_xl_column(excel_sheet,sheet1_name,4)
write_xl_col(sheet1_coln4,excel_sheet,sheet2_name,6)

#from telnum detect network
del sheet1_coln4[0]
telnum=[]
for number in sheet1_coln4:
	tel=Detect_network(number)
	telnum.append(tel)
telnum.insert(0,'Network')	
write_xl_col(telnum,excel_sheet,sheet2_name,7)
