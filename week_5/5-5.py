import sqlite3

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error
	
sql_cust = " \
SELECT DISTINCT Customers.CustomerID,Customers.ContactName \
FROM OrderDetails, Orders, Customers \
WHERE OrderDetails.ProductID = 7 \
AND OrderDetails.OrderID = Orders.OrderID \
AND Orders.CustomerID = Customers.CustomerID"

sql_prod = " \
SELECT DISTINCT Products.ProductName \
FROM Orders, OrderDetails, Products \
WHERE Orders.CustomerID = ? \
AND Orders.OrderID =  OrderDetails.OrderID \
AND Products.ProductID = OrderDetails.ProductID \
ORDER BY Orders.OrderID"

products = {}

# Find all the customers who bought Uncle Bobs Organic Dried Pears product
c.execute(sql_cust)
customers = c.fetchall()

# Iterate through these customers
for row in customers:

    customer_ID = row[0]
    customer_Name = row[1]

    print '\nCustomer\'s ID: %s' % customer_ID
    print 'Customer\'s Name: %s' % customer_Name

    # For each customer find the rest products
    t = (customer_ID,)
    c.execute(sql_prod, t)
    products[customer_ID] = c.fetchall()

    print 'Total of Distinct Products Ordered: %s' % len(products[customer_ID])
    print 'Customer\'s Products: %s' % products[customer_ID]
c.close()