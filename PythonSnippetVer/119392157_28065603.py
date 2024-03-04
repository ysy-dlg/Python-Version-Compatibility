import pandas as pd
import StringIO
io = StringIO.StringIO()
# Use a temp filename to keep pandas happy.
writer = pd.ExcelWriter('temp.xlsx', engine='xlsxwriter')
# Set the filename/file handle in the xlsxwriter.workbook object.
writer.book.filename = io
# Write the data frame to the StringIO object.
pd.DataFrame().to_excel(writer, sheet_name='Sheet1')
writer.save()
xlsx_data = io.getvalue()