---
title: "ComputerScience MS"
source_pdf: "ComputerScience_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/ComputerScience_MS.pdf"
pages: 14
pdf_bytes: 165909
pdf_sha256: "ab901e807de5b92035d8343c98c847e90e9207aa51ed850e29d593e9c3c76655"
text_chars: 26254
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience MS


---

## page 1

```
                            COMPUTER SCIENCE - NEW (083)
                           MARKING SCHEME – SQP (2019-20)
                                    CLASS- XII
Max. Marks: 70                                                                     Time: 3 hrs


General Instructions:

      ●     All questions are compulsory.
      ●     Question paper is divided into 4 sections A, B, C and D.
                         Section A : Unit-1
                         Section B : Unit-2
                         Section C: Unit-3
                         Section D: Unit-4

                                         SECTION-A
          (a)    Which of the following is valid arithmetic operator in Python:
Q1.                                                                                              1
                 (i) //      (ii) ?  (iii) <     (iv) and

          Ans.         (i)        //
                 (1 mark for correct answer)
                 Write the type of tokens from the following:
          (b)                                                                                    1
                 (i) if (ii) roll_no
                       (i)        Key word (ii) Identifier
          Ans.
                 (1/2 mark for each correct type)
                 Name the Python Library modules which need to be imported to invoke the
          (c)                                                                                    1
                 following functions:
                 (i) sin( ) (ii) randint ( )
                       (i)        math (ii) random
          Ans.
                 (1/2 mark for each module)
                 Rewrite the following code in python after removing all syntax error(s).
          (d)                                                                                    2
                 Underline each correction done in the code.
                 30=To
                 for K in range(0,To)
                         IF k%4==0:
                           print (K*4)
                       Else:
                         print (K+3)
                 To=30
          Ans.   for K in range(0,To) :
                        if k%4==0:
                           print (K*4)
                       else:
                           print (K+3)
                 (1/2 mark for each correction)
          (e)    Find and write the output of the following python code:                         2
                 def fun(s):
                               k=len(s)

                                                                                                 1
```

---

## page 2

```
                   m=" "
                  for i in range(0,k):
                        if(s[i].isupper()):
                                 m=m+s[i].lower()
                      elif s[i].isalpha():
                                 m=m+s[i].upper()
                     else:
                          m=m+'bb'
                 print(m)
       fun('school2@com')
       SCHOOLbbbbCOM
Ans.
       (2 marks for correct output)
       Note: Partial marking can also be given
(f)    Find and write the output of the following python code:                          3
       def Change(P ,Q=30):
               P=P+Q
               Q=P-Q
               print( P,"#",Q)
               return (P)
       R=150
       S=100
       R=Change(R,S)
       print(R,"#",S)
       S=Change(S)


Ans.   250 # 150
       250 # 100
       130 # 100
       (1 mark each for correct line)
       What possible outputs(s) are expected to be displayed on screen at the time of
(g)                                                                                     2
       execution of the program from the following code? Also specify the maximum
       values that can be assigned to each of the variables FROM and TO.
       import random
       AR=[20,30,40,50,60,70];
       FROM=random.randint(1,3)
       TO=random.randint(2,4)
       for K in range(FROM,TO+1):
             print (AR[K],end=”# “)

       (i) 10#40#70# (ii) 30#40#50#


                                                                                        2
```

---

## page 3

```
             (iii) 50#60#70# (iv) 40#50#70#
             (ii) 30#40#50# Maximum value FROM,TO is 3,4)
      Ans.
             (1/2 mark each for maximum value)
             (1 mark for correct option)
Q2.   (a)    What do you understand by the term Iteration?                              1
      Ans.   Repeatation of statement/s finite number of times is known as Iteration.
             (1 mark for correct answer)
      (b)    Which is the correct form of declaration of dictionary?                    1
                   (i)       Day={1:’monday’,2:’tuesday’,3:’wednesday’}
                   (ii)      Day=(1;’monday’,2;’tuesday’,3;’wednesday’)
                   (iii)     Day=[1:’monday’,2:’tuesday’,3:’wednesday’]
                   (iv)      Day={1’monday’,2’tuesday’,3’wednesday’]
      Ans.         (i)       Day={1:’monday’,2:’tuesday’,3:’wednesday’}
             (1 mark for correct answer)
              Identify the valid declaration of L:
      (c)                                                                               1
             L = [1, 23, ‘hi’, 6].
             (i) list    (ii) dictionary (iii) array    (iv) tuple

                 (i)     List
      Ans.
             (1 mark for correct answer)
      (d)    Find and write the output of the following python code:                    1

              x = "abcdef"
             i = "a"
             while i in x:
                print(i, end = " ")


      Ans.   aaaaaa----- OR infinite loop
             (1 mark for correct answer)
      (e)    Find and write the output of the following python code:                    1
             a=10
             def call():
                  global a
                  a=15
                  b=20
                  print(a)
             call()


      Ans.   15


                                                                                        3
```

---

## page 4

```
       (1 mark for correct answer)
(f)    What do you understand by local and global scope of variables? How can you access               2
       a global variable inside the function, if function has a variable with same name.
Ans.    A global variable is a variable that is accessible globally. A local variable is one that is
       only accessible to the current scope, such as temporary variables used in a single
       function definition.
        A variable declared outside of the function or in global scope is known as global variable.
       This means, global variable can be accessed inside or outside of the function where as
       local variable can be used only inside of the function. We can access by declaring
       variable as global A.
       (1 mark for correct difference)
       (1 mark for explanation)

(g)    A bar chart is drawn(using pyplot) to represent sales data of various models of cars, 2
       for a month. Write appropriate statements in Python to provide labels Month -
       June and Sale done to x and y axis respectively.
                                                OR
       Give the output from the given python code:

       import matplotlib.pyplot as plt; plt.rcdefaults()
       import numpy as np
       import matplotlib.pyplot as plt

       objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
       y_pos = np.arange(len(objects))
       performance = [10,8,6,4,2,1]

       plt.bar(y_pos, performance, align='center', alpha=0.5)
       plt.xticks(y_pos, objects)
       plt.ylabel('Usage')
       plt.title('Programming language usage')

       plt.show()




Ans.   import matplotlib.pyplot as plt
       import numpy as np
       model=(‘i20’,’Grandi10’,’Creta’,’Eon’,’Verna’,’Tucson’,’Elantra’)
       y_pos=np.arange(len(model))
       sale=[12369,12174,9390,4663,4077,3712,200,150]
       plt.bar(y_pos,sale,align=’center’,alpha=0.5)
       plt.xticks(y_pos,model)
       plt.xlabel(‘Month-June’)
       plt.ylabel(‘Sale done’)
       plt.title(‘Sales Bar Graph’)
       plt.show()

                                                                                                       4
```

---

## page 5

```
       (1/2 mark for correct plt.bar)
       (1/2 mark for each correct xlabel and ylabel)
       (1/2 mark for plt.show)


                                            OR




       (2 marks for correct output)
       Write a function in python to count the number of lines in a text file ‘STORY.TXT’
(h)    which is starting with an alphabet ‘A’ .                                             2

                                           OR

       Write a method/function DISPLAYWORDS() in python to read lines from a text
       file STORY.TXT, and display those words, which are less than 4 characters.

       def COUNTLINES():
Ans.
             file=open('STORY.TXT','r')
              lines = file.readlines()
              count=0
             for w in lines:
                  if w[0]=="A" or w[0]=="a":
                     count=count+1
              print(“Total lines “,count)
              file.close()
       (½ Mark for opening the file)
       (½ Mark for reading all lines, and using loop)
       (½ Mark for checking condition)
       (½ Mark for printing lines)
                                             OR


       def DISPLAYWORDS():
                c=0
             file=open(‘STORY.TXT','r')
            line = file.read()


                                                                                            5
```

---

## page 6

```
               word = line.split()
               for w in word:
                  if len(w)<4:
                      print( w)
           file.close()
       (½ Mark for opening the file)
       (½ Mark for reading line and/or splitting)
       (½ Mark for checking condition)
       (½ Mark for printing word)
(i)    Write a Recursive function in python BinarySearch(Arr,l,R,X) to search the given     3
       element X to be searched from the List Arr having R elements where l represents
       lower bound and R represents upper bound.
                                  OR
       Write a Recursive function recurfactorial(n) in python to calculate and return the
       factorial of number n passed to the parameter.
Ans.   def BinarySearch (Arr,l,R,X):


         if R >= l:
                mid = l + (R-l)//2
                if Arr[mid] == X:
                 return mid
               elif Arr[mid] > X:
                 return BinarySearch(Arr,l,mid-1,X)
               else:
                 return BinarySearch(Arr,mid+1,r,X)
         else:
            return -1
       Arr = [ 2, 3, 4, 10, 40 ]
       X =int(input(' enter element to be searched'))
       result = BinarySearch(Arr,0,len(Arr)-1,X)


       if result != -1:
         print ("Element is present at index ", result)
       else:
         print ("Element is not present in array")
       (1/2 mark for mid)


                                                                                            6
```

---

## page 7

```
       (1/2 mark for return mid)
       (1 mark each for returning function)
       (1 mark for invoking function)
                                    OR
       def recurfactorial(n):
         if n == 1:
           return n
        else:
           return n*recurfactorial(n-1)
       num = int(input("Enter a number: "))
       if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
       elif num == 0:
        print("The factorial of 0 is 1")
       else:
        print("The factorial of",num,"is",recurfactorial(num))
       (2 marks for correct recursive function)
       (1 mark for invoking)
(j)    Write a function in Python, INSERTQ(Arr,data) and DELETEQ(Arr) for performing 4
       insertion and deletion operations in a Queue. Arr is the list used for implementing
       queue and data is the value to be inserted.
                                             OR
       Write a function in python, MakePush(Package) and MakePop(Package) to add a
       new Package and delete a Package from a List of Package Description, considering
       them to act as push and pop operations of the Stack data structure.
       def INSERTQ(Arr):
Ans.
           data=int(input("enter data to be inserted: "))
           Arr.append(data)
       def DELETEQ(Arr):
           if (Arr==[]):
              print( "Queue empty")
           else:
              print ("Deleted element is: ",Arr[0])
             del(Arr[0])

        ( ½ mark insert header)
       ( ½ mark for accepting a value from user)
       ( ½ mark for adding value in list)
       ( ½ mark for delete header)
       ( ½ mark for checking empty list condition)

                                                                                          7
```

---

## page 8

```
             ( ½ mark for displaying “Queue empty”)
             ( ½ mark for displaying the value to be deleted)
             ( ½ mark for deleting value from list)
                                            OR
             def MakePush(Package):
                  a=int(input("enter package title : "))
                  Package.append(a)
             def MakePop(Package):
                  if (Package==[]):
                      print( "Stack empty")
                  else:
                      print ("Deleted element:",Package.pop())


             (½ mark for MakePush() header)
             ( ½ mark for accepting a value from user)
             ( ½ mark for adding value in list)
             ( ½ mark for MakePop() header)
             ( ½ mark for checking empty list condition)
             ( ½ mark for displaying “Stack empty”)
             ( ½ mark for displaying the value to be deleted)
             ( ½ mark for deleting value from list)




                                 SECTION-B
Q.3          Questions 3 (a) to 3 (c) : Fill in the blanks
      (a)    ………………………..is an example of Public cloud.                                                  1
      Ans.   Google Drive or any other correct example
             (1 mark for correct answer)
      (b)    ……………………………. is a network of physical objects embedded with electronics,                   1
             software, sensors and network connectivity.
      Ans.   The internet of things OR Internet

             (1 mark for correct answer)
      (c)    ---------------------- is a device that forwards data packets along networks.              1
      Ans.   Router
             (1 mark for correct answer)
      (d)    ---------------------- describes the maximum data transfer rate of a network or Internet   1
             connection.
      Ans.   Band width
             (1 mark for correct answer)
      (e)    Give the full forms of the following                                                       2

                                                                                                        8
```

---

## page 9

```
                   (i) HTTP
                   (ii) FTP
                   (iii) VoIP
                   (iv) SSH
Ans.       (i)         Hyper text transfer protocol
           (ii)        File transfer protocol
           (iii)       Voice over internet protocol
           (iv)        Secure shell
           (1/2 mark for each correct expansion)
       How many pair of wires are there in twisted pair cable(Ethernet)?What is the name
(f)                                                                                                2
       of port ,which is used to connect Ethernet cable to a computer or a labtop?


       Two insulated copper wires , Ethernet port
Ans.
       (1 mark for each correct Answer)

(g)    Identify the type of cyber crime for the following situations:                              3
           (i)         A person complains that Rs. 4.25 lacs have been fraudulently stolen
                       from his/her account online via some online transactions in two days
                       using NET BANKING.
           (ii)        A person complaints that his/her debit/credit card is safe with him still
                       some body has done shopping/ATM transaction on this card.
           (iii)       A person complaints that somebody has created a fake profile on
                       Facebook and defaming his/her character with abusive comments and
                       pictures.
Ans.       (i)         Bank Fraud
           (ii)        Identity Theft
           (iii)       Cyber Stalking
       (1 mark for each correct answer)
       Software Development Company has set up its new center at Raipur for its office
(h)                                                                                         4
       and web based activities. It has 4 blocks of buildings named Block A, Block B, Block
       C, Block D.




                                        Number of Computers



                                             Block A               25



                                                                                                   9
```

---

## page 10

```
                                                   Block B            50


                                                   Block C          125


                                                   Block D            10

                         Shortest distances between various Blocks in meters:

                              Block A to Block B             60 m
                              Block B to Block C             40 m
                              Block C to Block A             30 m
                              Block D to Block C             50 m


                 (i)    Suggest the most suitable place (i.e. block) to house the
                        server of this company with a suitable reason.
                 Ans. Block C , It has maximum number of computer.
                      (1 mark for correct answer )
                 (ii) Suggest the type of network to connect all the blo)cks with
                        suitable reason .
                 Ans. LAN
                           (1 mark for correct answer )
             (iii)The company is planning to link all the blocks through secure and high-speed
             wired medium. Suggest a way to connect all the blocks.
                    Ans. Star topology
                           OR Diagram
                        (1 mark for correct answer )
               (iv) Suggest the most suitable wired medium for efficiently connecting each
             computer installed in every block out of the following network cables:
                            ● Coaxial Cable
                            ● Ethernet Cable
                              ● Single Pair Telephone Cable.
                       Ans. Ethernet Cable
                          (1 mark for correct answer )


                                             SECTION-C
Q.4   (a)    Which key word is used to sort the records of a table in descending order?           1
      Ans.   DESC
             (1 mark for correct answer )


                                                                                                 10
```

---

## page 11

```
(b)    Which clause is used to sort the records of a table?                                       1
Ans.   ORDER BY
       (1 mark for correct answer )
(c)    Which command is used to modify the records of the table?                                  1
Ans.   UPDATE
       (1 mark for correct answer )
(d)    Which clause is used to remove the duplicating rows of the table?                          1
Ans.   DISTINCT
       (1 mark for correct answer )
(e)    Differentiate between Primary key and Candidate key.                                       2
                                    OR
       Differentiate between Degree and Cardinality.
Ans.   A Candidate Key can be any column or a combination of columns that can qualify as
       unique key in database. There can be multiple Candidate Keys in one table where as
        A Primary Key is a column or a combination of columns that uniquely identify a record.
       Only one Candidate Key can be Primary Key.

       (2 marks for correct difference)
                     OR
       Degree : It is the total number of attributes in the table.
       Cardinality: It is the total number of tuples in the table
       (2 marks for correct difference)
(f)    Differentiate between Django GET and POST method.                                          2
Ans.   GET and POST. GET and POST are the only HTTP methods to use when dealing with
       forms. Django's login form is returned using the POST method, in which the browser
       bundles up the form data, encodes it for transmission, sends it to the server, and then
       receives back its response.
       Both of these are dictionary-like objects that give you access to GET and POST
       data. POST data generally is submitted from an HTML <form> , while GET data can
       come from a <form> or the query string in the page's URL.
       (2 Marks for correct difference)
       Write a output for SQL queries (i) to (iii), which are based on the table: STUDENT
(g)                                                                                               3
       given below:
                                          Table : STUDENT




                                                                                                 11
```

---

## page 12

```
          (i)     SELECT COUNT(*), City FROM STUDENT GROUP BY CITY HAVING
                  COUNT(*)>1;
          Ans.      COUNT(*)            City
                      2             Mumbai
                      2                Delhi
                      2                Moscow
                  (1 mark for correct output)
          (ii)    SELECT MAX(DOB),MIN(DOB) FROM STUDENT;
          Ans.            MAX(DOB)                  MIN(DOB)
                          08-12-1995             07-05-1993
                    (1 mark for correct output)
          (iii)   SELECT NAME,GENDER FROM STUDENT WHERE CITY=”Delhi”;
          Ans.            NAME                 GENDER
                          Sanal                 F
                          Store                 M
                    (1 mark for correct output)


      Write SQL queries for (i) to (iv), which are based on the table: STUDENT given in the
(h)                                                                                            4
      question 4(g):

          (i)     To display the records from table student in alphabetical order as per
                  the name of the student.
          Ans.        SELECT * FROM STUDENT ORDER BY NAME;
                      (1 mark for correct statement)
          (ii)    To display Class, Dob and City whose marks is between 450 and 551.
          Ans.    SELECT CLASS,DOB,CITY FROM STUDENT WHERE MARKS
                  BETWEEN 450 AND 551;
                     (1 mark for correct statement)

                                                                                              12
```

---

## page 13

```
                 (iii)     To display Name, Class and total number of students who have secured
                           more than 450 marks, class wise.
                 Ans.      SELECT NAME,CLASS ,COUNT(*) FROM STUDENT GROUP BY CLASS
                            HAVING MARKS>450;
                         (1 mark for correct statement)
                 (iv)      To increase marks of all students by 20 whose class is “XII”.
                 Ans.      UPDATE STUDENT SET MARKS=MARKS+20 where class=”XII”;
                         (1 mark for correct statement)


                                       SECTION-D
Q.5   (a)    It is an internet service for sending written messages electronically from one         1
             computer to another. Write the service name.
      Ans.   e-mail
             (1 mark for correct answer)
      (b)    As a citizen of india , What advise you should give to others for e-waste disposal?    1
      Ans.   As a citizen of india , We can advice the following principle of waste management:
             Reduce , Reuse and Recycle.
             (1 mark for correct answer)
      (c)    What can be done to reduce the risk of identity theft? Write any two ways.             2
             1. Don't Give out Personal Information to anyone
      Ans.   2.Don't Carry Your Social Security Card.
             (1 mark for each point)

      (d)                                                                                           2




             Ravi received a mail form IRS department ( as shown above). On clicking “ Click-
             Here” ,he was taken to a site designed to imitate an official-looking website, such
             as IRS.gov. He uploaded some important information on it.

             Identify and explain the cyber crime being discussed in the above scenario.

                                                                                                   13
```

---

## page 14

```
Ans.   It is an example of phishing. phishing is a term used to describe a malicious
       individual or group of individuals who scam users. They do so by sending e-mails or
       creating web pages that are designed to collect an individual's online bank, credit
       card, or other login information.
       (1 mark for identification)
       (1 mark for explanation)
       Differentiate between open source and open data.
(e)                                                                                                 2
       These licenses are based on the copyright protection of the code; thus, the “open”
Ans.   of open source refers to the source code. Difference between open data and open
       source is that of data versus application. Data can be numbers, locations, names, etc.
       (2 Marks for correct difference)

(f)    Enumerate any two disability issues while teaching and using computers.                      2

Ans.   There are several types of disabilities that can affect computer accessibility. Although
       there is no single universally accepted classification, an indicative list of impairments
       includes the following :Visual impairments: blindness, low vision and color blindness.
       (1 mark for each point)




                                                                                                   14
```