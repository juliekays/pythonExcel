import openpyxl
#from read1 import read_xl_column
def write_xl_col(data_list,xlsx,sheet_name="",column_number=""):
	book=openpyxl.load_workbook(xlsx)
	sheet2=book[sheet_name]
	row_counter=1
	for data in data_list:
		sheet2.cell(row=row_counter,column=column_number).value=data
		row_counter+=1
	book.save(xlsx)

#data=read_xl_column('julikay.xlsx','INPUT',1)
#write_xl_col(data,'julikay.xlsx','RESULTS',1)	

