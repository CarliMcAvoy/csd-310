# Connect to MySQL
import mysql.connector, sys
from mysql.connector import errorcode

# Confirm MySQL Credentials
user = input("Enter MySQL username: ")
password = input("Enter MySQL password: ")

try:
    db_connection = mysql.connector.connect(
        host="localhost",
        user=user,
        password=password,
        database="Willson_Financial"
    )
    cursor = db_connection.cursor()
except mysql.connector.Error as error:

    if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif error.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print("An unexpected error occurred: {}".format(error))
    # Exit the program on error
    sys.exit(1)


# Drop tables if they exist
cursor.execute("DROP TABLE IF EXISTS Transaction")
cursor.execute("DROP TABLE IF EXISTS Asset")
cursor.execute("DROP TABLE IF EXISTS Client")
cursor.execute("DROP TABLE IF EXISTS Employee")

# Create tables
cursor.execute("""
CREATE TABLE Client (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ContactInfo VARCHAR(100),
    DateAdded DATE
)
""")

cursor.execute("""
CREATE TABLE Asset (
    AssetID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT,
    AssetType VARCHAR(50),
    AssetValue DECIMAL(12,2),
    FOREIGN KEY (ClientID) REFERENCES Client(ClientID)
)
""")

cursor.execute("""
CREATE TABLE Transaction (
    TransactionID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT,
    Date DATE,
    Type VARCHAR(50),
    Amount DECIMAL(10,2),
    FOREIGN KEY (ClientID) REFERENCES Client(ClientID)
)
""")

cursor.execute("""
CREATE TABLE Employee (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Role VARCHAR(50),
    EmploymentType VARCHAR(50)
)
""")

# Insert sample data
cursor.executemany("INSERT INTO Client (FirstName, LastName, ContactInfo, DateAdded) VALUES (%s, %s, %s, %s)", [
    ("Alice", "Smith", "alice@example.com", "2025-06-15"),
    ("Bob", "Jones", "bob@example.com", "2025-07-01"),
    ("Carol", "Lee", "carol@example.com", "2025-08-10"),
    ("David", "Kim", "david@example.com", "2025-09-12"),
    ("Eva", "Chen", "eva@example.com", "2025-10-20"),
    ("Frank", "Hall", "frank@example.com", "2025-11-25")
])

cursor.executemany("INSERT INTO Asset (ClientID, AssetType, AssetValue) VALUES (%s, %s, %s)", [
    (1, "Retirement", 250000.00),
    (2, "Investment", 180000.00),
    (3, "Savings", 95000.00),
    (4, "Real Estate", 320000.00),
    (5, "Stocks", 150000.00),
    (6, "Bonds", 120000.00)
])

cursor.executemany("INSERT INTO Transaction (ClientID, Date, Type, Amount) VALUES (%s, %s, %s, %s)", [
    (1, "2025-06-16", "Deposit", 5000.00),
    (2, "2025-07-02", "Withdrawal", 2000.00),
    (3, "2025-08-11", "Deposit", 3000.00),
    (4, "2025-09-13", "Transfer", 1000.00),
    (5, "2025-10-21", "Deposit", 4000.00),
    (6, "2025-11-26", "Withdrawal", 1500.00)
])

cursor.executemany("INSERT INTO Employee (FirstName, LastName, Role, EmploymentType) VALUES (%s, %s, %s, %s)", [
    ("Phoenix", "Two Star", "Office Manager", "Full-Time"),
    ("June", "Santos", "Compliance Manager", "Part-Time")
])

db_connection.commit()

#Display Tables
print('\n-- CLIENT RECORDS --')

cursor.execute("SELECT * FROM client")
clients = cursor.fetchall()

for client in clients:
    print("Client ID: {} - First Name: {} - Last Name: {} - Contact Information: {} - Date Added: {}\n".format(client[0],
                                                                                                           client[1],
                                                                                                           client[2],
                                                                                                           client[3],
                                                                                                           client[4]))

print('-- ASSET RECORDS --')

cursor.execute("SELECT * FROM asset")
assets = cursor.fetchall()

for asset in assets:
    print("Asset ID: {} - Client ID: {} - Asset Type: {} - Asset Value: {}\n".format(asset[0],
                                                                                asset[1],
                                                                                asset[2],
                                                                                asset[3]))

print('-- TRANSACTION RECORDS --')

cursor.execute("SELECT * FROM transaction")
transactions = cursor.fetchall()

for transaction in transactions:
    print("Transaction ID: {} - Client ID: {} - Date: {} - Type: {} - Amount: {}\n".format(transaction[0],
                                                                                           transaction[1],
                                                                                           transaction[2],
                                                                                           transaction[3],
                                                                                           transaction[4]))

print('-- EMPLOYEE RECORDS --')

cursor.execute("SELECT * FROM employee")
employees = cursor.fetchall()

for employee in employees:
    print("Employee ID: {} - First Name: {} - Last Name: {} - Role: {} - Employment Type: {}\n".format(employee[0],
                                                                                                       employee[1],
                                                                                                       employee[2],
                                                                                                       employee[3],
                                                                                                       employee[4]))

db_connection.close()