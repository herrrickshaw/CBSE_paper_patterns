---
title: "91 Computer Science"
source_pdf: "91_Computer Science.pdf"
source_url: ""
pages: 12
pdf_bytes: 1967532
pdf_sha256: "d23992c58aa8097ae36787663a2cb667ad68a82411b7bdd39d418974ef233393"
text_chars: 8996
low_text_pages: 1
converter: "macOS Vision OCR (accurate, en-US) @200dpi via ocr.swift"
ocr: true
ocr_note: "Devanagari NOT recognised - Vision has no Hindi model; the Hindi column of bilingual papers is noise"
---

# 91 Computer Science


---

## page 1

```
Series: %BAB%
SET-4
Q.P. Code
91
tri.
Roll No.
Candidates must write the Q.P. Code
on the title page of the answer-book.
Please check that this question paper contains 12 printed pages.
on the title page of the answer-book by the candidate.
Please check that this question paper contains 13 questions.
COMPUTER SCIENCE
Time allowed : 2 hours
aximum Marks : 35
91
318
Page 1
P.T.O.
```

---

## page 2

```
DRO
General Instructions :
(i) This question paper is divided into 3 Sections - A, B and C.
(ii) Section A, consists of 7 questions (1-7). Each question carries 2 marks.
(iii) Section B, consists of 3 questions (8-10). Each question carries
3 marks.
(iv) Section C, consists of 3 questions (11-13). Each question carries
4 marks.
(0) Internal choices have been given for question numbers - 7, 8 and 12.
SECTION - A
(Each question carries 2 marks)
"Stack is a linear data structure which follows a particular order in which
the operations are performed."
2
What is the order in which the operations are performed in a Stack?
Name the List method/function available in Python which is used to
remove the last element from a list implemented stack.
Also write an example using Python statements for removing the last
element of the list.
(i)
Expand the following:
1
VOIP, PPP
(ii) Riya wants to transfer pictures from her mobile phone to her laptop.
She uses Bluetooth technology to connect two devices. Which type of
network (PAN/LAN/MAN/WAN) will be formed in this case?
1
91
Page 2
```

---

## page 3

```
3.
Differentiate between the terms Attribute and Domain in the context of
Relational Data Model.
2
Consider the following SQL table MEMBER in a SQL Database CLUB :
2
Table : MEMBER
M ID
NAME
ACTIVITY
M1001
Amina
GYM
M1002
Pratik
GYM
M1003
Simon
SWIMMING
M1004
Rakesh
GYM
M1005
Avneet
SWIMMING
Assume that the required library for establishing the connection between
Python and MYSQL is already imported in the given Python code. Also
assume that DB is the name of the database connection for table
MEMBER stored in the database CLUB.
Predict the output of the following code :
MYCUR = DB.cursor ()
MYCUR. execute ("USE CLUB")
MYCUR. execute ("SELECT * FROM MEMBER WHERE ACTIVITY= 'GYM'
")
R=MYCUR. fetchone ()
for i in range (2) :
R=MYCUR. fetchone ()
print (R[0], R[1], sep = "#")
91
Page 3
P.T.O.
```

---

## page 4

```
5. Write the output of SQL queries (a) to (d) based on the table
VACCINATION_DATA given below :
2
TABLE : VACCINATION _DATA
VID
Name
Age
Dosel
Dose2
City
101
Jenny
27
2021-12-25
2022-01-31
Delhi
102
Harjot
55
2021-07-14
2021-10-14
Mumbai
103
Srikanth
43
2021-04-18
2021-07-20
Delhi
104
Gazala
75
2021-07-31
NULL
Kolkata
105
Shiksha
32
2022-01-01
NULL
Mumbai
(a) SELECT Name, Age FROM VACCINATION_DATA
WHERE Dose2 IS NOT NULL AND Age > 40;
(b) SELECT City, COUNT (*) FROM VACCINATION_DATA GROUP BY City;
(c) SELECT DISTINCT City FROM VACCINATION_DATA;
(d) SELECT MAX (Dosel), MIN (Dose2) FROM VACCINATION_DATA;
Write the output of SQL queries (a) and (b) based on the following two
tables DOCTOR and PATIENT belonging to the same database :
2
Table : DOCTOR
DNO
DNAME
FEES
D1
AMITABH
1500
D2
ANIKET
1000
D3
NIKHIL
1500
ANJANA
1500
91
Page 4
```

---

## page 5

```
Table: PATIENT
PNO
PNAME
ADMDATE
DNO
P1
NOOR
2021-12-25
D1
P2
ANNIE
2021-11-20
P3
PRAKASH
2020-12-10
NULL
P4
HARMEET
2019-12-20
D1
(a) SELECT DNAME, PNAME FROM DOCTOR
NATURAL JOIN PATIENT ;
(b) SELECT PNAME, ADMDATE, FEES
FROM PATIENT P, DOCTOR D
WHERE D.DNO = P. DNO AND FEES > 1000;
7.
Differentiate between Candidate Key and Primary Key in the context of
Relational Database Model.
2
OR
Consider the following table PLAYER :
Table : PLAYER
PNO
NAME
SCORE
P1
RISHABH
52
P2
HUSSAIN
45
P3
ARNOLD
23
P4
ARNAV
18
P5
GURSHARAN
42
91
Page 5
P.T.O.
```

---

## page 6

```
(a) Identify and write the name of the most appropriate column from the
given table PLAYER that can be used as a Primary key.
(b) Define the term Degree in relational data model. What is the Degree
of the given table PLAYER ?
SECTION - B
(Each question carries 3 marks)
8.
•
Write the definition of a user defined function PushNV (N) which
accepts a list of strings in the parameter N and pushes all strings
which have no vowels present in it, into a list named NoVowel.
3
Write a program in Python to input 5 words and push them one by
one into a list named A11.
The program should then use the function PushNV () to create a
stack of words in the list Novowel so that it stores only those words
which do not have any vowel present in it, from the list A11.
Thereafter, pop each word from the list Novowel and display the
popped word. When the stack is empty display the message
"EmptyStack".
For example :
If the Words accepted and pushed into the list All are
['DRY', 'LIKE'
'RHYTHM'
'WORK', 'GYM']
91
Page 6
```

---

## page 7

```
Then the stack Novowel should store
['DRY', 'RHYTHM', 'GYM']
And the output should be displayed as
GYM RHYTHM DRY EmptyStack
OR
Write the definition of a user defined function Push3_5 (N) which
accepts a list of integers in a parameter N and pushes all those
integers which are divisible by 3 or divisible by 5 from the list N
into a list named on1y3_5.
Write a program in Python to input 5 integers into a list named NUM.
The program should then use the function Push 3_5 () to create the
stack of the list Only3
_5. Thereafter pop each integer from the list
On1y3_
_5 and display the popped value. When the list is empty,
display the message "StackEmpty".
For example :
If the integers input into the list NUM are :
110, 6, 14, 18, 30]
Then the stack only3_5 should store
110, 6, 18, 30]
And the output should be displayed as
30 18 6 10 StackEmpty
91
Page 7
P.T.O.
```

---

## page 8

```
0R0
9.
(i) A SQL table ITEMS contains the following columns :
1
INO, INAME, QUANTITY, PRICE, DISCOUNI
Write the SQL command to remove the column DISCOUNT from the
table.
(ii) Categorize the following SQL commands into DDL and DML :
2
CREATE, UPDATE, INSERT, DROP
Rohan is learning to work upon Relational Database Management System
(RDBMS) application. Help him to perform following tasks :
3
(a) To open the database named "LIBRARY".
(b) To display the names of all the tables stored in the opened database.
(c) To display the structure of the table "BOOKS" existing in the already
opened database "LIBRARY".
SECTION - C
(Each question carries 4 marks)
11. Write SQL queries for (a) to (d) based on the tables PASSENGER and
FLIGHT given below :
4
Table :
PASSENGER
PNO
NAME
GENDER
ENO
1001
suresh
MALE
F101
1002
Anita
FEMALE
F104
1003
Harjas
MALE
F102
1004
Nita
FEMALE
F103
91
Page 8
```

---

## page 9

```
Table : FLIGHT
ENO
START
END
F_DATE
FARE
F101
MUMBAI
CHENNAI
2021-12-25
4500
F102
MUMBAI
BENGALURU
2021-11-20
4000
F103
DELHI
CHENNAI
2021-12-10
5500
F104
KOLKATA
MUMBAI
2021-12-20
4500
F105
DELHI
BENGALURU
2021-01-15
5000
(a) Write a query to change the fare to 6000 of the flight whose FNO is
F104.
(b) Write a query to display the total number of MALE and FEMALE
PASSENGERS.
(c) Write a query to display the NAME, corresponding FARE and F_DATE
of all PASSENGERS who have a flight to START from DELHI.
(d) Write a query to delete the records of flights which end at Mumbai.
12. (i) Differentiate between Bus Topology and Tree Topology. Also, write
one advantage of each of them.
2
OR
Differentiate between HTML and XML.
(ii) What is a web browser ? Write the names of any two commonly used
web browsers.
2
91
Page 9
P.T.O.
```

---

## page 10

```
20
13. Galaxy Provider Ltd. is planning to connect its office in Texas, USA with
its branch at Mumbai. The Mumbai branch has 3 Offices in three blocks
located at some distance from each other for different operations -
ADMIN, SALES and ACCOUNTS.
4
As a network consultant, you have to suggest the best network related
solutions for the issues/problems raised in (a) to (d), keeping in mind the
distances between various locations and other given parameters.
Layout of the Offices in the Mumbai branch :
Admin
Block
sales
Accounts
Block
Block
Shortest distances between various locations :
ADMIN Block to SALES Block
300 m
SALES Block to ACCOUNTS Block
175 m
ADMIN Block to ACCOUNTS Block
350 m
MUMBAI Branch to TEXAS Head Office
14000 km
91
Page 10
```

---

## page 11

```
Number of Computers installed at various locations are as follows :
ADMIN Block
255
ACCOUNTS Block
75
SALES Block
30
TEXAS Head Office
90
(a) It is observed that there is a huge data loss during the process of
data transfer from one block to another. Suggest the most
appropriate networking device out of the following, which needs to be
placed along the path of the wire connecting one block office with
another to refresh the signal and forward it ahead.
(i)
MODEM
(ii) ETHERNET CARD
(iii) REPEATER
(iv) HUB
(b)
Which hardware networking device out of the following, will you
suggest to connect all the computers within each block ?
(1)
SWITCH
(ii) MODEM
(111) REPEATER
(iv) ROUTER
(c)
Which service/protocol out of the following will be most helpful to
conduct live interactions of employees from Mumbai Branch and
their counterparts in Texas?
FTP
(ii) PPP
(iii) SMTP
(iv) VolP
(d)
Draw the cable layout (block to block) to efficiently connect the three
offices of the Mumbai branch.
91
Page 11
```

---

## page 12

```
91
318
Page 12
```