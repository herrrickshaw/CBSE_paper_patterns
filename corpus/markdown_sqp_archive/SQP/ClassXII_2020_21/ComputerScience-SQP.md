---
title: "ComputerScience-SQP"
source_pdf: "ComputerScience-SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/ComputerScience-SQP.pdf"
pages: 11
pdf_bytes: 290120
pdf_sha256: "fee433166c1b4b16df58f178e84c37bd582d1bb85dc0d9e846599494b7114038"
text_chars: 20822
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-SQP


---

## page 1

```
                                       Class: XII Session: 2020-21
                                        Computer Science (083)
                                   Sample Question Paper (Theory)
    Maximum Marks: 70                                                            Time Allowed: 3 hours


General Instructions:
       1. This question paper contains two parts A and B. Each part is compulsory.
       2. Both Part A and Part B have choices.
       3. Part-A has 2 sections:
              a. Section – I is short answer questions, to be answered in one word or one line.
              b. Section – II has two case studies questions. Each case study has 4 case-based sub-
                  parts. An examinee is to attempt any 4 out of the 5 subparts.
       4. Part - B is Descriptive Paper.
       5. Part- B has three sections
           a. Section-I is short answer questions of 2 marks each in which two question have
              internal options.
           b. Section-II is long answer questions of 3 marks each in which two questions have internal
              options.
          c. Section-III is very long answer questions of 5 marks each in which one question has
             internal option.
       6. All programming questions are to be answered using Python Language only


Question                                             Part-A                                    Marks
No.                                                                                            allocated
                                                     Section-I
             Select the most appropriate option out of the options given for each
             question. Attempt any 15 questions from question no 1 to 21.


1            Find the invalid identifier from the following                                    1
                         a) MyName         b) True     c) 2ndName         d) My_Name


2            Given the lists L=[1,3,6,82,5,7,11,92] , write the output of print(L[2:5])        1


3            Write the full form of CSV.                                                       1


4            Identify the valid arithmetic operator in Python from the following.              1
                         a) ?          b) <          c) **       d) and


                                                                                              Page 1 of 11
```

---

## page 2

```
5    Suppose a tuple T is declared as T = (10, 12, 43, 39), which of the following is    1
     incorrect?
          a) print(T[1])
          b) T[2] = -29
          c) print(max(T))
          d) print(len(T))


6    Write a statement in Python to declare a dictionary whose keys are 1, 2, 3          1
     and values are Monday, Tuesday and Wednesday respectively.


7    A tuple is declared as                                                              1
             T = (2,5,6,9,8)
     What will be the value of sum(T)?


8    Name the built-in mathematical function / method that is used to return an          1
     absolute value of a number.


9    Name the protocol that is used to send emails.                                      1


10   Your friend Ranjana complaints that somebody has created a fake profile on          1
     Facebook and defaming her character with abusive comments and pictures.
     Identify the type of cybercrime for these situations.


11   In SQL, name the clause that is used to display the tuples in ascending order       1
     of an attribute.


12   In SQL, what is the use of IS NULL operator?                                        1

13   Write any one aggregate function used in SQL.                                       1

14   Which of the following is a DDL command?                                            1
       a) SELECT b) ALTER            c) INSERT       d) UPDATE

15   Name The transmission media best suitable for connecting to hilly areas.            1

16   Identify the valid declaration of L:                                                1
                    L = [‘Mon’, ‘23’, ‘hello’, ’60.5’]


                                                                                        Page 2 of 11
```

---

## page 3

```
       a. dictionary     b. string   c.tuple   d. list
17   If the following code is executed, what will be the output of the following    1
     code?


              name="ComputerSciencewithPython"
              print(name[3:10])


18   In SQL, write the query to display the list of tables stored in a database.    1


19   Write the expanded form of Wi-Fi.                                              1


20   Which of the following types of table constraints will prevent the entry of    1
     duplicate rows?
                     a) Unique
                     b) Distinct
                     c) Primary Key
                     d) NULL


21   Rearrange the following terms in increasing order of data transfer rates.      1
     Gbps, Mbps, Tbps, Kbps, bps
                                          Section-II
     Both the Case study based questions are compulsory. Attempt any 4
     sub parts from each question. Each question carries 1 mark


22   A departmental store MyStore is considering to maintain their inventory
     using SQL to store the data. As a database administer, Abhay has decided
     that :
         •    Name of the database - mystore
         •    Name of the table - STORE
         •    The attributes of STORE are as follows:
                     ItemNo - numeric
                     ItemName – character of size 20
                     Scode - numeric
                     Quantity – numeric




                                                                                   Page 3 of 11
```

---

## page 4

```
                    Table : STORE
                    ItemNo   ItemName                  Scode    Quantity
                    2005     Sharpener Classic           23     60
                    2003     Ball Pen 0.25               22     50
                    2002     Get Pen Premium             21     150
                    2006     Get Pen Classic             21     250
                    2001     Eraser Small                22     220
                    2004     Eraser Big                  22     110
                    2009     Ball Pen 0.5                21     180
        (a) Identify the attribute best suitable to be declared as a primary key,     1
        (b) Write the degree and cardinality of the table STORE.                      1

        (c) Insert the following data into the attributes ItemNo, ItemName and        1
            SCode respectively in the given table STORE.
            ItemNo = 2010, ItemName = “Note Book” and Scode = 25
        (d) Abhay want to remove the table STORE from the database MyStore.           1
            Which command will he use from the following:
                   a) DELETE FROM store;
                   b) DROP TABLE store;
                   c) DROP DATABASE mystore;
                   d) DELETE store FROM mystore;


        (e) Now Abhay wants to display the structure of the table STORE, i.e,         1
            name of the attributes and their respective data types that he has
            used in the table. Write the query to display the same.


23   Ranjan Kumar of class 12 is writing a program to create a CSV file “user.csv”
     which will contain user name and password for some entries. He has written
     the following code. As a programmer, help him to successfully execute the
     given task.


     import _____________                                             # Line 1


     def addCsvFile(UserName,PassWord):            # to write / add data into the
     CSV file
        f=open(' user.csv','________')                                 # Line 2



                                                                                     Page 4 of 11
```

---

## page 5

```
        newFileWriter = csv.writer(f)
        newFileWriter.writerow([UserName,PassWord])
        f.close()


     #csv file reading code
     def readCsvFile():                     # to read data from CSV file
       with open(' user.csv','r') as newFile:
              newFileReader = csv._________(newFile)                       # Line 3
              for row in newFileReader:
                    print (row[0],row[1])
       newFile.______________                                              # Line 4


     addCsvFile(“Arjun”,”123@456”)
     addCsvFile(“Arunima”,”aru@nima”)
     addCsvFile(“Frieda”,”myname@FRD”)
     readCsvFile()                                                         #Line 5


      (a) Name the module he should import in Line 1.                                  1

      (b) In which mode, Ranjan should open the file to add data into the file         1
      (c) Fill in the blank in Line 3 to read the data from a csv file.                1
      (d) Fill in the blank in Line 4 to close the file.                               1
      (e) Write the output he will obtain while executing Line 5.                      1
                                             Part – B


                                            Section-I
24   Evaluate the following expressions:                                               2
        a) 6 * 3 + 4**2 // 5 – 8
        b) 10 > 5 and 7 > 12 or not 18 > 3


25   Differentiate between Viruses and Worms in context of networking and data         2
     communication threats.
                                              OR
     Differentiate between Web server and web browser. Write any two popular
     web browsers.
26   Expand the following terms:                                                       2
                    a.   SMTP       b. XML     c. LAN      d. IPR

                                                                                      Page 5 of 11
```

---

## page 6

```
27   Differentiate between actual parameter(s) and a formal parameter(s) with a         2
     suitable example for each.
                                           OR
     Explain the use of global key word used in a function with the help of a
     suitable example.


28   Rewrite the following code in Python after removing all syntax error(s).           2
     Underline each correction done in the code.


          Value=30
          for VAL in range(0,Value)
              If val%4==0:
                  print (VAL*4)
              Elseif val%5==0:
                 print (VAL+3)
              else
                 print(VAL+10)


29   What possible outputs(s) are expected to be displayed on screen at the time        2
     of execution of the program from the following code? Also specify the
     maximum values that can be assigned to each of the variables Lower and
     Upper.


     import random
     AR=[20,30,40,50,60,70];
     Lower =random.randint(1,3)
     Upper =random.randint(2,4)
     for K in range(Lower, Upper +1):
        print (AR[K],end=”#“)


     (i) 10#40#70#           (ii) 30#40#50#         (iii) 50#60#70#             (iv)
     40#50#70#




30   What do you understand by Candidate Keys in a table? Give a suitable               2
     example of Candidate Keys from a table containing some meaningful data.


                                                                                       Page 6 of 11
```

---

## page 7

```
31   Differentiate between fetchone() and fetchall() methods with suitable              2
     examples for each.
32   Write the full forms of DDL and DML. Write any two commands of DML in              2
     SQL.
33   Find and write the output of the following Python code:                            2


     def Display(str):
          m=""
          for i in range(0,len(str)):
             if(str[i].isupper()):
                     m=m+str[i].lower()
             elif str[i].islower():
                     m=m+str[i].upper()
             else:
                 if i%2==0:
                     m=m+str[i-1]
                 else:
                     m=m+"#"
          print(m)


     Display('Fun@Python3.0')


                                        Section- II


34   Write a function LShift(Arr,n) in Python, which accepts a list Arr of numbers      3
     and n is a numeric value by which all elements of the list are shifted to left.
      Sample Input Data of the list
      Arr= [ 10,20,30,40,12,11], n=2
      Output
      Arr = [30,40,12,11,10,20]


35   Write a function in Python that counts the number of “Me” or “My” words            3
     present in a text file “STORY.TXT”.
               If the “STORY.TXT” contents are as follows:
               My first book
               was Me and


                                                                                       Page 7 of 11
```

---

## page 8

```
              My Family. It
              gave me
              chance to be
              Known to the
              world.


          The output of the function should be:
                     Count of Me/My in file: 4


                                              OR


      Write a function AMCount() in Python, which should read each character
      of a text file STORY.TXT, should count and display the occurance of
      alphabets A and M (including small cases a and m too).
      Example:
      If the file content is as follows:
              Updated information
              As simplified by official websites.
      The EUCount() function should display the output as:
              A or a:4
              M or m :2


36   Write the outputs of the SQL queries (i) to (iii) based on the relations Teacher    3
     and Posting given below:


       Table : Teacher
       T_ID Name            Age     Department      Date_of_join   Salary   Gender
           1 Jugal            34    Computer Sc      10/01/2017    12000    M
           2 Sharmila         31    History          24/03/2008    20000    F
           3 Sandeep          32    Mathematics      12/12/2016    30000    M
           4 Sangeeta         35    History          01/07/2015    40000    F
           5 Rakesh           42    Mathematics      05/09/2007    25000    M
           6 Shyam            50    History          27/06/2008    30000    M
           7 Shiv Om          44    Computer Sc      25/02/2017    21000    M
           8 Shalakha         33    Mathematics      31/07/2018    20000    F



                                                                                        Page 8 of 11
```

---

## page 9

```
                              Table : Posting
                              P_ID     Department              Place
                              1        History                 Agra
                              2        Mathematics             Raipur
                              3        Computer Science        Delhi


                        i.        SELECT Department, count(*) FROM Teacher
                                  GROUP BY Department;
                       ii.        SELECT Max(Date_of_Join),Min(Date_of_Join)
                                  FROM Teacher;
                       iii.       SELECT Teacher.name,Teacher.Department,
                                  Posting.Place FROM Teachr, Posting WHERE
                                  Teacher.Department = Posting.Department AND
                                  Posting.Place=”Delhi”;


37   Write a function in Python PUSH(Arr), where Arr is a list of numbers. From       3
     this list push all numbers divisible by 5 into a stack implemented by using a
     list. Display the stack if it has at least one element, otherwise display
     appropriate error message.
                                                 OR
     Write a function in Python POP(Arr), where Arr is a stack implemented by a
     list of numbers. The function returns the value deleted from the stack.


                                                 Section-III
38   MyPace University is setting up its academic blocks at Naya Raipur               5
     and is planning to set up a network. The University has 3 academic
     blocks and one Human Resource Center as shown in the diagram
     below:




          Center to Center distances between various blocks/center is as follows:

                                                                                     Page 9 of 11
```

---

## page 10

```
                         Law Block to business Block           40m
                         Law block to Technology Block         80m
                         Law Block to HR center                105m
                         Business Block to technology
                                                               30m
                         Block
                         Business Block to HR Center           35m
                         Technology block to HR center         15m
        Number of computers in each of the blocks/Center is as follows:
                         Law Block               15
                         Technology Block        40
                         HR center               115
                         Business Block          25


           a) Suggest the most suitable place (i.e., Block/Center) to install
             the server of this University with a suitable reason.
           b) Suggest an ideal layout for connecting these blocks/centers for a
             wired connectivity.
           c) Which device will you suggest to be placed/installed in each
             of these blocks/centers to efficiently connect all the
             computers within these blocks/centers.
           d) Suggest the placement of a Repeater in the network

             with justification.
           e) The university is planning to connect its admission office in
             Delhi, which is more than 1250km from university. Which
             type of network out of LAN, MAN, or WAN will be formed?
             Justify your answer.




39   Write SQL commands for the following queries (i) to (v) based on the                5
     relations Teacher and Posting given below:

      Table : Teacher
     T_ID Name          Age Department        Date_of_join       Salary       Gender
                               Computer
       1    Jugal       34                      10/01/2017       12000        M
                               Sc
       2    Sharmila    31     History          24/03/2008       20000        F


                                                                                       Page 10 of 11
```

---

## page 11

```
       3      Sandeep 32           Mathematics      12/12/2016       30000      M
       4      Sangeeta 35          History          01/07/2015       40000      F
       5      Rakesh        42     Mathematics      05/09/2007       25000      M
       6      Shyam         50     History          27/06/2008       30000      M
                                   Computer
       7      Shiv Om       44                      25/02/2017       21000      M
                                   Sc
       8      Shalakha 33          Mathematics      31/07/2018       20000      F


                           Table : Posting
                           P_ID      Department             Place
                           1         History                Agra
                           2         Mathematics            Raipur
                           3         Computer Science       Delhi


            i.       To show all information about the teacher of History
                     department.
           ii.       To list the names of female teachers who are in Mathematics
                     department.
           iii.      To list the names of all teachers with their date of joining in
                     ascending order.
           iv.       To display teacher’s name, salary, age for male teachers only.
           v.        To display name, bonus for each teacher where bonus is 10%
                     of salary.
40                                                                                       5
     A binary file “Book.dat” has structure [BookNo, Book_Name, Author, Price].
                  i. Write a user defined function CreateFile() to input data for a
                     record and add to Book.dat .
                  ii. Write a function CountRec(Author) in Python which accepts the
                     Author name as parameter and count and return number of
                     books by the given Author are stored in the binary file
                     “Book.dat”

                                               OR
     A binary file “STUDENT.DAT” has structure (admission_number, Name,
     Percentage). Write a function countrec() in Python that would read contents
     of the file “STUDENT.DAT” and display the details of those students whose
     percentage is above 75. Also display number of students scoring above 75%



                                                                                       Page 11 of 11
```