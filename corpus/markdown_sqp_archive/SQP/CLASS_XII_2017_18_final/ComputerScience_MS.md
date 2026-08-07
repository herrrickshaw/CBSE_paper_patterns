---
title: "ComputerScience MS"
source_pdf: "ComputerScience_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/ComputerScience_MS.pdf"
pages: 35
pdf_bytes: 912705
pdf_sha256: "ee985c9bdae9130fc8a8c56e904b55d9074c36dd8a5845cc57943708b45da078"
text_chars: 43262
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience MS


---

## page 1

```
                                                 MARKING SCHEME
                                               Subject: Computer Science
                                                  Class: XII (2017-18)

Time: 3 Hrs.                                                                                               M.M.:70
Instructions:
      (a) All questions are compulsory,
      (b) Answer either Section A or Section B:
                (i) Section A              -       Programming Language with C++
                (ii) Section B             -       Programming Language with Python
      (c) Section C is compulsory.
                                                   SECTION – A (C++)
Q.     Part     Question Description                                                                         Marks
No.
Q1.    (a)      What is the role of a parameter/argument passed in a function? Can a default value be            2
                assigned to a parameter(Yes/No)? If yes, justify your answer with the help of a suitable
                example otherwise give reason.
       Ans      Parameters/arguments are values passed in the function for the attributes which are
                required by the function to work and provide desired output.
                Yes, an argument may be assigned a default value.
                E.g.
                int Sum(int a, int b=10)               //Here b is given a default value of 10
                {      return (a+b); }
                void main()
                {
                       int x=5;
                -      cout<<Sum(x);
                }
                Output: 15


                (1 mark for correct role of parameter)
                (1/2 mark for correct answer)
                (1/2 mark for giving correct example)
       (b)      Raman suggests Kishan the following header files which are required to be included in            1


                                                       Page No. 1
```

---

## page 2

```
      the given C++ program. Identify the header files which are wrongly suggested by
      Raman.
      Program:




      Suggested header files:-
         1. iostream.h
         2. stdio.h
         3. conio.h
         4. ctype.h

Ans   stdio.h
      conio.h


      (1/2 mark for each correct header file)
(c)   Rewrite the following program after removing the syntactical errors (if any). Underline   2
      each correction.




Ans #include<iostream.h>
      #include<conio.h>
      typdef int Num;              //Typedef should be written as typedef
      Num full=100;

                                          Page No. 2
```

---

## page 3

```
      Num Calc(int X)
      {
             full=(X>2)?1:2;
             return (full%2);     //; is missing
      }
      void main()
      {
             int full=1000;
             full=Calc(::full);
             cout<<::full<<”::”<<full<<endl;
      }


      (1/2 mark for every corrected line of code) Or
      (1 Mark for only identifying any 4 errors without suggesting corrections)
(d)   Write the output of the following C++ program code(assume all necessary header files   2
      are included in program):




Ans   Output:
      New Encrypted Message after Pass 1 is : Dpnqvufs3128
      New Encrypted Message after Pass 2 is : Eqorwvgt4239


                                         Page No. 3
```

---

## page 4

```
      (1 mark of each correct line of output)
(e)   Write the output of the following C++ program code(assume all necessary header files   3
      are included in program):




Ans   Output:
      B:380
      A:350
      C:275


      (1 mark of each correct line of output)
(f)   Consider the following C++ program code and choose the option(s) which are not         2
      possible as output. Also, print the minimum & maximum value of variable Pick during
      complete execution of the program.(assume all necessary header files are included in
      program):




                                         Page No. 4
```

---

## page 5

```
                   (a) 5:6:6:6:
                   (b) 4:7:5:3:
                   (c) 8:6:1:2:
                   (d) 7:5:3:1
      Ans   Output:
            Option (a) & (c)
            Maximum value of Pick will be 8
            Minimum value of Pick will be 1


            (1/2 mark for each correct option)
            (1 mark each giving correct values of both max & min)
Q2.   (a)   What do you mean by Data Abstraction in OOPs? Explain its significance with a suitable     2
            example.
      Ans   Data abstraction in OOPs is the process of showing only the essential details of a class
            without going into background details.
            E.g.




                                                 Page No. 5
```

---

## page 6

```
      In the above example, public member Mult( ) is invoked using the object p of class
      PRODUCT. Thus, demonstrating Data abstraction.


      (1 mark for correct definition of data abstraction)
      (1 mark for giving a valid example)
(b)   Answer the question (i) & (ii) after going through the following code. (assume all   2
      necessary header files are included in program):-




                                           Page No. 6
```

---

## page 7

```
         (i)     Give the name of the feature of OOP which is implemented by Function 1 &
                 2 together in the above class Game.
         (ii)    Anuj made changes to the above class Game and made Function 3 private.
                 Will he be able to execute the Line 1 successfully given below? Justify.
                                           void main()
                                           {
                                                   Game ABC;              //Line 1
                                           }
Ans      (i)     Polymorphism or Function Overloading or Constructor Overloading
                 (1 mark for correct answer)
         (ii)    Yes, an error “Destructor for Game is not accessible” will come. As there is a
                 destructor defined in the class and it cannot be made private.
                 (1/2 mark for correct answer Yes)
                 (1/2 mark for correct reason)
(c)   Define a class Bill in OOP with the following specification:-                               4
      Private members:
         1. Bill_no                 -      type long(bill number)
         2. Bill_period             -      type integer(number of months)

                                           Page No. 7
```

---

## page 8

```
   3. No_of_calls              -     type integer(number of mobile calls)
   4. Payment_mode             -     type string(“online” or “offline”)
   5. Amount                   -     type float(amount of bill)
   6. Calculate_Bill() function to calculate the amount of bill given as per the
       following conditions:
                                              Calculation Rate/call
                       No_of_calls
                                                  (in rupees)
                          <=500                          1.0
                        501-1200                         2.0
                          >1200                          4.0
       Also, the value of Amount should be reduced by 5% if Payment_mode is
“online”.


Public members:
   1. A member function New_Bill() that will accept the values for Bill_no,
       Bill_period, No_of_calls,       Payment_mode from the user and invoke
       Caluclate_Bill() to assign the value of Amount.
   2. A member function Print_Bill() that will display all details of a Bill.




                                     Page No. 8
```

---

## page 9

```
Ans




      ( ½ Mark for correct syntax of class header)
      ( ½ Mark for correct declarations of data members)
      (1 Mark for correct definition of Caluclate_Bill() function)
      (1 Mark for correct definition of New_Bill() function)
      (1 Mark for correct definition of print_Bill() function)
      Note:


                                          Page No. 9
```

---

## page 10

```
      Deduct ½ Mark if Caluclate_Bill() is not invoked properly inside New_Bill()
      function.
(d)   Answer the question from (i) to (iv) based on the given below code(assume all necessary       4
      header files are included in program):-




         (i)      Write name of the class whose constructor is invoked first on the creation of a
                  new object of class Country.
         (ii)     Write name of the data members which are accessible through the object of
                  class Country.
         (iii)    List name of the members which are accessible through the member function
                  “void New_Country()”.
         (iv)     What will be the size(in bytes) of an object of class Country & State
                  respectively.

                                           Page No. 10
```

---

## page 11

```
     Ans      (i)        class City
                         (1 mark for correct answer)
              (ii)       None
                         (1 mark for correct answer)
              (iii)      Data    members:        Country_Id,    Country_Name[25],      State_Population,
                         City_Population
                         Member functions:           Display_Country(),    New_State(), Print_State(),
                         Get_Population(), New_City(), Show_City()
                         (1 mark for correct answer)
              (iv)       90 bytes for object of class Country & 63 bytes for object of class State
                         (1/2 mark for each correct answer)
Q3   (a)   Write the definition of function named Array_Swap() that will accept an integer array &         3
           its size as arguments and the function will interchange/swap elements in such a way that
           the first element is swapped with the last element, second element is swapped with the
           second last element and so on, only if anyone or both the elements are odd.
                     E.g. if initially array of seven elements is:
                                      5, 16, 4, 7, 19, 8, 2
                     After execution of the above function, the contents of the array will be:
                                      2,16, 19, 7, 4, 8, 5
     Ans




           (½ Mark for correct function header)
           (½ Mark for correct loop)
           (1 Mark for correct checking of odd elements in each pair)
           (1 Mark for swapping the elements)
     (b)   An array A[50][30] is stored along the row in the memory with each element requiring 4          3
           bytes of storage. If the element A[10][15] is stored at 21500, then find out the base
                                                      Page No. 11
```

---

## page 12

```
      address of the array and the memory address of element stored at location A[30][25]?
Ans   Row-major Formula:-                 A[I][J]= B+ W*((I-Lr)*Nc + (J-Lc))
      Nr=50, Nc=30, B=?, W=4, Lr=0, Lc=0, A(10,15)=21500
      A[10][15]= B + 4*((10-0)*30 + (15-0))
      21500= B + 4*(300+15)
      21500=B + 4*315
      B=21500 – 1260
      B=20240


      A[30][25] = 20240 + 4*((30-0)*30 + (25-0))
      A[30][25] = 20240 + 4*(900+25)
      A[30][25] = 20240 + 4*925
      A[30][25] = 23940


      (1 Mark for using correct formula for row major)
      (1/2 Mark each for substituting formula with correct values for calculation of Base
      address & address of A[30][25] element)
      (1/2 Mark for each correct final answer of Base address & address of A[30][25])
(c)   Write the definition of a member function Q_Insert() for a class Exam_Queue in C++       4
      to insert a new Application information in a dynamically allocated queue whose code is
      already given below as a part of the program(assume all necessary header files are
      included in program):




                                          Page No. 12
```

---

## page 13

```
Ans




      (1 Mark for creating new node)
      (½ Mark for entering values for the new node)
      (½ Mark for assigning NULL value to the new node)
      (½ Mark for assigning Front to the first node)
      (½ Mark for linking the last node to the new node)
      (1 Mark for assigning Rear to the new node)
(d)   Write the definition of a user-defined function REPEAT_ROW(int A[][3],int R, int C)         2
      in C++ that will store the elements in the following manner
         1. All row elements except the 1st element replaced by the 1st element,
         2. All row elements except the 1st & 2nd element replaced by the 2nd element,
         3. All row elements except the 1st , 2nd & 3rd element replaced by the 3rd element and
             so on.
      For example: if initially the array was:-
                               5        6         10       2
                               2        6         9        12
                              18        14        5        6
      Then, the contents of the array after execution of the above function will be:-
                               5        5         5        5
                               2        6         6        6
                              18        14        5        5




                                             Page No. 13
```

---

## page 14

```
Ans




      (1 Mark for correct loop)
      (1 Mark for correct placing elements)
(e)   Evaluate the following POSTFIX expression. Show the status of Stack after execution of   2
      each operation separately:
                    TRUE, FALSE, OR, NOT, TRUE, FALSE, AND, OR
Ans      S. No.               Element Scanned     Operation           Stack Status
         1                    True                Push (True)         True
         2                    False               Push (False)        True, False
         3                    OR                  Pop(False)          True
                                                  Pop(True)
                                                  OR(True,
                                                  False)=True
                                                  Push (True)
         4                    NOT                 Pop(True)           False
                                                  NOT(True)=False


         5                    True                Push (True)         False, True
         6                    False               Push (False)        False, True, False
         7                    AND                 Pop(False)          False, False
                                                  Pop(True)
                                                  AND(False,
                                                  True)=False
                                                  Push False
         8                    OR                  Pop(False)          False
                                                  Pop(False)
                                                  OR(False,
                                                  False)=False


                                         Page No. 14
```

---

## page 15

```
            The result is False
            (½ Mark for evaluating till OR operator)
            (½ Mark for evaluating till NOT operator)
            (½ Mark for evaluating till AND operator)
            (½ Mark for evaluating till OR operator)
            Note: (1 Mark to be given for writing correct answer as FALSE without showing
            the Stack Status)
Q4.   (a)   Answer the questions (i) & (ii) in the program segment given below for the required task.    1




               (i)
                       Write Statement 1 to position the file pointer to the appropriate place so that
                       the data updation is done for the correct Route.
               (ii)    Write Statement 2 to perform the write operation so that the updation is done
                       in the binary file “ROUTE.DAT”.

                                                 Page No. 15
```

---

## page 16

```
Ans      (i)        File.seekg(-sizeof(R), ios::cur);
         (ii)       File.write((char*)&R,sizeof(R));
      (½ Mark for each correct answer)
(b)   Write a user-defined function named Count() that will read the contents of text file     2
      named “Report.txt” and display the count of the number of lines that start with either
      „I‟ or „M‟.
      E.g. In the following paragraph, there are 3 lines starting with „I‟ or „M‟:
      “India is the fastest growing economy.
      India is looking for more investments around the globe.
      The whole world is looking at India as a great market.
      Most of the Indians can foresee the heights that India is capable of reaching.”
Ans




      (½ Mark for opening opinion.txt correctly)
      (½ Mark for fetching each line from the file correctly)
      (½ Mark for counting each word)
      (½ Mark for correct displaying the no. of lines which starts with „M‟ or „I‟)
(c)   Consider the following class Item:-                                                      3




                                             Page No. 16
```

---

## page 17

```
           Write a function named Change_Item(int Id, float Pr) to modify the price of the item
           whose Itemid & new price are passed as an argument.
     Ans




           (½ Mark for opening ITEM.DAT correctly)
           (1 Mark for reading all records from the file)
           (1 Mark for comparing value of Id from file & calling Set_Price() function)
           (½ Mark for writing new value of price in file)
                                         SECTION – B (Python)
Q1   (a)
           Differentiate between break and continue statement with the help of an example.
                                                                                                  2
     Ans   break statement is used to terminate the execution of the loop.

           For example:
                                               Page No. 17
```

---

## page 18

```
      The output of the above code will be:



      The loop terminates when i becomes 3 due to break statement
      Whereas,
      continue statement is used to force the next iteration while skipping the statements in
      the present iteration.




      The output of the above code will be:




      continue statement forces next iteration when i becomes 3 , bypassing the print
      statement .Thus ,in the output 3 is missing.

      (1 mark for explaining break statement with example)
      (1 mark for explaining continue statement with example)

(b)   Identify and write the name of the module to which the following functions belong:        1
      i. ceil( ) ii. findall()

Ans   i. ceil( ) - math module
      ii. findall( ) – re module

      (½ mark for each module)

(c)   Observe the following Python code very carefully and rewrite it after removing all        2
      syntactical errors with each correction underlined.




                                          Page No. 18
```

---

## page 19

```
Ans




      (½ mark for each correction)

(d)   Write the output of the following Python code:                                               2




Ans   14 : 7
      8 : 49

      (1 mark for each line of correct output)

(e)   Write the output of the following Python program code:                                       3




Ans   ['d', 'o', 'I', 'i', 't', '@', '@', '1', '1', '2', '3', '!', '!']
      (½ mark for converting „D‟ to „d‟)
      (½ mark for converting „I‟ to „i‟)
      (½ mark for substituting each „ „ with the consecutive character)
(f)   Study the following program and select the possible output(s) from the options (i) to (iv)   2

                                          Page No. 19
```

---

## page 20

```
           following it. Also, write the maximum and the minimum values that can be assigned to
           the variable Y.




           i) 0 : 0
           ii) 1 : 6
           iii) 2 : 4
           iv) 0 : 3
     Ans   i) and iv) are the possible output(s)

           Minimum value that can be assigned to Y = 0
           Maximum value assigned to Y = 3

           ( ½ mark for each correct possible output)
           ( ½ mark for each correct possible minimum and maximum value)

Q2   (a)   Explain operator overloading with the help of an example.                                   2
     Ans   The feature where an operator can be used in different forms is known as Operator
           Overloading. It is one of the methods to implement polymorphism.

           '+' operator behaves differently with different data types. With integers it adds the two
           numbers and with strings it concatenates or joins two strings.
            For example: Print 8+9 will give 17 and Print "Python" + "programming" will give the
           output as Python programming.


           (2 marks for correct explanation using an example)
           (1 mark for only writing a definition)

     (b)   Observe the following Python code and answer the questions (i) and (ii):




     (i)   How is data member „count‟ different from data member „Author‟?                             1
     Ans   Data member „count‟is a Class attribute whereas the data member „Author‟ is an
                                                   Page No. 20
```

---

## page 21

```
       Instance attribute.
       Class Attributes belong to the class itself. These attributes will be shared by all the
       instances. Such attributes are defined in the class body part, usually at the top, for
       legibility.
       Attributes defined for each class instance are known as Instance Attributes. These are
       called instance attributes and they belong to each instance/object of a class.

       (1 mark for correct point of difference)
(ii)   Fill in the blanks:                                                                       1
       B= BOOK()
       ______________________________ #Write statement to invoke Function 2
       ______________________________ #Write statement to invoke Function 3
Ans

       ( ½ mark for each correct statement)
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
                         Score             CNAME                   Fees
                         >=9.0 -<=10.0 Clinical Psychology         10000.0
                         >=8.0 - <9.0      Corporate Counselling    8000.0
                         >=5.0 - <8.0      Guidance and
                                           Counselling              6000.0
                         less than 5.0     Not Eligible                 0.0

                     GETDATA() to input REGNO and Score and invoke SetCourse()
                     DISPLAY() to display all the details.




                                          Page No. 21
```

---

## page 22

```
Ans




      (½ mark for correct definition of __init__())
      (2 marks for correct definition of SetCourse() :
             1 mark for applying conditions using if..elif..else
             1 mark for assigning correct values to CNAME and Fees
      )
      (1 mark for correct definition of GETDATA())
      (½ mark for correct definition of DISPLAY() )

(d)   Answer the questions (i) and (ii) based on the following:      4




                                          Page No. 22
```

---

## page 23

```
(i)    Explain the relationship between Line 1 , Line 2 and Line 3.
Ans    Line 1 is a parameterized constructor of derived class RacingCar that accepts values for
       its instance variables turnRadius ,speed . It accepts clr,seats,l,w to initialize the
       instance variables colour with clr , seatingCapacity with seats of base class Car
       through its constructor function/__init__()(Line 2) and invokes constructor
       function/__init__() of base class Vehicle to initialize its instance variables length with l
       and width with w(Line 3).

       (2 marks for appropriate answer justifying the passing of parameters to initialize
       members of base class via __init__( ))


(ii)   Predict the output that will be produced on the execution of the following statements :




Ans




       (½ mark for each line of output)




                                            Page No. 23
```

---

## page 24

```
Q3   (a)    Write the definition of a function Reverse(X) in Python, to display the elements in        2
            reverse order such that each displayed element is the twice of the original element
            (element * 2) of the List X in the following manner:
            Example:
            If List X contains 7 integers is as follows:
               X[0]      X[1]       X[2]       X[3]      X[4]    X[5]       X[6]
                 4         8          7          5         6       2         10
            After executing the function, the array content should be displayed as follows:
                20         4         12         10        14      16         8

     Ans


            (1 mark for correct loop)
            (1 mark for displaying twice of the list element)
     (b)    Consider the following unsorted list :                                                     3
            [22, 54, 12, 90, 55, 78]
            Write the passes of selection sort for sorting the list in ascending order till the 3rd
            iteration.

     Ans    Pass 1: [12, 54, 22, 90, 55, 78]
            Pass 2 : [12, 22, 54, 90, 55, 78]
            Pass 3 : [12, 22, 54, 90, 55, 78]

            (1 mark to produce correct List after each pass.)
     (c)    Consider the following class Order and do as directed:                                     4




                                                                   Blank 1
                         :
                         :
            i. Fill in the blank 1 with a statement to insert OID in the Queue maintained using List
            L.
            ii. Complete the definition of delorder() to delete OID from the Queue maintained using
            List L, the function should return the OID being deleted or -1 in case the Queue is
            empty.

     Ans:   i. self.L.append(self.OID)

            ( 1 mark for the correct answer)
            ii.




                                                  Page No. 24
```

---

## page 25

```
       (1 mark for applying condition to check if Queue is empty)
       (½ mark for returning -1)
       (1 mark for deleting the first element from the Queue)
       (½ mark for returning the deleted value)
d)     Write a generator function to generate odd numbers between a and b (including b).Note:      3
       a and b are received as an argument by the function.
Ans:




       (½ mark for correct function header)
       (1 mark for correct use of loop)
       ( ½ mark for condition)
       (1 mark for using yield() to yield the correct value)
(e)    Evaluate the following postfix expression using a stack. Show the contents of stack after   2
       execution of each operation:
       10,40,25,-,*,15,4,*,+
Ans
         Symbol Operation                  Stack         Result

         10         Push(10)               10

         40         Push(40)               10,40

         25         Push(25)               10,40,25

         -          Pop(25)                10,15
                    Pop(40)
                    Push(40-25)
                    =15

         *          Pop(15)                150
                    Pop(10)
                    Push(10*15)
                    =150

         15         Push(15)               150,15

         4          Push(4)                150,15,4

         *          Pop(4)                 150,60
                    Pop(15)
                    Push(15*4)=60

                                           Page No. 25
```

---

## page 26

```
              +          Pop(60)                 210          210
                         Pop(150)
                         Push(150+60)=210
             (½ mark for correct stack status till „-‟)
             (½ mark for correct stack status till „*‟)
             (½ mark for correct stack status till „*‟)
             (½ mark for correct stack status till „+‟)
             or
            (½ mark for writing the correct result without showing the working of Stack)
Q4.   (a)   Nancy intends to position the file pointer to the beginning of a text file.Write Python   1
            statement for the same assuming F is the Fileobject.
      Ans   F.seek(0)

            (1 mark for the correct answer)
      (b)   Write a function countmy( )in Python to read the text file “DATA.TXT” and count the
            number of times “my” occurs in the file.
            For example if the file “DATA.TXT” contains:
                                                                                                      2
            “This is my website. I have displayed my preferences in the CHOICE section.”
            The countmy( ) function should display the output as:
            “my occurs 2 times”.
      Ans




            (½ mark for reading the file using read)
            (½ mark for correctly using split())
            (½ mark for the correct loop)
            (½ mark for displaying the correct value of count)
      (c)   Write a function in Python to search and display details of all those students, whose     3
            stream is “HUMANITIES” from pickled file “Student.dat”. Assuming the pickled file is
            containing the objects of the following class:




                                                Page No. 26
```

---

## page 27

```
     Ans:




                                                                       -


            (½ mark for opening the file in correct mode)
            (½ mark for try.. except EOFError)
            (½ mark for while loop)
            (½ mark for using pickle.load() correctly)
            (½ mark for comparison using if)
            (½ mark for displaying)

                                               SECTION – C
Q5   (a)    Differentiate between DDL & DMLcommands. Identify DDL & DML commands from       2
            the following:-
                              (UPDATE, SELECT, ALTER, DROP)
     Ans    DDL stands for Data Definition language and comprises of commands which will
            change the structure of database object.
            DML stands for Data Manipulation Language and comprises of commands which
            are used to insert, edit, view & delete the data stored in a database object.
            DDL Commands:          ALTER, DROP
            DML Commands:          UPDATE, SELECT

                                                Page No. 27
```

---

## page 28

```
      (1 Mark for correct definition of DDL & DML commands)
      (½ Mark each for correct identification of commands)
(b)   Consider the following relations MobileMaster & MobileStock:-                           6
                                               MobileMaster
                 M_Id        M_Company           M_Name            M_Price       M_Mf_Date
                 MB001         Samsung            Galaxy            4500         2013-02-12
                 MB003           Nokia             N1100            2250         2011-04-15
                 MB004        Micromax             Unite3           4500         2016-10-17
                 MB005           Sony            XperiaM            7500         2017-11-20
                 MB006           Oppo             SelfieEx          8500         2010-08-21


                                                MobileStock
                  S_Id               M_Id               M_Qty                 M_Supplier
                  S001             MB004                     450              New Vision
                  S002             MB003                     250            Praveen Gallery
                  S003             MB001                     300       Classic Mobile Store
                  S004             MB006                     150             A-one Mobiles
                  S005             MB003                     150              The Mobile
                  S006             MB006                     50              Mobile Centre


      Write the SQL query for questions from (i) to (iv) & write the output of SQL command
      for questions from (v) to (viii) given below:-
         (i)       Display the Mobile company, Mobile name & price in descending order of
                   their manufacturing date.
         (ii)      List the details of mobile whose name starts with „S‟.
         (iii)     Display the Mobile supplier & quantity of all mobiles except „MB003‟.
         (iv)      To display the name of mobile company having price between 3000 & 5000.
         (v)       SELECT M_Id, SUM(M_Qty) FROM MobileStock GROUP BY M_Id;
         (vi)      SELECT MAX(M_Mf_Date), MIN(M_Mf_Date) FROM MobileMaster;
         (vii)     SELECT M1.M_Id, M1.M_Name, M2.M_Qty, M2.M_Supplier FROM
                   MobileMaster M1, MobileStock M2 WHERE M1.M_Id=M2.M_Id AND
                   M2.M_Qty>=300;


                                               Page No. 28
```

---

## page 29

```
      (viii) SELECT AVG(M_Price) FROM MobileMaster;
Ans   (i)     SELECT M_Compnay, M_Name, M_Price FROM MobileMaster
              ORDER BY M_Mf_Date DESC;
              (½ mark for correct SELECT)
              (½ mark for correct ORDER BY)
      (ii)    SELECT * FROM MobileMaster WHERE M_Name LIKE „S%‟;
              (½ mark for correct SELECT)
              (½ mark for correct WHERE clause)
      (iii)   SELECT M_Supplier, M_Qty FROM MobileStock WHERE M_Id <>
              „MB003‟;
              (½ mark for correct SELECT)
              (½ mark for correct WHERE clause)
      (iv)    SELECT     M_Company         FROM      MobileMaster   WHERE   M_Price
              BETWEEN 3000 AND 5000;
              (½ mark for correct SELECT)
              (½ mark for correct BETWEEN clause)


      (v)
               M_Id                  SUM(M_Qty)
               MB004                 450
               MB003                 400
               MB001                 300
               MB006                 200
              (½ mark for correct output)


      (vi)
               MAX(M_Mf_Date)              MIN(M_Mf_Date)
               2017-11-20                  2010-08-21
              (½ mark for correct output)


      (vii)
               M_Id         M_Name           M_Qty        M_Supplier
               MB004        Unite3           450          New_Vision


                                      Page No. 29
```

---

## page 30

```
                        MB001           Galaxy        300               Classic Mobile Store
                       (½ mark for correct output)
                 (viii) 5450
                       (½ mark for correct output)
Q6.   (a)   State & prove De-Morgan‟s law using truth table.                                      2
      Ans   De-morgan‟s Law: (A+B)‟ = A‟.B‟
                                  (A.B)‟ = A‟+B‟
            Proof using Truth Table
             A         B          A+B       (A+B)‟    A‟           B‟           A‟.B‟
             0         0          0         1         1            1            1
             0         1          1         0         1            0            0
             1         0          1         0         0            1            0
             1         1          1         0         0            0            0


            (½ mark each for stating correct De-morgan‟s law)
            (1 mark for correct proof)
      (b)   Draw the equivalent logic circuit diagram of the following Boolean expression:-       2
                                  (A‟ + B).C‟
      Ans   Logic Circuit Diagram for (A‟ + B).C‟ is given as:-




            (½ mark each for correct placement of gate)
      (c)   Write the SOP form for the Boolean Function F(X,Y,Z) represented by the given truth   1
            table:-
                                      X           Y            Z            F
                                      0           0            0            0
                                      0           0            1            1
                                      0           1            0            1

                                                 Page No. 30
```

---

## page 31

```
                                   0          1            1        0
                                   1          0            0        0
                                   1          0            1        0
                                   1          1            0        1
                                   1          1            1        1
      Ans   SOP Form is : X‟.Y‟.Z + X‟.Y.Z‟ + X.Y.Z‟ + X.Y.Z

            (1 mark for correct answer)
            Note: Deduct ½ mark if wrong variable names are written in the expression
      (d)   Reduce the following Boolean expression using K-Map:-                              3
                         F(U,V,W,Z)= π(0,2,5,7,12,13,15)
      Ans   POS form using K-Map is given as:-




            Quad 1: (V‟+Z')
            Pair 1: (U+V+Z)
            Pair 2: (U‟+V‟+W)
            POS Form: (V‟+Z').(U+V+Z).(U‟+V‟+W)


            ( ½ Mark for drawing K‐Map with correct variable names)
            ( ½ Mark each for correct placement of 0)
            ( ½ Mark each for 3 groupings)
            ( ½ Mark for writing final expression in reduced/minimal form)
            Note: Deduct ½ mark if wrong variable names are used
Q7.   (a)   A teacher provides “http://www.XtSchool.com/default.aspx” to his/her students to   1
                                             Page No. 31
```

---

## page 32

```
      identify the URL & domain name.
Ans   URL: http://www.XtSchool.com/default.aspx
      Domain name: XtSchool.com


      (½ mark for each correct answer)
(b)   Which out of the following does not come under Cyber Crime?                                 1
      (i) Copying data from the social networking account of a person without his/her
              information & consent.
      (ii) Deleting some files, images, videos, etc. from a friend‟s computer with his consent.
      (iii) Viewing & transferring funds digitally from a person‟s bank account without
              his/her knowledge.
      (iv) Intentionally making a false account on the name of a celebrity on a social
              networking site.
Ans   (ii)


      (1 mark for correct answer)
(c)   Expand the following:-                                                                      1
             1. GSM                    2. TDMA
Ans   GSM: Global System for Mobile Communication
      TDMA: Time Division Multiple Access


      (½ mark for each correct answer)
(d)   What is the significance of cookies stored on a computer?                                   1
Ans   Cookies is small text file that web servers send to a web browser so that the web server
      can keep track of the user‟s activity on a particular website.


      (1 mark for correct answer)
(e)   Kabir wants to purchase a Book online and placed the order for that book using an e-        1
      commerce website. Now, he is going to pay the amount for that book online using his
      Mobile, he needs which of the following to complete the online transaction:-
             1. A bank account,
             2. A Mobile connection/phone which is attached to above bank account,
             3. The mobile banking app of the above bank installed on that mobile,


                                            Page No. 32
```

---

## page 33

```
         4. Login credentials(UserId & Password) provided by the bank,
         5. All of above.
Ans   Option No.5


      (1 mark for correct answer)
(f)   What do you mean by data encryption? For what purpose it is used for?                      1
Ans   Data encryption is a technique used for data security in which original message is
      converted or encoded using an algorithm into a form not understood by anyone
      except the person who has the key to decode it.


      (½ mark for correct definition)
      (½ mark for its purpose: data security)
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
                     Building 1              Building 2          Distance(in mtrs.)

                        Main                   Admin                     50

                        Main                  Finance                    100
                        Main                 Academic                    70
                       Admin                  Finance                    50
                      Finance                Academic                    70
                       Admin                 Academic                    60
      Number of computers:-
                                          Page No. 33
```

---

## page 34

```
                                Building                 No. of Computers
                                 Main                          150
                                 Admin                          75
                                Finance                         50
                                Academic                        60
      As a network expert, you are required to give best possible solutions for the given
      queries of the university administration:-
         (a) Suggest cable layout for the connections between the various buildings,
         (b) Suggest the most suitable building to house the server of the network of the     1
             university,
         (c) Suggest the placement of following devices with justification:                   1
             1. Switch/Hub
             2. Repeater                                                                      1
         (d) Suggest the technology out of the following for setting-up very fast Internet
             connectivity among buildings of the university                                   1
             1. Optical Fibre
             2. Coaxial cable
             3. Ethernet Cable
Ans      (a) Star topology




             (1 mark for drawing correct layout)
         (b) Server should be placed at Main Building as it has the maximum number of
             computers.
             (1 mark for correct answer)
         (c) Hub/Switch each would be needed in all the buildings to interconnect the group
             of cables from the different computers in each building
             A repeater needs to be placed along the wire between main building & finance
             building as the distance between them is more than 70 mtr.
                                           Page No. 34
```

---

## page 35

```
   (½ mark for each correct placement)
   (½ mark for each correct justification)
(d) Optical Fibre
   (1 mark for correct answer)

                                 *********




                              Page No. 35
```