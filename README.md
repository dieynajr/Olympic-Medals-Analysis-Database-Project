# Olympic Medals Analysis – Database Project
📄 The full report, with step-by-step screenshots and comments (written in French), is available here: [Projet 2 Olympic done.pdf](Projet%202%20Olympic%20done.pdf)

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

## Screenshoots
*The screenshots and the report are in French (university coursework).*

<img width="459" height="149" alt="image" src="https://github.com/user-attachments/assets/1f6fbc01-ad8e-4485-ab42-83bc8ebfec98" />

*Entity-Relationship (ER) model*

<img width="331" height="195" alt="image" src="https://github.com/user-attachments/assets/3690ec07-e3b1-474e-886a-a910c86c054d" />

*SQL query with GROUP BY and HAVING*

<img width="362" height="402" alt="image" src="https://github.com/user-attachments/assets/812d9530-6868-4d82-b2d2-a362d633cf17" />
<img width="343" height="404" alt="image" src="https://github.com/user-attachments/assets/c518da83-78a7-4653-a9e9-538ca8fb0b23" />

*Python transaction handling (commit and rollback)*

<img width="374" height="221" alt="image" src="https://github.com/user-attachments/assets/4cd8be4c-e3b6-4d93-8531-7aee45688845" />

*Excel chart:distribution of gold medals by country*



