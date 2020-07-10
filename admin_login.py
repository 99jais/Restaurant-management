#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()
b=form.getvalue("temail")
d=form.getvalue("tpassword")


k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()
cr.execute("select email from admin")
em=cr.fetchall()
cr.execute("select password from admin")
pw=cr.fetchall()
print("""
<html>
<body> 
    <div>
				<style>
					body{
							
							background-image: url('img/admin.jpeg');
							background-repeat: no-repeat;
							background-attachment: fixed;
							background-size: cover;
							background-size: 100% 100%;
					}
						
				</style>
	</div>
		</body>
		</html>""")

f=0
for i,j in zip(em,pw):
	if i[0]==b and j[0]==d:
		f=1
		break
if f==1:
	print("""<html><body>
<h2 align="center"><i style="color:ghostwhite">Data saved successfully!!</i></h2>
<table align="center">
<tr>
<td>
<div style="text-align:center;padding:110px"><button onclick="window.location.href = 'view_orders.py';">SHOW BOOKINGS</div>
</td>
<td>
<div style="text-align:center;padding:111px"><button onclick="window.location.href = 'add_items_admin.html';">ADD ITEMS</div>
</td>
</tr>
</table>
</body></html>
""")
else:
	print("""<html><body>
<h2 align="center"><i style="color:ghostwhite">Data not saved successfully!!</i></h2>
</body></html>
""")
