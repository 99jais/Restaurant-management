#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
k=sqlite3.connect('restaurant_management.db')
kt=sqlite3.connect('restaurant_management.db')

cr=k.cursor()
cr.execute("select * from product")
data=cr.fetchall()

crr=kt.cursor()
crr.execute("select * from menu")
data1=crr.fetchall()

k.commit()
k.close()

kt.commit()
kt.close()
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
print("""
<html>
<body>
<form action="price_check.py" style="color: white;text-align: center;padding: 300px">
<table align="center">
<tr><td>
<select name="Coffee">
""")
for i in data:
	print(""""
	<option value="%s">%s</option>
	"""%(i[1],i[1]))
print("""
</select>
<select name="size">
	<option value="L">LARGE</option>
	<option value="M">MEDIUM</option>
	<option value="S">SMALL</option>
</select>
<input type="number" name="quantity">
</td></tr>
<tr>
<td align="center"><input type="submit" value="Order"></td>
</tr>
</table>
</form>

	</body>
	</html>
	""")