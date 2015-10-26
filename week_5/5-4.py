import sqlite3

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error

sql = 'SELECT DISTINCT Customers.ContactName \
       FROM OrderDetails, Orders, Customers \
       WHERE OrderDetails.ProductID = 7  AND OrderDetails.OrderID = Orders.OrderID \ 
       AND Orders.CustomerID = Customers.CustomerID'

for row in c.execute(sql):
    print row

sql = 'SELECT COUNT (DISTINCT Customers.ContactName) as Total \
       FROM OrderDetails, Orders, Customers \
       WHERE OrderDetails.ProductID = 7  AND OrderDetails.OrderID = Orders.OrderID  \
       AND Orders.CustomerID = Customers.CustomerID'

c.execute(sql)
print '\n\nCounted number of customers : %s' % c.fetchone()
c.close()