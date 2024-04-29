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

<Screenshot here>

## Task 2

A table named website was created.

```SQL
mySQL>
CREATE TABLE member(
id BIGINT AUTO_INCREMENT,
name VARCHAR(255) NOT NULL,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL,
follower_count INT UNSIGNED DEFAULT 0 NOT NULL,
time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
PRIMARY KEY (id)
);
```

Output:
```SQL
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
```

<Screenshot here>

## Task 3

### Subtask 1
mysql> INSERT INTO member (name,username, password)
    -> VALUES("test", "test", "test");
Query OK, 1 row affected (0.03 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("red", "Red", "hongse");
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("orange", "Orange", "chengse");
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("yellow", "Yellow", "huangse");
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO member (name,username, password)
    -> VALUES("green", "Green", "lyuse");
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM member;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time
   |
+----+--------+----------+----------+----------------+---------------------+
|  1 | test   | test     | test     |              0 | 2024-04-29 17:09:09 |
|  2 | red    | Red      | hongse   |              0 | 2024-04-29 17:10:00 |
|  3 | orange | Orange   | chengse  |              0 | 2024-04-29 17:10:39 |
|  4 | yellow | Yellow   | huangse  |              0 | 2024-04-29 17:11:15 |
|  5 | green  | Green    | lyuse    |              0 | 2024-04-29 17:11:38 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)

<Screenshot here>

### Subtask 3

mysql> SELECT * FROM member ORDER BY time DESC;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  5 | green  | Green    | lyuse    |              0 | 2024-04-29 17:11:38 |
|  4 | yellow | Yellow   | huangse  |              0 | 2024-04-29 17:11:15 |
|  3 | orange | Orange   | chengse  |              0 | 2024-04-29 17:10:39 |
|  2 | red    | Red      | hongse   |              0 | 2024-04-29 17:10:00 |
|  1 | test   | test     | test     |              0 | 2024-04-29 17:09:09 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)

<Screenshot here>

### Subtask 4

mysql> SELECT * FROM member ORDER BY time DESC
    -> LIMIT 3 OFFSET 1;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  4 | yellow | Yellow   | huangse  |              0 | 2024-04-29 17:11:15 |
|  3 | orange | Orange   | chengse  |              0 | 2024-04-29 17:10:39 |
|  2 | red    | Red      | hongse   |              0 | 2024-04-29 17:10:00 |
+----+--------+----------+----------+----------------+---------------------+
3 rows in set (0.00 sec)

### Subtask 5

mysql> SELECT * from member WHERE username = "test";
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-29 17:09:09 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.00 sec)

### Subtask 6
mysql> SELECT * from member WHERE name LIKE "%es%";
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-29 17:09:09 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.00 sec)

### Subtask 7
mysql> SELECT * from member WHERE username = "test" AND password = "test";
+----+------+----------+----------+----------------+---------------------+
| id | name | username | password | follower_count | time                |
+----+------+----------+----------+----------------+---------------------+
|  1 | test | test     | test     |              0 | 2024-04-29 17:09:09 |
+----+------+----------+----------+----------------+---------------------+
1 row in set (0.00 sec)

### Subtask 8
mysql> UPDATE member
    -> SET name = "test2"
    -> WHERE username = "test";
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> SELECT * from member;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  1 | test2  | test     | test     |              0 | 2024-04-29 17:09:09 |
|  2 | red    | Red      | hongse   |              0 | 2024-04-29 17:10:00 |
|  3 | orange | Orange   | chengse  |              0 | 2024-04-29 17:10:39 |
|  4 | yellow | Yellow   | huangse  |              0 | 2024-04-29 17:11:15 |
|  5 | green  | Green    | lyuse    |              0 | 2024-04-29 17:11:38 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.00 sec)

<Screenshot here>