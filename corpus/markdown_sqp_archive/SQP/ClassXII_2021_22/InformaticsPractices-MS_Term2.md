---
title: "InformaticsPractices-MS Term2"
source_pdf: "InformaticsPractices-MS_Term2.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2021_22/InformaticsPractices-MS_Term2.pdf"
pages: 6
pdf_bytes: 519890
pdf_sha256: "6d6c2e4ad83c16335e1fbf9ffc541c0bbdc1801277aaf1f63dcdf54021d482a3"
text_chars: 8968
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPractices-MS Term2


---

## page 1

```
                                         MARKING SCHEME
                               INFORMATICS PRACTICES (Code: 065)
Maximum Marks: 35                                                       Time: 2 hours


General Instructions

         The question paper is divided into 3 sections – A, B and C
         Section A, consists of 7 questions (1-7). Each question carries 2 marks.
         Section B, consists of 3 questions (8-10). Each question carries 3 marks.
         Section C, consists of 3 questions( 11-13). Each question carries 4 marks.
         Internal choices have been given for question numbers – 1 , 3, 8 and 12.


                                             Section –A
                                    Each question carries 2 marks
 Q.       Part                                Question                                         Marks
No        No.
1.                Differentiation between static and dynamic web pages:                  (2)

                   Static Web page                     Dynamic Web page
                   1. Content of this type of          1. Content of this type of
                   webpage cannot be changed           webpage can be changed at
                   at run time.                        run time.
                   2. No      interaction   with       3. Interaction with server’s
                       server’s    database    is      database is possible in case of
                       possible in case of static      dynamic web pages.
                       web pages.

                  1 mark each for each correct differentiation mentioned above
                  or any other relevant point of differentiation.

                  OR

                  The difference between a website and a web page is that a
                  website is a collection of different web pages containing
                  information on a particular topic. A web page is an individual
                  page of a big website usually containing more specific
                  information. If we compare a website with a book, then a
                  webpage can be compared with a single page of that book.

                  2 marks for correct answer
                                                 [1]
```

---

## page 2

```
2.   (i)    Cookies                                                              (1)

            1 mark for correct answer
     (ii)   Name of any two popular web browsers:                                (1)
                Mozilla firefox
                Google Chrome
                   OR
                   Any other correct name

            ½ mark each for each correct browser name
3.          Output:                                                              (2)
            i. 125
            ii. 2

            1 Mark for each correct answer
                                         OR

            i. power(): It returns the value of a number raised to the power
            of another number.
            For example:

            Select power(5,3);
            Output: 125

            ii. mod(): It returns the remainder of a number divided by
            another number.

            For example:

            Select mod(5,3);
            Output: 2

            1 Mark for each correct answer
4.          Role of web server in hosting a website:                             (2)

            A web server is the main centralized computer system that hosts
            and runs the websites. It has a computer program that distributes
            web pages as they are requisitioned. The basic role of the web
            server is to store, process and deliver the web pages to the users
            as and when required.

            2 Marks for correct answer



                                           [2]
```

---

## page 3

```
5.   Output:                                                          (2)
     i) 8.720
     ii) 10

     1 Mark for each correct answer
6.   Having clause is used to further filter those groups of records (2)
     which will be generated through group by clause.

     For example:

     Select max(marks) from student group by classes having classes
     in (10,12);

     Above given query will arrange records in groups according to
     the classes. Further filtering on these groups will happen
     through having clause, which will finally display the highest
     marks from classes 10 and 12.

     1 Mark for correct clause
     1 Mark for correct example
7.   Mr. Som, a HR Manager in a multinational company “Star-X (2)
     world” has created the following table to store the records of
     employees:
     Table: Emp
      Eid      EName Department DOB                  DOJ
      Star1    Ivan       Sales        1994-08-28 2020-02-14
      Star2    Melinda IT              1997-10-15 2021-11-19
      Star3    Raj        Accounts     1998-10-02 2019-04-02
      Star4    Michael Sales           2000-02-17 2020-05-01
      Star5    Sajal      IT           2001-12-05 2018-06-13
      Star6    John       Accounts     1995-01-03 2019-07-15
      Star7    Julia      Sales        1985-11-13 2020-08-19

     Output:

     i) 2001
     ii) Melinda

     1 Mark for each correct answer
                                  OR

     Queries:

                                  [3]
```

---

## page 4

```
      i) select ENAME,min(year(DOB)) from emp;

      ii) select ENAME from emp where month(DOJ)=5;

      1 Mark for each correct answer
                               SECTION – B
                       Each question carries 3 marks
8.    Output:                                                         (3)
         i. 11
        ii. cbse
       iii. exams

      1 Mark for each correct answer
                                      OR
         i.      right()
                 select right(user_id,2) from hotel;
         ii.     lower()
                 select lower(name) from hotel;
         iii.    mid()/substr()/substring()
                 Select mid(city,3,3) from hotel;

      ½ Mark for suggesting each correct function name
      ½ Mark for writing each correct query
9.      i.     It returns the current date and time.                  (3)
        ii.    None
        iii.   The return type for NOW() function is either in ‘YYYY-
               MM-DD             HH:MM:SS’           format        or
               YYYYMMDDHHMMSS.uuuuuu format, depending on
               whether the function is used in a string or numeric
               context.

      1 Mark for each correct answer
10.      i. To remove leading space characters: ltrim()               (3)
        ii. To remove trailing space characters: rtrim()
       iii. To remove both type of space characters: trim()

      MySQL Queries:

      Select ltrim(‘ Hello ’);
      Select rtrim(‘ Hello ’);
      Select trim(‘ Hello ’);

      Output:
                                     [4]
```

---

## page 5

```
      Hello

      ½ Mark for suggesting each correct function name
      ½ Mark for writing each correct MySQL query
                                 Section C
                       Each question carries 4 marks
11.     (a) select * from stock order by price desc;                  (4)
        (b) select category, sum(qty) from stock group by category;
        (c) select category,avg(price) from stock group by category;
        (d) select category, max(price) from stock group by category;

      1 Mark for each correct query
12.   Output:                                                           (4)

      (a) 193
      (b) 194
      (c) 93.75
      (d) 6

      1 Mark for each correct output

                                      OR


      First query will produce the output 7.
      Justification: count (*) will count and display total number of
      rows (irrespective of any null value present in any of the
      column).

      Second query will produce the output 6.
      Justification: count (col_name) will count and display total
      number of not null values in the specified column.

      1 Mark each for each correct output
      1 Mark each for each correct justification
13.      (a) LAN                                                   (4)
             As computers are placed with-in the same campus with-
             in a small range.
      ½ Mark for correct answer
      ½ Mark for correct justification
         (b) Star topology
      ½ Mark for correct answer
                                      [5]
```

---

## page 6

```
Cable Layout:




½ Mark for correct cable layout
  (c)
             i. Repeater should be placed in between Block
                 ‘D’ (Design) and Block ‘P’ as distance is more.
             ii.      Hub/Switch should be placed in each
                      building to connect various computers
                      together.
½ Mark for each correct answer
  (d) Video Conferencing software: Teams, Zoom, Skype etc.
      (Any one)
      Protocol of Video Conferencing software: VOIP
½ Mark for each correct answer




                               [6]
```