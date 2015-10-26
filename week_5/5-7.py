import sqlite3

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