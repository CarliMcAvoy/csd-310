CREATE DATABASE IF NOT EXISTS willson_financial;

USE willson_financial;

DROP TABLE IF EXISTS Transaction, Asset, Client, Employee;

CREATE TABLE Client(
    ClientID int auto_increment primary key,
    FirstName varchar(50),
    LastName varchar(50),
    ContactInfo varchar(100),
    DateAdded date
);

CREATE TABLE Asset(
    AssetID int auto_increment primary key,
    ClientID int,
    AssetType varchar(50),
    AssetValue decimal(12,2),
    foreign key (ClientID) references Client(ClientID)
);

CREATE TABLE Transaction(
    TransactionID int auto_increment primary key,
    ClientID int,
    Date date,
    Type varchar(50),
    Amount decimal(10,2),
    foreign key (ClientID) references Client(ClientID)
);

CREATE TABLE Employee(
    EmployeeID int auto_increment primary key,
    FirstName varchar(50),
    LastName varchar(50),
    Role varchar(50),
    EmploymentType varchar(50)
);

INSERT INTO Client (FirstName, LastName, ContactInfo, DateAdded) VALUES
    ('Alice', 'Smith', 'alice@example.com', '2025-06-15'),
    ('Bob', 'Jones', 'bob@example.com', '2025-07-01'),
    ('Carol', 'Lee', 'carol@example.com', '2025-08-10'),
    ('David', 'Kim', 'david@example.com', '2025-09-12'),
    ('Eva', 'Chen', 'eva@example.com', '2025-10-20'),
    ('Frank', 'Hall', 'frank@example.com', '2025-11-25');

INSERT INTO Asset(ClientID, AssetType, AssetValue) VALUES
    (1, 'Retirement', 250000.00),
    (2, 'Investment', 180000.00),
    (3, 'Savings', 95000.00),
    (4, 'Real Estate', 320000.00),
    (5, 'Stocks', 150000.00),
    (6, 'Bonds', 120000.00);

INSERT INTO Transaction(ClientID, Date, Type, Amount) VALUES
    (1, '2025-06-16', 'Deposit', 5000.00),
    (2, '2025-07-02', 'Withdrawal', 2000.00),
    (3, '2025-08-11', 'Deposit', 3000.00),
    (4, '2025-09-13', 'Transfer', 1000.00),
    (5, '2025-10-21', 'Deposit', 4000.00),
    (6, '2025-11-26', 'Withdrawal', 1500.00);

INSERT INTO Employee(FirstName, LastName, Role, EmploymentType) VALUES
    ('Phoenix','Two Star','Office Manager','Full-Time'),
    ('June','Santos','Compliance Manager','Part-Time');





