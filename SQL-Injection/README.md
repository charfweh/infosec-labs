# DIY : SQL truncation lab

Repo demonstrate how sql truncation attack is performed and what are the technical implications of it

# Lab Setup

## Requirements
- flask
- MySql
- Burpsuite

The setup is divided into two sections `Setting up MySql` first and `Flask `
## Mysql Setup

Assuming you're already familiar with Mysql CLI and USER privileges in the same, following does the database and table setup. Still, if you're new you can refer to references below.

### SQL mode
- Start mysql server
```bash
sudo service mysqld start
```
- Login with mysql user and password in CLI
```bash
sudo mysql -u USERNAME -p
```
- In mysql cli, do `select @@sql_mode`:
```bash
STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
```
- In mysql cli, remove the `STRICT_TRANS_TABLES`:
```bash
set session sql_mode =  'ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
```

## Create Database
- After setting the `@@sql_mode`, create a database
```sql
CREATE DATABASE db_name;
```

- Select `db_name`:
```sql
SELECT db_name;
```

- Create table
```bash
CREATE TABLE users(email varchar(20),password varchar(10));
```
Note: Its important to note `email varchar(20)` as thats the flaw we're going to exploit


## Flask Setup

### Create .env 
- Follow the `.sampledotenv` notations

## Deploy

- In CLI
```python
flask --app app.py --debug run --host=0.0.0.0 --port=8000
```
This will expose app.py to your local network.


# Attack vector

The flaw exists in `email varchar(20)`, what sql truncation attack does is you put in `email` thats longer than `20` by inserting `whitespace`, resulting in duplication of `email` and basically you have `admin account` with your own `password`. 

For more reading, refer to the blog [blog here]

## sql modes

- original sql mode
```bash
STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
```

- modified sql mode
```bash
set session sql_mode =  'ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
```

- STRICT_TRANS_TABLES:
- https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sqlmode_strict_trans_tables


