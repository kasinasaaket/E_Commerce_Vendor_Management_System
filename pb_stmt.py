#1. Creating schema and tables. Use either Pythonprogram or MySQL Workbench UI for thisactivity.
#a.Create a database named ecommerce_record.
#b.Create the required tables, mentioned in the ER diagram.
#Do ensure that the tables and their respective columns have the same name asmentioned. Also make a note on creating the required primary and foreign keys.

#2. Implement functionality to implement insertand select operations
#a.In the setup.py file, you have to write the correct insert method to perform insert operation ontheusers,productsandorderstables with the dataavailable in      #the relevant csv file. Theplaceholders where you have to write the code have been marked.

#b.After the above step, write 5 insert operations on the orders table. Each insert operation should be for a different customer.
#c.Write a read operation that will fetch all the records of the orders table and print the data on the console.

#3. Performing analysis data and creating a report
#a. From theorderstable write a query to find the maximumand minimum order value. Print thevalues on the console.
#b.Fetch and print the orders with value (total_value) greater than the average value (total_value)of all the orders in the orders table.
#c.Create a new table in the name of customer_leaderboard. It should have the following fieldscustomer_id (string)total_value (float),customer_name #(string)#customer_email (string)Insert one row for each registered customer who has made a purchase. And fill the(total_value) of this table, with the #highest purchasevalue (total_value) of theorderstable fora customer. In case a customer has not made any purchase, then do not add a record of the customer.