---
title: "90 INFORMATIC PRACTICES"
source_pdf: "90 INFORMATIC PRACTICES.pdf"
source_url: ""
pages: 8
pdf_bytes: 442298
pdf_sha256: "397ee0b6856c9d554a12dd17be36052e4ebccf5625f76f82105e08191bcc5a85"
text_chars: 12485
low_text_pages: 0
converter: "pdftotext -layout"
---

# 90 INFORMATIC PRACTICES


---

## page 1

```
                                                                             SET-4
Series %BAB%/C
                                                                    Q.P. Code
                                                                                  90

Roll No.                                         Candidates must write the Q.P. Code on
                                                 the title page of the answer-book.




     Please check that this question paper contains 8 printed pages.
     Q.P. Code given on the right hand side of the question paper should be written
     on the title page of the answer-book by the candidate.
     Please check that this question paper contains 13 questions.
     Please write down the serial number of the question in the
     answer-book before attempting it.
     15 minute time has been allotted to read this question paper. The question
     paper will be distributed at 10.15 a.m. From 10.15 a.m. to 10.30 a.m., the
     students will read the question paper only and will not write any answer on
     the answer-book during this period.




             INFORMATICS PRACTICES


Time allowed : 2 hours                                         Maximum Marks : 35



90                                     Page 1                                   P.T.O.
```

---

## page 2

```
General Instructions :
(i)   This question paper is divided into 3 sections   A, B and C.
(ii) Section A, consists of 7 questions (1    7). Each question carries 2 marks.
(iii) Section B, consists of 3 questions (8   10). Each question carries 3 marks.
(iv) Section C, consists of 3 questions (11    13). Each question carries 4 marks.
(v)   Internal choices have been given for questions number 1, 3, 7, 8 and 12.

                                      SECTION A
                          (Each question carries 2 marks)

1.    (a)   Arshiya is a web developer and one of her clients wants her to
            design a web page to accept donations for an NGO. Which type of
            web page (static/dynamic) will she create ?                              2
                                        OR
      (b)   Danny has created a website on Python resources on his laptop.
            Now, he wants that others should be able to access his website and
            use the resources. What should he do to achieve his objective ?          2

2.    (a)   Define a web browser.                                                    1
      (b)   Give examples of any two network devices.                                1

3.    (a)   Find the output of the following SQL queries :                           2
            (i)    SELECT ROUND(21.341, 2);
            (ii)   SELECT MOD(10, 3);
                                   OR
      (b)   Give any two differences between MOD() and AVG() functions in
            SQL.                                                                     2

4.    Define the following terms :                                                   2
      (a)   Plug-ins
      (b)   Add-ons

5.    Find the output of the following SQL queries :                                 2
      (a)   SELECT MID("YOUNG INDIA",5);
      (b)   SELECT INSTR("MACHINE INTELLIGENCE","IN");

90                                       Page 2
```

---

## page 3

```
6.   Harjat has created the table EMP in his database.
     Table : EMP
       E_Id      Name           Dept             Comm
       E001      Ditya          Admin            35000
       E002      Uzair          Production       42500
       E003      Rajnikant      Admin            21000
       E004      Moushami       Sales            23575
       E005      Samantha       Sales            37000
       E006      Sunder         Admin            43000
     Now he wants to find the sum of commission earned by each department.
     He has executed the following query :
     SELECT dept,sum(comm)
     GROUP BY dept
     FROM EMP;
     But, he got an error. Rewrite the correct query after identifying the
     error(s).                                                                   2

7.   (a)   Ms. Anubha is working in a school and stores the details of all
           students in a Table : SCHOOL
                                Table : SCHOOL
      Admid       Sname            Grade    House    Per   Gender   Dob
      20150001    Aditya Das       10       Green    86    Male     2006-02-20
      20140212    Harsh Sharma     11       Red      50    Male     2004-10-05
      20090234    Swapnil Pant     10       Yellow   84    Female   2005-11-21
      20130216    Soumen Rao       9        Red      90    Male     2006-04-10
      20190227    Rahil Arora      10       Blue     70    Male     2005-05-14
      20120200    Akasha Singh     11       Red      70    Female   2004-12-16

     Write the SQL statements from the given table to :                          2
           (i)   Remove TRAILING SPACES from column Sname.
           (ii)  Display the names of students who were born on Tuesday.
                                          OR
     (b)   Predict the output of the following SQL queries from the above
           Table : SCHOOL :                                                      2
           (i)   SELECT AVG(Per) FROM SCHOOL WHERE House="Red";
           (ii)  SELECT Sname, Per FROM SCHOOL WHERE MONTH(Dob)=11;

90                                    Page 3                              P.T.O.
```

---

## page 4

```
                                       SECTION B
                             (Each question carries 3 marks)


8.   (a)     Predict the output of the following SQL queries :                        3

             (i)     SELECT LENGTH("GOOD LUCK");

             (ii)    SELECT POWER(3, 3);

             (iii)   SELECT UPPER("examination");

                              OR

     (b)     Consider a Table "PETDATA" with the following data :

                                     Table : PETDATA
       Id          Pname     Breed                      LifeSpan   Price   Discount
       101         Adi       Golden Retriever           15         16000   5
       202         Candy     Boxer                      11         22000   10
       303         Dazzler   Bulldog                    10         18000   NULL
       404         Cooper    Yorkshire Terrier          16         20000   12
       505         Akira     Pug                        NULL       25000   8

     Write SQL queries for the following :                                            3

     (i)     Display all the pet names in uppercase.

     (ii)    Display the total price of all the pets.

     (iii)   Display the average discount available on all the pets.


9.   Write the names of SQL functions to perform the following operations :           3

     (a)     Display the name of the month from the given date value.

     (b)     Display the day of month from the given date value.

     (c)     Count the number of characters in a given string.

90                                         Page 4
```

---

## page 5

```
10. Consider the following Table : ITEM :

                             Table : ITEM
       ID          INAME                   PRICE           QTY
       P1001       Sketch Pen              20.50           5
       P1002       Roller Ball Pen         55.00           1
       P1003       Gel Pen                 25.10           3
       P1004       Notebook                75.80           1

     Find the output of the following SQL queries :                                   3
     (a)    SELECT 10+ QTY FROM ITEM WHERE ID = "P1003";

     (b)    SELECT PRICE*QTY FROM ITEM WHERE QTY < 2;

     (c)    SELECT LEFT(INAME,3) FROM ITEM;


                                     SECTION C
                         (Each question carries 4 marks)

11. Consider the Table FURNITURE with the following data :

                                Table : FURNITURE
      S.No.    Item                Type           Price              Stockdate
      1        Hammock             Bedroom        35500.58           2020-04-21
      2        Divan               Living         31000              2019-03-18
      3        Bookshelf           Study          38000.657          2019-01-10
      4        Writing Desk        Living         61357.425          2020-10-18
      5        Nightstand          Bedroom        NULL               2021-07-23

     Write SQL queries for the following :                                            4

     (a)    Display all the records in alphabetical order of Item.
     (b)    Display the Type and total number of items of each Type.

     (c)    Display the highest Price.
     (d)    Display the Item with their price rounded to 1 decimal place.

90                                       Page 5                                   P.T.O.
```

---

## page 6

```
12. (a)    Consider the following table :

                                    Table : EMPLOYEE

      Ecode        Ename         Area       Salary     Dept               Doj
      S001         Ramesh        North      12000      Sales              2015-12-01
      S002         Rohit         South      10500      Finance            2012-08-01
      S003         Sunil         South      6800       Front Office       2018-02-01
      S004         Sambhav       West       28000      Back Office        2010-04-01
      S005         Ankit         East       9000       NULL               2018-10-01
      S006         Rishu         North      25000      Finance            2019-02-01


     Predict the output for the following SQL queries :                                4

           (i)     SELECT MAX(Salary), FROM EMPLOYEE;

           (ii)    SELECT COUNT(Dept) FROM EMPLOYEE;

           (iii)   SELECT UCASE(Ename) FROM EMPLOYEE WHERE MONTH(Doj)=2;

           (iv)    SELECT Ename FROM EMPLOYEE WHERE Right(Ecode,1)=5;


                                             OR

     (b)   Based on the given table EMPLOYEE write SQL queries to perform
           the following operations :                                                  4

           (i)     Count the total number of employees.

           (ii)    Display the minimum salary from each area.

           (iii)   Display the average salary from each department where number
                   of employees is more than 1.

           (iv)    Display all the records in descending order of date of joining.


90                                          Page 6
```

---

## page 7

```
13. ABC Private Ltd., Bangalore has different divisions, Finance (A1),
     Sales (A2), Production (A3) and Marketing (A4).

     The layout of the Bangalore branch is :

           FINANCE                          SALES
             (A1)                            (A2)

                                                                    SHIMLA
                                                                    BRANCH
           PRODUCTION                     MARKETING
              (A3)                           (A4)

     The company also has a branch in Shimla. The management wants to
     connect all the divisions as well as all the computers of each division (A1,
     A2, A3, A4).

     Distance between the branches are as follows :
      A3 to A1                           25 m
      A1 to A2                           40 m
      A2 to A4                           25 m
      A4 to A3                           120 m
      A3 to A2                           990 m
      A1 to A4                           170 m

     The number of computers in each branch is as follows :
      A1              50
      A2              40
      A3              110
      A4              60

     Based on the above specifications, answer the following questions :            4

     (a)   Suggest the topology and draw the most suitable cable layout for
           connecting all the divisions of Bangalore branch.


90                                     Page 7                                   P.T.O.
```

---

## page 8

```
     (b)   Suggest the kind of network required (out of LAN, MAN, WAN) for
           connecting Production (A3) with Shimla branch.

     (c)   Suggest the placement of the following devices :
           (i)    Repeater
           (ii)   Switch/Hub

     (d)   The company wanted to develop a healthy relation among the
           employees, therefore the HRA planned an online session with
           everyone so that they could play games from their devices. Suggest
           the protocol that helped to send the voice signals over Internet.




90                                      Page 8
```