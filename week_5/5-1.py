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
	
sql = "SELECT * FROM Territories WHERE RegionID = 1"
c.execute(sql)
eastern_region = c.fetchall()

print "TERRITORIES "

for territory in eastern_region:
	print territory
	
sql = "SELECT Title, COUNT (*) AS employees_by_department FROM Employees GROUP BY Title"
c.execute(sql)
empl_dpt = c.fetchall()
print "\nTOTAL NUMBER OF EMPLOYEES BY DEPARTMENT"

for total in empl_dpt:
	print totalc.close()

#########################
# NoSQL IMPLEMENETATION #
#########################

client = pymongo.MongoClient()
db = client.Northwind
orders = db.orders
products = db.products
customers = db.customers

order_details = db[’order-details’]

print order_details