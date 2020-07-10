#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()
a=int(form.getvalue("b5"))
k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()


sql = 'DELETE FROM bill WHERE id=?'
cr.execute(sql,(a,))
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
print("""<html>
 <h1 align="center"> 
 <i style="color:white">CANCELLED !!</i></h1> 
</html>""")
'''
cr.execute("DELETE FROM bill WHERE id='%d'"(%a))
'''
k.commit()