---
title: "90 Informatics Practices"
source_pdf: "90_Informatics Practices.pdf"
source_url: ""
pages: 8
pdf_bytes: 1778230
pdf_sha256: "7ba2b79bfc2564d0c69b61c0c8d06003379e5e9eea6f9ac1c75ad10ab958d2c0"
text_chars: 7126
low_text_pages: 1
converter: "macOS Vision OCR (accurate, en-US) @200dpi via ocr.swift"
ocr: true
ocr_note: "Devanagari NOT recognised - Vision has no Hindi model; the Hindi column of bilingual papers is noise"
---

# 90 Informatics Practices


---

## page 1

```
Series: %BAB%
SET-4
Q.P. Code
90
tri.
Roll No.
Candidates must write the Q.P. Code
on the title page of the answer-book.
Please check that this question paper contains 8 printed pages.
on the title page of the answer-book by the candidate.
Please check that this question paper contains 13 questions.
INFORMATICS PRACTICES
Time allowed: 2 hours
Махітит Marks : 35
90
317
Page 1
P.T.O.
```

---

## page 2

```
General Instructions:
(i) This question paper is divided into 3 Sections - A, B and C.
(ii) Section A, consists 7 questions (1-7). Each question carries 2 marks.
(iii) Section
B, consists 3 questions (8-10). Each question carries
3 marks.
*
(iv) Section
C, consists
3 questions (11-13). Each question carries
4 marks.
(v) Internal choices have been given for question numbers - 1, 3, 7, 8 and 12.
SECTION - A
(Each question carries 2 marks)
Rushil thought "WWW" and "Internet" are synonyms ie., they meant
same and can be used interchangeably. But the teacher said that they are
not same. Help him to understand the meaning of both the terms with the
help of a suitable example of each.
2
OR
What are Cookies? How can we disable Cookies ?
(1)
What is the function of a Gateway?
1
(ii) Give examples of any two plug-ins.
1
3.
Find the output of the following SQL Queries :
2
(i) SELECT ROUND (7658.345,2);
(ii) SELECT MOD(ROUND (13.9,0),3);
OR
Give any two differences between the POWER ) and SUM( ) SQL
functions.
4.
Give one advantage and disadvantage each of Bus and Star topology.
2
Find the output of the following SQL queries:
2
(i) SELECT SUBSTR"FIT INDIA MOVEMENT", 5);
(ii) SELECT INSTR("ARTIFICIAL INTELLIGENCE", "IA");
90
Page 2
```

---

## page 3

```
6. Srikanth created the following table STUDENT in his database.
2
Table: STUDENT
RollNo
Name
Class
Marks
1
Ritikar
12
40
2
Angad
12
35
3
Kaveri
11
42
4
Lalitha
12
21
5
Daniel
11
44
6
Rabindra
11
39
Rabia
11
28
He now wants to count number of students in each class where the
number of students is more than 3. He has executed the following query :
SELECT MAX (Marks) FROM STUDENT WHERE COUNT (*) >3 GROUP BY
Class;
But, he got an error. Identify the error(s) and rewrite the query. Also
underline the correction(s) done.
7.
Ms. Mohini is working in a school and stores the details of all students in
a table SCHOOLDATA.
2
TABLE: SCHOOLDATA
Admno
Name
ClassR
House Percent
Gender
Dob
20150001
Aditya Das
10
Green
86
Male
2006-02-20
20140212
Harsh Sharma
11
Red
75
Male
2004-10-05
20090234
Swapnil Pant
10
Yellow
84
Female
2005-11-21
20130216
Soumen Rao
9
Red
91
Male
2006-04-10
20190227
Rahil Arora
10
Blue
70
Male
2005-05-14
20120200
Akasha Singh
11
Red
64
Female
2004-12-16
Write SQL statements from the above given table to :
(i)
To remove leading spaces from the column Name.
(i) Display the names of students who were born on Sunday.
OR
90
Page 3
P.T.O.
```

---

## page 4

```
Predict the output of the following SQL queries from the given table :
SCHOOLDATA
(i) SELECT MAX(Percent) FROM SCHOOLDATA;
(ii) SELECT LEFT(Gender,1),Name FROM SCHOOLDATA WHERE YEAR
(Dob) =2005;
SECTION - B
(Each question carries 3 marks)
Predict the output of the following SQL queries :
3
(i) SELECT TRIM(" ALL THE BEST ");
(ii) SELECT POWER(5,2);
(iii) SELECT UPPER (MID("start up india",10));
OR
Consider a table "MYPET" with the following data :
Table : MYPET
Pet_id
Pet_Name
Breed
LifeSpan Price Discount
101
Rocky
Labrador Retriever
12
16000
5
202
Duke
German Shepherd
13
22000
10
303
Oliver
Bulldog
10
18000
7
404
Cooper
Yorkshire Terrier
16
20000
12
505
Oscar
Shih Tzu
NULL
25000
8
Write SQL queries for the following :
(i) Display the Breed of all the pets in uppercase.
(I1) Display the total price of all the pets.
(iii) Display the average life span of all the pets.
9.
Write the names of SQL functions to perform the following operations :
3
(i) Display name of the Month from your date of birth.
(ii) Convert email-id to lowercase.
(iii) Count the number of characters in your name.
90
Page 4
```

---

## page 5

```
10. Consider the following table : PRODUCT
3
Table: PRODUCT
PID
PNAME
PRICE
QUANTITY
P1001
Eraser
10.50
5
P1002
Ball Pen
15.00
2
P1003
Gel Pen
25.10
3
P1004
Ruler
5.00
1
Find the output of the following SQL queries :
(i) SELECT 10+MOD(QUANTITY,3) FROM PRODUCT WHERE PNAME =
"Eraser";
(ii) SELECT ROUND(PRICE,2)*QUANTITY FROM PRODUCT WHERE
QUANTITY > 2;
(iii) SELECT UCASE(RIGHI(PNAME,2)) FROM PRODUCT;
SECTION - C
(Each question carries 4 marks)
11. Consider the table : ITEM
4
Table : ITEM
SNo
Itemname
Type
Price
Stockdate
1
Chaises
Living
11500.58
2020-02-19
2
Accent Chairs
Living
31000.67
2021-02-15
Baker Racks
Kitchen
25000.623
2019-01-01
Sofa
Living
7000.3
2020-10-18
5
Nightstand
Bedroom
NULL
2021-07-23
Write SQL queries for the following :
(i)
Display all the records in descending order of Stockdate.
(ii) Display the Type and total number of items of each Type.
(iii) Display the least Price.
(iv) Display the Itemname with their price rounded to 1 decimal place.
90
Page 5
P.T.O.
```

---

## page 6

```
12. Consider the following table :
Table: SALESMAN
Scode
Sname
Area
Qtysold
Dateofjoin
S001
Ravi
North
120
2015-10-01
S002
Sandeep
South
105
2012-08-01
S003
Sunil
NULL
68
2018-02-01
S004
Subh
West
280
2010-04-01
S005
Ankit
East
90
2018-10-01
S006
Raman
NorthR
NULL
2019-12-01
Predict the output for the following SQL queries:
(i)
SELECT MAX(Qtysold), MIN(Qtysold) FROM SALESMAN;
(11)
SELECT COUNT (Area FROM SALESMAN;
(iii)
SELECT LENGTH (Sname) FROM SALESMAN WHERE
MONTH(Dateofjoin)=10;
(iv) SELECT Sname FROM SALESMAN WHERE RIGHT (Scode, 1)=5;
OR
Based on the given table SALESMAN write SQL queries to perform the
following operations :
(i) Count the total number of salesman.
(ii) Display the maximum qtysold from each area.
(iii)
Display the average qtysold from each area where number of
salesman is more than 1.
(iv) Display all the records in ascending order of area.
ABC International School, Delhi has different wings Administrative Wing
(W1), Primary Wing (W2), Middle Wing(W3) and Secondary Wing(W4) as
shown in the diagram :
4
ADMINISTRATIVE,
PRIMARY /
WING (W1)
WING (W2)
MUMBAI
BRANCH
MIDDLE
SECONDARY
WING (W3),
WING (W4)
The school also has a branch in Mumbai. The school management wants
to connect all the wings as well as all the computers of each wing
(W1, W2, W3, W4).
90
Page 6
```

---

## page 7

```
Distance between the wings are as follows:
W3 to W1
85 m
W1 to W2
40 m
W2 to W4
25 m
W4 to W3
120 m
W3 to W2
150 m
W1 to W4
170 m
Number of computers in each of the wing :
W1
125
W2
40
W3
42
W4
60
Based on the above specifications, answer the following questions :
(i)
Suggest the topology and draw the most suitable cable layout for
connecting all the wings of Delhi branch.
(ii) Suggest the kind of network required (out of LAN, MAN, WAN) for
connecting
(a) Administrative Wing (W1) with Middle Wing (W3)
(b) Administrative Wing (W1) with the Mumbai branch.
(iii) Suggest the placement of the following devices with justification :
(a) Repeater
(b) Switch/Hub
(iv) Due to pandemic school had to adopt Online classes. Suggest the
protocol that is used for sending the voice signals over internet. Also,
give an example of an application of WWW that helped the teachers
to send messages instantly to the students.
90
Page 7
```

---

## page 8

```
0.6
90
317
Page 8
```