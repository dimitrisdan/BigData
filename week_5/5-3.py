import sqlite3

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error
	
t = ("ALFKI", "ALFKI")

sql = "SELECT Orders.OrderID, Orders.CustomerID, OrderDetails.ProductID, Products.ProductName \
		FROM orders \
		LEFT JOIN OrderDetails LEFT JOIN Products \
		WHERE Orders.CustomerID = ? AND Orders.OrderID = OrderDetails.Orderid \ 
		AND OrderDetails.ProductID = Products.ProductID AND Orders.OrderID in \
		(SELECT OrderID FROM \
		(SELECT Orders.OrderID, Orders.CustomerID, OrderDetails.ProductID, \ Products.ProductName, \ 
		COUNT(Orders.OrderID) CNT \
		FROM orders \
		LEFT JOIN OrderDetails LEFT JOIN Products \
		WHERE Orders.CustomerID = ? \
		AND Orders.OrderID = OrderDetails.Orderid AND OrderDetails.ProductID = Products.ProductID \
		GROUP BY Orders.OrderID) \
		WHERE CNT > 1)"

c.execute(sql, t)
products = c.fetchall()

for product in products:
    print product