import mysql.connector

# Prompt for credentials at runtime
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")

conn = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password,
    database="Willson_Financial"
)
cursor = conn.cursor()

# Example query for Report 1
print("\n--- Report 1: Client Asset Summary ---")
cursor.execute("""
SELECT c.FirstName, c.LastName, a.AssetType, a.AssetValue
FROM Client c
JOIN Asset a ON c.ClientID = a.ClientID
""")
client_list = cursor.fetchall()
for client in client_list:
    print("Client Name: {} {} | Asset Type: {} | Asset Value: ${:,.2f}\n".format(client[0],
                                                                           client[1],
                                                                           client[2],
                                                                           client[3]))


#Report 2: Average amount of assets for all clients
print("\n\n--- Report 2: Average Asset Amount ---")
cursor.execute("""
SELECT COUNT(ClientID), ROUND(AVG(AssetValue))
FROM Asset
""")
assets = cursor.fetchall()
for asset in assets:
    print("Total Clients: {}\nAverage of Total Assets: ${:,.2f}".format(asset[0],
                                                                  asset[1]))


#Report 3: Clients added per month
print("\n\n--- Report 3: New Clients Added (Six Months) ---")
cursor.execute("""
SELECT MONTHNAME(DateAdded), COUNT(ClientID)
FROM Client
GROUP BY MONTHNAME(DateAdded)
""")
clients = cursor.fetchall()
for client in clients:
    print("Month: {} | Clients Added: {}\n".format(client[0],
                                                   client[1]))


#Report 4: Clients with more than 10 transactions in a month
print("\n\n--- Report 4: High Activity Clients (10+ Transactions/Month) ---")
cursor.execute("""
SELECT ClientID, COUNT(ClientID) AS TransactionCount, MONTHNAME(DateMade) AS Month
FROM `Transaction`
GROUP BY ClientID, MONTH(DateMade), MONTHNAME(DateMade)
HAVING COUNT(*) > 10
ORDER BY ClientID, MONTH(DateMade)
""")
transactions = cursor.fetchall()
for transaction in transactions:
    print("Client ID: {} | Transactions: {} | Month: {}\n".format(transaction[0],
                                                                  transaction[1],
                                                                  transaction[2]))

conn.close()
