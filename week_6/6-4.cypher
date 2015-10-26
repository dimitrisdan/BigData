MATCH (n:Order)-[r:ORDERS]-(p:Product {productID:"7"})
RETURN count(distinct n.customerID)

MATCH (n:Order)-[r:ORDERS]-(p:Product {productID:"7"})
RETURN distinct n AS y, p