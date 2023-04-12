import xlsxwriter
 
# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('compiler_construction.xlsx')
 
# The workbook object is then used to add new
# worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet()
 
# Use the worksheet object to write
# data via the write() method.


my_list = [['Book_id', 'author', 'Genre','Title' ,'Price','Publish-Date','Description'],['BK101', 'Gambardella', 'Developer guide', 'computer', 44.95, 2000-10-1, 'an in depth--']]

for row_num, row_data in enumerate(my_list):
    for col_num, col_data in enumerate(row_data):
        worksheet.write(row_num, col_num, col_data)
workbook.close()