---
title: "ComputerScience-SQP Term2"
source_pdf: "ComputerScience-SQP_Term2.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2021_22/ComputerScience-SQP_Term2.pdf"
pages: 7
pdf_bytes: 722961
pdf_sha256: "1ea1bb255ef00734e1bfc1f070f8f096212ffb7cea0b0095263fdd1a12f47c54"
text_chars: 11290
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-SQP Term2


---

## page 1

```
                                       Sample Question Paper
                                  COMPUTER SCIENCE (Code: 083)
Maximum Marks: 35                                                       Time: 2 hours


General Instructions

         The question paper is divided into 3 sections – A, B and C
         Section A, consists of 7 questions (1-7). Each question carries 2 marks.
         Section B, consists of 3 questions (8-10). Each question carries 3 marks.
         Section C, consists of 3 questions (11-13). Each question carries 4 marks.
         Internal choices have been given for question numbers 7, 8 and 12.


                                                 Section -A
                                        Each question carries 2 marks
  Q.       Part                                  Question                                  Marks
 No        No.
 1.                 Give any two characteristics of stacks.                                (2)

 2.          (i)    Expand the following:                                                  (1)
                       SMTP , XML

             (ii)   Out of the following, which is the fastest wired and wireless medium   (1)
                    of transmission?

                    Infrared,   coaxial   cable,                  optical        fibre,
                    microwave, Ethernet cable

 3.                 Differentiate between char(n) and varchar(n) data types with respect (2)
                    to databases.

 4.                 A resultset is extracted from the database using the cursor object     (2)
                    (that has been already created) by giving the following statement.

                    Mydata=cursor.fetchone()

                       (a)     How many records will be returned by fetchone()
                               method?
                       (b)     What will be the datatype of Mydata object after the
                               given command is executed?

                                                  [1]
```

---

## page 2

```
5.          Write the output of the queries (a) to (d) based on the table,          (2)
            Furniture given below:

            Table: FURNITURE
             FID      NAME       DATEOFPURCHASE        COST      DISCOUNT
             B001     Double     03-Jan-2018           45000     10
                      Bed
             T010     Dining     10-Mar-2020           51000     5
                      Table
             B004     Single     19-Jul-2021           22000     0
                      Bed
             C003     Long       30-Dec-2016           12000     3
                      Back
                      Chair
             T006     Console    17-Nov-2019           15000     12
                      Table
             B006     Bunk       01-Jan-2021           28000     14
                      Bed


            (a)     SELECT SUM(DISCOUNT)
                    FROM FURNITURE
                    WHERE COST>15000;

            (b)     SELECT MAX(DATEOFPURCHASE)
                    FROM FURNITURE;

            (c)     SELECT * FROM FURNITURE
                    WHERE DISCOUNT>5 AND FID LIKE "T%";

             (d) SELECT DATEOFPURCHASE FROM FURNITURE
                WHERE NAME IN ("Dining Table", "Console
            Table");



6.   (i)    Which command is used to view the list of tables in a database?         (1)

     (ii)   Give one point of difference between an equi-join and a natural join.   (1)

7.          Consider the table, MOVIEDETAILS given below:                           (2)

            Table: MOVIEDETAILS
             MOVIEID TITLE               LANGUAGE RATING PLATFORM
             M001        Minari    Korean             5          Netflix
             M004        MGR Magan Tamil              4          Hotstar
                                          [2]
```

---

## page 3

```
      M010        Kaagaz          Hindi         3         Zee5
      M011        Harry           English       4         Prime
                  Potter                                  Video
                  and the
                  Chamber
                  of
                  Secrets
      M015        Uri             Hindi         5         Zee5
      M020        Avengers:       English       4         Hotstar
                  Endgame


        (a) Identify the degree and cardinality of the table.
        (b) Which field should be made the primary key? Justify your
            answer.

                                         OR

        (a) Identify the candidate key(s) from the table MOVIEDETAILS.
        (b) Consider the table SCHEDULE given below:

     Table: SCHEDULE
      SLOTID                 MOVIEID                 TIMESLOT
      S001                   M010                    10 AM to 12 PM
      S002                   M020                    2 PM to 5 PM
      S003                   M010                    6 PM to 8 PM
      S004                   M011                    9 PM to 11 PM

     Which field will be considered as the foreign key if the tables
     MOVIEDETAILS and SCHEDULE are related in a database?

                                 SECTION – B
                         Each question carries 3 marks

8.   Julie has created a dictionary containing names and marks as key       (3)
     value pairs of 6 students. Write a program, with separate user
     defined functions to perform the following operations:

          ● Push the keys (name of the student) of the dictionary into a
             stack, where the corresponding value (marks) is greater than
             75.
          ● Pop and display the content of the stack.
     For example:
     If the sample content of the dictionary is as follows:

                                   [3]
```

---

## page 4

```
             R={"OM":76, "JAI":45, "BOB":89, "ALI":65, "ANU":90,
             "TOM":82}

             The output from the program should be:
             TOM ANU BOB OM

                                                OR

             Alam has a list containing 10 integers. You need to help him create
             a program with separate user defined functions to perform the
             following operations based on this list.
                 ● Traverse the content of the list and push the even numbers
                    into a stack.
                 ● Pop and display the content of the stack.

             For Example:
             If the sample Content of the list is as follows:
             N=[12, 13, 34, 56, 21, 79, 98, 22, 35, 38]

             Sample Output of the code should be:
             38 22 98 56 34 12

9.    (i)    A table, ITEM has been created in a database with the following        (1)
             fields:
             ITEMCODE, ITEMNAME, QTY, PRICE

             Give the SQL command to add a new field, DISCOUNT (of type
             Integer) to the ITEM table.
      (ii)   Categorize following commands into DDL and DML commands?               (2)

             INSERT INTO, DROP TABLE, ALTER TABLE,
             UPDATE...SET

10.          Charu has to create a database named MYEARTH in MYSQL.                 (3)
             She now needs to create a table named CITY in the database to store
             the records of various cities across the globe. The table CITY has the
             following structure:

             Table: CITY
              FIELD NAME             DATA TYPE           REMARKS

              CITYCODE               CHAR(5)             Primary
                                                         Key
              CITYNAME               CHAR(30)
              SIZE                   INTEGER


                                          [4]
```

---

## page 5

```
       AVGTEMP                INTEGER
       POLLUTIONRATE          INTEGER
       POPULATION             INTEGER


      Help her to complete the task by suggesting appropriate SQL
      commands.
                                   Section C
                        Each question carries 4 marks

11.   Write queries (a) to (d) based on the tables EMPLOYEE and              (4)
      DEPARTMENT given below:

      Table: EMPLOYEE
       EMPID NAME          DOB     DEPTID DESIG               SALARY
       120      Alisha 23-         D001      Manager          75000
                       Jan-
                       1978
       123      Nitin  10-         D002      AO               59000
                       Oct-
                       1977
       129      Navjot 12-         D003      Supervisor 40000
                       Jul-
                       1971
       130      Jimmy  30-         D004      Sales Rep
                       Dec-
                       1980
       131      Faiz   06-         D001      Dep              65000
                       Apr-                  Manager
                       1984

      Table: DEPARTMENT

       DEPTID            DEPTNAME         FLOORNO
       D001              Personal         4
       D002              Admin            10
       D003              Production       1
       D004              Sales            3


      (a) To display the average salary of all employees, department wise.

      (b) To display name and respective department name of each
          employee whose salary is more than 50000.
                                   [5]
```

---

## page 6

```
             (c) To display the names of employees whose salary is not known, in
                 alphabetical order.

             (d) To display DEPTID from the table EMPLOYEE without repetition.

12.   (i)    Give two advantages and two disadvantages of star topology            (2)

                                                  OR

             Define the following terms:
             www , web hosting

      (ii)   How is packet switching different from circuit switching?             (2)

13.          BeHappy Corporation has set up its new centre at Noida, Uttar         (4)
             Pradesh for its office and web-based activities. It has 4 blocks of
             buildings.



                     BeHappy Corporation
                                                  Block B
                      Block A




                                                            Block D
                       Block C




             Distance between the various blocks is as follows:
                    A to B       40 m
                    B to C       120m
                    C to D       100m
                    A to D       170m
                    B to D       150m
                    A to C       70m

             Numbers of computers in each block
                  Block A - 25
                                            [6]
```

---

## page 7

```
   Block B - 50
   Block C - 125
   Block D - 10

(a) Suggest and draw the cable layout to efficiently connect
    various blocks of buildings within the Noida centre for
    connecting the digital devices.

(b) Suggest the placement of the following device with
    justification
             i.   Repeater
             ii.   Hub/Switch

(c) Which kind of network (PAN/LAN/WAN) will be formed if the
    Noida office is connected to its head office in Mumbai?

(d) Which fast and very effective wireless transmission medium
    should preferably be used to connect the head office at
    Mumbai with the centre at Noida?




                          [7]
```