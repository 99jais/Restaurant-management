#!C:\Program Files\Anaconda3\python.exe
print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()
k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()
cr.execute("select * from bill")
x=cr.fetchall()

print("""
        <html>
        <table border=3 align="center"  style="background-color:#1E312D;text-align:center;padding:100px">
        <tr>
            <th style="color:ghostwhite">Product name</th>
            <th style="color:ghostwhite">Product size</th>
            <th style="color:ghostwhite">Product quantity</th>
            <th style="color:ghostwhite">Total Price</th>
            <th style="color:ghostwhite">Product id</th>
        </tr>""")

for i in x:
	print("""
        <tr>
            <td style="color:ghostwhite">%s</td>
            <td style="color:ghostwhite">%s</td>
            <td style="color:ghostwhite">%d</td>
            <td style="color:ghostwhite">%d</td>
            <td style="color:ghostwhite">%d</td>
        </tr>
        """%(i[0],i[1],i[2],i[3],i[4]))

print("""</table>
</html>""")
print("""
<html>
<body> 
    <span style="align:center"><button onclick="window.location.href = 'add_items_admin.html';">ADD ITEMS</span>
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

'''
for i in x:

	print("""<html><body>
	<form>
	<table>

	<tr><td>Product name</td><td><input type="text" name="a1" value="%s" readonly></td></tr>
 	<tr><td>Product Size</td><td><input type="text" name="a2" value="%s" readonly></td></tr>
	<tr><td>Product Quantity</td><td><input type="text" name="a3" value="%d" readonly></td></tr>
	<tr><td>Product Price</td><td><input type="text" name="a4" value="%d" readonly></td></tr>
	<tr><td>Product id</td><td><input type="text" name="a5" value="%d" readonly></td></tr>

	</table>
	</form>
	</body></html>
	"""%(i[0],i[1],i[2],i[3],i[4]))
'''

