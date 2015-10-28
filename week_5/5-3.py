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

#########################
# NoSQL IMPLEMENETATION #
#########################

product_details = \
	order_details.aggregate(
		[{"$match":{"OrderID" : { "$in": orders.find({"CustomerID" : "ALFKI"}).distinct("OrderID")}}},
		 {"$group": {"_id": "$OrderID", "productID": { "$push": "$ProductID" }, "count": {"$sum": 1}}},
		 { "$match" : { "count" : { "$gte": 2 } } }])

for product_detail in product_details:
	print "\n"
	print "order id: {} has products:".format(product_detail["_id"])

	for product in products.find({"ProductID" : { "$in": product_detail["productID"] }}):
		print unicode("{} with ID:{}").format(product["ProductName"],product["ProductID"])