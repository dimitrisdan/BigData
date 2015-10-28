# Norwich Database Testing #
# DB : http://ulfaslak.com/files/northwind.db #
#######################
# SQL IMPLEMENETATION #
#######################

import sqlite3
import pymongo
from collections import Counter

# DB Connection
conn = sqlite3.connect('northwind.db')

# Return Bytestrings instead of Unicode
conn.text_factory = str

# Create a Cursor object
c = conn.cursor()
if not c:
    print error
	
def flatten(seq, container=None):
    """
    :param seq: A list of lists
    :return: A flattened list containing all the items of the input
    """
    if container is None:
        container = []

    for s in seq:
        if hasattr(s, '__iter__'):
            flatten(s, container)
        else:
            container.append(s)

    return container

sql1 = "SELECT DISTINCT Orders.CustomerID " \
       "FROM Orders, OrderDetails " \
       "WHERE Orders.OrderID = OrderDetails.OrderID " \
       "AND OrderDetails.ProductID = 7"

sql2 = "SELECT DISTINCT Orders.OrderID " \
       "FROM Orders " \
       "WHERE Orders.CustomerID = ?"

sql3 = "SELECT OrderDetails.ProductID " \
       "FROM OrderDetails " \
       "WHERE Orderdetails.Orderid = ? "

all_orders = []
all_products = []

c.execute(sql1)
customers = c.fetchall()

for customer in customers:
    c.execute(sql2, customer)
    orders = c.fetchall()
    all_orders.append(orders)
    
all_orders = flatten(all_orders)

for order in all_orders:
    c.execute(sql3, (order,))
    products = c.fetchall()
    all_products.append(products)

most_ordered = Counter(flatten(all_products)).most_common(3)
print 'Most ordered products :'
print 'Product %d have been ordered %d times' % (most_ordered[1][0], most_ordered[1][1])
print 'Product %d have been ordered %d times' % (most_ordered[2][0], most_ordered[2][1])

c.close()

#########################
# NoSQL IMPLEMENETATION #
#########################

#ordersID's with product 7
orders_with_7 = order_details.find({"ProductID" : 7, }).distinct("OrderID")

#CustomerID's who bought product 7
Customer_product_7 = orders.find({"OrderID": { "$in": orders_with_7 }}).distinct("CustomerID")

#Orders made by cusmomers who bought product 7
orders_from_customer_7 = orders.find({"CustomerID" : { "$in": Customer_product_7 }}).distinct("OrderID")

#get Order_details where orderID is in orders_from_customer_7, and then group by product id. Each group has a count
#we sort it by count
most_ordered_7 = \
    list(
        order_details.aggregate(
            [{"$match": {"OrderID" : { "$in": orders_from_customer_7 }}},
             {"$group": {"_id": "$ProductID", "count": {"$sum": 1}}},
             { '$sort' : { "count" : -1} }])
    )

print "top 5:"
print "Count,ProductName"

for product in most_ordered_7[:5]:

    product_name = \
        products.find_one({"ProductID" : product["_id"]})['ProductName']
    
    count = product["count"]
    
    print "{} \t {}".format(count,product_name)