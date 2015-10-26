import sqlite3

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error
	
customer_ID = ("ALFKI",)
sql = "SELECT Orders.orderid, customerid, orderdetails.productid, productname \
		FROM orders INNER JOIN orderdetails INNER JOIN products \
		WHERE customerid = ?  \
		AND orders.orderid = orderdetails.orderid  \
		AND orderdetails.productid = products.productid"

c.execute(sql, customer_ID)
products = c.fetchall()

for product in products:
	print product