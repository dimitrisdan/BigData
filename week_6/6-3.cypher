MATCH (n:Order {customerID:"ALFKI"})-[r:ORDERS]->(p:Product)
WITH n, COUNT(r) AS rc
WHERE rc > 1
MATCH n-[r:ORDERS]-(p:Product)
RETURN n, p