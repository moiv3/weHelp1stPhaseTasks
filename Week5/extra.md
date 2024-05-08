# Wehelp Week 5 Assignment Discussion

## Task 1


```SQL
Enter password: *************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 31
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
| website            |
+--------------------+
5 rows in set (0.01 sec)

mysql> use website;
Database changed
mysql> show tables
    -> ;
+---------------------+
| Tables_in_website   |
+---------------------+
| member              |
| membertest          |
| message             |
| randomdata          |
| randomdatalarge     |
| randomdatalarge300k |
+---------------------+
6 rows in set (0.00 sec)

mysql> SELECT * from member;
+----+--------+----------+----------+----------------+---------------------+
| id | name   | username | password | follower_count | time                |
+----+--------+----------+----------+----------------+---------------------+
|  1 | test2  | test     | test     |              5 | 2024-04-30 14:50:26 |
|  2 | Red    | red      | hongse   |             40 | 2024-04-30 14:52:14 |
|  3 | Orange | orange   | chengse  |            300 | 2024-04-30 14:52:27 |
|  4 | Yellow | yellow   | huangse  |           2000 | 2024-04-30 14:52:39 |
|  5 | Green  | green    | lyuse    |          10000 | 2024-04-30 14:52:52 |
+----+--------+----------+----------+----------------+---------------------+
5 rows in set (0.01 sec)

mysql> SELECT * from message;
+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
| id | member_id | content                                                                                                      | like_count | time                |
+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
|  1 |         1 | 我年紀還輕，閱歷不深的時候，                                                                                 |         10 | 2024-04-30 15:19:18 |
|  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。
                          |         20 | 2024-04-30 15:19:32 |
|  3 |         2 | 「每逢你想要批評任何人的時候，」他對我說，
                          |         30 | 2024-04-30 15:19:51 |
|  4 |         3 | 「你就記住，這個世界上所有的人，並不是個個都有過你擁有的那些優越條件。」
                          |         40 | 2024-04-30 15:20:02 |
|  5 |         1 | 他沒再說別的。
                          |         50 | 2024-04-30 15:20:14 |
|  6 |         5 | 但是，我們父子之間話雖不多，
                          |         60 | 2024-04-30 15:20:24 |
|  7 |         4 | 卻一向許多事情是特別會意的，因此我明白他的話大有弦外之音。
                          |         70 | 2024-04-30 15:20:35 |
|  8 |         4 | 久而久之，我就慣於對所有的人都保留判斷，
                          |         80 | 2024-04-30 15:20:55 |
|  9 |         3 | 這個習慣既使得許多有怪僻的人肯跟我講心裡話，
                          |         90 | 2024-04-30 15:20:59 |
| 10 |         1 | 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。
                          |        100 | 2024-04-30 15:21:10 |
+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
10 rows in set (0.01 sec)

mysql> create table reply(
    -> reply_id BIGINT AUTO_INCREMENT,
    -> post_id BIGINT NOT NULL,
    -> username VARCHAR(255) NOT NULL,
    -> time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -> message_text VARCHAR(255) NOT NULL,
    -> PRIMARY KEY reply_id;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 7
mysql> create table reply(
    -> reply_id BIGINT AUTO_INCREMENT,
    -> post_id BIGINT NOT NULL,
    -> username VARCHAR(255) NOT NULL,
    -> time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -> message_text VARCHAR(255) NOT NULL,
    -> PRIMARY KEY (reply_id);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 7
mysql> create table reply(
    -> reply_id BIGINT AUTO_INCREMENT,
    -> post_id BIGINT NOT NULL,
    -> username VARCHAR(255) NOT NULL,
    -> time DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    -> message_text VARCHAR(255) NOT NULL,
    -> PRIMARY KEY (reply_id)
    -> );
Query OK, 0 rows affected (0.07 sec)

mysql> SELECT * FROM reply;
Empty set (0.01 sec)

mysql> DESC reply;
+--------------+--------------+------+-----+-------------------+-------------------+
| Field        | Type         | Null | Key | Default           | Extra             |
+--------------+--------------+------+-----+-------------------+-------------------+
| reply_id     | bigint       | NO   | PRI | NULL              | auto_increment    |
| post_id      | bigint       | NO   |     | NULL              |                   |
| username     | varchar(255) | NO   |     | NULL              |                   |
| time         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| message_text | varchar(255) | NO   |     | NULL              |                   |
+--------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.01 sec)

mysql> ALTER TABLE message
    -> ADD FOREIGN KEY (post_id) REFERENCES message(id);

ERROR 1072 (42000): Key column 'post_id' doesnt exist in table

mysql> ALTER TABLE reply
    -> ADD FOREIGN KEY (post_id) REFERENCES message(id);
Query OK, 0 rows affected (0.12 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE reply
    -> ADD COLUMN member_id bigint notnull;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'notnull' at line 2
mysql> ALTER TABLE reply
    -> ADD COLUMN member_id bigint not null;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc reply;
+--------------+--------------+------+-----+-------------------+-------------------+
| Field        | Type         | Null | Key | Default           | Extra             |
+--------------+--------------+------+-----+-------------------+-------------------+
| reply_id     | bigint       | NO   | PRI | NULL              | auto_increment    |
| post_id      | bigint       | NO   | MUL | NULL              |                   |
| username     | varchar(255) | NO   |     | NULL              |                   |
| time         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| message_text | varchar(255) | NO   |     | NULL              |                   |
| member_id    | bigint       | NO   |     | NULL              |                   |
+--------------+--------------+------+-----+-------------------+-------------------+
6 rows in set (0.00 sec)

mysql> alter table reply
    -> drop table username;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'table username' at line 2
mysql> alter table reply
    -> drop column username;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc reply;
+--------------+--------------+------+-----+-------------------+-------------------+
| Field        | Type         | Null | Key | Default           | Extra             |
+--------------+--------------+------+-----+-------------------+-------------------+
| reply_id     | bigint       | NO   | PRI | NULL              | auto_increment    |
| post_id      | bigint       | NO   | MUL | NULL              |                   |
| time         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| message_text | varchar(255) | NO   |     | NULL              |                   |
| member_id    | bigint       | NO   |     | NULL              |                   |
+--------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)

mysql> alter table reply
    -> add foreign key (member_id) references member(id);
Query OK, 0 rows affected (0.09 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc reply;
+--------------+--------------+------+-----+-------------------+-------------------+
| Field        | Type         | Null | Key | Default           | Extra             |
+--------------+--------------+------+-----+-------------------+-------------------+
| reply_id     | bigint       | NO   | PRI | NULL              | auto_increment    |
| post_id      | bigint       | NO   | MUL | NULL              |                   |
| time         | datetime     | NO   |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
| message_text | varchar(255) | NO   |     | NULL              |                   |
| member_id    | bigint       | NO   | MUL | NULL              |                   |
+--------------+--------------+------+-----+-------------------+-------------------+
5 rows in set (0.00 sec)

mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(2,"HAHAHA",
    -> 3);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(2,"HAHAHA",4);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(2,"HAHAHAHO",5);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(3,"HEHEHE",3);
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * FROM reply;
+----------+---------+---------------------+--------------+-----------+
| reply_id | post_id | time                | message_text | member_id |
+----------+---------+---------------------+--------------+-----------+
|        1 |       2 | 2024-05-06 00:12:16 | HAHAHA       |         3 |
|        2 |       2 | 2024-05-06 00:12:27 | HAHAHA       |         4 |
|        3 |       2 | 2024-05-06 00:12:35 | HAHAHAHO     |         5 |
|        4 |       3 | 2024-05-06 00:12:52 | HEHEHE       |         3 |
+----------+---------+---------------------+--------------+-----------+
4 rows in set (0.00 sec)

mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymember, member.username AS postusername
    -> FROM reply
    -> JOIN member
    -> ON reply.member_id = member.id
    -> WHERE reply.member_id = 3;
+-----------+-------------+--------------+
| replytext | replymember | postusername |
+-----------+-------------+--------------+
| HAHAHA    |           3 | orange       |
| HEHEHE    |           3 | orange       |
+-----------+-------------+--------------+
2 rows in set (0.00 sec)

mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymemberid, member.username AS po
stusername, member.id AS postmemberid
    -> FROM reply
    -> JOIN member
    -> ON reply.member_id = member.id
    -> WHERE reply.member_id = 3;
+-----------+---------------+--------------+--------------+
| replytext | replymemberid | postusername | postmemberid |
+-----------+---------------+--------------+--------------+
| HAHAHA    |             3 | orange       |            3 |
| HEHEHE    |             3 | orange       |            3 |
+-----------+---------------+--------------+--------------+
2 rows in set (0.00 sec)

mysql> FROM reply
    -> JOIN message
    -> ON reply.messafge;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'FROM reply JOIN message
ON reply.messafge' at line 1
mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymemberid, member.username AS postusername, member.id AS postmemberid
    -> FROM reply
    -> JOIN message
    -> ON reply.post_id = message.id
    -> WHERE reply.member_id = 3;
ERROR 1054 (42S22): Unknown column 'member.username' in 'field list'
mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymemberid, member.username AS postusername, member.id AS postmemberid
    -> FROM reply
    -> JOIN message ON reply.post_id = message.id
    -> JOIN member ON message.member_id = member.id
    -> ;
+-----------+---------------+--------------+--------------+
| replytext | replymemberid | postusername | postmemberid |
+-----------+---------------+--------------+--------------+
| HAHAHA    |             3 | test         |            1 |
| HAHAHA    |             4 | test         |            1 |
| HAHAHAHO  |             5 | test         |            1 |
| HEHEHE    |             3 | red          |            2 |
+-----------+---------------+--------------+--------------+
4 rows in set (0.00 sec)

mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymemberid, message.id AS messageid, member.username AS postusername, member.id AS postmemberid
    -> FROM reply
    -> JOIN message ON reply.post_id = message.id
    -> JOIN member ON message.member_id = member.id
    -> ;
+-----------+---------------+-----------+--------------+--------------+
| replytext | replymemberid | messageid | postusername | postmemberid |
+-----------+---------------+-----------+--------------+--------------+
| HAHAHA    |             3 |         2 | test         |            1 |
| HAHAHA    |             4 |         2 | test         |            1 |
| HAHAHAHO  |             5 |         2 | test         |            1 |
| HEHEHE    |             3 |         3 | red          |            2 |
+-----------+---------------+-----------+--------------+--------------+
4 rows in set (0.00 sec)

mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(8,"EEEEEHEHEHE",5);
Query OK, 1 row affected (0.01 sec)

mysql> VALUES(8,"EEEEEHEHEHE6",6);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(8,"EEEEEHEHEHE6",6)' at line 1
mysql> VALUES(8,"EEEEEHEHEHE6",5);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(8,"EEEEEHEHEHE6",5)' at line 1
mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(8,"EEEEEHEHEHE6",6);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`website`.`reply`, CONSTRAINT `reply_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`))
mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(8,"EEEEEHEHEHE6",5);
Query OK, 1 row affected (0.01 sec)

mysql> VALUES(10,"NARCISSUSATOASISEEEEEHEHEHE6",1);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(10,"NARCISSUSATOASISEEEEEHEHEHE6",1)' at line 1
mysql> INSERT INTO reply(post_id, message_text, member_id)
    -> VALUES(10,"NARCISSUSATOASISEEEEEHEHEHE6",1);
Query OK, 1 row affected (0.02 sec)

mysql> SELECT * from JOIN message ON reply.post_id = message.id
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'JOIN message ON reply.post_id = message.id' at line 1
mysql> SELECT * from (JOIN message ON reply.post_id = message.id AS YO);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'JOIN message ON reply.post_id = message.id AS YO)' at line 1
mysql> SELECT * from reply JOIN message ON reply.post_id = message.id;
+----------+---------+---------------------+------------------------------+-----------+----+-----------+--------------------------------------------------------------------+------------+---------------------+
| reply_id | post_id | time                | message_text                 | member_id | id | member_id | content                                                            | like_count | time
   |
+----------+---------+---------------------+------------------------------+-----------+----+-----------+--------------------------------------------------------------------+------------+---------------------+
|        1 |       2 | 2024-05-06 00:12:16 | HAHAHA                       |         3 |  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                           |         20 | 2024-04-30 15:19:32 |
|        2 |       2 | 2024-05-06 00:12:27 | HAHAHA                       |         4 |  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                           |         20 | 2024-04-30 15:19:32 |
|        3 |       2 | 2024-05-06 00:12:35 | HAHAHAHO                     |         5 |  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                           |         20 | 2024-04-30 15:19:32 |
|        4 |       3 | 2024-05-06 00:12:52 | HEHEHE                       |         3 |  3 |         2 | 「每逢你想要批評任何人的時候，」他對我說，                         |         30 | 2024-04-30 15:19:51 |
|        5 |       8 | 2024-05-06 00:25:57 | EEEEEHEHEHE                  |         5 |  8 |         4 | 久而久之，我就慣於對所有的人都保留判斷，                           |         80 | 2024-04-30 15:20:55 |
|        7 |       8 | 2024-05-06 00:26:25 | EEEEEHEHEHE6                 |         5 |  8 |         4 | 久而久之，我就慣於對所有的人都保留判斷，                           |         80 | 2024-04-30 15:20:55 |
|        8 |      10 | 2024-05-06 00:26:48 | NARCISSUSATOASISEEEEEHEHEHE6 |         1 | 10 |         1 | 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。                       |        100 | 2024-04-30 15:21:10 |
+----------+---------+---------------------+------------------------------+-----------+----+-----------+--------------------------------------------------------------------+------------+---------------------+
7 rows in set (0.00 sec)
       SELECT * from reply RIGHT JOIN message ON reply.post_id = message.id;
+----------+---------+---------------------+------------------------------+-----------+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
| reply_id | post_id | time                | message_text                 | member_id | id | member_id | content                                                                                                      | like_count | time                |
+----------+---------+---------------------+------------------------------+-----------+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
|     NULL |    NULL | NULL                | NULL                         |      NULL |  1 |         1 | 我年紀還輕，閱歷不深的時候，                                                                                 |         10 | 2024-04-30 15:19:18 |
|        1 |       2 | 2024-05-06 00:12:16 | HAHAHA                       |         3 |  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                                                                     |         20 | 2024-04-30 15:19:32 |
|        2 |       2 | 2024-05-06 00:12:27 | HAHAHA                       |         4 |  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                                                                     |         20 | 2024-04-30 15:19:32 |
|        3 |       2 | 2024-05-06 00:12:35 | HAHAHAHO                     |         5 |  2 |         1 | 我父親教導過我一句話，我至今還念念不忘。                                                                     |         20 | 2024-04-30 15:19:32 |
|        4 |       3 | 2024-05-06 00:12:52 | HEHEHE                       |         3 |  3 |         2 | 「每逢你想要批評任何人的時候，」他對我說，                                                                   |         30 | 2024-04-30 15:19:51 |
|     NULL |    NULL | NULL                | NULL                         |      NULL |  4 |         3 | 「你就記住，這個世界上所有的人，並不是個個都有過你擁有的那些優越條件。」                                     |         40 | 2024-04-30 15:20:02 |
|     NULL |    NULL | NULL                | NULL                         |      NULL |  5 |         1 | 他沒再說別的。                                                                                               |         50 | 2024-04-30 15:20:14 |
|     NULL |    NULL | NULL                | NULL                         |      NULL |  6 |         5 | 但是，我們父子之間話雖不多，                                                                                 |         60 | 2024-04-30 15:20:24 |
|     NULL |    NULL | NULL                | NULL                         |      NULL |  7 |         4 | 卻一向許多事情是特別會意的，因此我明白他的話大有弦外之音。                                                   |         70 | 2024-04-30 15:20:35 |
|        5 |       8 | 2024-05-06 00:25:57 | EEEEEHEHEHE                  |         5 |  8 |         4 | 久而久之，我就慣於對所有的人都保留判斷，
     |         80 | 2024-04-30 15:20:55 |
|        7 |       8 | 2024-05-06 00:26:25 | EEEEEHEHEHE6                 |         5 |  8 |         4 | 久而久之，我就慣於對所有的人都保留判斷，
     |         80 | 2024-04-30 15:20:55 |
|     NULL |    NULL | NULL                | NULL                         |      NULL |  9 |         3 | 這個習慣既使得許多有怪僻的人肯跟我講心裡話，
     |         90 | 2024-04-30 15:20:59 |
|        8 |      10 | 2024-05-06 00:26:48 | NARCISSUSATOASISEEEEEHEHEHE6 |         1 | 10 |         1 | 也使我成為不少愛嘮叨的惹人厭煩的人的受害者。
     |        100 | 2024-04-30 15:21:10 |
+----------+---------+---------------------+------------------------------+-----------+----+-----------+--------------------------------------------------------------------------------------------------------------+------------+---------------------+
13 rows in set (0.00 sec)

mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymemberid, message.id AS messageid, member.username AS postusername, member.id AS postmemberid
    -> FROM reply
    -> JOIN message ON reply.post_id = message.id
    -> JOIN member ON message.member_id = member.id
    -> WHERE message.id = 1;
Empty set (0.00 sec)

mysql> SELECT reply.message_text AS replytext, reply.member_id AS replymemberid, message.id AS messageid, member.username AS postusername, member.id AS postmemberid
    -> FROM reply
    -> JOIN message ON reply.post_id = message.id
    -> JOIN member ON message.member_id = member.id
    -> WHERE message.id = 8;
+--------------+---------------+-----------+--------------+--------------+
| replytext    | replymemberid | messageid | postusername | postmemberid |
+--------------+---------------+-----------+--------------+--------------+
| EEEEEHEHEHE  |             5 |         8 | yellow       |            4 |
| EEEEEHEHEHE6 |             5 |         8 | yellow       |            4 |
+--------------+---------------+-----------+--------------+--------------+
2 rows in set (0.00 sec)
```

## Task 2

```SQL
mysql> create table tags
    -> tag_id bigint auto_increment;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'tag_id bigint auto_increment' at line 2
mysql> create table tags
    -> tag_id bigint auto_increment,
    -> tag_name varchar(255) not null;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'tag_id bigint auto_increment,
tag_name varchar(255) not null' at line 2
mysql> create table tags(
    -> tag_id bigint auto_increment,
    -> tag_name varchar(255) not null,
    -> primary key(tag_id)
    -> );
Query OK, 0 rows affected (0.06 sec)

mysql> desc tags;
+----------+--------------+------+-----+---------+----------------+
| Field    | Type         | Null | Key | Default | Extra          |
+----------+--------------+------+-----+---------+----------------+
| tag_id   | bigint       | NO   | PRI | NULL    | auto_increment |
| tag_name | varchar(255) | NO   |     | NULL    |                |
+----------+--------------+------+-----+---------+----------------+
2 rows in set (0.01 sec)

mysql> insert into tags (tag_name) values (tag1);
ERROR 1054 (42S22): Unknown column 'tag1' in 'field list'
mysql> insert into tags (tag_name) values ("tag1");
Query OK, 1 row affected (0.01 sec)

mysql> insert into tags (tag_name) values ("tag2");
Query OK, 1 row affected (0.01 sec)

mysql> insert into tags (tag_name) values ("tag3");
Query OK, 1 row affected (0.01 sec)

mysql> insert into tags (tag_name) values ("tag4");
Query OK, 1 row affected (0.01 sec)

mysql> select * from tags;
+--------+----------+
| tag_id | tag_name |
+--------+----------+
|      1 | tag1     |
|      2 | tag2     |
|      3 | tag3     |
|      4 | tag4     |
+--------+----------+
4 rows in set (0.00 sec)

mysql> create table replytags(
    -> entry_id bigint auto increment,
    -> reply_id bigint not null,
    -> tag_id bigint not null);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'auto increment,
reply_id bigint not null,
tag_id bigint not null)' at line 2
mysql> create table replytags(
    -> entry_id bigint auto_increment,
    -> reply_id bigint not null,
    -> tag_id bigint not null);
ERROR 1075 (42000): Incorrect table definition; there can be only one auto column and it must be defined as a key
mysql> create table replytags(
    -> entry_id bigint auto increment,
    -> reply_id bigint not null,
    -> tag_id bigint not null,
    -> primary key(entry_id);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'auto increment,
reply_id bigint not null,
tag_id bigint not null,
primary key(en' at line 2
mysql> create table replytags(
    -> entry_id bigint auto increment,
    -> reply_id bigint not null,
    -> tag_id bigint not null,
    -> primary key(entry_id)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'auto increment,
reply_id bigint not null,
tag_id bigint not null,
primary key(en' at line 2
mysql> create table replytags(
    -> entry_id bigint auto_increment,
    -> reply_id bigint not null,
    -> tag_id bigint not null,
    -> primary key(entry_id)
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> alter table replytags
    -> add foreign key (reply_id) references reply.reply_id;
ERROR 1239 (42000): Incorrect foreign key definition for 'foreign key without name': Key reference and table reference dont match
mysql> alter table replytags
    -> add foreign key (reply_id) references reply(reply_id);
Query OK, 0 rows affected (0.11 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> alter table replytags
    -> add foreign key (tag_id) references tags(tag_id);
Query OK, 0 rows affected (0.10 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> insert into replytags(reply_id, tag_id)
    -> values(1,2);
Query OK, 1 row affected (0.01 sec)

mysql> values(1,3);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(1,3)' at line 1
mysql> insert into replytags(reply_id, tag_id) values(1,3);
Query OK, 1 row affected (0.01 sec)

mysql> insert into replytags(reply_id, tag_id) values(1,4);
Query OK, 1 row affected (0.00 sec)

mysql> insert into replytags(reply_id, tag_id) values(1,1);
Query OK, 1 row affected (0.00 sec)

mysql> insert into replytags(reply_id, tag_id) values(2,2);
Query OK, 1 row affected (0.01 sec)

mysql> insert into replytags(reply_id, tag_id) values(3,3);
Query OK, 1 row affected (0.01 sec)

mysql> insert into replytags(reply_id, tag_id) values(3,4);
Query OK, 1 row affected (0.01 sec)

mysql> select * from reply;
+----------+---------+---------------------+------------------------------+-----------+
| reply_id | post_id | time                | message_text                 | member_id |
+----------+---------+---------------------+------------------------------+-----------+
|        1 |       2 | 2024-05-06 00:12:16 | HAHAHA                       |         3 |
|        2 |       2 | 2024-05-06 00:12:27 | HAHAHA                       |         4 |
|        3 |       2 | 2024-05-06 00:12:35 | HAHAHAHO                     |         5 |
|        4 |       3 | 2024-05-06 00:12:52 | HEHEHE                       |         3 |
|        5 |       8 | 2024-05-06 00:25:57 | EEEEEHEHEHE                  |         5 |
|        7 |       8 | 2024-05-06 00:26:25 | EEEEEHEHEHE6                 |         5 |
|        8 |      10 | 2024-05-06 00:26:48 | NARCISSUSATOASISEEEEEHEHEHE6 |         1 |
+----------+---------+---------------------+------------------------------+-----------+
7 rows in set (0.00 sec)

mysql> insert into replytags(reply_id, tag_id) values(5,4);
Query OK, 1 row affected (0.01 sec)

mysql> insert into replytags(reply_id, tag_id) values(6,4);
ERROR 1452 (23000): Cannot add or update a child row: a foreign key constraint fails (`website`.`replytags`, CONSTRAINT `replytags_ibfk_1` FOREIGN KEY (`reply_id`) REFERENCES `reply` (`reply_id`))
mysql> insert into replytags(reply_id, tag_id) values(7,4);
Query OK, 1 row affected (0.01 sec)

mysql> insert into replytags(reply_id, tag_id) values(8,4);
Query OK, 1 row affected (0.01 sec)

mysql> SELECT reply.message_text, tags.tag_name FROM reply
    -> JOIN replytags on reply.post_id = replytags.reply_id
    -> JOIN tags ON replytags.tag_id = tags.tag_id;
+--------------+----------+
| message_text | tag_name |
+--------------+----------+
| HAHAHA       | tag2     |
| HAHAHA       | tag2     |
| HAHAHAHO     | tag2     |
| HEHEHE       | tag4     |
| HEHEHE       | tag3     |
| EEEEEHEHEHE  | tag4     |
| EEEEEHEHEHE6 | tag4     |
+--------------+----------+
7 rows in set (0.03 sec)

mysql> SELECT reply.post_id, reply.message_text, tags.tag_name FROM reply
    -> RIGHT JOIN replytags on reply.post_id = replytags.reply_id
    -> RIGHT JOIN tags ON replytags.tag_id = tags.tag_id;
+---------+--------------+----------+
| post_id | message_text | tag_name |
+---------+--------------+----------+
|    NULL | NULL         | tag1     |
|    NULL | NULL         | tag2     |
|       2 | HAHAHA       | tag2     |
|       2 | HAHAHA       | tag2     |
|       2 | HAHAHAHO     | tag2     |
|    NULL | NULL         | tag3     |
|       3 | HEHEHE       | tag3     |
|    NULL | NULL         | tag4     |
|       3 | HEHEHE       | tag4     |
|    NULL | NULL         | tag4     |
|    NULL | NULL         | tag4     |
|       8 | EEEEEHEHEHE  | tag4     |
|       8 | EEEEEHEHEHE6 | tag4     |
+---------+--------------+----------+
13 rows in set (0.00 sec)

mysql> SELECT reply.reply_id, reply.post_id, reply.message_text, tags.tag_name FROM reply
    -> RIGHT JOIN replytags on reply.post_id = replytags.reply_id
    -> RIGHT JOIN tags ON replytags.tag_id = tags.tag_id;
+----------+---------+--------------+----------+
| reply_id | post_id | message_text | tag_name |
+----------+---------+--------------+----------+
|     NULL |    NULL | NULL         | tag1     |
|     NULL |    NULL | NULL         | tag2     |
|        1 |       2 | HAHAHA       | tag2     |
|        2 |       2 | HAHAHA       | tag2     |
|        3 |       2 | HAHAHAHO     | tag2     |
|     NULL |    NULL | NULL         | tag3     |
|        4 |       3 | HEHEHE       | tag3     |
|     NULL |    NULL | NULL         | tag4     |
|        4 |       3 | HEHEHE       | tag4     |
|     NULL |    NULL | NULL         | tag4     |
|     NULL |    NULL | NULL         | tag4     |
|        5 |       8 | EEEEEHEHEHE  | tag4     |
|        7 |       8 | EEEEEHEHEHE6 | tag4     |
+----------+---------+--------------+----------+
13 rows in set (0.00 sec)

mysql> SELECT reply.post_id, reply.message_text, tags.tag_name FROM reply
    -> LEFT JOIN replytags on reply.post_id = replytags.reply_id
    -> JOIN tags ON replytags.tag_id = tags.tag_id;
+---------+--------------+----------+
| post_id | message_text | tag_name |
+---------+--------------+----------+
|       2 | HAHAHA       | tag2     |
|       2 | HAHAHA       | tag2     |
|       2 | HAHAHAHO     | tag2     |
|       3 | HEHEHE       | tag4     |
|       3 | HEHEHE       | tag3     |
|       8 | EEEEEHEHEHE  | tag4     |
|       8 | EEEEEHEHEHE6 | tag4     |
+---------+--------------+----------+
7 rows in set (0.00 sec)
```