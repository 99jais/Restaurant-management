#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()
a=form.getvalue("Coffee")
b=form.getvalue("size")
c=int(form.getvalue("quantity"))
k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()
cr.execute("select * from product where Coffee='%s'"%(a))
cr.execute("select * from menu where size='%s'"%(b))
x=cr.fetchone()
z=cr.fetchone()
d=c*z[1]
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
<form action="bill.py">
<table align="center" style="color:ghostwhite;text-align: center;padding: 350px">
<tr><td>Coffee name</td><td><input type="text" name="a1" value="%s" readonly></td></tr>
<tr><td>Size</td><td><input type="text" name="a2" value="%s" readonly></td></tr>
<tr><td>Quantity</td><td><input type="text" name="a3" value="%d" readonly></td></tr>
<tr><td>Price</td><td><input type="text" name="a4" value="%d" readonly></td></tr>
<tr><td colspan=5 align="center"><input type="submit" value="confirm"></td></tr>
</form>
<button align="center"><a href="menu.py">Cancel</a>
</button></td></tr>
</body></html>
"""%(a,b,c,d))