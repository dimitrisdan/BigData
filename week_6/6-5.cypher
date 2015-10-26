MATCH (n:Order)-[r:ORDERS]-(p:Product {productID:"7"})
WITH distinct n.customerID AS y
MATCH (n:Order)-[r:ORDERS]-(p:Product)
WHERE n.customerID in y
RETURN distinct p.productName