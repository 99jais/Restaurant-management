#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi
import sqlite3
form=cgi.FieldStorage()
a=form.getvalue("tname")
b=form.getvalue("tsize")
c=int(form.getvalue("tprice"))

k=sqlite3.connect('restaurant_management.db')

cr=k.cursor()
cr.execute("insert into product(Coffee) values ('%s')"%(a))
cr.execute("insert into menu(size,price) values ('%s','%d')"%(b,c))
k.commit()
k.close()
print("""<html>
 <h1 align="center"> 
 <i style="color:white">ITEMS ADDED!!</i></h1> 
</html>""")
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
    <div style="align:center;padding:10px"><button onclick="window.location.href = 'view_orders.py';">VIEW ORDERS</div>

		</body>
		</html>""")