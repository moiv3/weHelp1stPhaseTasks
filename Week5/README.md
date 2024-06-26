# Wehelp Week 5 Assignment Response

## Task 1

MySQL 8.3 was successfully installed.

```SQL
mysql> STATUS;
--------------
C:\Program Files\MySQL\MySQL Server 8.3\bin\mysql.exe  Ver 8.3.0 for Win64 on x86_64 (MySQL Community Server - GPL)

Connection id:          9
Current database:       website
Current user:           root@localhost
SSL:                    Cipher in use is TLS_AES_128_GCM_SHA256
Using delimiter:        ;
Server version:         8.3.0 MySQL Community Server - GPL
Protocol version:       10
Connection:             localhost via TCP/IP
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    utf8mb4
Conn.  characterset:    utf8mb4
TCP port:               3306
Binary data as:         Hexadecimal
Uptime:                 2 hours 47 min 6 sec

Threads: 2  Questions: 165  Slow queries: 0  Opens: 194  Flush tables: 3  Open tables: 98  Queries per second avg: 0.016
--------------
```

## Task 2

A database named **website** was created.

A table named **member** in the **website** database was created under specifications in the assignement.

```SQL
mysql> CREATE DATABASE website;
Query OK, 1 row affected (0.01 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| website            |
+--------------------+
5 rows in set (0.00 sec)

mysql> USE website;
Database changed
mysql> CREATE TABLE member(
    -> id BIGINT AUTO_INCREMENT,
    -> name VARCHAR(255) NOT NULL,
    -> username VARCHAR(255) NOT NULL,
    -> password VARCHAR(255) NOT NULL,
    -> follower_count INT UNSIGNED DEFAULT 0 NOT NULL,
    -> time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -> PRIMARY KEY (id)
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> SHOW TABLES;
+-------------------+
| Tables_in_website |
+-------------------+
| member            |
+-------------------+
1 row in set (0.00 sec)

mysql> desc member;
+----------------+--------------+------+-----+-------------------+-------------------+
| Field          | Type         | Null | Key | Default           | Extra             |
+----------------+--------------+------+-----+-------------------+-------------------+
| id             | bigint       | NO   | PRI | NULL              | auto_increment    |
| name           | varchar(255) | NO   |     | NULL              |                   |
| username       | varchar(255) | NO   |     | NULL              |                   |
| password       | varchar(255) | NO   |     | NULL              |                   |
| follower_count | int unsigned | NO   |     | 0                 |                   |
| time           | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+----------------+--------------+------+-----+-------------------+-------------------+
6 rows in set (0.02 sec)
```
Screenshots of this task are as follows:  
![screenshot1](screenshots/scr1.png)  
![screenshot2](screenshots/scr2.png)

## Task 3

### Subtask 1

One row of "test" and 4 rows of arbitary data were inserted.

```SQL
mysql> INSERT INTO member (name,username, password)
    -> VALUES("test", "test", "test");
Query OK, 1 row affected (0.04 sec)

mysql> SELECT * FROM member;
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-30 14:50:26 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.00 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("Red", "red", "hongse");
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("Orange", "orange", "chengse");
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("Yellow", "yellow", "huangse");
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("Green", "green", "lyuse");
Query OK, 1 row affected (0.01 sec)
```

### Subtask 2

All rows from table **member** are selected.

```SQL
mysql> SELECT * FROM member;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  1 | test   | test     | test     |              0 | 2024-04-30 14:50:26 |
|  2 | Red    | red      | hongse   |              0 | 2024-04-30 14:52:14 |
|  3 | Orange | orange   | chengse  |              0 | 2024-04-30 14:52:27 |
|  4 | Yellow | yellow   | huangse  |              0 | 2024-04-30 14:52:39 |
|  5 | Green  | green    | lyuse    |              0 | 2024-04-30 14:52:52 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)
```
Screenshots for subtasks 1 and 2:  
![screenshot3](screenshots/scr3.png)  

### Subtask 3

All rows from table **member** by **descending order of time** are selected.

```SQL
mysql> SELECT * FROM member ORDER BY time DESC;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  5 | Green  | green    | lyuse    |              0 | 2024-04-30 14:52:52 |
|  4 | Yellow | yellow   | huangse  |              0 | 2024-04-30 14:52:39 |
|  3 | Orange | orange   | chengse  |              0 | 2024-04-30 14:52:27 |
|  2 | Red    | red      | hongse   |              0 | 2024-04-30 14:52:14 |
|  1 | test   | test     | test     |              0 | 2024-04-30 14:50:26 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)
```

<Screenshot here>

### Subtask 4

The **2nd to 4th rows** from table **member** by **descending order of time** are selected.

```SQL
mysql> SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  4 | Yellow | yellow   | huangse  |              0 | 2024-04-30 14:52:39 |
|  3 | Orange | orange   | chengse  |              0 | 2024-04-30 14:52:27 |
|  2 | Red    | red      | hongse   |              0 | 2024-04-30 14:52:14 |
+----+--------+----------+----------+----------------+---------------------+
3 rows in set (0.02 sec)
```

### Subtask 5

Rows where **username = "test"** are selected.

```SQL
mysql> SELECT * from member WHERE username = "test";
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-30 14:50:26 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.00 sec)
```

### Subtask 6

Rows where **name includes "es"** are selected.

```SQL
mysql> SELECT * from member WHERE name LIKE "%es%";
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-30 14:50:26 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.02 sec)
```

### Subtask 7

Rows where **both username and password = "test"** are selected.

```SQL
mysql> SELECT * from member WHERE username = "test" AND password = "test";
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-30 14:50:26 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.00 sec)
```

Screenshot for subtasks 3, 4, 5, 6 and 7:  
![screenshot4](screenshots/scr4.png)  

### Subtask 8

Username "test" was **updated to "test2"**.

```SQL
mysql> UPDATE member
    -> SET name = "test2"
    -> WHERE username = "test";
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM member;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  1 | test2  | test     | test     |              0 | 2024-04-30 14:50:26 |
|  2 | Red    | red      | hongse   |              0 | 2024-04-30 14:52:14 |
|  3 | Orange | orange   | chengse  |              0 | 2024-04-30 14:52:27 |
|  4 | Yellow | yellow   | huangse  |              0 | 2024-04-30 14:52:39 |
|  5 | Green  | green    | lyuse    |              0 | 2024-04-30 14:52:52 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)
```

Screenshot for subtask 8:
![screenshot5](screenshots/scr5.png)

## Task 4

### Subtask 1

The **number of rows** from the member table were selected.

```SQL
mysql> SELECT COUNT(*) FROM member;
+----------+
| COUNT(*) |
+----------+
|        5 |
+----------+
1 row in set (0.04 sec)
```

Screenshot for subtask 1:
![screenshot6](screenshots/scr6.png)

### Subtask 2

First, **follower_count** data were slightly modified for easier verification.

```SQL
mysql> UPDATE member SET follower_count = 5 WHERE id = 1;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE member SET follower_count = 40 WHERE id = 2;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE member SET follower_count = 300 WHERE id = 3;
Query OK, 1 row affected (0.03 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE member SET follower_count = 2000 WHERE id = 4;
Query OK, 1 row affected (0.02 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> UPDATE member SET follower_count = 10000 WHERE id = 5;
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * FROM member;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  1 | test2  | test     | test     |              5 | 2024-04-30 14:50:26 |
|  2 | Red    | red      | hongse   |             40 | 2024-04-30 14:52:14 |
|  3 | Orange | orange   | chengse  |            300 | 2024-04-30 14:52:27 |
|  4 | Yellow | yellow   | huangse  |           2000 | 2024-04-30 14:52:39 |
|  5 | Green  | green    | lyuse    |          10000 | 2024-04-30 14:52:52 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)
```

The **sum of follower_count** of all rows were selected.

```SQL
mysql> SELECT SUM(follower_count) FROM member;
+---------------------+
| SUM(follower_count) |
+---------------------+
|               12345 |
+---------------------+
1 row in set (0.02 sec)
```

### Subtask 3

The **average of follower_count** of all rows were selected.

```SQL
mysql> SELECT AVG(follower_count) FROM member;
+---------------------+
| AVG(follower_count) |
+---------------------+
|           2469.0000 |
+---------------------+
1 row in set (0.00 sec)
```

### Subtask 4

The **average of follower_count** of the first 2 rows, in descending order of follower_count from the member table were selected.

```SQL
mysql> SELECT AVG(follower_count_subset) FROM (SELECT follower_count AS follower_count_subset FROM member ORDER BY follower_count DESC LIMIT 2) as follower_count_avg;
+----------------------------+
| AVG(follower_count_subset) |
+----------------------------+
|                  6000.0000 |
+----------------------------+
1 row in set (0.00 sec)
```

Screenshot of subtask 2, 3 and 4:
![screenshot8](screenshots/scr8.png)

## Task 5

### Subtask 1

A new table named **message** in the **website** database was created.

```SQL
mysql> CREATE TABLE message(
    -> id BIGINT AUTO_INCREMENT,
    -> member_id BIGINT NOT NULL,
    -> content VARCHAR(255) NOT NULL,
    -> like_count INT UNSIGNED DEFAULT 0 NOT NULL,
    -> time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -> PRIMARY KEY(id)
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> ALTER TABLE message
    -> ADD FOREIGN KEY (member_id) REFERENCES member(id);
Query OK, 0 rows affected (0.15 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc message;
+------------+--------------+------+-----+-------------------+-------------------+
| Field      | Type         | Null | Key | Default           | Extra             |
+------------+--------------+------+-----+-------------------+-------------------+
| id         | bigint       | NO   | PRI | NULL              | auto_increment    |
| member_id  | bigint       | NO   | MUL | NULL              |                   |
| content    | varchar(255) | NO   |     | NULL              |                   |
| like_count | int unsigned | NO   |     | 0                 |                   |
| time       | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
+------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)
```
Screenshot of subtask 1:
![screenshot9](screenshots/scr9.png)

### Adding Data into "message" table

Some data were added into the **message** table.

```SQL
mysql> INSERT INTO message(member_id, content, like_count)
    -> VALUES(1, "我年紀還輕，閱歷不深的時候，",10)
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO message(member_id, content, like_count)
    -> VALUES(1, "我父親教導過我一句話，我至今還念念不忘。",20);
Query OK, 1 row affected (0.01 sec)

...
```
以下，新增資料動作中，重複的部分省略，直接跳到結果：

```SQL
mysql> SELECT * FROM message;
+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
| id | member_id | content                                                                                                      | like_count | time                |
+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
|  1 |         1 | 我年紀還輕，閱歷不深的時候，                                                                                 |         10 | 2024-04-30 15:19:18 |
|  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                                                                     |         20 | 2024-04-30 15:19:32 |
|  3 |         2 | 「每逢你想要批評任何人的時候，」他對我說，                                                                   |         30 | 2024-04-30 15:19:51 |
|  4 |         3 | 「你就記住，這個世界上所有的人，並不是個個都有過你擁有的那些優越條件。」                                     |         40 | 2024-04-30 15:20:02 |
|  5 |         1 | 他沒再說別的。                                                                                               |         50 | 2024-04-30 15:20:14 |
|  6 |         5 | 但是，我們父子之間話雖不多，                                                                                 |         60 | 2024-04-30 15:20:24 |
|  7 |         4 | 卻一向許多事情是特別會意的，因此我明白他的話大有弦外之音。                                                   |         70 | 2024-04-30 15:20:35 |
|  8 |         4 | 久而久之，我就慣於對所有的人都保留判斷，                                                                     |         80 | 2024-04-30 15:20:55 |
|  9 |         3 | 這個習慣既使得許多有怪僻的人肯跟我講心裡話，                                                                 |         90 | 2024-04-30 15:20:59 |
| 10 |         1 | 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。                                                                 |        100 | 2024-04-30 15:21:10 |
+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
10 rows in set (0.00 sec)
```

### Subtask 2

All message text including sender names were selected.

```SQL
mysql> SELECT message.content, member.name
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id;
+--------------------------------------------------------------------------------------------------------------+--------+
| content                                                                                                      | name   |
+--------------------------------------------------------------------------------------------------------------+--------+
| 我年紀還輕，閱歷不深的時候，                                                                                 | test2  |
| 我父親教導過我一句話，我至今還念念不忘。                                                                     | test2  |
| 他沒再說別的。                                                                                               | test2  |
| 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。                                                                 | test2  |
| 「每逢你想要批評任何人的時候，」他對我說，                                                                   | Red    |
| 「你就記住，這個世界上所有的人，並不是個個都有過你擁有的那些優越條件。」                                     | Orange |
| 這個習慣既使得許多有怪僻的人肯跟我講心裡話，                                                                 | Orange |
| 卻一向許多事情是特別會意的，因此我明白他的話大有弦外之音。                                                   | Yellow |
| 久而久之，我就慣於對所有的人都保留判斷，                                                                     | Yellow |
| 但是，我們父子之間話雖不多，                                                                                 | Green  |
+--------------------------------------------------------------------------------------------------------------+--------+
10 rows in set (0.00 sec)
```

### Subtask 3

All message text with **username = "test"** were selected.

```SQL
mysql> SELECT message.content, member.name
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id
    -> WHERE member.username = "test";
+--------------------------------------------------------------------+-------+
| content                                                            | name  |
+--------------------------------------------------------------------+-------+
| 我年紀還輕，閱歷不深的時候，                                       | test2 |
| 我父親教導過我一句話，我至今還念念不忘。                           | test2 |
| 他沒再說別的。                                                     | test2 |
| 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。                       | test2 |
+--------------------------------------------------------------------+-------+
4 rows in set (0.00 sec)
```

Screenshot of subtask 2 and 3:
![screenshot11](screenshots/scr11.png)

### Subtask 4

The **average like count** of messages where (username = "test") was calculated.

```SQL
mysql> SELECT AVG(message.like_count)
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id
    -> WHERE member.username = "test";
+-------------------------+
| AVG(message.like_count) |
+-------------------------+
|                 45.0000 |
+-------------------------+
1 row in set (0.00 sec)

mysql> SELECT message.content, message.like_count, member.name
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id
    -> WHERE member.username = "test";
+--------------------------------------------------------------------+------------+-------+
| content                                                            | like_count | name  |
+--------------------------------------------------------------------+------------+-------+
| 我年紀還輕，閱歷不深的時候，                                       |         10 | test2 |
| 我父親教導過我一句話，我至今還念念不忘。                           |         20 | test2 |
| 他沒再說別的。                                                     |         50 | test2 |
| 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。                       |        100 | test2 |
+--------------------------------------------------------------------+------------+-------+
4 rows in set (0.00 sec)
```

### Subtask 5

The average like count of messages was calculated and **grouped by sender username**.

```SQL
mysql> SELECT AVG(message.like_count), member.username
    -> FROM message
    -> JOIN member
    -> ON message.member_id = member.id
    -> GROUP BY member.username;
+-------------------------+----------+
| AVG(message.like_count) | username |
+-------------------------+----------+
|                 45.0000 | test     |
|                 30.0000 | red      |
|                 65.0000 | orange   |
|                 75.0000 | yellow   |
|                 60.0000 | green    |
+-------------------------+----------+
5 rows in set (0.02 sec)
```

Screenshot of subtask 4 and 5:
![screenshot12](screenshots/scr12.png)

## Final steps

### Exporting the database

The database was exported by mysqldump (outside of the MySQL command-line client) to **data.sql**.

```bat
Microsoft Windows [版本 10.0.22631.3447]
(c) Microsoft Corporation. 著作權所有，並保留一切權利。

C:\Windows\System32>cd C:\Program Files\MySQL\MySQL Server 8.3\bin

C:\Program Files\MySQL\MySQL Server 8.3\bin>mysqldump -u root -p website > data.sql
Enter password: ***

C:\Program Files\MySQL\MySQL Server 8.3\bin>
```

**data.sql** was then moved to the Week5 repository folder.

### Writing the process to README.md

This README.md is the result of the writeup.