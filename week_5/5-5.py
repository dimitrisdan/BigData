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
	
sql  = "SELECT distinct orderdetails.productID, products.productname \
        FROM orderdetails , products \
        WHERE  products.productid=orderdetails.productid \
        AND orderdetails.orderid IN \
        (SELECT orders.orderID \
        FROM orders \
        WHERE orders.customerID IN \
        (SELECT  orders.customerid \
        FROM Orders, OrderDetails  \
        WHERE Orders.OrderID = OrderDetails.OrderID \
        AND OrderDetails.ProductID = 7))"
          
c.execute(sql)
products = c.fetchall()

# Iterate through these customers
print products 

print '\n---------------------------------------------------'
print 'Total of Distinct Products Ordered: %s \n' % len(products)

print '---------------------------------------------------'

#########################
# NoSQL IMPLEMENETATION #
#########################

Customer_product_7 = orders.find({"OrderID": { "$in": orders_with_7 }}).distinct("CustomerID")

#All orders made of customers who bought product 7
orders_from_customer_7 = orders.find({"CustomerID" : { "$in": Customer_product_7 }}).distinct("OrderID")

#All distinct products bought by customers who bought product 7
products_bought_customer_7  = order_details.find({"OrderID" : { "$in": orders_from_customer_7 }}).distinct("ProductID")

print "number of distinct products {}".format(len(products_bought_customer_7))

print list(products.find({"ProductID" : { "$in": products_bought_customer_7 }}).distinct("ProductName"))

