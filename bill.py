#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()
a=form.getvalue("a1")
b=form.getvalue("a2")
c=int(form.getvalue("a3"))
d=int(form.getvalue("a4"))
k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()
cr.execute("insert into bill (coffee,size,quantity,price) values ('%s','%s','%d','%d')"%(a,b,c,d))
cr.execute("select * from bill where coffee='%s' and size ='%s'"%(a,b))
x=cr.fetchone()
print("""
<html>
<body> 
    <div>
				<style>
					body{
							
							background-image: url('img/coffee_cup.jpeg');
							background-repeat: no-repeat;
							background-attachment: fixed;
							background-size: cover;
							background-size: 100% 100%;
					}
						
				</style>
	</div>
		</body>
		</html>""")
print("""<html><body>
<button>
<a href="menu.py">Back</a>
</button></body></html>""")

print("""<html><body>
<form action="cancel.py">  
<table align="center" style="color:white;text-align: center;padding: 350px">

<tr><td>Coffee name</td><td><input type="text" name="b1" value="%s" readonly></td></tr>
<tr><td>Size</td><td><input type="text" name="b2" value="%s" readonly></td></tr>
<tr><td>Quantity</td><td><input type="text" name="b3" value="%d" readonly></td></tr>
<tr><td>Total Price</td><td><input type="text" name="b4" value="%d" readonly></td></tr>
<tr><td>Order id</td><td><input type="text" name="b5" value="%d"></td></tr>
<tr><td><input type="submit" value="Cancel"></td></tr>

</table>
</form>

</body></html>"""%(a,b,c,d,x[4]))
k.commit()