---
title: "ComputerScience-MS"
source_pdf: "ComputerScience-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/ComputerScience-MS.pdf"
pages: 15
pdf_bytes: 956476
pdf_sha256: "d1f25014a3a77b7d455adc2ceb31ed59cca7787cb13fdcf7f36200caecc0a9c2"
text_chars: 26353
low_text_pages: 1
converter: "pdftotext -layout"
---

# ComputerScience-MS


---

## page 1

```
                                   Class XII

                            Computer Science (083)

                               Marking Scheme

Time Allowed: 3 hours                                       MM: 70

 Ques                   Question and Answers         Distribution   Total
  No                                                  of Marks      Marks

                                 SECTION A
  1     False                                        1 mark for       1
                                                     correct
                                                     answer

  2     Option b                                     1 mark for       1
                                                     correct
        6,20
                                                     answer

  3     Option c                                     1 mark for       1
                                                     correct
        -244.0                                       answer

  4     PYTHON-is-Fun                                1 mark for       1
                                                     correct
                                                     answer

  5     Option b                                     1 mark for       1
                                                     correct
        8,15
                                                     answer

  6     Option a                                     1 mark for       1
                                                     correct
        PAN
                                                     answer

  7     Option b                                     1 mark for       1
                                                     correct
        del D1["Red"]                                answer

  8     Option b                                     1 mark for       1
                                                     correct
                                                     answer

                                      [1]
```

---

## page 2

```
     ceieP0

9    Option d                                                      1 mark for   1
                                                                   correct
     Statement 4                                                   answer

10   Option b                                                      1 mark for   1
                                                                   correct
            WHITE*                                                 answer

            BLACK*

11   Option b                                                      1 mark for   1
                                                                   correct
     Modulator                                                     answer

12   Option c                                                      1 mark for   1
                                                                   correct
     global b                                                      answer

13   True                                                          1 mark for   1
                                                                   correct
                                                                   answer

14   Option c                                                      1 mark for   1
                                                                   correct
     A candidate key that is not a primary key is a foreign key.   answer

15   Circuit                                                       1 mark for   1
                                                                   correct
                                                                   answer

16   Option c                                                      1 mark for   1
                                                                   correct
     seek()                                                        answer

17   Option d                                                      1 mark for   1
     A is false but R is True                                      correct
                                                                   answer




                                            [2]
```

---

## page 3

```
18   Option b                                                              1 mark for         1
                                                                           correct
     Both A and R are true but R is not the correct explanation for A      answer


                                         SECTION B
19      (i)                                                                ½ mark for       1+1=2
                                                                           each correct
     POP3 – Post Office Protocol 3                                         expansion

     URL – Uniform Resource Locator

        (ii)

     HTML( Hyper text mark Up language)

         We use pre-defined tags
         Static web development language – only focuses on how
               data looks
         It use for only displaying data, cannot transport data
         Not case sensistive

     XML (Extensible Markup Language)                                      1 mark for
                                                                           any one
                                                                           correct
         we can define our own tags and use them
                                                                           difference
         Dynamic web development language – as it is used for
                                                                           No mark to
               transporting and storing data                               be awarded if
         Case sensitive                                                   only full form
                                                                           is given
                                         OR


               (i)   Bandwidth is the maximum rate of data transfer over   1 mark for
                                                                           correct
                     a given transmission medium. / The amount of          definition
                     information that can be transmitted over a network.


                                               [3]
```

---

## page 4

```
         (ii)   https (Hyper Text Transfer Protocol Secure) is the     1 mark for
                                                                       correct
                protocol that uses SSL (Secure Socket Layer) to
                                                                       difference.
                encrypt data being transmitted over the Internet.
                Therefore, https helps in secure browsing while http
                does not.

20   def revNumber(num):                                               ½ mark for      2
         rev = 0                                                       each
         rem = 0                                                       correction
         while num > 0:                                                made
             rem =num %10
             rev = rev*10 + rem
             num = num//10
         return rev
     print(revNumber(1234))

21                                                                     ½ mark for      2
                                                                       correct
                                                                       function
                                                                       header

                                                                       ½ mark for
                                                                       correct loop

                                                                       ½ mark for
                                                                       correct if
                                                                       statement

                                                                       ½ mark for
                                                                       displaying
                                  OR
                                                                       the output



                                                                       ½ mark for
                                                                       correct
                                                                       function
                                                                       header

                                                                       ½ mark for
                                                                       using split()


                                          [4]
```

---

## page 5

```
                                                   ½ mark for
                                                   adding to
                                                   tuple

                                                   ½ mark for
                                                   return
                                                   statement




     Note: Any other correct logic may be marked

22   4*L                                           ½ mark for         2
                                                   each correct
     33*4
                                                   line of output
     21*S
     10*6
23     (i) L1.insert(2,200)                        1 mark for       1+1=2
                                                   each correct
       (ii) message.endswith('.')                  statement


                                       OR
     import statistics
                                                   1 mark for
     print( statistics.mode(studentAge) )
                                                   correct
                                                   import
                                                   statement

                                                   1 mark for
                                                   correct
                                                   command
                                                   with mode()
                                                   and print()

24   SQL Command to add primary key:               1 mark for         2
                                                   correct
     ALTER TABLE Employee ADD EmpId INTEGER        ALTER TABLE
                                                   command
     PRIMARY KEY;


                                       [5]
```

---

## page 6

```
      As the primary key is added as the last field, the command for
      inserting data will be:                                          1 mark for
                                                                       correct
      INSERT INTO Employee                                             INSERT
      VALUES("Shweta","Production",26900,999);                         command

      Alternative answer:
      INSERT INTO
      Employee(EmpId,Ename,Department,Salary)
      VALUES(999,"Shweta","Production",26900);
                                        OR
      To delete the attribute, category:
                                                                       1 mark for
      ALTER TABLE Sports                                               correct
      DROP category;                                                   ALTER TABLE
                                                                       command
                                                                       with DROP
      To add the attribute, TypeSport
                                                                       1 mark for
                                                                       correct
      ALTER TABLE Sports                                               ALTER TABLE
                                                                       command
      ADD TypeSport char(10) NOT NULL;                                 with ADD

 25   10.0$20                                                          1 mark for         2
                                                                       each correct
      10.0$2.0###
                                                                       line of output

                                           SECTION C
 26   ND-*34                                                           ½ mark for         3
                                                                       each correct
                                                                       character

27

                                                                       1 mark for       1*3=3
                                                                       each correct
                (i)
                                                                       output
                 COUNT(DISTINCT SPORTS)

                                              [6]
```

---

## page 7

```
             4


             (ii)
     CNAME                 SPORTS
     AMINA                 CHESS


             (iii)
     CNAME           AGE        PAY
     AMRIT           28         1000
     VIRAT           35         1050




28                                        1 mark for      3
                                          correctly
                                          opening and
                                          closing files

                                          ½ mark for
                                          correctly
                                          reading data

                                          1 mark for
                                          correct loop
                                          and if
                                          statement
                           OR
                                          ½ mark for
                                          displaying
                                          data



                                          1 mark for
                                          correctly
                                          opening and
                                          closing the
                                          files

                                    [7]
```

---

## page 8

```
                                                    ½ mark for
                                                    correctly
                                                    reading data

                                                    1 mark for
                                                    correct loop
                                                    and if
                                                    statement

                                                    ½ mark for
                                                    displaying
                                                    the output.



     Note: Any other correct logic may be marked
29     (i)                                          1 mark for     1*3=3
                                                    each correct
               UPDATE Personal
                                                    query
               SET Salary=Salary + Salary*0.5
               WHERE Allowance IS NOT NULL;


       (ii)
               SELECT Name, Salary + Allowance AS
               "Total Salary" FROM Personal;


       (iii)
               DELETE FROM Personal
               WHERE Salary>25000




                                       [8]
```

---

## page 9

```
30                                                   1 ½ marks for     3
                                                     each function




                             SECTION D
31   (i)                                             1 mark for      1*4=4
                                                     each correct
            SELECT PName, BName FROM PRODUCT P,
                                                     query
            BRAND B WHERE P.BID=B.BID;
     (ii)
            DESC PRODUCT;
     (iii)
            SELECT BName, AVG(Rating) FROM PRODUCT
            P, BRAND B
            WHERE P.BID=B.BID
            GROUP BY BName
            HAVING BName='Medimix' OR
            BName='Dove';
     (iv)
            SELECT PName, UPrice, Rating
            FROM PRODUCT
            ORDER BY Rating DESC;




                                [9]
```

---

## page 10

```
32                                      ½ mark for        4
                                        accepting
                                        data
                                        correctly

                                        ½ mark for
                                        opening and
                                        closing file

                                        ½ mark for
                                        writing
                                        headings

                                        ½ mark for
                                        writing row



                                        ½ mark for
                                        opening and
                                        closing file

                                        ½ mark for
                                        reader object

                                        ½ mark for
                                        print heading

                                        ½ mark for
                                        printing data

                        SECTION E
33       a)                             1 mark for      1*5=5
                                        each correct
     Bus Topology
                                        answer
                          ENGINEERING
              Admin


                           BUSINESS
                MEDIA




                           [10]
```

---

## page 11

```
     b) Switch
     c) Admin block, as it has maximum number of computers.
     d) Microwave
     e) No, a repeater is not required in the given cable layout as the
     length of transmission medium between any two blocks does not
     exceed 70 m.


34      (i)                                                               1 mark for      2+3=5
                                                                          each correct
               r+ mode:
                                                                          difference
                Primary function is reading
                                                                          ( minimum
                File pointer is at beginning of file                     two
                                                                          differences
                if the file does not exist, it results in an error
                                                                          should be
               w+ mode:                                                   given)
                primary function is writing
                if the file does not exist, it creates a new file.
                If the file exists, previous data is overwritten
                File pointer is at the beginning of file
        (ii)
                                                                          ½ mark for
                                                                          correctly
                                                                          opening and
                                                                          closing files

                                                                          ½ mark for
                                                                          correct try
                                                                          and except
                                                                          block

                                                                          ½ mark for
                                                                          correct loop

                                                                          1 mark for
                                                                          correctly
                                                                          copying data

                                              [11]
```

---

## page 12

```
                                                                  ½ mark for
                                                                  correct
                                                                  return
                                                                  statement



                                                                  ½ mark for
                                                                  correctly
                                                                  opening and
                                                                  closing files

                                                                  ½ mark for
                                                                  correct try
                                                                  and except
                                                                  block

                                                                  ½ mark for
                                                                  correct loop

                                                                  ½ mark for
                              OR                                  correct if
(i)    Text files:                                                statement

        Extension is .txt                                     1 mark for
                                                               correctly
        Data is stored in ASCII format that is human readable
                                                               displaying
        Has EOL character that terminates each line of data   data
          stored in the text files


       Binary Files
        Extension is .dat
        Data is stored in binary form (0s and 1s), that is not
          human readable.


(ii)




                                     [12]
```

---

## page 13

```
     Note: Any other correct logic may be marked
35     (i)    Domain is a set of values from which an attribute can    ½ mark for      1+4=5
                                                                       correct
              take value in each row. For example, roll no field can
                                                                       definition
              have only integer values and so its domain is a set of
                                                                       ½ mark for
              integer values                                           correct
                                                                       example



       (ii)

                                                                       ½ mark for
                                                                       importing
                                                                       correct
                                                                       module

                                                                       1 mark for
                                                                       correct
                                                                       connect()

                                                                       ½ mark for
                                                                       correctly
                                                                       accepting the
                                                                       input
     Note: Any other correct logic may be marked
                                                                       1 ½ mark for
                                                                       correctly

                                           [13]
```

---

## page 14

```
                                                                executing the
                                                                query

                                                                ½ mark for
                                                                correctly
                                                                using
                           OR                                   commit()



(i)    All keys that have the properties to become a primary
       key are candidate keys. The candidate keys that do not
       become primary keys are alternate keys.
                                                                1 mark for
(ii)                                                            correct
                                                                difference




                                                                ½ mark for
                                                                importing
                                                                correct
                                                                module

                                                                1 mark for
                                                                correct
                                                                connect()

                                                                1 mark for
                                                                correctly
                                                                executing
                                                                the query

                                                                ½ mark for
                                                                correctly
                                                                using
                                                                fetchall()

                                                                1 mark for
                                                                correctly


                                   [14]
```

---

## page 15

```
       displaying
       data




[15]
```