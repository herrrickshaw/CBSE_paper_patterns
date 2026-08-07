---
title: "InformaticsPractices-SQP Term2"
source_pdf: "InformaticsPractices-SQP_Term2.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2021_22/InformaticsPractices-SQP_Term2.pdf"
pages: 6
pdf_bytes: 533937
pdf_sha256: "f15d7b6d8c9171c8a202dd5e443d7dfc7593d580be86eec818355bf0ff1bd671"
text_chars: 9821
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPractices-SQP Term2


---

## page 1

```
                                       Sample Question Paper
                               INFORMATICS PRACTICES (Code : 065)
Maximum Marks: 35                                                    Time: 2 hours


General Instructions

         The question paper is divided into 3 sections – A, B and C
         Section A, consists of 7 questions (1-7). Each question carries 2 marks.
         Section B, consists of 3 questions (8-10). Each question carries 3 marks.
         Section C, consists of 3 questions( 11-13). Each question carries 4 marks.
         Internal choices have been given for question numbers – 1 , 3, 8 and 12.


                                             Section –A
                                    Each question carries 2 marks
 Q.       Part                                Question                                       Marks
No        No.
1.                 Aman, a freelance web site developer, has been assigned a task (2)
                   to design few web pages for a book shop. Help Aman in deciding
                   out of static web page and dynamic web page, what kind of web
                   pages should be designed by clearly differentiating between
                   static and dynamic web pages on at least two points.

                   OR

                   Priyanka, a beginner in IT field has just started learning web
                   technologies. Help her in understanding the difference between
                   website and web pages with the help of a suitable general
                   example of each.
2.          (i)        I:                                                         (1)
                             am a small text file
                             created on a user’s computer
                             contain small pieces of data — like a username,
                               password and user’s browsing history as well as
                               preferences
                             may help to improve user’s web browsing
                               experience.

                   Who am I?
            (ii)   Name any two popular web browsers.                                  (1)

                                                 [1]
```

---

## page 2

```
3.   Predict the output of the following queries:                      (2)
     i. Select power(5,3);
     ii. Select mod(5,3);

                                    OR

     Briefly explain the purpose of the following SQL functions:
     i. power()
     ii. mod()
4.   Navya has just created a website for her company and now need (2)
     to host it. Briefly discuss the role of a web server in hosting a
     website.
5.   Help Reshma in predicting the output of the following queries:    (2)
     i) select round(8.72,3);
     ii) select round(9.8);
6.   Aryan, a database administrator, has grouped records of a table (2)
     with the help of group by clause.

     He needs to further filter groups of records generated through
     group by clause.

     Suggest suitable clause for it and properly explain its usage with
     the help of an example.
7.   Mr. Som, a HR Manager in a multinational company “Star-X (2)
     world” has created the following table to store the records of
     employees:
     Table: Emp
      Eid       EName Department DOB                    DOJ
      Star1     Ivan      Sales           1994-08-28 2020-02-14
      Star2     Melinda IT                1997-10-15 2021-11-19
      Star3     Raj       Accounts        1998-10-02 2019-04-02
      Star4     Michael Sales             2000-02-17 2020-05-01
      Star5     Sajal     IT              2001-12-05 2018-06-13
      Star6     John      Accounts        1995-01-03 2019-07-15
      Star7     Julia     Sales           1985-11-13 2020-08-19

     He has written following queries:
     i) select max(year(DOB)) from emp;
     ii) select ENAME from emp where month(DOJ)=11;

     Predict the output.
                                    OR

                                    [2]
```

---

## page 3

```
      Based on the table given above, help Mr. Som writing queries for
      the following task:
      i) To display the name of eldest employee and his/her date of
      birth.
      ii) To display the name of those employees whose joining month
      is May.
                                  SECTION – B
                         Each question carries 3 marks

8.    Predict the output of the following queries:                       (3)
         i. select instr('exams@cbse.nic.in','.');
        ii. select substr('exams@cbse.nic.in',7,4);
       iii. select left('exams@cbse.nic.in',5);
                                      OR

      Ms.Saumya is working on a MySQL table named ‘Hotel’ having
      following structure:




      She need to perform following task on the table:
         i.     To fetch last 2 characters from the user_id column.
         ii.    To display the values of name column in lower case.
         iii.   To display 3 characters from 3rd place from the
                column city.

      Suggest suitable SQL function for the same. Also write the query
      to achieve the desired task.
9.    Reena is working with functions of MySQL. Explain her following: (3)
          i. What is the purpose of now () function?
         ii. How many parameters does it accept?
        iii. What is the general format of its return type?
10.   While dealing with string data type in MySQL, its observed that (3)
      sometimes unnecessary space character comes in between
      which hampers the successful execution of a string manipulation
      module. Name the suitable MySQL function (s) to remove
      leading, trailing and both type of space characters from a string.
      Also give MySQL queries to depict the same.
                                   Section C

                                    [3]
```

---

## page 4

```
                       Each question carries 4 marks
11.   Carefully observe the following table named ‘stock’:             (4)

      Table: stock
       Pid       PName            Category      Qty        Price
       1         Keyboard         IO            15         450
       2         Mouse            IO            10         350
       3         Wifi-router      NW            5          2600
       4         Switch           NW            3          3000
       5         Monitor          O             10         4500
       6         Printer          O             4          17000

      Write SQL queries for the following:
      (a) To display the records in decreasing order of price.
      (b) To display category and category wise total quantities of
          products.
      (c) To display the category and its average price.
      (d) To display category and category wise highest price of the
          products.

12.   Satyam, a database analyst has created the following table:      (4)

      Table: Student
       RegNo SName             Stream        Optional   Marks
       S1001 Akshat            Science       CS         99
       S1002 Harshit           Commerce      IP         95
       S1003 Devika            Humanities    IP         100
       S1004 Manreen           Commerce      IP         98
       S1005 Gaurav            Humanities    IP         82
       S1006 Saurav            Science       CS         NULL
       S1007 Bhaskar           Science       CS         95
       S1007 Bhaskar           Science       CS         96

      He has written following queries:

      ( a) select sum(MARKS) from student where OPTIONAL= ‘IP’ and
      STREAM= ‘Commerce’;
      (b) select max(MARKS)+min(MARKS) from student where
      OPTIONAL= ‘CS’;
      (c) select avg(MARKS) from student where OPTIONAL= ‘IP’;
      (d) select length(SNAME) from student where MARKS is NULL;


                                      [4]
```

---

## page 5

```
      Help him in predicting the output of the above given queries.

                                    OR
      Based on the above given table named ‘Student’, Satyam has
      executed following queries:

      Select count(*) from student;
      Select count(MARKS) from student;

      Predict the output of the above given queries.
      Also give proper justifications of the output generated through
      each query.
13.   “Anutulya Creations”-A start-up fashion house has set up its (4)
      main centre at Kanpur, Uttar Pradesh for its dress designing,
      production and dress supplying activities. It has 4 blocks of
      buildings.
      Distance between the various blocks is as follows:
              A to D         50 m
              A to P         60 m
              A to S         110m
              D to S         60m
              P to S         50m
              P to D         150m
       Numbers of computers in each block
              Block A - 20
              Block D - 80
              Block P - 15
              Block S - 8




                                    [5]
```

---

## page 6

```
Based on the above specifications, answer the following
questions:
   (a) Out of LAN, WAN and MAN, what type of network will be
       formed if we interconnect different computers of the
       campus? Justify.
   (b) Suggest the topology which should be used to efficiently
       connect various blocks of buildings within Kanpur centre
       for fast communication.
       Also draw the cable layout for the same.
   (c) Suggest the placement of the following device with
       justification
                i. Repeater
                ii.   Hub/Switch
   (d) Now a day, video-conferencing software is being used
       frequently by the company to discuss the product details
       with the clients. Name any one video conferencing
       software.
       Also mention the protocol which is used internally in
       video conferencing software.




                             [6]
```