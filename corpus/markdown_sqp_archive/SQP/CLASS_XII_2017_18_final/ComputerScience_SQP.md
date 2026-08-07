---
title: "ComputerScience SQP"
source_pdf: "ComputerScience_SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/ComputerScience_SQP.pdf"
pages: 15
pdf_bytes: 565328
pdf_sha256: "5e921a89c3bf1b6236a9e965d66644af96052436969438742acd045850b9921e"
text_chars: 23944
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience SQP


---

## page 1

```
                                       SAMPLE QUESTION PAPER
                                        Subject: Computer Science
                                           Class: XII (2017-18)

Time: 3 Hrs.                                                                                               M.M.:70
Instructions:
      (a) All questions are compulsory,
      (b) Answer either Section A or Section B:
                (i) Section A              -     Programming Language with C++
                (ii) Section B             -     Programming Language with Python
      (c) Section C is compulsory.
                                                 SECTION – A (C++)
Q.     Part     Question Description                                                                         Marks
No.
Q1.    (a)      What is the role of a parameter/argument passed in a function? Can a default value be            2
                assigned to a parameter(Yes/No)? If yes, justify your answer with the help of a suitable
                example otherwise give reason.
       (b)      Raman suggests Kishan the following header files which are required to be included in            1
                the given C++ program. Identify the header files which are wrongly suggested by
                Raman.
                Program:




                Suggested header files:-
                   1. iostream.h
                   2. stdio.h
                   3. conio.h
                   4. ctype.h

       (c)      Rewrite the following program after removing the syntactical errors (is any). Underline          2
                each correction.




                                                    Page No. 1
```

---

## page 2

```
(d)   Write the output of the following C++ program code(assume all necessary header files   2
      are included in program):




(e)   Write the output of the following C++ program code(assume all necessary header files   3
      are included in program):




                                       Page No. 2
```

---

## page 3

```
      (f)   Consider the following C++ program code and choose the option(s) which are not         2
            possible as output. Also, print the minimum & maximum value of variable Pick during
            complete execution of the program.(assume all necessary header files are included in
            program):




                   (a) 5:6:6:6:
                   (b) 4:7:5:3:
                   (c) 8:6:1:2:
                   (d) 7:5:3:1
Q2.   (a)   What do you mean by Data Abstraction in OOPs? Explain its significance in              2
            programming with a suitable example.
      (b)   Answer the question (i) & (ii) after going through the following code. (assume all     2
            necessary header files are included in program):-

                                               Page No. 3
```

---

## page 4

```
         (i)       Give the name of the feature of OOP which is implemented by Function 1 &
                   2 together in the above class Game.
         (ii)      Anuj made changes to the above class Game and made Function 3 private.
                   Will he be able to execute the Line 1 successfully given below? Justify.
                                             void main()
                                             {
                                                    Game ABC;              //Line 1
                                             }
(c)   Define a class Bill in OOP with the following specification:-                           4
      Private members:
         1. Bill_no                     -    type long(bill number)
         2. Bill_period                 -    type integer(number of months)
         3. No_of_calls                 -    type integer(number of mobile calls)
         4. Payment_mode                -    type string(“online” or “offline”)
         5. Amount                      -    type float(amount of bill)
         6. Calculate_Bill() function to calculate the amount of bill given as per the
                following conditions:
                                                      Calculation Rate/call
                               No_of_calls
                                                          (in rupees)
                                  <=500                        1.0
                                 501-1200                      2.0
                                  >1200                        4.0

                                            Page No. 4
```

---

## page 5

```
                Also, the value of Amount should be reduced by 5% if Payment_mode is
      “online”.


      Public members:
         1. A member function New_Bill() that will accept the values for Bill_no,
                Bill_period,   No_of_calls,    Payment_mode       from   the   user   and   invoke
                Caluclate_Bill() to assign the value of Amount.
         2. A member function Print_Bill() that will display all details of a Bill.
(d)   Answer the question from (i) to (iv) based on the given below code(assume all necessary        4
      header files are included in program):-




         (i)       Write name of the class whose constructor is invoked first on the creation of a
                   new object of class Country.
         (ii)      Write name of the data members which are accessible through the object of
                   class Country.


                                              Page No. 5
```

---

## page 6

```
              (iii)      List name of the members which are accessible through the member function
                         “void New_Country()”.
              (iv)       What will be the size(in bytes) of an object of class Country & State
                         respectively.
Q3   (a)   Write the definition of function named Array_Swap() that will accept an integer array &     3
           its size as arguments and the function will interchange/swap elements in such a way that
           the first element is swapped with the last element, second element is swapped with the
           second last element and son on, only if anyone or both the elements are odd.
                     E.g. if initially array of seven elements is:
                                     5, 16, 4, 7, 19, 8, 2
                     After execution of the above function, the contents of the array will be:
                                     2,16, 19, 7, 4, 8, 5
     (b)   An array A[50][30] is stored along the row in the memory with each element requiring 4      3
           bytes of storage. If the element A[10][15] is stored at 21500, then find out the base
           address of the array and the memory address of element stored at location A[30][25]?
     (c)   Write the definition of a member function Q_Insert() for a class Exam_Queue in C++          4
           to insert a new Application information in a dynamically allocated queue whose code is
           already given below as a part of the program(assume all necessary header files are
           included in program):




     (d)   Write the definition of a user-defined function REPEAT_ROW(int A[][3],int R, int C)         2
           in C++ that will store the elements in the following manner
              1. All row elements except the 1st element replaced by the 1st element,
              2. All row elements except the 1st & 2nd element replaced by the 2nd element,
              3. All row elements except the 1st , 2nd & 3rd element replaced by the 3rd element and


                                                   Page No. 6
```

---

## page 7

```
                      so on.
            For example: if initially the array was:-
                                      5        6        10       2
                                      2        6         9       12
                                     18       14         5       6
            Then, the contents of the array after execution of the above function will be:-
                                      5        5        5        5
                                      2        6         6       6
                                     18       14        14       14
      (e)   Evaluate the following POSTFIX expression. Show the status of Stack after execution of         2
            each operation separately:
                               TRUE, FALSE, OR, NOT, TRUE, FALSE, AND, OR
Q4.   (a)   Answer the questions (i) & (ii) in the program segment given below for the required task.      1




               (i)       Write Statement 1 to position the file pointer to the appropriate place so that
                         the data updation is done for the correct Route.
               (ii)      Write Statement 2 to perform the write operation so that the updation is done
                                                   Page No. 7
```

---

## page 8

```
                      in the binary file “ROUTE.DAT”.
     (b)   Write a user-defined function named Count() that will read the contents of text file    2
           named “Report.txt” and count the number of lines which starts with either „I‟ or „M‟.
           E.g. In the following paragraph, there are 2 lines starting with „I‟ or „M‟:
           “India is the fastest growing economy.
           India is looking for more investments around the globe.
           The whole world is looking at India as a great market.
           Most of the Indians can foresee the heights that India is capable of reaching.”
     (c)   Consider the following class Item:-                                                     3




           Write a function named Change_Item(int Id, float Pr) to modify the price of the item
           whose ItemId & new price are passed as an argument.
                                           SECTION – B (Python)
Q1   (a)
           Differentiate between break and continue statement with the help of an example.
                                                                                                   2
     (b)   Identify and write the name of the module to which the following functions belong:      1
           i. ceil( ) ii. findall()
     (c)   Observe the following Python code very carefully and rewrite it after removing all      2
           syntactical errors with each correction underlined.




     (d)   Write the output of the following Python code:                                          2
                                                 Page No. 8
```

---

## page 9

```
     (e)    Write the output of the following Python program code:                                       3




     (f)    Study the following program and select the possible output(s) from the options (i) to (iv)   2
            following it. Also, write the maximum and the minimum values that can be assigned to
            the variable Y.




            i) 0 : 0
            ii) 1 : 6
            iii) 2 : 4
            iv) 0 : 3
Q2   (a)    Explain operator overloading with the help of an example.                                    2
     (b)    Observe the following Python code and answer the questions (i) and (ii):




     (i)    How is data member „count‟ different from data member „Author‟?                              1
     (ii)   Fill in the blanks:                                                                          1
            B= BOOK()
            ______________________________ #Write statement to invoke Function 2

                                                Page No. 9
```

---

## page 10

```
       ______________________________ #Write statement to invoke Function 3
(c)    Define a class COURSE in Python with the following description :                          4
       Instance Attributes:
              REGNO Integer
              CNAME String
              Score Float
              Fees Float
       Methods:
                    A constructor to assign REGNO as 0, Score and Fees as 0.0
                    SetCourse() to assign Course and Fees on the basis of the Score input as
                       per the following criteria:
                          Score             CNAME                  Fees
                          >=9.0 -<=10.0 Clinical Psychology        10000.0
                          >=8.0 - <9.0      Corporate Counselling   8000.0
                          >=5.0 - <8.0      Guidance and
                                            Counselling             6000.0
                          less than 5.0     Not Eligible                 0.0

                     GETDATA() to input REGNO and Score and invoke SetCourse()
                     DISPLAY() to display all the details.

(d)    Answer the questions (i) and (ii) based on the following:                                 4




(i)    Explain the relationship between Line 1 , Line 2 and Line 3.
(ii)   Predict the output that will be produced on the execution of the following statements :




                                          Page No. 10
```

---

## page 11

```
Q3    (a)   Write the definition of a function Reverse(X) in Python, to display the elements in          2
            reverse order such that each displayed element is the twice of the original element
            (element * 2) of the List X in the following manner:
            Example:
            If List X contains 7 integers is as follows:

               X[0]      X[1]       X[2]      X[3]       X[4]        X[5]     X[6]
                 4         8          7         5          6           2       10
            After executing the function, the array content should be displayed as follows:
                20         4         12        10         14          16        8
      (b)   Consider the following unsorted list :                                                       3
            [22, 54, 12, 90, 55, 78]
            Write the passes of selection sort for sorting the list in ascending order till the 3rd
            iteration.

      (c)   Consider the following class Order and do as directed:                                       4




                                                                    Blank 1

                        :
                        :
            i. Fill in the blank 1 with a statement to insert OID in the Queue maintained using List
            L.
            ii. Complete the definition of delorder() to delete OID from the Queue maintained using
            List L, the function should return the OID being deleted or -1 in case the Queue is empty.

      d)    Write a generator function to generate odd numbers between a and b(including b).Note: a      3
            and b are received as an argument by the function.
      (e)   Evaluate the following postfix expression using a stack. Show the contents of stack after    2
            execution of each operation:
            10,40,25,-,*,15,4,*,+
Q4.   (a)   Nancy intends to position the file pointer to the beginning of a text file. Write Python     1
            statement for the same assuming F is the File object.
      (b)   Write a function countmy( )in Python to read the text file “DATA.TXT” and count the
            number of times “my” occurs in the file.
            For example if the file “DATA.TXT” contains:
                                                                                                         2
            “This is my website. I have displayed my preferences in the CHOICE section.”
            The countmy( ) function should display the output as:
            “my occurs 2 times”.
      (c)   Write a function in python to search and display details of all those students, whose        3
            stream is “HUMANITIES” from pickled file “Student.dat”. Assuming the pickled file is
            containing the objects of the following class:




                                                 Page No. 11
```

---

## page 12

```
                                                SECTION – C
Q5   (a)   Differentiate between DDL & DML. Identify DDL & DML commands from the                  2
           following:-
                            (UPDATE, SELECT, ALTER, DROP)
     (b)   Consider the following relation MobileMaster & MobileStock:-                           6
                                                 MobileMaster
                    M_Id         M_Company          M_Name            M_Price       M_Mf_Date
                    MB001          Samsung           Galaxy            4500         2013-02-12
                    MB003            Nokia           N1100             2250         2011-04-15
                    MB004          Micromax          Unite3            4500         2016-10-17
                    MB005            Sony           XperiaM            7500         2017-11-20
                    MB006            Oppo           SelfieEx           8500         2010-08-21


                                                  MobileStock
                     S_Id                M_Id                 M_Qty              M_Supplier
                     S001              MB004                   450               New Vision
                     S002              MB003                   250            Praveen Gallery
                     S003              MB001                   300        Classic Mobile Store
                     S004              MB006                   150              A-one Mobiles
                     S005              MB003                   150               The Mobile
                     S006              MB006                   50               Mobile Centre


           Write the SQL query for questions from (i) to (iv) & write the output of SQL command
           for questions from (v) to (viii) given below:-
              (i)        Display the Mobile company, name & price in descending order of their


                                                Page No. 12
```

---

## page 13

```
                        manufacturing date,
                (ii)    List the details of mobile whose name starts with „S‟ or ends with „a‟,
                (iii)   Display the Mobile supplier & quantity of all mobiles except „MB003‟,
                (iv)    List showing the name of mobile company having price between 3000 &
                        5000,
                (v)     SELECT M_Id, SUM(M_Qty) FROM MobileStock GROUP BY M_Id;
                (vi)    SELECT MAX(M_Date), MIN(M_Date) FROM MobileMaster;
                (vii)   SELECT M1.M_Id, M1.M_Name, M2.M_Qty, M2.M_Supplier FROM
                        MobileMaster M1, MobileStock M2 WHERE M1.M_Id=M2.M_Id AND
                        M2.M_Qty>=300;
                (viii) SELECT AVG(M_Price) FROM MobileMaster;
Q6.   (a)   State & prove De-Morgan‟s law using truth table.                                            2
      (b)   Draw the equivalent logic circuit diagram of the following Boolean expression:-             2
                                   (A‟ + B).C‟
      (c)   Write the SOP form for the Boolean Function F(X,Y,Z) represented by the given truth         1
            table:-
                                       X           Y           Z           F
                                       0           0           0           0
                                       0           0           1           1
                                       0           1           0           1
                                       0           1           1           0
                                       1           0           0           0
                                       1           0           1           0
                                       1           1           0           1
                                       1           1           1           1
      (d)   Reduce the following Boolean expression using K-Map:-                                       3
                           F(U,V,W,Z)= π(0,2,5,7,12,13,15)
Q7.   (a)   A teacher provides “http://www.XtSchool.com/default.aspx” to his/her students to            1
            identify the URL & domain name.
      (b)   Which out of the following does not come under Cyber Crime?                                 1
            (i) Copying data from the social networking account of a person without his/her
                  information & consent.
            (ii) Deleting some files, images, videos, etc. from a friend‟s computer with his consent.
            (iii) Viewing & transferring funds digitally from a person‟s bank account without
                  his/her knowledge.
            (iv) Intentionally making a false account on the name of a celebrity on a social
                                                 Page No. 13
```

---

## page 14

```
           networking site.
(c)   Expand the following:-                                                                     1
         1. GSM                     2. TDMA
(d)   What is the significance of cookies stored on a computer?                                  1
(e)   Kabir wants to purchase a Book online and he has placed the order for that book using an   1
      e-commerce website. Now, he is going to pay the amount for that book online using his
      Mobile, then he needs which of the following to complete the online transaction:-
         1. A bank account,
         2. Mobile phone which is attached to above bank account,
         3. The mobile banking app of the above bank installed on that mobile,
         4. Login credentials(UID & Pwd) provided by the bank,
         5. Or all of above.
(f)   What do you mean by data encryption? For what purpose it is used for?                      1
(g)   Sanskar University of Himachal Pradesh is setting up a secured network for its campus at
      Himachal Pradesh for operating their day-to-day office & web based activities. They are
      planning to have network connectivity between four buildings. Answer the question (i) to
      (iv) after going through the building positions in the campus & other details which are
      given below:



                                                   Main
                       Admin                       Building




                                                                             Academic
                Finance


      The distances between various buildings of university are given as:-
                     Building 1              Building 2           Distance(in mtrs.)

                        Main                   Admin                     50

                        Main                  Finance                    100
                        Main                 Academic                    70
                       Admin                  Finance                    50
                      Finance                Academic                    70
                       Admin                 Academic                    60




                                         Page No. 14
```

---

## page 15

```
Number of computers:-
                          Building                 No. of Computers
                           Main                          150
                           Admin                          75
                          Finance                         50
                          Academic                        60
As a network expert, you are required to give best possible solutions for the given    1
queries of the university administration:-
   (a) Suggest cable layout for the connections between the various buildings,         1
   (b) Suggest the most suitable building to house the server of the network of the
       university,                                                                     1
   (c) Suggest the placement of following devices with justification:
       1. Switch/Hub                                                                   1
       2. Repeater
   (d) Suggest the technology out of the following for setting-up very fast Internet
       connectivity among buildings of the university
       1. Optical Fibre
       2. Coaxial cable
       3. Ethernet Cable

                                      ********




                                     Page No. 15
```