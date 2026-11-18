# Olympic Medals Analysis – Database Project

Individual project from a second-year university Databases course. The goal: clean a Kaggle dataset, build a relational database from it, then query and analyze the data with SQL, Python and Excel.

## Technologies
Kaggle dataset (Olympic medals), MySQL (phpMyAdmin), SQL, Python (pandas), Excel

## What I Did
1. **Data cleaning:** cleaned the Kaggle dataset before loading it
2. **Database design:** created the ER (Entity-Relationship) model and normalized the schema to 3NF (Third Normal Form)
3. **Database creation:** created the tables and imported the CSV file with phpMyAdmin
4. **SQL queries:** wrote queries with conditions, joins, `GROUP BY ... HAVING`, `EXISTS` and set difference
5. **Python:** created a `Country` table with Python and pandas, and wrote a script that queries, updates and deletes records in the database
6. **Transactions:** implemented commit and rollback in Python to illustrate ACID properties
7. **Excel analysis:** built pivot tables, a histogram and a pie chart, with comments on the results

## Repository Content
- `Olympics (1896-2024).csv`: dataset
- `LMD_LDD.sql`: SQL scripts (DDL/DML: table creation, insertion and deletion)
- `Pays.py`: Python script creating the `Country` table
- `Projet 2 Olympic done.pdf`: project report with screenshots and comments

