#!C:\Program Files\Anaconda3\python.exe
#print("Content-type:text/html\r\n\r\n")
import cgi 
import sqlite3
form=cgi.FieldStorage()

uname=form.getvalue("uname")
email=form.getvalue("email")
dob=form.getvalue("dob")
gender=form.getvalue("gen")
password=form.getvalue("pass")
k=sqlite3.connect('restaurant_management.db')
cr=k.cursor()
cr.execute("select * from customers")
m=cr.fetchall()
f=0
for i in m:
	if i[2]==email:
		f=1
if f==0:
	cr.execute("insert into customers (uname,email,dob,gender,pass) values('%s','%s','%s','%s','%s')"%(uname,email,dob,gender,password))
	k.commit()
	k.close()
	print("""Content-type:text/html\r\n\r\n <html><body><a href="index.html"></a> </body></html>""")
	msg="Done"
	print("""
			<center><h2>Registration Successful!!</h2><hr>
			<h3><a href=cus_login.py>Click Here to Sign In</a></h3>
			</center>
			""")

else:
	print("""Content-type:text/html\r\n\r\n <html><body><a href="cus_login.py"></a></body></html>	""")
	msg="Not done"
	print("<h3><a href=cus_login.html>Wrong Credentials..Enter value again..</a></h3>")

#print("""Content-type:text/html\r\n\r\n<html><body><p>%s</p></body></html>"""%(msg))




