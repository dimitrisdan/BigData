MATCH (c)-[p:ORDERS]->(products)
WHERE c.customerID="ALFKI"
MATCH (c2)-[q:ORDERS]->(products)
WHERE NOT (c2.customerID="ALFKI")
RETURN DISTINCT c2, products