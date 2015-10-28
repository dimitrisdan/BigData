# Norwich Database Testing #
# DB : http://ulfaslak.com/files/northwind.db #
#######################
# SQL IMPLEMENETATION #
#######################

import sqlite3
import pymongo
import operator
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


sql = "SELECT DISTINCT OrderDetails.ProductID \
       FROM Orders, OrderDetails \
       WHERE Orders.OrderID = OrderDetails.OrderID \
       AND Orders.CustomerID = ? \
       ORDER BY ProductID"

c.execute(sql, ('ALFKI',))
alfki_products = c.fetchall()
print 'Products bought by customer ALFKI:\n%s\n' % alfki_products

similar_buyers = []

for product in alfki_products:
    # Find customers who bought each product
    sql = "SELECT DISTINCT orders.customerid \
           FROM Orders, OrderDetails \
           WHERE Orders.OrderID = OrderDetails.OrderID \
           AND Orderdetails.productid = ?"

    c.execute(sql, product)
    product_bought_by = c.fetchall()
    similar_buyers.append(product_bought_by)

most_similar = Counter(flatten(similar_buyers,)).most_common(2)
print 'Customer who bought most of the same products: %s' % most_similar[1][0]
print 'Number of common products: %s' % most_similar[1][1]

#########################
# NoSQL IMPLEMENETATION #
#########################

#ordersID's with product 7
orders_with_7 = order_details.find({"ProductID" : 7, }).distinct("OrderID")

#CustomerID's who bought product 7
Customer_product_7 = orders.find({"OrderID": { "$in": orders_with_7 }})\
    .distinct("CustomerID")

#Orders made by custmomers who bought product 7
orders_from_customer_7 = orders.find({"CustomerID" : { "$in": Customer_product_7 }})

#Orders grouped by customerID
grouped_orders = orders.aggregate([{"$match":{"CustomerID" : { "$in": Customer_product_7}}},
                                   {"$group": {"_id": "$CustomerID",
                                               "OrderID": { "$push": "$OrderID" },
                                               "count": {"$sum": 1}}}])

grouped_orders_ALFKI = orders.aggregate([{"$match":{"CustomerID" : "ALFKI"}},
                                   {"$group": {"_id": "$CustomerID",
                                               "OrderID": { "$push": "$OrderID" },
                                               "count": {"$sum": 1}}}])


#order made by ALFKI
ALFKI_orders = list(grouped_orders_ALFKI)[0]["OrderID"]

#products bought by ALFKI
ALFKI_products = order_details.find({"OrderID": { "$in": ALFKI_orders }})\
    .distinct("ProductID")

#Dictonary to keep tab on user and products in common with ALFKI
common_product_count = {}

#looped throug users orders
for order in grouped_orders:
    #get distinct products in order
    user_products = set(order_details.find({"OrderID": { "$in": order["OrderID"]}})
                        .distinct("ProductID"))
    #Find intersecction between ALFKI products and user products and find length
    common_product_count[order['_id']] = len(set(ALFKI_products)
                                             .intersection(user_products))

# Find the user with most in common with ALFKI
max_common = max(common_product_count, key=common_product_count.get)

# print result
print "User {} with {} in common with ALFKI"\
    .format(max_common,common_product_count[max_common])