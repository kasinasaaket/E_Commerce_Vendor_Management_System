import csv
import database as db

PW = ""  # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"  # considering you have installed MySQL server on your computer

RELATIVE_CONFIG_PATH = '../config/'

USER = 'users'
PRODUCTS = 'products'
ORDER = 'orders'

connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB
db.create_and_switch_database(connection, DB, DB)

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation

create_users_table = """
    create table if not exists users(
        user_id varchar(10) PRIMARY key,
        user_name varchar(45) NOT NULL,
        user_email varchar(45) NOT NULL,
        user_password varchar(45) NOT NULL,
        user_address varchar(60) NOT NULL,
        is_vendor tinyint(1) DEFAULT 0
    );
    """

create_products_table = """
    create table if not exists products(
        product_id varchar(45) NOT NULL primary key,
        product_name varchar(45) NOT NULL,
        product_description varchar(100) NOT NULL,
        product_price float(45) NOT NULL,
        emi_available varchar(10) NOT NULL,
        vendor_id varchar(10) NOT NULL,
        FOREIGN KEY (vendor_id) REFERENCES users (user_id)
    );
    """
create_orders_table = """
    create table if not exists orders(
        order_id int primary key,
        total_value double,
        order_quantity int,
        reward_point int,
        vendor_id varchar(10),
        customer_id varchar(10),
        FOREIGN KEY (vendor_id) REFERENCES users (user_id)
    );
    """

create_customer_leaderboard = """
    create table if not exists customer_leaderboard(
        customer_id varchar(10) NOT NULL,
        total_value float(45) NOT NULL,
        customer_name varchar(50) NOT NULL,
        customer_email varchar(50) NOT NULL,
        FOREIGN KEY (customer_id) REFERENCES users (user_id)
    )
    """

print("-------E-Commerce Data Storage Solution--------------\n")
print("Solution problem 1a")
connection = db.create_server_connection("localhost","root","")
db.create_and_switch_database(connection,DB,DB)

print("Solution 1a is complete\n")
print("Solution problem 1b\n")
print("Initiating creation of tables:")
db.create_table(connection,create_users_table)
print("users table created")
db.create_table(connection,create_products_table)
print("products table created")
db.create_table(connection,create_orders_table)
print("orders table created")
db.create_table(connection,create_customer_leaderboard)
print("--------Solution - Problem 1.b is complete. ---------")
print("\n")
print("------------Solution Problem 2.a ----------")
print("Initializing data insertion in user table")
with open(RELATIVE_CONFIG_PATH + USER + '.csv') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    sql = '''
    INSERT INTO USERS (user_id,user_name,user_email,user_password,user_address,is_vendor)
    VALUES (%s,%s,%s,%s,%s,%s)
    '''
    val.pop(0)
    db.insert_many_records(connection,sql,val)
print("Data insertion in user table is complete\n")
print("Initializing the data insertion in Products table")

with open(RELATIVE_CONFIG_PATH + PRODUCTS + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    sql = '''
    INSERT INTO products (product_id,product_name,product_price,product_description,vendor_id,emi_available)
    VALUES (%s,%s,%s,%s,%s,%s)
    '''
    val.pop(0)
    db.insert_many_records(connection,sql,val)
print("Data insertion in products table is complete")


with open(RELATIVE_CONFIG_PATH + ORDER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    sql = '''
    INSERT INTO orders (order_id,total_value,order_quantity,reward_point,vendor_id,customer_id)
    VALUES (%s,%s,%s,%s,%s,%s)
    '''
    val.pop(0)
    db.insert_many_records(connection,sql,val)
print("Data insertion in orders table is complete")
print("--------Solution - Problem 2.a is complete ---------")
