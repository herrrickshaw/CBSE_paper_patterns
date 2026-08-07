---
title: "ComputerScience-SQP"
source_pdf: "ComputerScience-SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/ComputerScience-SQP.pdf"
pages: 14
pdf_bytes: 730033
pdf_sha256: "08999d6a627bf51a37c864b04b676f4c5dbf453d275e491bacc51369270b1e00"
text_chars: 26374
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-SQP


---

## page 1

```
                             Class: XII Session: 2022-23
                              Computer Science (083)
                          Sample Question Paper (Theory)
Maximum Marks: 70                                            Time Allowed: 3 hours
General Instructions:
     1. This question paper contains five sections, Section A to E.
     2. All questions are compulsory.
     3. Section A have 18 questions carrying 01 mark each.
     4. Section B has 07 Very Short Answer type questions carrying 02 marks each.
     5. Section C has 05 Short Answer type questions carrying 03 marks each.
     6. Section D has 03 Long Answer type questions carrying 05 marks each.
     7. Section E has 02 questions carrying 04 marks each. One internal choice is
        given in Q35 against part c only.
     8. All programming questions are to be answered using Python Language only.


                                      SECTION A
1.    State True or False                                                        1
       “Variable declaration is implicit in Python.”

2.    Which of the following is an invalid datatype in Python?                   1
        (a) Set (b) None (c)Integer (d)Real


3.    Given the following dictionaries                                           1

      dict_exam={"Exam":"AISSCE", "Year":2023}
      dict_result={"Total":500, "Pass_Marks":165}

      Which statement will merge the contents of both dictionaries?
        a. dict_exam.update(dict_result)
        b. dict_exam + dict_result
        c. dict_exam.add(dict_result)
        d. dict_exam.merge(dict_result)


4.    Consider the given expression:                                             1
      not True and False or True
      Which of the following will be correct output if the given expression is
      evaluated?

          (a) True
          (b) False
          (c) NONE
          (d) NULL

5.    Select the correct output of the code:                                     1
      a = "Year 2022 at All the best"
                                           1
```

---

## page 2

```
     a = a.split('2')
     b = a[0] + ". " + a[1] + ". " + a[3]
     print (b)

        (a) Year . 0. at All the best
        (b) Year 0. at All the best
        (c) Year . 022. at All the best
        (d) Year . 0. at all the best


6.   Which of the following mode in file opening statement results or      1
     generates an error if the file does not exist?

        (a) a+    (b) r+   (c) w+    (d) None of the above


7.   Fill in the blank:                                                    1

     ______ command is used to remove primary key from the table in SQL.

        (a) update           (b)remove          (c) alter       (d)drop


8.      Which of the following commands will delete the table from MYSQL   1
        database?
        (a)       DELETE TABLE
        (b)       DROP TABLE
        (c)       REMOVE TABLE
        (d)       ALTER TABLE

9.   Which of the following statement(s) would give an error after         1
     executing the following code?

     S="Welcome to class XII"                 # Statement 1
     print(S)                                 # Statement 2
     S="Thank you"                            # Statement 3
     S[0]= '@'                                 # Statement 4
     S=S+"Thank you"                          # Statement 5

     (a)    Statement 3
     (b)    Statement 4
     (c)    Statement 5
     (d)    Statement 4 and 5


10. Fill in the blank:                                                     1

     _________ is a non-key attribute, whose values are derived from the
     primary key of some other table.
        (a) Primary Key
        (b) Foreign Key
        (c) Candidate Key

                                          2
```

---

## page 3

```
        (d) Alternate Key


11. The correct syntax of seek() is:                                       1
    (a) file_object.seek(offset [, reference_point])
    (b) seek(offset [, reference_point])
    (c) seek(offset, file_object)
    (d) seek.file_object(offset)
12. Fill in the blank:                                                     1
    The SELECT statement when combined with __________ clause,
    returns records without repetition.

        (a)         DESCRIBE
        (b)         UNIQUE
        (c)         DISTINCT
        (d)         NULL


13. Fill in the blank:                                                     1
    ______is a communication methodology designed to deliver both voice
    and multimedia communications over Internet protocol.

        (a) VoIP            (b) SMTP        (c) PPP     (d)HTTP


14. What will the following expression be evaluated to in Python?          1
    print(15.0 / 4 + (8 + 3.0))

        (a) 14.75           (b)14.0         (c) 15      (d) 15.5


15. Which function is used to display the total number of records from     1
    table in a database?
       (a)        sum(*)
       (b)        total(*)
       (c)        count(*)
       (d)        return(*)


16. To establish a connection between Python and SQL database,             1
    connect() is used. Which of the following arguments may not
    necessarily be given while calling connect() ?

     (a)   host
     (b)   database
     (c)   user
     (d)   password


Q17 and 18 are ASSERTION AND REASONING based questions. Mark the correct
choice as
   (a) Both A and R are true and R is the correct explanation for A

                                        3
```

---

## page 4

```
   (b) Both A and R are true and R is not the correct explanation for A
   (c) A is True but R is False
   (d) A is false but R is True


17. Assertion (A):- If the arguments in function call statement match the      1
    number and order of arguments as defined in the function definition,
    such arguments are called positional arguments.
    Reasoning (R):- During a function call, the argument list first contains
    default argument(s) followed by positional argument(s).

18. Assertion (A): CSV (Comma Separated Values) is a file format for data      1
    storage which looks like a text file.
    Reason (R): The information is organized with one record on each line
    and each field is separated by comma.

                                    SECTION B
19. Rao has written a code to input a number and check whether it is           2
    prime or not. His code is having errors. Rewrite the correct code and
    underline the corrections made.

     def prime():
       n=int(input("Enter number to check :: ")
       for i in range (2, n//2):
         if n%i=0:
           print("Number is not prime \n")
         break
         else:
           print("Number is prime \n’)

20. Write two points of difference between Circuit Switching and Packet        2
    Switching.

                                     OR

     Write two points of difference between XML and HTML.

21. (a) Given is a Python string declaration:                                  1
           myexam="@@CBSE Examination 2022@@"

            Write the output of: print(myexam[::-2])

                                                                               1
     (b) Write the output of the code given below:
            my_dict = {"name": "Aman", "age": 26}
            my_dict['age'] = 27
            my_dict['address'] = "Delhi"
            print(my_dict.items())


22. Explain the use of ‘Foreign Key’ in a Relational Database Management       2
    System. Give example to support your answer.

                                          4
```

---

## page 5

```
23. (a) Write the full forms of the following:                          2
      (i) SMTP    (ii) PPP

      (b) What is the use of TELNET?



24. Predict the output of the Python code given below:                  2

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

                                        OR

      Predict the output of the Python code given below:

      tuple1 = (11, 22, 33, 44, 55 ,66)
      list1 =list(tuple1)
      new_list = []
      for i in list1:
          if i%2==0:
              new_list.append(i)
      new_tuple = tuple(new_list)
      print(new_tuple)

25. Differentiate between count() and count(*) functions in SQL with    2
    appropriate example.

                                       OR

      Categorize the following commands as DDL or DML:
      INSERT, UPDATE, ALTER, DROP


                                       SECTION C

26.      (a) Consider the following tables – Bank_Account and Branch:   1+2

      Table: Bank_Account
       ACode     Name         Type
       A01       Amrita       Savings
       A02       Parthodas    Current
       A03       Miraben      Current
                                            5
```

---

## page 6

```
     Table: Branch

      ACode     City
      A01       Delhi
      A02       Mumbai
      A01       Nagpur

     What will be the output of the following statement?


     SELECT * FROM Bank_Account NATURAL JOIN Branch;


        (b) Write the output of the queries (i) to (iv) based on the table,
            TECH_COURSE given below:

                         Table: TECH_COURSE
        CID      CNAME                 FEES          STARTDATE       TID
        C201     Animation and VFX     12000         2022-07-02      101
        C202     CADD                  15000         2021-11-15      NULL
        C203     DCA                   10000         2020-10-01      102
        C204     DDTP                   9000         2021-09-15      104
        C205     Mobile Application    18000         2022-11-01      101
                 Development
        C206     Digital marketing     16000         2022-07-25      103


       (i)      SELECT DISTINCT TID FROM TECH_COURSE;
       (ii)     SELECT TID, COUNT(*), MIN(FEES) FROM
           TECH_COURSE GROUP BY TID HAVING COUNT(TID)>1;
      (iii)     SELECT CNAME FROM TECH_COURSE WHERE
        FEES>15000 ORDER BY CNAME;
      (iv)      SELECT AVG(FEES) FROM TECH_COURSE WHERE
        FEES BETWEEN 15000 AND 17000;
27. Write a method COUNTLINES() in Python to read lines from text file        3
    ‘TESTFILE.TXT’ and display the lines which are not starting with any
    vowel.

     Example:

     If the file content is as follows:

     An apple a day keeps the doctor away.
     We all pray for everyone’s safety.
     A marked difference will come in our country.

     The COUNTLINES() function should display the output as:


                                          6
```

---

## page 7

```
     The number of lines not starting with any vowel - 1

                                          OR

     Write a function ETCount() in Python, which should read each
     character of a text file “TESTFILE.TXT” and then count and display
     the count of occurrence of alphabets E and T individually (including
     small cases e and t too).

     Example:

     If the file content is as follows:

     Today is a pleasant day.
     It might rain today.
     It is mentioned on weather sites

     The ETCount() function should display the output as:
     E or e: 6
     T or t : 9

28. (a) Write the outputs of the SQL queries (i) to (iv) based on the            3
    relations Teacher and Placement given below:

     Table : Teacher

      T_ID   Name        Age   Department       Date_of_join   Salary   Gender
      1      Arunan      34    Computer Sc      2019-01-10     12000    M
      2      Saman       31    History          2017-03-24     20000    F
      3      Randeep     32    Mathematics      2020-12-12     30000    M
      4      Samira      35    History          2018-07-01     40000    F
      5      Raman       42    Mathematics      2021-09-05     25000    M
      6      Shyam       50    History          2019-06-27     30000    M
      7      Shiv        44    Computer Sc      2019-02-25     21000    M
      8      Shalakha    33    Mathematics      2018-07-31     20000    F

     Table : Placement
      P_ID       Department                    Place
      1          History                       Ahmedabad
      2          Mathematics                   Jaipur
      3          Computer Sc                   Nagpur

    (i)      SELECT Department, avg(salary) FROM Teacher
             GROUP BY Department;
   (ii)      SELECT MAX(Date_of_Join),MIN(Date_of_Join) FROM
             Teacher;
 (iii)       SELECT Name, Salary, T.Department, Place FROM
             Teacher T, Placement P WHERE T.Department =
             P.Department AND Salary>20000;
   (iv)      SELECT Name, Place FROM Teacher T, Placement P

                                           7
```

---

## page 8

```
            WHERE Gender =’F’ AND T.Department=P.Department;
     (b) Write the command to view all tables in a database.

29. Write a function INDEX_LIST(L), where L is the list of elements passed    3
    as argument to the function. The function returns another list named
    ‘indexList’ that stores the indices of all Non-Zero Elements of L.

     For example:

     If L contains [12,4,0,11,0,56]

     The indexList will have - [0,1,3,5]

30. A list contains following record of a customer:                           3
    [Customer_name, Phone_number, City]

     Write the following user defined functions to perform given operations
     on the stack named ‘status’:
        (i)    Push_element() - To Push an object containing name and
               Phone number of customers who live in Goa to the stack
        (ii)   Pop_element() - To Pop the objects from the stack and
               display them. Also, display “Stack Empty” when there are no
               elements in the stack.
     For example:
     If the lists of customer details are:

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


                                      OR

     Write a function in Python, Push(SItem) where , SItem is a dictionary
     containing the details of stationary items– {Sname:price}.
     The function should push the names of those items in the stack who
     have price greater than 75. Also display the count of elements pushed
     into the stack.
     For example:
     If the dictionary contains the following data:
                                             8
```

---

## page 9

```
     Ditem={"Pen":106,"Pencil":59,"Notebook":80,"Eraser":25}

     The stack should contain
     Notebook
     Pen

     The output should be:
     The count of elements in the stack is 2

                                    SECTION D
31. MakeInIndia Corporation, an Uttarakhand based IT training company,
    is planning to set up training centres in various cities in next 2 years.
    Their first campus is coming up in Kashipur district. At Kashipur
    campus, they are planning to have 3 different blocks for App
    development, Web designing and Movie editing. Each block has
    number of computers, which are required to be connected in a
    network for communication, data and resource sharing. As a network
    consultant of this company, you have to suggest the best network
    related solutions for them for issues/problems raised in question nos.
    (i) to (v), keeping in mind the distances between various
    blocks/locations and other given parameters.
                                                  KASHIPUR
                                          APP      CAMPUS
                                       DEVELOPM                 MOVIE
                                          ENT                  EDITING
              MUSSOORIE
               CAMPUS
                                                    WEB
                                                  DESIGNING




     Distance between various blocks/locations:

            Block                                         Distance
            App development to Web designing                28 m
            App development to Movie editing                55 m
            Web designing to Movie editing                  32 m
            Kashipur Campus to Mussoorie Campus            232 km

     Number of computers
         Block                             Number of Computers
        App development                              75
        Web designing                                50
        Movie editing                                80

      (i)    Suggest the most appropriate block/location to house the
             SERVER in the Kashipur campus (out of the 3 blocks) to get the     1
             best and effective connectivity. Justify your answer.
     (ii)   Suggest a device/software to be installed in the Kashipur
                                                                                1
          Campus to take care of data security.
    (iii) Suggest the best wired medium and draw the cable layout (Block
                                                                                1
                                            9
```

---

## page 10

```
         to Block) to economically connect various blocks within the
         Kashipur Campus.
    (iv) Suggest the placement of the following devices with appropriate   1
         reasons:
               a. Switch / Hub
               b. Repeater
                                                                           1
     (v) Suggest a protocol that shall be needed to provide Video
         Conferencing solution between Kashipur Campus and Mussoorie
         Campus.
32. (a) Write the output of the code given below:                          2+3

     p=5
     def sum(q,r=2):
         global p
         p=r+q**2
         print(p, end= '#')


     a=10
     b=5
     sum(a,b)
     sum(r=5,q=1)


     (b) The code given below inserts the following record in the table
     Student:

              RollNo – integer
              Name – string
              Clas – integer
              Marks – integer

     Note the following to establish connectivity between Python and
     MYSQL:
                Username is root
                Password is tiger
                The table exists in a MYSQL database named school.
                The details (RollNo, Name, Clas and Marks) are to
                   be accepted from the user.
     Write the following missing statements to complete the code:
     Statement 1 – to form the cursor object
     Statement 2 – to execute the command that inserts the record in the
     table Student.
     Statement 3- to add the record permanently in the database


     import mysql.connector as mysql
     def sql_data():
         con1=mysql.connect(host="localhost",user="root",

                                        10
```

---

## page 11

```
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


(b) The code given below reads the following record from the table
    named student and displays only those records who have
    marks greater than 75:
       RollNo – integer
       Name – string
       Clas – integer
       Marks – integer

Note the following to establish connectivity between Python and
MYSQL:
          Username is root
          Password is tiger
          The table exists in a MYSQL database named school.

Write the following missing statements to complete the code:
Statement 1 – to form the cursor object
Statement 2 – to execute the query that extracts records of those
students whose marks are greater than 75.
Statement 3- to read the complete result of the query (records whose
                                   11
```

---

## page 12

```
      marks are greater than 75) into the object named data, from the
      table student in the database.

      import mysql.connector as mysql
      def sql_data():

              con1=mysql.connect(host="localhost",user="root",
              password="tiger", database="school")
             mycursor=_______________           #Statement 1
             print("Students with marks greater than 75 are :
      ")
             _________________________                          #Statement 2
             data=__________________                            #Statement 3
             for i in data:
                 print(i)
             print()

33. What is the advantage of using a csv file for permanent storage?                    5
    Write a Program in Python that defines and calls the following user
    defined functions:

           (i) ADD() – To accept and add data of an employee to a CSV file
                ‘record.csv’. Each record consists of a list with field elements
                as empid, name and mobile to store employee id, employee
                name and employee salary respectively.
           (ii) COUNTR() – To count the number of records present in the CSV
                file named ‘record.csv’.
                                     OR

      Give any one point of difference between a binary file and a csv file.
      Write a Program in Python that defines and calls the following user
      defined functions:

                 (i)    add() – To accept and add data of an employee to a CSV
                        file ‘furdata.csv’. Each record consists of a list with field
                        elements as fid, fname and fprice to store furniture
                        id, furniture name and furniture price respectively.
                 (ii)   search()- To display the records of the furniture whose
                        price is more than 10000.


                                    SECTION E
34.    Navdeep creates a table RESULT with a set of records to maintain                 1+1+2
       the marks secured by students in Sem 1, Sem2, Sem3 and their
       division. After creation of the table, he has entered data of 7
       students in the table.

      ROLL_NO SNAME             SEM1 SEM2 SEM3      DIVISION

           101          KARAN   366    410   402        I

           102          NAMAN   300    350   325        I

                                               12
```

---

## page 13

```
        103         ISHA    400   410    415        I

        104        RENU     350   357    415        I

        105        ARPIT    100   75     178       IV

        106        SABINA   100   205    217        II

        107       NEELAM    470   450    471        I



     Based on the data given above answer the following questions:

      (i)     Identify the most appropriate column, which can be considered
              as Primary key.
     (ii)     If two columns are added and 2 rows are deleted from the table
              result, what will be the new degree and cardinality of the
              above table?
    (iii)     Write the statements to:
                  a. Insert the following record into the table
                     Roll No- 108, Name- Aadit, Sem1- 470, Sem2-444, Sem3-
                     475, Div – I.
                  b. Increase the SEM2 marks of the students by 3% whose
                     name begins with ‘N’.
                                       OR (Option for part iii only)

     (iii) Write the statements to:
                a. Delete the record of students securing IV division.
                b. Add a column REMARKS in the table with datatype as
                    varchar with 50 characters


35. Aman is a Python programmer. He has written a code and created a
    binary file record.dat with employeeid, ename and salary. The file
    contains 10 records.
    He now has to update a record based on the employee id entered by
    the user and update the salary. The updated record is then to be
    written in the file temp.dat. The records which are not to be
    updated also have to be written to the file temp.dat. If the
    employee id is not found, an appropriate message should to be
    displayed.
    As a Python expert, help him to complete the following code based on
    the requirement given above:

     import _______                         #Statement 1
     def update_data():
        rec={}
        fin=open("record.dat","rb")
        fout=open("_____________")          #Statement 2
        found=False
        eid=int(input("Enter employee id to update their
                                           13
```

---

## page 14

```
        salary :: "))
        while True:
          try:
            rec=______________                #Statement 3
            if rec["Employee id"]==eid:
                  found=True
                  rec["Salary"]=int(input("Enter new salary
            :: "))
                  pickle.____________        #Statement 4
            else:
                  pickle.dump(rec,fout)
          except:
            break
        if found==True:
          print("The salary of employee id ",eid," has
          been updated.")
        else:
          print("No employee with such id is not found")
        fin.close()
        fout.close()
                                                                          1
 (i)      Which module should be imported in the program? (Statement
                                                                          1
          1)
(ii)      Write the correct statement required to open a temporary file
          named temp.dat. (Statement 2)                                   2
(iii)     Which statement should Aman fill in Statement 3 to read the
          data from the binary file, record.dat and in Statement 4 to
          write the updated data in the file, temp.dat?




                                      14
```