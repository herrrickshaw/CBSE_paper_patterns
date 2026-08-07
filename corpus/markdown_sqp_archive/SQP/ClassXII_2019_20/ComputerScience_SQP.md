---
title: "ComputerScience SQP"
source_pdf: "ComputerScience_SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/ComputerScience_SQP.pdf"
pages: 7
pdf_bytes: 125027
pdf_sha256: "7cc9433e98f9524bd950fcf3f924905da105f71ecdb263a32a200af85cb2bf90"
text_chars: 14209
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience SQP


---

## page 1

```
                           COMPUTER SCIENCE – NEW (083)
                          SAMPLE QUESTION PAPER (2019-20)
                                    CLASS- XII


Max. Marks: 70                                                                        Time: 3 hrs

General Instructions:

      ●     All questions are compulsory.
      ●     Question paper is divided into 4 sections A, B, C and D.
                         Section A : Unit-1
                         Section B : Unit-2
                         Section C: Unit-3
                         Section D: Unit-4


                                           SECTION-A
          (a)   Which of the following is valid arithmetic operator in Python:
Q1.                                                                                            1
                (i) //      (ii) ?  (iii) <          (iv) and

                Write the type of tokens from the following:
          (b)                                                                                  1
                (i) if (ii) roll_no
                Name the Python Library modules which need to be imported to invoke the
          (c)                                                                                  1
                following functions:
                (i) sin() (ii) randint ()
                Rewrite the following code in python after removing all syntax error(s).
          (d)                                                                                  2
                Underline each correction done in the code.
                30=To
                for K in range(0,To)
                      IF k%4==0:
                        print (K*4)
                     Else:
                        print (K+3)
          (e)   Find and write the output of the following python code:                        2
                 def fun(s):
                             k=len(s)
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
          (f)   Find and write the output of the following python code:                        3


                                                                                                   1
```

---

## page 2

```
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


            What possible outputs(s) are expected to be displayed on screen at the time of
      (g)                                                                                    2
            execution of the program from the following code? Also specify the maximum
            values that can be assigned to each of the variables FROM and TO.
            import random
            AR=[20,30,40,50,60,70];
            FROM=random.randint(1,3)
            TO=random.randint(2,4)
            for K in range(FROM,TO+1):
                  print (AR[K],end=”#“)

            (i) 10#40#70# (ii) 30#40#50#
            (iii) 50#60#70# (iv) 40#50#70#
Q2.   (a)   What do you understand by the term Iteration?                                    1
      (b)   Which is the correct form of declaration of dictionary?                          1
                  (i)      Day={1:’monday’,2:’tuesday’,3:’wednesday’}
                  (ii)     Day=(1;’monday’,2;’tuesday’,3;’wednesday’)
                  (iii)    Day=[1:’monday’,2:’tuesday’,3:’wednesday’]
                  (iv)     Day={1’monday’,2’tuesday’,3’wednesday’]
             Identify the valid declaration of L:
      (c)                                                                                    1
            L = [1, 23, ‘hi’, 6].
            (i) list    (ii) dictionary (iii) array    (iv) tuple



      (d)   Find and write the output of the following python code:                          1

             x = "abcdef"
            i = "a"
            while i in x:
               print(i, end = " ")




                                                                                                 2
```

---

## page 3

```
(e)   Find and write the output of the following python code:                           1
      a=10
      def call():
         global a
         a=15
         b=20
         print(a)
      call()


(f)   What do you understand by local and global scope of variables? How can you 2
      access a global variable inside the function, if function has a variable with same
      name.
(g)   A bar chart is drawn(using pyplot) to represent sales data of various models of   2
      cars, for a month. Write appropriate statements in Python to provide labels
      Month - June and Sale done to x and y axis respectively.
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




(h)   Write a function in python to count the number of lines in a text file ‘STORY.TXT’ 2
      which is starting with an alphabet ‘A’ .


                                          OR

      Write a method/function DISPLAYWORDS() in python to read lines from a text
      file STORY.TXT, and display those words, which are less than 4 characters.


(i)   Write a Recursive function in python BinarySearch(Arr,l,R,X) to search the given 3
      element X to be searched from the List Arr having R elements,where l represents
      lower bound and R represents the upper bound.
                                          OR


                                                                                             3
```

---

## page 4

```
            Write a Recursive function recurfactorial(n) in python to calculate and return the
            factorial of number n passed to the parameter.
      (j)   Write a function in Python, INSERTQ(Arr,data) and DELETEQ(Arr) for performing 4
            insertion and deletion operations in a Queue. Arr is the list used for implementing
            queue and data is the value to be inserted.
                                                    OR
            Write a function in python, MakePush(Package) and MakePop(Package) to add a
            new Package and delete a Package from a List of Package Description, considering
            them to act as push and pop operations of the Stack data structure.
                                       SECTION-B
Q.3         Questions 3 (a) to 3 (c) : Fill in the blanks
      (a)   ………………………..is an example of Public cloud.                                                1
      (b)   ……………………………. is a network of physical objects embedded with electronics, 1
            software, sensors and network connectivity.
      (c)   ---------------------- is a device that forwards data packets along networks.            1
      (d)   ---------------------- describes the maximum data transfer rate of a network or 1
            Internet connection.
      (e)   Give the full forms of the following                                                     2
                (i)     HTTP
                 (ii)    FTP
                (v)     VoIP
                (vi)    SSH
            How many pair of wires are there in twisted pair cable(Ethernet)?What is the name
      (f)                                                                                            2
            of port ,which is used to connect Ethernet cable to a computer or a labtop?

      (g)   Identify the type of cyber crime for the following situations:                           3
                (i)      A person complains that Rs. 4.25 lacs have been fraudulently stolen
                         from his/her account online via some online transactions in two days
                         using NET BANKING.
                (ii)     A person complaints that his/her debit/credit card is safe with him still
                         some body has done shopping/ATM transaction on this card.
                (iii)    A person complaints that somebody has created a fake profile on
                         Facebook and defaming his/her character with abusive comments and
                         pictures.




            Software Development Company has set up its new center at Raipur for its office
      (h)                                                                                        4
            and web based activities. It has 4 blocks of buildings named Block A, Block B, Block
            C, Block D.
                                    Number of Computers


                                                                                                         4
```

---

## page 5

```
                                                  Block A              25


                                                  Block B              50


                                                  Block C             125


                                                  Block D              10

                        Shortest distances between various Blocks in meters:

                             Block A to Block B             60 m
                             Block B to Block C             40 m
                             Block C to Block A             30 m
                             Block D to Block C             50 m


                (i)       Suggest the most suitable place (i.e. block) to house the
                       server of this company with a suitable reason.
                (ii) Suggest the type of network to connect all the blocks with
                      suitable reason .
                 (iii)The company is planning to link all the blocks through a secure and high
            speed wired medium. Suggest a way to connect all the blocks.
             (iv)       Suggest the most suitable wired medium for efficiently connecting each
                        computer installed in every block out of the following network cables:
                        ● Coaxial Cable
                        ● Ethernet Cable
                        ● Single Pair Telephone Cable.


                                    SECTION-C
Q.4   (a)   Which key word is used to sort the records of a table in descending order?           1
      (b)   Which clause is used to sort the records of a table?                                 1
      (c)   Which command is used to modify the records of the table?                            1
      (d)   Which clause is used to remove the duplicating rows of the table?                    1
      (e)   Differentiate between Primary key and Candidate key.                                 2
                                          OR
            Differentiate between Degree and Cardinality.
      (f)   Differentiate between Django GET and POST method.                                    2
            Write a output for SQL queries (i) to (iii), which are based on the table: STUDENT
      (g)                                                                                        3

                                                                                                     5
```

---

## page 6

```
            given below:
                                              Table : STUDENT




                (i)     SELECT COUNT(*), City FROM STUDENT GROUP BY CITY HAVING
                        COUNT(*)>1;
                (ii)    SELECT MAX(DOB),MIN(DOB) FROM STUDENT;
                (iii)   SELECT NAME,GENDER FROM STUDENT WHERE CITY=”Delhi”;


            Write SQL queries for (i) to (iv), which are based on the table: STUDENT given in
      (h)                                                                                         4
            the question 4(g):
                (i)     To display the records from table student in alphabetical order as per
                        the name of the student.
                (ii)    To display Class, Dob and City whose marks is between 450 and 551.
                (iii)   To display Name, Class and total number of students who have
                        secured more than 450 marks, class wise
                (iv)    To increase marks of all students by 20 whose class is “XII”


                                      SECTION-D
Q.5   (a)   It is an internet service for sending written messages electronically from one 1
            computer to another. Write the service name.
      (b)   As a citizen of india , What advise you should give to others for e-waste disposal?   1
      (c)   What can be done to reduce the risk of identity theft? Write any two ways.            2




                                                                                                      6
```

---

## page 7

```
(d)                                                                                         2




      Ravi received a mail form IRS department ( as shown above). On clicking “ Click-
      Here” ,he was taken to a site designed to imitate an official-looking website, such
      as IRS.gov. He uploaded some important information on it.

      Identify and explain the cybercrime being discussed in the above scenario.
(e)                                                                                         2
      Differentiate between open source and open data.
(f)   Enumerate any two disability issues while teaching and using computers                2




                                                                                                7
```