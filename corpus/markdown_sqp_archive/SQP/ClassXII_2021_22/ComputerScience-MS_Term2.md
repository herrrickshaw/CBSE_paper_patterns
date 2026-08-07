---
title: "ComputerScience-MS Term2"
source_pdf: "ComputerScience-MS_Term2.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2021_22/ComputerScience-MS_Term2.pdf"
pages: 6
pdf_bytes: 580357
pdf_sha256: "efdc43c63179060570a8def36733f43a4198b60ba38f348e355a0a620dcec21f"
text_chars: 12417
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-MS Term2


---

## page 1

```
                                           Marking Scheme
                                  COMPUTER SCIENCE (Code : 083)
Maximum Marks: 35                                                        Time: 2 hours


General Instructions

         The question paper is divided into 3 sections – A, B and C
         Section A, consists of 7 questions (1-7). Each question carries 2 marks.
         Section B, consists of 3 questions (8-10). Each question carries 3 marks.
         Section C, consists of 3 questions( 11-13). Each question carries 4 marks.
         Internal choices have been given for question numbers – 7, 8 and 12




                                       Section -A
                              Each question carries 2 marks
 Q.       Part                         Question                               Marking      Marks
 No       No.                                                               Instructions
 1.                Characteristics of Stacks:                               1 mark for
                       It is a LIFO data structure                         each point      (2)
                       The insertion and deletion happens at one
                          end i.e. from the top of the stack

 2.         (i)    SMTP : Simple Mail Transfer Protocol                     ½ mark for
                   XML: Extensible Mark Up Language                         each correct    (1)
                                                                            expansion
            (ii)   Wired- optical fibre                                     ½ mark for
                   Wireless – microwave                                     each correct    (1)
                                                                            answer
 3.                char(n):                                                 1 mark for
                        stores a fixed length string between 1 and         each correct
                          255 characters                                    difference
                        if the value is of smaller length, adds blank      ( minimum 2
                          spaces                                            differences     (2)
                        some space is wasted                               to be given)
                   varchar(n) :
                        stores a variable length string
                        no blanks are added even if value is of
                          smaller length
                        no wastage of space
                                                  [1]
```

---

## page 2

```
4.             (a)         One record                            1 mark for
               (b)         tuple                                 each correct    (2)
                                                                 answer
5.
                     (a) 29

                     (b) 19-Jul-2021
                                                                 ½ mark for      (2)
                     (c)                                         each correct
                                                                 output
             T006          Console      17-Nov- 15000    12
                           Table        2019

                     (d)
                           10-Mar- 2020
                           17-Nov-2019

6.   (i)    SHOW TABLES;                                         1 mark for
                                                                 correct         (1)
                                                                 answer
     (ii)   Equi- join:                                          1 mark for
                The join in which columns from two tables       correct
                    are compared for equality                    difference
                Duplicate columns are shown                     (Any one        (1)
            Natural Join                                         point may be
                The join in which only one of the identical     given)
                    columns existing in both tables is present
                No duplication of columns

7.          (a) Degree: 5                                        ½ mark each
                Cardinality: 6                                   for correct
                                                                 degree and
                                                                 cardinality


            (b) MOVIEID should be made the primary key as it     ½ mark for
                uniquely identifies each record of the table.    correct field
                                                                 and ½ mark      (2)
                                                                 for
                                                                 justification




                                             [2]
```

---

## page 3

```
                          OR


       (a) MOVIEID and TITLE                 ½ mark for
                                             each correct
                                             field name


       (b) MOVIEID                           1 mark for
                                             correct
                                             answer
                     SECTION – B
             Each question carries 3 marks

8.   # Question No 8 (first option)
     R={"OM":76, "JAI":45, "BOB":89,         1 mark for
     "ALI":65, "ANU":90, "TOM":82}           correct PUSH
     def PUSH(S,N):                          operation
       S.append(N)
     def POP(S):
                                             1 mark for
       if S!=[]:
         return S.pop()                      correct POP
       else:                                 operation
         return None
     ST=[]                                   1 mark for
     for k in R:                             correct
       if R[k]>=75:                          function calls
         PUSH(ST,k)                          and              (3)
     while True:                             displaying
       if ST!=[]:                            the output
         print(POP(ST),end=" ")
       else:
         break


                          OR


     # Question No 8 (second option)         1 mark for
                                             correct PUSH
     N=[12, 13, 34, 56, 21, 79, 98, 22,      operation
     35, 38]
     def PUSH(S,N):

                                [3]
```

---

## page 4

```
               S.append(N)                           1 mark for
             def POP(S):                             correct POP
               if S!=[]:                             operation
                 return S.pop()
               else:                                 1 mark for
                 return None
                                                     correct
             ST=[]
             for k in N:                             function calls
               if k%2==0:                            and
                 PUSH(ST,k)                          displaying
             while True:                             the output
               if ST!=[]:
                 print(POP(ST),end=" ")
               else:
                 break

                                                     Note: Marks
                                                     to be
                                                     awarded for
                                                     any other
                                                     correct logic
                                                     given by the
                                                     student
9.    (i)    ALTER TABLE Item                        1 mark for
             ADD (Discount INT);                     correct          (1)
                                                     command
      (ii)   DDL: DROP TABLE, ALTER TABLE            ½ mark for       (2)
             DML: INSERT INTO, UPDATE...SET          each correct
                                                     command
                                                     identified
10.          CREATE DATABASE MYEARTH;                1 mark for
                                                     correctly
             CREATE TABLE CITY                       creating
             (                                       database.
               CITYCODE CHAR(5)PRIMARY KEY,                           (3)
               CITYNAME CHAR(30),
                                                     2 marks for
               SIZE INT,
               AVGTEMP INT,                          correctly
               POPULATIONRATE INT,                   creating the
               POPULATION INT,                       table.
             );

                              Section C
                     Each question carries 4 marks
11.          (a) SELECT AVG(SALARY)

                                        [4]
```

---

## page 5

```
                 FROM EMPLOYEE
                 GROUP BY DEPTID;

            (b) SELECT NAME, DEPTNAME
                                                                   1 mark for
                FROM EMPLOYEE, DEPARTMENT                          each correct
                WHERE                                              query
                  EMPLOYEE.DEPTID=                                                (4)
                      DEPARTMENT.DEPTID
                  AND SALARY>50000;

            (c) SELECT NAME FROM EMPLOYEE
                WHERE SALARY IS NULL
                ORDER BY NAME;

            (d) SELECT DISTINCT DEPTID
                FROM EMPLOYEE;
12. (i)     Advantages
                Ease of service
                Centralized control
                Easy to diagnose faults
                One device per connection                         ½ mark for
                                                                   each correct
            Disadvantages                                          advantage /    (2)
                 long cable length                                disadvantage
                 difficult to expand
                 central node dependency

                                    OR

            www: a set of protocols that allow you to access any
            document on the internet through the naming            1 mark for
            systems based on URLs                                  each correct
            Web hosting: Web hosting is a service that             definition
            allows organizations and individuals to post a
            website or web page onto the server, which can be
            viewed by everyone on the Internet.
     (ii)   Packet switching:                                      1 mark for
                 uses store and forward concept to send           each correct
                   messages                                        difference
                 no physical path is actually establishes
                 message is divided into smaller parts, known     (minimum
                   as packets and then sent forward                two points     (2)
                 tight upper limit on block size                  should be
                 Each data unit knows only the final              given)
                   receiver’s address
                                          [5]
```

---

## page 6

```
      Circuit switching
           physical connection is established between
              sender and receiver
           Each data unit knows the entire path from
              sender to receiver
           It does not follow store and forward
              concept

13.


             (a)

        BeHappy Corporation                                              (4)
                                    Block B
            Block A




             Block C                      Block D


                                                          1 mark for
                                                          each correct
                                                          answer
            (b)
      Repeater : between C and D as the distance
      between them is 100 mts.

      Hub/ Switch : in each block as they help to share
      data packets within the devices of the network in
      each block

             (c) WAN.

             (d) Satellite




                                    [6]
```