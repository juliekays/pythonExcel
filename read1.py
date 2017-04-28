import openpyxl
def read_xl_column(xlsx,sheet_name,column_number):
"""
 here we are reading an excel sheet which we saved in our containing folder
"""

	book=openpyxl.load_workbook(xlsx)
	sheet1=book[sheet_name]
	columns=tuple(sheet1.columns)
	col_list=[]			
	for cell in columns[column_number-1]:
		col_list.append(str(cell.value))
	return col_list
#print read_xl_column('julikay.xlsx','INPUT',4)

"""column1=columns[0]
				column2=columns[1]
				column3=columns[2]
				column4=columns[3]
			print cells
for C1 in cells:
	print C1[0].value
"""