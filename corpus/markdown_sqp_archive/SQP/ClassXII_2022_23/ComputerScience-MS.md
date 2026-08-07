---
title: "ComputerScience-MS"
source_pdf: "ComputerScience-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/ComputerScience-MS.pdf"
pages: 25
pdf_bytes: 954833
pdf_sha256: "0fe0aee3cc26b15eb7f9f9fd72354f17a8d98421b994d39aa5718356777efb77"
text_chars: 39020
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-MS


---

## page 1

```
                                   Class: XII Session: 2022-23
                                    Computer Science (083)
                                Sample Question Paper (Theory)
       Maximum Marks: 70                                            Time Allowed: 3 hours


                                          SECTION A

                      (1 mark to be awarded for every correct answer)

1.   State True or False –                                                           1
     “Variable declaration is implicit in Python.”

     Ans. TRUE

2.   Which of the following is an invalid datatype in Python?                        1
       (a) Set (b) None (c)Integer (d)Real


     Ans: (d) Real


3.   Given the following                                                             1
     dictionaries

     dict_exam={"Exam":"AISSCE", "Year":2023}
     dict_result={"Total":500, "Pass_Marks":165}

     Which statement will merge the contents of both dictionaries?
       a. dict_exam.update(dict_result)
       b. dict_exam + dict_result
       c. dict_exam.add(dict_result)
       d. dict_exam.merge(dict_result)


     Ans: (a) dict_exam.update(dict_result)


4.   Consider the given expression:                                                  1
     not True and False or True
     Which of the following will be correct output if the given expression is
     evaluated?

        (a)          True
        (b)          False
        (c)          NONE
        (d)          NULL


     Ans: (a) True

                                                 1
```

---

## page 2

```
5.   Select the correct output of the code:                                          1
     a = "Year 2022 at All the best"
     a = a.split('2')
     b = a[0] + ". " + a[1] + ". " + a[3]
     print (b)

        (a) Year . 0. at All the best
        (b) Year 0. at All the best
        (c) Year . 022. at All the best
        (d) Year . 0. at all the best


     Ans: (a) Year . 0. at All the best

6.   Which of the following mode in file opening statement results or generates an   1
     error if the file does not exist?

        (a) a+     (b) r+   (c) w+    (d) None of the above


     Ans: (b) r+

7.   Fill in the blank:                                                              1
     ______ command is used to remove primary key from a table in SQL.

        (a)        update            (b)remove       (c) alter         (d)drop


     Ans: (c) alter


8.      Which of the following commands will delete the table from MYSQL             1
        database?
        (a) DELETE TABLE
        (b) DROP TABLE
        (c) REMOVE TABLE
        (d) ALTER TABLE

     Ans: (b) DROP TABLE

9.   Which of the following statement(s) would give an error after executing the     1
     following code?
     S="Welcome to class XII"            # Statement 1
     print(S)                            # Statement 2
     S="Thank you"                       # Statement 3
     S[0]= '@'                            # Statement 4
     S=S+"Thank you"                     # Statement 5

     (a)   Statement 3
     (b)   Statement 4
     (c)   Statement 5
                                                 2
```

---

## page 3

```
     (d)    Statement 4 and 5
     Ans: (b) – Statement 4

10. Fill in the blank:                                                                 1

     _________ is a non-key attribute, whose values are derived from the primary key
     of some other table.
         (a) Primary Key
         (b) Foreign Key
         (c) Candidate Key
         (d) Alternate Key


     Ans: (b) Foreign Key

11. The correct syntax of seek() is:
       (a) file_object.seek(offset [, reference_point])
       (b) seek(offset [, reference_point])
       (c) seek(offset, file_object)
       (d) seek.file_object(offset)
     Ans: (a) file_object.seek(offset [, reference_point])

12. Fill in the blank:
    The SELECT statement when combined with __________ clause, returns records
    without repetition.

        (a) DESCRIBE

        (b) UNIQUE
        (c) DISTINCT

        (d) NULL


     Ans: (c) DISTINCT

13. Fill in the blank:

     ______is a communication methodology designed to deliver both voice
     and multimedia communications over Internet protocol.

        (a) VoIP         (b) SMTP          (c) PPP        (d)HTTP


     Ans: (a) VoIP

14. What will the following expression be evaluated to in Python?
    print(15.0 / 4 + (8 + 3.0))

        (a) 14.75         (b)14.0          (c) 15         (d) 15.5

                                                3
```

---

## page 4

```
     Ans: (a) 14.75

15. Which function is used to display the total number of records from a table in a 1
    database?
       (a)       sum(*)
       (b)       total(*)
       (c)       count(*)
       (d)       return(*)


     Ans: (c) count(*)

16. To establish a connection between Python and SQL database, connect() is        1
    used. Which of the following arguments may not necessarily be given while
    calling connect() ?

     (a) host
     (b) database
     (c) user
     (d) password

     Ans: (b) – database

Q17 and 18 are ASSERTION AND REASONING based questions. Mark the correct choice as
   (a) Both A and R are true and R is the correct explanation for A
   (b) Both A and R are true and R is not the correct explanation for A
   (c) A is True but R is False
   (d) A is false but R is True


17. Assertion (A):- If the arguments in a function call statement match the number 1
    and order of arguments as defined in the function definition, such arguments
    are called positional arguments.
    Reasoning (R):- During a function call, the argument list first contains default
    argument(s) followed by positional argument(s).

     Ans: (c) A is True but R is False

18. Assertion (A): CSV (Comma Separated Values) is a file format for data storage 1
    which looks like a text file.
    Reason (R): The information is organized with one record on each line and each
    field is separated by comma.

     Ans: (a) Both A and R are true and R is the correct explanation for A

                                         SECTION B
19. Rao has written a code to input a number and check whether it is prime or      2
    not. His code is having errors. Rewrite the correct code and underline the
    corrections made.

                                               4
```

---

## page 5

```
    def prime():
      n=int(input("Enter number to check :: ")
      for i in range (2, n//2):
        if n%i=0:
          print("Number is not prime \n")
        break
        else:
          print("Number is prime \n’)

    Ans:
    def prime():
       n=int(input("Enter number to check :: ")) #bracket missing
       for i in range (2, n//2):
          if n%i==0:                              # = missing
              print("Number is not prime \n")
              break                               #wrong indent
          else:
              print("Number is prime \n”)         # quote mismatch


    (½ mark for each correct correction made and underlined.)

20. Write two points of difference between Circuit Switching and Packet Switching. 2

    Ans:
     Circuit Switching                    Packet Switching
     Circuit switching is the method      Packet switching is the method
     of switching which is used for       of switching where no dedicated
     establishing     a     dedicated     path is established from the
     communication path between           source to the destination.
     the sender and the receiver.
     Data     is    processed     and     Data       is    processed and
     transmitted at the source only.      transmitted, not only at the
                                          source but at each switching
                                          station.
     It is more reliable.                 It is less reliable.


    ( 1 mark for each correct point of difference)


                                           OR

    Write two points of difference between XML and HTML.

    Ans:

           XML (Extensible MarkupLangauge)
            XML tags are not predefined, they are user defined
            XML stores and transfers data.
            Dynamic in nature
                                                 5
```

---

## page 6

```
             HTML (Hypertext Markup Langauge)
              HTML tags are pre-defined and it is a markup language
              HTML is about displaying data.
              Static in nature


      (1 mark for each correct difference - Any two)

21.      a. Given is a Python string declaration:                                        1
            myexam="@@CBSE Examination 2022@@"

             Write the output of: print(myexam[::-2])

                                                                                         1
      Ans: @20 otnmx SC@

      (1 mark for the correct answer)

         b. Write the output of the code given below:
            my_dict = {"name": "Aman", "age": 26}
            my_dict['age'] = 27
            my_dict['address'] = "Delhi"
            print(my_dict.items())
      Ans: dict_items([('name', 'Aman'), ('age', 27), ('address', 'Delhi')])


      (1 mark for the correct answer)


22. Explain the use of ‘Foreign Key’ in a Relational Database Management System.         2
    Give example to support your answer.

      Ans:

      A foreign key is used to set or represent a relationship between two relations (
      or tables) in a database. Its value is derived from the primary key attribute of
      another relation.

      For example:
      In the tables TRAINER and COURSE given below, TID is primary key in TRAINER
      table but foreign key in COURSE table.

       TRAINER

             TID    TNAME         CITY         HIREDATE           SALARY
             101      Ritu        Nagpur       1998-10-15          56700
             102     Navin         Goa         1994-12-24          80000
             103    Murugan     Chandigarh     2001-12-21          82000
             104     Jyothi      Guwahati      2002-12-25          68000
             105     Chanu       Mumbai        1996-01-12          95000
                                                  6
```

---

## page 7

```
            106      Arbaaz        Delhi         2001-12-12   69000

      COURSE

              CID       CNAME       FEES       STARTDATE      TID
              C201      Deepa       12000       2018-07-02    101
              C202       Sindhu     15000       2018-07-15    103
              C203       Neeraj     10000       2018-10-01    102
              C204       Prakash     9000       2018-09-15    104
              C205       Nikhat     20000       2018-08-01    101



     (1 mark for explanation and 1 mark for example)
     ( Any relevant correct example may be marked)

23. (a) Write the full forms of the following:                        2
     (i) SMTP               (ii) PPP

     Ans:
            (i)     SMTP: Simple Mail Transfer Protocol
            (ii)   PPP: Point to Point Protocol


     (½ mark for every correct full form)

     (b) What is the use of TELNET?

     Ans: TELNET is used to access a remote computer / network.

     (1 mark for correct answer)

24. Predict the output of the Python code given below:                2

     def Diff(N1,N2):
         if N1>N2:
             return N1-N2
         else:
             return N2-N1

     NUM= [10,23,14,54,32]
     for CNT in range (4,0,-1):
         A=NUM[CNT]
         B=NUM[CNT-1]
         print(Diff(A,B),'#', end=' ')

     Ans: 22 # 40 # 9 # 13 #

     (½ mark for the correct digit with a #)

                                               OR

                                                    7
```

---

## page 8

```
    Predict the output of the Python code given below:

    tuple1 = (11, 22, 33, 44, 55 ,66)
    list1 =list(tuple1)
    new_list = []
    for i in list1:
        if i%2==0:
            new_list.append(i)
    new_tuple = tuple(new_list)
    print(new_tuple)

    Ans: (22,44,66)

    ( ½ mark for each correct digit , ½ mark for enclosing in parenthesis)

25. Differentiate between COUNT() and COUNT(*) functions in SQL with            2
    appropriate example.

    Ans:
    COUNT(*) returns the count of all rows in the table, whereas COUNT () is
    used with Column_Name passed as argument and counts the number of
    non-NULL values in a column that is given as argument.


       Example: Table : EMPL
                 EMPNO       ENAME             JOB          SAL        DEPTNO
                  8369       SMITH            CLERK         2985         10
                  8499        ANYA            NULL          9870         20
                  8566        AMIR          SALESMAN        8760         30
                  8698        BINA          MANAGER         5643         20
                  8912         SUR            NULL          3000         10

      e.g. SELECT COUNT(*) FROM EMPL;
      Output
    COUNT(*)
    5

       e.g.2 SELECT COUNT(JOB) FROM EMPL;
       Output

    COUNT(JOB)
    3
    Since JOB has 2 NULL values

    (1 mark for the difference and 1 mark for appropriate example)

                                      OR

    Categorize the following commands as DDL or DML:
    INSERT, UPDATE, ALTER, DROP

                                              8
```

---

## page 9

```
      Ans:
      DDL- ALTER, DROP
      DML – INSERT, UPDATE

      (½ mark for each correct categorization)


                                           SECTION C

26.      (a) Consider the following tables – Bank_Account and Branch:          1+2

      Table: Bank_Account
       ACode     Name          Type
       A01       Amrita        Savings
       A02       Parthodas     Current
       A03       Miraben       Current



      Table: Branch

       ACode    City
       A01      Delhi
       A02      Mumbai
       A01      Nagpur

      What will be the output of the following statement?


      SELECT * FROM Bank_Account NATURAL JOIN Branch;



      Ans:


       Acode     Name        Type         City
       A01       Amrita      Savings      Delhi
       A01       Amrita      Savings      Nagpur
       A02       Parthodas   Current      Mumbai


         (1 mark for correct output)


         (b) Write the output of the queries (i) to (iv) based on the table,
             TECH_COURSE given below:

                       Table: TECH_COURSE
         CID     CNAME               FEES              STARTDATE     TID
         C201    Animation and VFX   12000             2022-07-02    101
         C202    CADD                15000             2021-11-15    NULL
                                                   9
```

---

## page 10

```
        C203     DCA                    10000        2020-10-01   102
        C204     DDTP                    9000        2021-09-15   104
        C205     Mobile Application     18000        2022-11-01   101
                 Development
        C206     Digital marketing      16000        2022-07-25   103


        (i)       SELECT DISTINCT TID FROM TECH_COURSE;
     Ans:
        DISTINCT TID
        101
        NULL
        102
        104
        103

     ( ½ mark for the correct output)

        (ii)   SELECT TID, COUNT(*), MIN(FEES) FROM TECH_COURSE
          GROUP BY TID HAVING COUNT(TID)>1;


     Ans:
        TID     COUNT(*)    MIN(FEES)
        101     2           12000

     ( ½ mark for the correct output)

        (iii) SELECT CNAME FROM TECH_COURSE WHERE FEES>15000
          ORDER BY CNAME;
     Ans:
        CNAME
        Digital marketing
        Mobile Application Development

     ( ½ mark for the correct output)

      (iv)    SELECT AVG(FEES) FROM TECH_COURSE WHERE FEES
        BETWEEN 15000 AND 17000;


     Ans:
     15500.00

     ( ½ mark for the correct output)


27. Write a method COUNTLINES() in Python to read lines from text file            3
    ‘TESTFILE.TXT’ and display the lines which are not starting with any vowel.


                                                10
```

---

## page 11

```
Example:

If the file content is as follows:

An apple a day keeps the doctor away.
We all pray for everyone’s safety.
A marked difference will come in our country.

The COUNTLINES() function should display the output as:
The number of lines not starting with any vowel - 1

Ans:
def COUNTLINES() :
     file = open ('TESTFILE.TXT', 'r')
     lines = file.readlines()
     count=0
     for w in lines :
         if (w[0]).lower() not in 'aeoiu'
             count = count + 1
     print ("The number of lines not starting with any
vowel: ", count)
     file.close()

COUNTLINES()

( ½ mark for correctly opening and closing the file
½ for readlines()
½ mar for correct loop
½ for correct if statement
½ mark for correctly incrementing count
½ mark for displaying the correct output)

                                     OR

Write a function ETCount() in Python, which should read each character of a
text file “TESTFILE.TXT” and then count and display the count of occurrence
of alphabets E and T individually (including small cases e and t too).

Example:

If the file content is as follows:

Today is a pleasant day.
It might rain today.
It is mentioned on weather sites

The ETCount() function should display the output as:
The number of E or e: 6
The number of T or t : 9

Ans:
def ETCount() :
                                          11
```

---

## page 12

```
             file = open ('TESTFILE.TXT', 'r')
             lines = file.readlines()
             countE=0
             countT=0
             for w in lines :
                 for ch in w:
                     if ch in 'Ee':
                         countE = countE + 1
                     if ch in 'Tt':
                         countT=countT + 1
             print ("The number of E or e : ", countE)
             print ("The number of T or t : ", countT)
             file.close()




      (½ mark for correctly opening and closing the file
      ½ for readlines()
      ½ mark for correct loops
      ½ for correct if statement
      ½ mark for correctly incrementing counts
      ½ mark for displaying the correct output)

      Note: Any other relevant and correct code may be marked

28.                                                                                       3
           (a) Write the outputs of the SQL queries (i) to (iii) based on the relations
               Teacher and Placement given below:

      Table : Teacher

       T_ID Name          Age Department         Date_of_join Salary Gender
       1       Arunan     34    Computer Sc      2019-01-10     12000 M
       2       Saman      31    History          2017-03-24     20000    F
       3       Randeep    32    Mathematics      2020-12-12     30000    M
       4       Samira     35    History          2018-07-01     40000    F
       5       Raman      42    Mathematics      2021-09-05     25000    M
       6       Shyam      50    History          2019-06-27     30000    M
       7       Shiv       44    Computer Sc      2019-02-25     21000 M
       8       Shalakha 33      Mathematics      2018-07-31     20000    F


      Table : Placement
       P_ID       Department                   Place


                                                   12
```

---

## page 13

```
 1         History                 Ahmedabad
 2         Mathematics             Jaipur
 3         Computer Sc             Nagpur



       (i) SELECT Department, avg(salary) FROM Teacher GROUP
         BY Department;
Ans:
 Department     Avg(Salary)
 Computer Sc    16500.00
 History        30000.00
 Mathematics    25000.00


( ½ mark for the correct output)

(ii) SELECT MAX(Date_of_Join),MIN(Date_of_Join) FROM
Teacher;
Ans:
                Max(Date_of_Join) Min(Date_of_Join)
                2021-09-05        2017-03-04
( ½ mark for the correct output)

(iii)SELECT Name, Salary, T.Department, Place FROM Teacher
T, Placement P WHERE T.Department = P.Department AND
Salary>20000;
Ans:

 Name          Salary    Department    Place
 Randeep       30000     Mathematics   Jaipur
 Samira        40000     History       Ahmedabad
 Raman         25000     Mathematics   Jaipur
 Shyam         30000     History       Ahmedabad
 Shiv          21000     Computer Sc   Nagpur

( ½ mark for the correct output)

(iv)SELECT Name, Place FROM Teacher T, Placement P WHERE
Gender='F' and T.Department=P.Department;
Ans:

 Name          Place
 Samira        Ahmedabad
 Suman         Ahmedabad
 Shalaka       Jaipur


                                       13
```

---

## page 14

```
     ( ½ mark for the correct output)


        (b) Write the command to view all tables in a database.

     Ans:
     SHOW TABLES;

     ( 1 mark for correct answer)

29. Write a function INDEX_LIST(L), where L is the list of elements passed as   3
    argument to the function. The function returns another list named indexList
    that stores the indices of all Non-Zero Elements of L.

     For example:

     If L contains [12,4,0,11,0,56]

     The indexList will have - [0,1,3,5]

     Ans:

     def INDEX_LIST(L):
         indexList=[]
         for i in range(len(L)):
             if L[i]!=0:
                 indexList.append(i)
         return indexList


     (½ mark for correct function header
     1 mark for correct loop
     1 mark for correct if statement
     ½ mark for return statement)

     Note: Any other relevant and correct code may be marked

30. A list contains following record of a customer:                                  3
    [Customer_name, Phone_number, City]

     Write the following user defined functions to perform given operations on the
     stack named status:
        (i)    Push_element() - To Push an object containing name and Phone
               number of customers who live in Goa to the stack
        (ii)   Pop_element() - To Pop the objects from the stack and display them.
               Also, display “Stack Empty” when there are no elements in the
               stack.
     For example:
     If the lists of customer details are:


                                               14
```

---

## page 15

```
[“Gurdas”, “99999999999”,”Goa”]
[“Julee”, “8888888888”,”Mumbai”]
[“Murugan”,”77777777777”,”Cochin”]
[“Ashmit”, “1010101010”,”Goa”]

The stack should contain
[“Ashmit”,”1010101010”]
[“Gurdas”,”9999999999”]

The output should be:
[“Ashmit”,”1010101010”]
[“Gurdas”,”9999999999”]
Stack Empty


Ans:

status=[]
def Push_element(cust):
    if cust[2]=="Goa":
        L1=[cust[0],cust[1]]
        status.append(L1)

def Pop_element ():
    num=len(status)
    while len(status)!=0:
        dele=status.pop()
        print(dele)
        num=num-1
    else:
        print("Stack Empty")



(1.5 marks for correct push_element() and 1.5 marks for correct
pop_element())

                                      OR

Write a function in Python, Push(SItem) where , SItem is a dictionary
containing the details of stationary items– {Sname:price}.
The function should push the names of those items in the stack who have price
greater than 75. Also display the count of elements pushed into the stack.
For example:
If the dictionary contains the following data:
Ditem={"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}

The stack should contain
Notebook
Pen

The output should be:

                                           15
```

---

## page 16

```
     The count of elements in the stack is 2

     Ans:
     stackItem=[]
     def Push(SItem):
          count=0
          for k in SItem:
              if (SItem[k]>=75):
                  stackItem.append(k)
                  count=count+1
          print("The count of elements in the stack is :                    ",
     count)


     (1 mark for correct function header
     1 mark for correct loop
     ½ mark for correct If statement
     ½ mark for correct display of count)


                                            SECTION D

31. MakeInIndia Corporation, an Uttarakhand based IT Training company, is planning
    to set up training centres in various cities in next 2 years. Their first campus is
    coming up in Kashipur district. At Kashipur campus, they are planning to have 3
    different blocks for App development, Web designing and Movie Editing. Each
    block has number of computers, which are required to be connected in a
    network for communication, data and resource sharing. As a network consultant
    of this company, you have to suggest the best network related solutions for them
    for issues/problems raised in question nos. (i) to (v), keeping in mind the
    distances between various blocks/locations and other given parameters.




                                                  KASHIPUR
                                         APP       CAMPUS
                                       DEVELOP                  MOVIE
                                        MENT                   EDITING
            MUSSOORIE
             CAMPUS
                                                     WEB
                                                   DESIGNING




     Distance between various blocks/locations:

          Block                                            Distance
          App development to Web designing                   28 m
          App development to Movie editing                   55 m
          Web designing to Movie editing                     32 m
          Kashipur Campus to Mussoorie Campus               232 km

                                                  16
```

---

## page 17

```
Number of computers
    Block                           Number of Computers
   App development                            75
   Web designing                              50
   Movie editing                              80

   (i)      Suggest the most appropriate block/location to house the SERVER in    1
            the Kashipur campus (out of the 3 blocks) to get the best and
            effective connectivity. Justify your answer.

   Ans: Movie editing block is the most appropriate to house the server as
   it has the maximum number of computers.


(1/2 mark for naming the server block and ½ mark for correct reason.)

   (ii)     Suggest a device/software to be installed in the Kashipur Campus to   1
            take care of data security.

   Ans: Firewall
   (1 mark for the correct answer)

  (iii) Suggest the best wired medium and draw the cable layout (Block to         1
    Block) to economically connect various blocks within the Kashipur Campus.
    Ans: Ethernet Cable

   Layout:



                                            KASHIPUR
                                   APP       CAMPUS
                                 DEVELOP                  MOVIE
                                  MENT                   EDITING



                                               WEB
                                             DESIGNING




   ( ½ mark correct wired medium , ½ mark for layout)

  (iv) Suggest the placement of the following devices with appropriate            1
    reasons:
           a. Switch / Hub
           b. Repeater

         Ans: Switch/hub will be placed in all blocks to have connectivity
         within the block.
                                           17
```

---

## page 18

```
           Repeater is not required between the blocks as the distances are less
           than 100 mts.


    (1 mark for the correct answer)

       (v) Suggest the protocol that shall be needed to provide Video Conferencing
         solution between Kashipur Campus and Mussoorie Campus.                      1
         Ans: Protocol: VoIP
    (1 mark for the correct answer)


32. (a) Write the output of the code given below                                     2+3

    p=5
    def sum(q,r=2):
        global p
        p=r+q**2
        print(p, end= '#')


    a=10
    b=5
    sum(a,b)
    sum(r=5,q=1)


    Ans:

    Output:
    105#6#


    (1 mark for 105# and 1 mark for 6#)

    (b) The code given below inserts the following record in the table Student:

              RollNo – integer
              Name – string
              Clas – integer
              Marks – integer

    Note the following to establish connectivity between Python and MYSQL:
               Username is root
               Password is tiger
               The table exists in a MYSQL database named school.
               The details (RollNo, Name, Clas and Marks) are to be
                  accepted from the user.
    Write the following missing statements to complete the code:
    Statement 1 – to form the cursor object
                                              18
```

---

## page 19

```
Statement 2 – to execute the command that inserts the record in the table
Student.
Statement 3- to add the record permanently in the database


import mysql.connector as mysql
def sql_data():
    con1=mysql.connect(host="localhost",user="root",
password="tiger", database="school")
    mycursor=_________________          #Statement 1
    rno=int(input("Enter Roll Number :: "))
    name=input("Enter name :: ")
    clas=int(input("Enter class :: "))
    marks=int(input("Enter Marks :: "))
    querry="insert into student
values({},'{}',{},{})".format(rno,name,clas,marks)
    ______________________              #Statement 2
    ______________________              # Statement 3
    print("Data Added successfully")


Ans:
Statement 1:
con1.cursor()

Statement 2:
mycursor.execute(querry)

Statement 3:
con1.commit()

(1 mark for each correct answer)


                                      OR

   (a) Predict the output of the code given below:

s="welcome2cs"
n = len(s)
m=""
for i in range(0, n):
    if (s[i] >= 'a' and s[i] <= 'm'):
        m =   m +s[i].upper()
    elif (s[i] >= 'n' and s[i] <= 'z'):
        m = m +s[i-1]
    elif (s[i].isupper()):
        m = m + s[i].lower()
    else:
        m = m +'&'
print(m)


                                           19
```

---

## page 20

```
Ans:
sELCcME&Cc

(1 mark for first 5 characters, 1 mark for next 5 characters)


   (b) The code given below reads the following record from the table
       named student and displays only those records who have marks
       greater than 75:
       RollNo – integer
       Name – string
       Clas – integer
       Marks – integer

Note the following to establish connectivity between Python and MYSQL:
          Username is root
          Password is tiger
          The table exists in a MYSQL database named school.

Write the following missing statements to complete the code:
Statement 1 – to form the cursor object
Statement 2 – to execute the query that extracts records of those students
whose marks are greater than 75.
Statement 3- to read the complete result of the query (records whose marks
are greater than 75) into the object named data, from the table student in
the database.

import mysql.connector as mysql
def sql_data():

      con1=mysql.connect(host="localhost",user="root",passwo
      rd="tiger", database="school")
     mycursor=_______________                  #Statement 1
     print("Students with marks greater than 75 are : ")
     _________________________                 #Statement 2
     data=__________________                   #Statement 3
     for i in data:
         print(i)
     print()


Ans:
Statement 1:
con1.cursor()

Statement 2:
mycursor.execute("select * from student where Marks>75")

Statement 3:
mycursor.fetchall()

                                        20
```

---

## page 21

```
     ( 1 mark for each correct statement)

33. What is the advantage of using a csv file for permanent storage?              5
    Write a Program in Python that defines and calls the following user defined
    functions:

        a) ADD() – To accept and add data of an employee to a CSV file
           ‘record.csv’. Each record consists of a list with field elements as
           empid, name and mobile to store employee id, employee name and
           employee salary respectively.
        b) COUNTR() – To count the number of records present in the CSV file
           named ‘record.csv’.


     Ans:
     Advantage of a csv file:
              It is human readable – can be opened in Excel and Notepad
                 applications
              It is just like text file

     Program:

     import csv
     def ADD():
     fout=open("record.csv","a",newline="\n")
        wr=csv.writer(fout)
        empid=int(input("Enter Employee id :: "))
        name=input("Enter name :: ")
        mobile=int(input("Enter mobile number :: "))
        lst=[empid,name,mobile] ---------1/2 mark
        wr.writerow(lst)        ---------1/2 mark
        fout.close()

     def COUNTR():
        fin=open("record.csv","r",newline="\n")
        data=csv.reader(fin)
        d=list(data)
        print(len(d))
        fin.close()

     ADD()
     COUNTR()



     (1 mark for advantage
     ½ mark for importing csv module
     1 ½ marks each for correct definition of ADD() and
     COUNTR()
     ½ mark for function call statements
     )
                                              21
```

---

## page 22

```
                                   OR


Give any one point of difference between a binary file and a csv file.
Write a Program in Python that defines and calls the following user defined
functions:

   a) add() – To accept and add data of an employee to a CSV file
      ‘furdata.csv’. Each record consists of a list with field elements as fid,
      fname and fprice to store furniture id, furniture name and furniture
      price respectively.
   b) search()- To display the records of the furniture whose price is more
      than 10000.


Ans:
Difference between binary file and csv file: (Any one difference may be
given)
Binary file:
           Extension is .dat
           Not human readable
           Stores data in the form of 0s and 1s
CSV file
           Extension is .csv
           Human readable
           Stores data like a text file

Program:

import csv
def add():
    fout=open("furdata.csv","a",newline='\n')
    wr=csv.writer(fout)
    fid=int(input("Enter Furniture Id :: "))
    fname=input("Enter Furniture name :: ")
    fprice=int(input("Enter price :: "))
    FD=[fid,fname,fprice]
    wr.writerow(FD)
    fout.close()

def search():
    fin=open("furdata.csv","r",newline='\n')
    data=csv.reader(fin)
    found=False
    print("The Details are")
    for i in data:
        if int(i[2])>10000:
            found=True
            print(i[0],i[1],i[2])
    if found==False:
        print("Record not found")

                                          22
```

---

## page 23

```
          fin.close()
      add()
      print("Now displaying")
      search()


      (1 mark for difference
      ½ mark for importing csv module
      1 ½ marks each for correct definition of add() and
      search()
      ½ mark for function call statements
      )

                                          SECTION E
34.    Navdeep creates a table RESULT with a set of records to maintain the marks       1+1+2
       secured by students in Sem 1, Sem2, Sem3 and their division. After creation
       of the table, he has entered data of 7 students in the table.

       Table: RESULT

      ROLL_NO SNAME          SEM1 SEM2 SEM3 DIVISION

         101        KARAN    366   410   402      I

         102        NAMAN    300   350   325      I

         103         ISHA    400   410   415      I

         104        RENU     350   357   415      I

         105        ARPIT    100    75   178     IV

         106        SABINA   100   205   217     II

         107       NEELAM    470   450   471      I



      Based on the data given above answer the following questions:

       i.      Identify the most appropriate column, which can be considered as
               Primary key.
         Ans: ROLL_NO

         (1 mark for correct answer)

       ii.     If two columns are added and 2 rows are deleted from the table result,
               what will be the new degree and cardinality of the above table?
         Ans:
         New Degree: 8
         New Cardinality: 5

         (1/2 mark for correct degree and ½ mark for correct cardinality)
                                                  23
```

---

## page 24

```
     iii.   Write the statements to:
               a. Insert the following record into the table – Roll No- 108, Name-
                   Aadit, Sem1- 470, Sem2-444, Sem3-475, Div – I.
               b. Increase the SEM2 marks of the students by 3% whose name
                   begins with ‘N’.
    Ans:
       a. INSERT INTO RESULT VALUES (108, ‘Aadit’, 470, 444, 475, ‘I’);
       b. UPDATE RESULT SET SEM2=SEM2+ (SEM2*0.03) WHERE SNAME LIKE
          “N%”;
        (1 mark for each correct statement)

                                    OR (Option for Part iii only)

    iii. Write the statements to:
                a. Delete the record of students securing IV division.
                b. Add a column REMARKS in the table with datatype as varchar with
                   50 characters
    Ans:
       a. DELETE FROM RESULT WHERE DIV=’IV’;
       b. ALTER TABLE RESULT ADD (REMARKS VARCHAR(50));
        (1 mark for each correct statement)

35. Aman is a Python programmer. He has written a code and created a binary file
    record.dat with employeeid, ename and salary. The file contains 10
    records.
    He now has to update a record based on the employee id entered by the user
    and update the salary. The updated record is then to be written in the file
    temp.dat. The records which are not to be updated also have to be written
    to the file temp.dat. If the employee id is not found, an appropriate message
    should to be displayed.
    As a Python expert, help him to complete the following code based on the
    requirement given above:


    import _______                               #Statement 1
    def update_data():
       rec={}
       fin=open("record.dat","rb")
       fout=open("_____________")                #Statement 2
       found=False
       eid=int(input("Enter employee id to update their salary
       :: "))
       while True:
         try:
           rec=______________                     #Statement 3
           if rec["Employee id"]==eid:
                found=True

                                               24
```

---

## page 25

```
                 rec["Salary"]=int(input("Enter new salary ::
           "))
            pickle.____________              #Statement 4
       else:
            pickle.dump(rec,fout)
     except:
       break
   if found==True:
     print("The salary of employee id ",eid," has been
     updated.")
   else:
     print("No employee with such id is not found")
  fin.close()
  fout.close()


       (i) Which module should be imported in the program? (Statement 1)
                                                                             1
 Ans: pickle

   (1 mark for correct module)

      (ii)Write the correct statement required to open a temporary file named 1
      temp.dat for writing the updated data. (Statement 2)
 Ans: fout=open(‘temp.dat’, ‘wb’)

(1 mark for correct statement)

   (iii) Which statement should Aman fill in Statement 3 to read the data
         from the binary file, record.dat and in Statement 4 to write the    2
         updated data in the file, temp.dat?
 Ans: Statement 3: pickle.load(fin)
      Statement 4: pickle.dump(rec,fout)

(1 mark for each correct statement)




                                         25
```