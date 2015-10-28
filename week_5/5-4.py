# Norwich Database Testing #
# DB : http://ulfaslak.com/files/northwind.db #
#######################
# SQL IMPLEMENETATION #
#######################

import sqlite3
import pymongo

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error

sql = "SELECT DISTINCT Customers.ContactName \
	   	FROM OrderDetails, Orders, Customers \
		WHERE OrderDetails.ProductID = 7 AND OrderDetails.OrderID = Orders.OrderID \
		AND Orders.CustomerID = Customers.CustomerID"

for row in c.execute(sql):
	print row

sql = "SELECT COUNT (DISTINCT Customers.ContactName) as Total \
		FROM OrderDetails, Orders, Customers \
		WHERE OrderDetails.ProductID = 7 AND OrderDetails.OrderID = Orders.OrderID \
		AND Orders.CustomerID = Customers.CustomerID"

c.execute(sql)
print '\n\nCounted number of customers : %s' % c.fetchone()
c.close()

#########################
# NoSQL IMPLEMENETATION #
#########################

#ordersID’s with product 7
orders_with_7 = order_details.find({"ProductID" : 7,
,→ }).distinct("OrderID")
#CustomerID’s who bought product 7
Customer_product_7 = orders.find({"OrderID": { "$in": orders_with_7
,→ }}).distinct("CustomerID")
#Names of customers who bought product 7
Customer_name_product_7 = customers.find({"CustomerID" : { "$in":
,→ Customer_product_7 }})
print "{} persons bought product Uncle Bob’s Organic Dried
,→ Pears".format(Customer_name_product_7.count())
print "who?:"
for customer in Customer_name_product_7:
print unicode("{} with id
,→ {}").format(customer[’ContactName’],customer[’CustomerID’])

