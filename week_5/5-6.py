import sqlite3

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error
	
sql = "SELECT Orders.CustomerID, OrderDetails.ProductID, \
       SUM( OrderDetails.Quantity) AS TotalQuantity \
       FROM Orders, OrderDetails \
       WHERE Orders.OrderID = OrderDetails.OrderID \
       AND OrderDetails.ProductID = 7 \
       GROUP BY Orders.CustomerID \
       ORDER BY TotalQuantity DESC \
       LIMIT 1"

c.execute(sql)
top_buyer = c.fetchone()

print 'CustomerID\t\tTotalQuantity\n%s\t\t\t%s' % (top_buyer[0], top_buyer[2])