MATCH (n:Order {customerID:"ALFKI"})-[o:ORDERS]->(x)
RETURN n.orderID,x.productNam