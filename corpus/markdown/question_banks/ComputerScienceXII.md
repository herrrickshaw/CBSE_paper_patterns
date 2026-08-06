---
title: "ComputerScienceXII"
source_pdf: "ComputerScienceXII.pdf"
source_url: "https://cbseacademic.nic.in/web_material/QuestionBank/ClassXII/ComputerScienceXII.pdf"
pages: 18
pdf_bytes: 283667
pdf_sha256: "d6a6c990470230822b39f8121b6305920e6f7ae890c0ed6d0b2b3fb5e25d693f"
text_chars: 36978
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScienceXII


---

## page 1

```
                                       Class: XII
                           Subject: COMPUTER SCIENCE
Q. No. 1   Rohit, a student of class 12th, is learning CSV File Module in Python. During
           examination, he has been assigned an incomplete python code (shown below)
           to create a CSV File 'Student.csv' (content shown below). Help him in
           completing the code which creates the desired CSV File.

           CSV File
           1,AKSHAY,XII,A
           2,ABHISHEK,XII,A
           3,ARVIND,XII,A
           4,RAVI,XII,A
           5,ASHISH,XII,A

           Incomplete Code
           import_____                          #Statement-1
           fh = open(_____, _____, newline='') #Statement-2
           stuwriter = csv._____                #Statement-3
           data = []
           header = ['ROLL_NO', 'NAME', 'CLASS', 'SECTION']
           data.append(header)
           for i in range(5):
                roll_no = int(input("Enter Roll Number : "))
                name = input("Enter Name : ")
                Class = input("Enter Class : ")
                section = input("Enter Section : ")
                rec = [_____]                   #Statement-4
                data.append(rec)
           stuwriter. _____ (data)              #Statement-5
           fh.close()
i.         Identify the suitable code for blank space in line marked as Statement-1.
                   a) csv file
                   b) CSV
                   c) csv
                   d) Csv

           Correct Answer : c) csv
ii.        Identify the missing code for blank space in line marked as Statement-2?
                   a) "School.csv","w"
                   b) "Student.csv","w"
                   c) "Student.csv","r"
                   d) "School.csv","r"

           Correct Answer : b) "Student.csv","w"
iii.       Choose the function name (with argument) that should be used in the blank
           space of line marked as Statement-3
                  a) reader(fh)
                  b) reader(MyFile)
                  c) writer(fh)
                  d) writer(MyFile)
```

---

## page 2

```
           Correct Answer : c) writer(fh)
iv.        Identify the suitable code for blank space in line marked as Statement-4.
                   a) 'ROLL_NO', 'NAME', 'CLASS', 'SECTION'
                   b) ROLL_NO, NAME, CLASS, SECTION
                   c) 'roll_no','name','Class','section'
                   d) roll_no,name,Class,section c) co.connect()

           Correct Answer : d) roll_no,name,Class,section
v.         Choose the function name that should be used in the blank space of line marked
           as Statement-5 to create the desired CSV File?
                   a) dump()
                   b) load()
                   c) writerows()
                   d) writerow()

           Correct Answer : c) writerows()

Q. No. 2   Amritya Seth is a programmer, who has recently been given a task to write a
           python code to perform the following binary file operations with the help of
           two user defined functions/modules:

                 a. AddStudents() to create a binary file called STUDENT.DAT
                    containing student information – roll number, name and marks (out
                    of 100) of each student.
                 b. GetStudents() to display the name and percentage of those students
                    who have a percentage greater than 75. In case there is no student
                    having percentage > 75 the function displays an appropriate
                    message. The function should also display the average percent.

           He has succeeded in writing partial code and has missed out certain
           statements, so he has left certain queries in comment lines. You as an expert
           of Python have to provide the missing statements and other related queries
           based on the following code of Amritya.

           Answer any four questions (out of five) from the below mentioned questions.

           import pickle
           def AddStudents():
                ____________ #1 statement to open the binary file to
           write data
                while True:
                      Rno = int(input("Rno :"))
                      Name = input("Name : ")
                      Percent = float(input("Percent :"))
                      L = [Rno, Name, Percent]
                      ____________ #2 statement to write the list L
           into the file
                      Choice = input("enter more (y/n): ")
                      if Choice in "nN":
                           break
                F.close()
```

---

## page 3

```
       def GetStudents():
            Total=0
            Countrec=0
            Countabove75=0
            with open("STUDENT.DAT","rb") as F:
                  while True:
                       try:
                             ____________ #3 statement to read
       from the file
                             Countrec+=1
                             Total+=R[2]
                             if R[2] > 75:
                                   print(R[1], " has percent =
       ",R[2])
                                   Countabove75+=1
                       except:
                             break
                  if Countabove75==0:
                       print("There is no student who has
       percentage more than 75")
            average=Total/Countrec
            print("average percent of class = ",average)

       AddStudents()
       GetStudents()
i.     Which of the following commands is used to open the file “STUDENT.DAT”
       for writing only in binary format? (marked as #1 in the Python code)
       a.      F= open("STUDENT.DAT",'wb')
       b.      F= open("STUDENT.DAT",'w')
       c.      F= open("STUDENT.DAT",'wb+')
       d.      F= open("STUDENT.DAT",'w+')

       Correct Answer : a. F= open("STUDENT.DAT",'wb')
ii.    Which of the following commands is used to write the list L into the binary file,
       STUDENT.DAT? (marked as #2 in the Python code)
       a.     pickle.write(L,f)
       b.     pickle.write(f, L)
       c.     pickle.dump(L,F)
       d.     f=pickle.dump(L)

       Correct Answer : c. pickle.dump(L,F)
iii.   Which of the following commands is used to read each record from the binary
       file STUDENT.DAT? (marked as #3 in the Python code)
       a.     R = pickle.load(F)
       b.     pickle.read(r,f)
       c.     r= pickle.read(f)
       d.     pickle.load(r,f)

       Correct Answer : a. R = pickle.load(F)
iv.    Which of the following statement(s) are correct regarding the file access
       modes?
```

---

## page 4

```
           a.       ‘r+’ opens a file for both reading and writing. File object points to its
           beginning.
           b.       ‘w+’ opens a file for both writing and reading. Adds at the end of the
           existing file if it exists and creates a new one if it does not exist.
           c.       ‘wb’ opens a file for reading and writing in binary format. Overwrites
           the file if it exists and creates a new one if it does not exist.
           d.       ‘a’ opens a file for appending. The file pointer is at the start of the file
           if the file exists.

           Correct Answer : a
v.         Which of the following statements correctly explain the function of seek()
           method?
           a.     tells the current position within the file.
           b.     determines if you can move the file position or not.
           c.     indicates that the next read or write occurs from that position in a file.
           d.     moves the current file position to a given specified position

           Correct Answer : d

Q. No. 3   Krrishnav is looking for his dream job but has some restrictions. He loves Delhi
           and would take a job there if he is paid over Rs.40,000 a month. He hates
           Chennai and demands at least Rs. 1,00,000 to work there. In any another
           location he is willing to work for Rs. 60,000 a month. The following code
           shows his basic strategy for evaluating a job offer.

           Code:

           pay= _________
           location= _________
           if location == "Mumbai":
               print ("I’ll take it!") #Statement 1
           elif location == "Chennai":
               if pay < 100000:
                   print ("No way") #Statement 2
               else:
                   print("I am willing!") #Statement 3
           elif location == "Delhi" and pay > 40000:
               print("I am happy to join") #Statement 4
           elif pay > 60000:
               print("I accept the offer") #Statement 5
           else:
               print("No    thanks,    I    can     find                          something
           better")#Statement 6

           On the basis of the above code, choose the right statement which will be
           executed when different inputs for pay and location are given.
i.         Input: location = "Chennai”, pay = 50000
           a.      Statement 1
           b.      Statement 2
           c.      Statement 3
           d.      Statement 4
```

---

## page 5

```
           Correct Answer : ii. Statement 2
ii.        Input: location = "Surat" ,pay = 50000
           a.      Statement 2
           b.      Statement 4
           c.      Statement 5
           d.      Statement 6

           Correct Answer: d. Statement 6
iii.       Input- location = "Any Other City", pay = 1

           a      Statement 1
           b.     Statement 2
           c.     Statement 4
           d.     Statement 6

           Correct Answer: d. Statement 6
iv.        Input location = "Delhi", pay = 500000
           a.      Statement 6
           b.      Statement 5
           c.      Statement 4
           d.      Statement 3

           Correct Answer: c. Statement 4
v.         v.     Input- location = "Lucknow", pay = 65000
           i.     Statement 2
           ii.    Statement 3
           iii.   Statement 4
           iv.    Statement 5

           Correct Answer: d. Statement 5

Q. No. 4   Consider the following code and answer the questions that follow:
           Book={1:'Thriller', 2:'Mystery', 3:'Crime', 4:'Children
           Stories'}
           Library ={'5':'Madras Diaries','6':'Malgudi Days'}
i.         Ramesh needs to change the title in the dictionary book from ‘Crime’ to ‘Crime
           Thriller’. He has written the following command:
           Book[‘Crime’]=’Crime Thriller’
           But he is not getting the answer. Help him choose the correct command:
           a. Book[2]=’Crime Thriller’
           b. Book[3]=’Crime Thriller’
           c. Book[2]=(’Crime Thriller’)
           d. Book[3] =(‘Crime Thriller’)

           Correct Answer: b
ii.        The command to merge the dictionary Book with Library the command would
           be:
           a. d=Book+Library
           b. print(Book+Library)
           c. Book.update(Library)
```

---

## page 6

```
       d. Library.update(Book)
       Correct Answer: d
iii.   What will be the output of the following line of code:
       print(list(Library))
       a. [‘5’,’Madras Diaries’,’6’,’Malgudi Days’]
       b. (‘5’,’Madras Diaries’,’6’,’Malgudi Days’)
       c. [’Madras Diaries’,’Malgudi Days’]
       d. [‘5’,’6’]

       Correct Answer: d
iv.    In order to check whether the key 2 is present in the dictionary Book, Ramesh
       uses the following command:
       2 in Book
       He gets the answer ‘True’. Now to check whether the name ‘Madras Diaries’
       exists in the dictionary Library, he uses the following command:
       ‘Madras Diaries’ in Library
       But he gets the answer as ‘False’. Select the correct reason for this:
       a. We cannot use the in function with values. It can be used with keys only.
       b. We must use the function Library.values() along with the in operator
       c. We can use the Library.items() function instead of the in operator
       d. Both b and c above are correct.

       Correct Answer: b
v.     With reference to the above declared dictionaries, predict the output of the
       following code fragments
             Code 1                        Code 2
             Library=Book                    Library=Book.copy()
             Library.pop(2)                  Library.pop(2)
             print(Library)                  print(Library)
             print(Book)                     print(Book)

        a) Code 1                              Code 2
            {1: 'Thriller', 2:                 {1: 'Thriller', 3:
            'Mystery', 3: 'Crime',             'Crime', 4: 'Children
            4: 'Children Stories'}             Stories'}
            {1: 'Thriller', 2:                 {1: 'Thriller', 3:
            'Mystery', 3: 'Crime',             'Crime', 4: 'Children
            4: 'Children Stories'}             Stories'}

        b) Code 1                              Code 2
                                               {1: 'Thriller', 3:
                                               'Crime', 4: 'Children
            {2:’Mystery’}                      Stories'}
            {1: 'Thriller', 2:                 {1: 'Thriller', 3:
            'Mystery', 3: 'Crime',             'Crime', 4: 'Children
            4: 'Children Stories'}             Stories'}

        c) Code 1                              Code 2
```

---

## page 7

```
                {1: 'Thriller', 3:                 {1: 'Thriller', 3:
                'Crime', 4: 'Children              'Crime', 4: 'Children
                Stories'}                          Stories'}
                {1: 'Thriller', 3:                 {1: 'Thriller', 2:
                'Crime', 4: 'Children              'Mystery', 3: 'Crime', 4:
                Stories'}                          'Children Stories'}

            d) Code 1                              Code 2
                {1: 'Thriller', 3:                 {1: 'Thriller', 3:
                'Crime', 4: 'Children              'Crime', 4: 'Children
                Stories'}                          Stories'}
                {1: 'Thriller', 2:                 {1: 'Thriller', 3:
                'Mystery', 3: 'Crime',             'Crime', 4: 'Children
                4: 'Children Stories'}             Stories'}

           Correct Answer: c


Q. No. 5   In a Database, there are two tables with the instances given below:

           Table: STUDENTS
              ADMNO NAME              CLASS     SEC RNO ADDRESS              PHONE
                   1211 MEENA         12A       D     4 A-26                 3245678
                   1212 VANI          10A       D     1 B-25                 5456789
                   1213 MEENA         12B       A     1 NULL                 NULL
                   1214 KARISH        10B       B     3 AB-234               4567890

           Table: SPORTS
                ADMNO GAME                         COACHNAME               GRADE
                    1215 CRICKET                   MR. RAVI                A
                    1213 VOLLEYBALL                MR. AMANDEEP            B
                    1211 VOLLEYBALL                MR. GOVARDHAN           A
                    1212 BASKET BALL               MR TEWARI               B


i.         Choose the command to display name and game of those students whose
           address is available in students’ table.

           a.      SELECT NAME, GAME FROM STUDENTS, SPORTS WHERE
                   STUDENTS.ADMNO=SPORTS.ADMNO AND ADDRESS IS NOT
                   NULL;
           b.      SELECT NAME, GAME FROM STUDENTS, SPORTS WHERE
                   STUDENTS.ADMNO=SPORTS.ADMNO AND ADDRESS IS
                   NULL;
           c.      SELECT NAME, GAME FROM STUDENTS, SPORTS WHERE
                   STUDENTS.ADMNO=SPORTS.ADMNO, ADDRESS IS NULL;
           d.      SELECT NAME, GAME FROM STUDENTS, SPORTS WHERE
                   STUDENTS.ADMNO=SPORTS.ADMNO NOT ADDRESS IS
           NULL;
```

---

## page 8

```
       Correct Answer:
       a.      SELECT NAME, GAME FROM STUDENTS, SPORTS WHERE
               STUDENTS.ADMNO=SPORTS.ADMNO AND ADDRESS IS NOT
               NULL;
ii.    Identify the statement to delete a column phone from the table students.

       a.     ALTER TABLE STUDENTS DROP PHONE;
       b.     DROP PHONE;
       c.     UPDATE DROP PHONE;
       d.     DELETE FROM STUDENTS WHERE DROP PHONE;

       Correct Answer:
       a. ALTER TABLE STUDENTS DROP PHONE;
iii.   Choose the command to display Name of the students who are studying in class
       12 and their corresponding Coach names

       a.    SELECT NAME, COACHNAME FROM STUDENTS, SPORTS
             WHERE CLASS LIKE “12%” AND STUDENTS.ADMNO
             =SPORTS.ADMNO;
       b.    SELECT NAME, COACHNAME FROM STUDENTS, SPORTS
             WHERE CLASS LIKE “12%” AND STUDENTS.ADMNO=
             SPORTS.ADMNO;
       c.    SELECT NAME, COACHNAME FROM STUDENTS, SPORTS
             WHERE CLASS LIKE “12%” AND ADMNO.STUDENTS
             =ADMNO.SPORTS;
       d.     SELECT NAME, COACHNAME FROM STUDENTS, SPORTS
             WHERE CLASS LIKE= “12%” AND STUDENTS.ADMNO
             =SPORTS.ADMNO;

       Correct Answer:
       a. SELECT NAME, COACHNAME FROM STUDENTS,SPORTS WHERE
       CLASS LIKE “12%” AND STUDENTS.ADMNO=SPORTS.ADMNO ;
iv.    which two select queries will give the same output

       A. SELECT NAME, GRADE FROM STUDENTS,SPORTS WHERE
           ADDRESS IS NULL AND STUDENTS.ADMNO =SPORTS.ADMNO ;
       B. SELECT NAME, GRADE FROM STUDENTS,SPORTS WHERE
           ADDRESS IS NOT NULL AND STUDENTS.ADMNO
           =SPORTS.ADMNO ;
       C SELECT NAME, GRADE FROM STUDENTS,SPORTS WHERE
           ADDRESS IS NULL OR STUDENTS.ADMNO=SPORTS.ADMNO ;
       D. SELECT ST.NAME, SP.GRADE FROM STUDENTS ST,SPORTS SP
           WHERE ADDRESS IS NULL AND ST.ADMNO=SP.ADMNO ;
       a. A AND B
       b. B AND C
       c. A AND D
       d. C AND D

       Correct Answer: c. A AND D
```

---

## page 9

```
v.         Choose the command to count the number of students who play volleyball

           a.   SELECT COUNT(*) FROM STUDENTS,SPORTS WHERE
           GAME=”VOLLEYBALL” AND STUDENTS.ADMNO=SPORTS.ADMNO
           ;
           b.   SELECT COUNT(GAME) FROM STUDENTS,SPORTS WHERE
           GAME=”VOLLEYBALL” AND STUDENTS.ADMNO=SPORTS.ADMNO
           ;
           c.   SELECT   COUNT(*) FROM STUDENTS,SPORTS   WHERE
           GAME=”VOLLEYBALL” ;
           d.   SELECT   COUNT(*) FROM STUDENTS,SPORTS   WHERE
           SPORTS=”VOLLEYBALL”                             AND
           STUDENTS.ADMNO=SPORTS.ADMNO

           Correct Answer :
           a.   SELECT      COUNT(*) FROM STUDENTS,SPORTS WHERE
           GAME=”VOLLEYBALL” AND STUDENTS.ADMNO=SPORTS.ADMNO
           ;

Q. No. 6   A company ABC Enterprises has four blocks of buildings as shown:

                                  B1                          B4



                                  B2                          B3


           Center to center distance between various blocks
                                      B3 TO B1 50 M
                                      B1 TO B2 60 M
                                      B2 TO B4 25 M
                                      B4 TO B3 170 M
                                      B3 TO B2 125 M
                                      B1 TO B4 90 M

           Number of computers in each block :
                                       B1       150 M
                                        B2      15 M
                                        B3      15 M
                                        B4      25 M
           Computers in each block are networked but blocks are not networked. The
           company has now decided to connect the blocks also.

i.         Suggest the most appropriate topology for the connections between the blocks.
           a.    Ring topology
           b.    Star topology
           c.    Mesh topology
           d.    Bus topology
```

---

## page 10

```
           Correct Answer: b. Star topology
ii.        The company wants internet accessibility in all the blocks. The suitable and
           cost-effective technology for that would be:
           a.      Satellite
           b.      Lease line
           c.      Telephone line
           d.      Broadband

           Correct Answer: d. Broadband

iii.       Which one of the following devices will you suggest for connecting all the
           computers with in each of their blocks?
           a.    Switch/Hub
           b.    Modem
           c.    Telephone
           d.    Repeater

           Correct Answer: a. Switch/Hub
iv.        The company is planning to link its head office situated in New Delhi with the
           offices in hilly areas. Suggest a way to connect it economically:
           a.      Micro waves
           b.      Coaxial cable
           c.       Fibre optic
           d.      Radio waves

           Correct Answer: d. Radio waves
v.         Suggest the most appropriate location of the server, to get the best connectivity
           for maximum number of computers.
           a.     BLOCK B2
           b.     BLOCK B1
           c.     BLOCK B4
           d.     BLOCK B3

           Correct Answer: b.     BLOCK B1

Q. No. 7   Millions of computer science students have taken a course on algorithms and
           data structures, typically the second course after the initial one introducing
           programming. One of the basic data structures in such a course is the stack. The
           stack has a special place in the emergence of computing as a science, as argued
           by Michael Mahoney, the pioneer of the history of the theory of computing.
           The Stack can be used in many computer applications, few are given below:
           a)      In recursive function
           b)      When function is called.
           c)      Expression conversion such as – Infix to Postfix, Infix to Prefix, Postfix
           to Infix, Prefix to Infix.
           In Stack, insertion operation is known as Push whereas deletion operation is
           known as Pop.

           Code – 1
```

---

## page 11

```
       def push(Country,N):
           Country._________(len(Country),N)) #Statement 1

       #Function Calling
       Country=[]
       C=['Indian', 'USA', 'UK', 'Canada', 'Sri Lanka']
       for i in range(0,len(C),________):    #Statement 2
           push(Country,C[i])
       print(Country)

       Required Output:
       ['Indian', 'UK', 'Sri Lanka']

       Code - 2
       def pop(Country):
           if ______________:                                 #Statement 3
               return "Under flow"
           else:
              return Country.________()                       #Statement 4

       #Function Calling
       for i in range(len(Country)+1):
           print(_______________)                             #Statement 5


       Required Output:
       Sri Lanka
       UK
       India
       Under flow

       Fill the above statement based on given questions:
i.     Identify the suitable code for the blank of statement 1.
       a.       .append()
       b.       .insert()
       c.       .extend()
       d.       .append(len(Country),N)

       Correct Answer : b. .insert()
ii.    Fill the statement 2, to insert the alternate element from Country list.
       a.       3
       b.       0
       c.       -1
       d.       2

       Correct Answer : d. 2
iii.   Fill the statement 3, to check the stack is empty.
       a.       Country=[]
       b.       Country.isEmpty()
       c.       len(country)==0
       d.       No of the above
```

---

## page 12

```
           Correct Answer : c. len(country)==0
iv.        Fill the statement 4, to delete an element from the stack.
           a.       pop(1)
           b.       pop()
           c.       del country[1]
           d.       Country.delete(1)

           Correct Answer: b.      pop()

v.         Fill the statement 5, to call the pop function.
           a.       pop(C)
           b.       pop(Country)
           c.       call pop(Country)
           d.       def pop(Country)

           Correct Answer: b.     pop(Country)

Q. No. 8   Arun, during Practical Examination of Computer Science, has been assigned
           an incomplete search() function to search in a pickled file student.dat. The File
           student.dat is created by his Teacher and the following information is known
           about the file.
               • File contains details of students in [roll_no,name,marks] format.
               • File contains details of 10 students (i.e. from roll_no 1 to 10) and
                   separate list of each student is written in the binary file using dump().
           Arun has been assigned the task to complete the code and print details of roll
           number 1.

           def search():
                f = open("student.dat",____)
           #Statement-1
                ____:                                                   #Statement-2
                      while True:
                           rec = pickle.____
           #Statement-3
                           if(____):                                    #Statement-4
                                 print(rec)
                except:
                           pass
                ____                                                    #Statement-5

i.         In which mode Arun should open the file in Statement-1?
                  a) r
                  b) r+
                  c) rb
                  d) wb

           Correct Answer: c) rb
ii.        Identify the suitable code to be used at blank space in line marked as Statement-
           2
                   a) if(rec[0]==1)
```

---

## page 13

```
                  b) for i in range(10)
                  c) try
                  d) pass

           Correct Answer: c) try
iii.       Identify the function (with argument), to be used at blank space in line marked
           as Statement-3.
                   a) load()
                   b) load(student.dat)
                   c) load(f)
                   d) load(fin)

           Correct Answer: c) load(f)
iv.        What will be the suitable code for blank space in line marked as Statement-4.
                  a) rec[0]==2
                  b) rec[1]==2
                  c) rec[2]==2
                  d) rec[0]==1

           Correct Answer: d) rec[0]==1
v.         Which statement Arun should use at blank space in line marked as Statement-
           4 to close the file.
                   a) file.close()
                   b) close(file)
                   c) f.close()
                   d) close()

           Correct Answer: c) f.close()

Q. No. 9   Radha Shah is a programmer, who has recently been given a task to write a
           python code to perform the following CSV file operations with the help of two
           user defined functions/modules:

           a.      CSVOpen() : to create a CSV file called BOOKS.CSV in append mode
           containing information of books – Title, Author and Price.
           b.      CSVRead() : to display the records from the CSV file called
           BOOKS.CSV where the field title starts with 'R'.
           She has succeeded in writing partial code and has missed out certain statements,
           so she has left certain queries in comment lines.

           import csv
           def CSVOpen():
                with open('books.csv','______',newline='') as csvf:
                #Statement-1
                      cw=______             #Statement-2
                      ______          #Statement-3
                      cw.writerow(['Rapunzel','Jack',300])
                      cw.writerow(['Barbie','Doll',900])
                      cw.writerow(['Johnny','Jane',280])

           def CSVRead():
```

---

## page 14

```
              try:
                   with open('books.csv','r') as csvf:
                        cr=______        #Statement-4
                        for r in cr:
                              if ______:      #Statement-5
                                   print(r)
              except:
                   print('File Not Found')


       CSVOpen()
       CSVRead()

       You as an expert of Python have to provide the missing statements and other
       related queries based on the following code of Radha.
       Answer any four questions (out of five) from the below mentioned questions.
i.     Choose the appropriate mode in which the file is to be opened in append mode
       (Statement 1)
       a.      w+
       b.      ab
       c.      r+
       d.      a

       Correct Answer: d. a
ii.    Which statement will be used to create a csv writer object in Statement 2.
       a.     csv.writer(csvf)
       b.     csv.writer(csvf)
       c.     csvf.writer()
       d.     cs.writer(csvf)

       Correct Answer: b. csv.writer(csvf)
iii.   Choose the correct option for Statement 3 to write the names of the column
       headings in the CSV file, BOOKS.CSV.
       a.     cw.writerow('Title','Author','Price')
       b.     cw.writerow(['Title','Author','Price'])
       c.     cw.writerows('Title','Author','Price')
       d.     cw.writerows(['Title','Author','Price'])

       Correct Answer: b. cw.writerow(['Title','Author','Price'])
iv.    Which statement will be used to read a csv file in Statement 4.
       a.     cs.read(csvf)
       b.     csv.reader(csvf)
       c.     csvf.read()
       d.     csvf.reader(cs)

       Correct Answer: b. csv.reader(csvf)
v.     Fill in the appropriate statement to check the field Title starting with ‘R’ for
       Statement 5 in the above program.
       a.       r[0][0]=='R'
       b.       r[1][0]=='R'
       c.       r[0][1]=='R'
```

---

## page 15

```
            d.     d) r[1][1]=='R'

            Correct Answer: a. r[0][0]=='R'

Q. No. 10   Ankita is writing a program to perform some operations in Queue. She has
            created three Insert_in_Queue(Student), Delete_from_Queue(Student) and
            Print_Queue(Student) methods/functions in Python to add a new Student name,
            delete a Student name and print list of student from a queue, considering them
            to act as insert, delete and print operations of the Queue data structure. She is
            not getting the desired result. Help her to get the desired result from the given
            python code.
            def Insert_in_Queue(queue):
                    a=input("enter student name: ")
                    queue.____________          # Statement-1

            def Delete_from_Queue (queue):
                    if (____________):          # Statement-2
                          print("Queue empty")
                    else:
                          print("Deleted element is: ",queue[0])
                    del queue[___]   #Statement-3

            def Print_Queue(queue):
                   if not ________: #Statement-4
                          print(queue[__:___ ])                    # Statement-5
i.          What Ankita should write to complete the Statement-1 to store the student
            name?
            a. queue.append(a)
            b. queue=append(a)
            c. queue.append=a
            d. append(a).queue

            Correct Answer: a queue.append(a)
ii.         Fill in the blank in Statement-2 to check whether the queue is empty or not?
            a. isEmpty(Queue)
            b. isEmpty(q)
            c. Queue.isEmpty
            d. Empty.Queue

            Correct Answer: a isEmpty(Queue)
iii.        iii.    Fill in the blank in Statement-3 with index number.
            a. delete(0)
            b. del queue[0]
            c. delete.queue(0)
            d. queue.delete[0]

            Correct Answer: b) del queue[0]
iv.         Select the correct option to complete the statement at statement-4.
            a.      isEmpty( )
            b.      Empty( )
            c.      len( ) = 0
```

---

## page 16

```
            d.     not Empty

            Correct Answer : a isEmpty( )
v.          Specify the range to print all queue elements in statement-5?
            a. print(queue=[0:len=(queue)])
            b. print(queue[0:len(queue)])
            c. print(queue[[0:len]])
            d. print(queue[0=len(queue)])

            Correct Answer : b. print(queue[0:len(queue)])

Q. No. 11   Priyank is a software developer with a reputed firm. He has been given the task
            to computerise the operations for which he is developing a form which will
            accept customer data as follows:
            i.     The DATA TO BE ENTERED IS :
            a.     Name
            b.     Age
            c.     Items bought( all the items that the customer bought)
            d.     Bill amount

            Correct Answer :
            i.      Choose the most appropriate data type to store the above information
            in the given sequence.
            a.      string, tuple, float, integer
            b.      string, integer, dictionary, float
            c.      string, integer, integer, float
            d.      string, integer, list, float

            Correct Answer :
            ii.     Now the data of each customer needs to be organised such that the
            customer can be identified by name followed by the age, item list and bill
            amount. Choose the appropriate data type that will help Priyank accomplish
            this task.
            a.      List
            b.      Dictionary
            c.      Nested Dictionary
            d.      Tuple

            Correct Answer :
            iii.   Which of the following is the correct way of storing information of
            customers named ‘Paritosh’ and ‘Bhavesh’ with respect to the option chosen
            above?
            a.     a.customers= {‘Paritosh’:24,[‘Printed Paper’, ‘ Penstand’], 3409,
            ‘Bhavesh’: 45,[‘A4 Rim’,’Printer Cartridge’, ‘Pen Carton’, ‘Gift Wrap’],
            8099.99 }
            b.     customers={‘Paritosh’:[24,[‘Printed Paper’, ‘ Penstand’], 3409],
            ‘Bhavesh’: [45,[‘A4 Rim’,’Printer Cartridge’, ‘Pen Carton’, ‘Gift Wrap’],
            8099.99] }
```

---

## page 17

```
            c.     c.customers= [‘Paritosh’:24,‘Printed Paper’, ‘ Penstand’, 3409,
            ‘Bhavesh’: 45,‘A4 Rim’,’Printer Cartridge’, ‘Pen Carton’, ‘Gift Wrap’,
            8099.99 ]
            d.     customers=(‘Paritosh’:24,[‘Printed Paper’, ‘ Penstand’], 3409,
            ‘Bhavesh’: 45,[‘A4 Rim’,’Printer Cartridge’, ‘Pen Carton’, ‘Gift Wrap’],
            8099.99 )

            Correct Answer :
            iv.    In order to calculate the total bill amount for 15 customers, Priyank
                    Statement 1. must use a variable of the type float to store the sum.
                    Statement 2. may use a loop to iterate over the values
            a.     Both statements are correct.
            b.     Statement 1 is correct, but statemnt 2 is not.
            c.     Both statements ar incorrect.
            d.     Statement 1 is incorrect but statement 2 is correct.

            Correct Answer :

Q. No. 12   Your teacher has given you a method/function FilterWords() in python which
            read lines from a text file NewsLetter.TXT, and display those words, which are
            lesser than 4 characters. Your teachers intentionally kept few blanks in between
            the code and asked you to fill the blanks so that the code will run to find desired
            result. Do the needful with the following python code.

            def FilterWords():
                 c=0
                 file=open('NewsLetter.TXT', '_____')                          #Statement-1
                 line = file._____                                             #Statement-2
                 word = _____                                                  #Statement-3
                 for c in word:
                       if _____:                                               #Statement-4
                            print(c)
                 _________                                                     #Statement-5

            FilterWords()
i.          Write mode of opening the file in statement-1?
            a.     a
            b.     ab
            c.     w
            d.     r

            Correct Answer: d. r
ii.         Fill in the blank in statement-2 to read the data from the file.
            a.       File.Read()
            b.       file.read()
            c.       read.lines( )
            d.       readlines( )

            Correct Answer: b. file.read()
iii.        Fill in the blank in statement-3 to read data word by word.
            a.       Line.Split()
```

---

## page 18

```
      b.      Line.split()
      c.      line.split()
      d.      split.word()

      Correct Answer: c. line.split()
iv.   Fill in the blank in statement-4, which display the word having lesser than 4
      characters.
      a.       len(c) ==4
      b.       len(c)<4
      c.       len ( )= =3
      d.       len ( )==3

      Correct Answer: b. len(c)<4
v.    Fill in the blank in Statement-5 to close the file.
      a.       file.close()
      b.       File.Close()
      c.       Close()
      d.       end()

      Correct Answer: a.      file.close()
```