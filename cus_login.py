#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()
b=form.getvalue("temail")
d=form.getvalue("tpassword")


k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()
cr.execute("select email from customers")
em=cr.fetchall()
cr.execute("select pass  from customers")
pw=cr.fetchall()
print("""
<html>
<body>
<div>
				<style>
					body{
							
							background-image: url('img/coffee_cup.jpeg');
							background-repeat: no-repeat;
							background-attachment: fixed;
							background-size:;
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
		<div style="text-align:center;padding:300px"><button onclick="window.location.href = 'menu.py';"><h1>MENU</h1></div>
	 
</body></html>
""")
else:
	print("""<html><body>
		<p>Please enter correct email and password</p>
</body></html>
""")
