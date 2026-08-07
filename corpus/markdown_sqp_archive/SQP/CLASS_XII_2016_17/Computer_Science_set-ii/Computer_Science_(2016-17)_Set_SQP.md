---
title: "Computer Science (2016-17) Set SQP"
source_pdf: "Computer_Science_(2016-17)_Set_SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2016_17/Computer Science set-ii/Computer Science (2016-17) Set SQP.pdf"
pages: 20
pdf_bytes: 144476
pdf_sha256: "b4c17d6e728b3a570e45d71f8b4013088d5b63c82eb72d92b1a1bbeb6df24b0b"
text_chars: 23479
low_text_pages: 0
converter: "pdftotext -layout"
---

# Computer Science (2016-17) Set SQP


---

## page 1

```
                       SQP - Computer Science (Code: 083)
                               Class XII (2016-17)
Time: 3Hrs.                                                                   MM: 70
Instructions:
i.    All Questions are Compulsory.
ii.   Programming Language : Section – A : C++
iii. Programming Language : Section – B : Python
iv. Answer either Section A or B and Section C is compulsory
                                   Section – A
1   (a)       Explain conditional operator with suitable example?                      2
    (b)       Which C++ header file(s) are essentially required to be included to      1
              run/execute the following C++ code :
              void main()
              {
              char *word1="Hello",*word2="Friends";
              strcat(word1,word2);
              cout<<word1;
              }
    (c)       Rewrite the following program after removing the syntactical errors      2
              (if any). Underline each correction.

              #include<conio.h>
              #include<iostream.h>
              #include<string.h>
              #include<stdio.h>
              class product
              {
                int product_code,qty,price;
                char name[20];
                public:
                product(){
                            product_code=0;qty=0;price=0;
                            name=NULL;
                            }
                void entry()
                {
```

---

## page 2

```
         cout<<"\n Enter code,qty,price";
         cin>>product_code>>qty>>price;
         gets(name);
        }
         void tot_price() {return qty*price;}
      };
      void main()
      {
        p product;
        p.entry();
        cout<<tot_price();
      }
(d)   Write the output of the following C++ program code:                    2
      Note: Assume all required header files are already being included in
      the program.
      void change(int *s)
      {
       for(int i=0;i<4;i++)
       {
         if(*s<40)
         {
         if(*s%2==0)
         *s=*s+10;
         else
         *s=*s+11;
         }
         else
         {
         if(*s%2==0)
         *s=*s-10;
         else
         *s=*s-11;
         }
         cout<<*s<<" ";
         s++;
       }
      }
      void main()
      {
```

---

## page 3

```
       int score[]={25,60,35,53};
       change(score);
      }
(e)   Write the output of the following C++ program code:                    3
      Note: Assume all required header files are already being included in
      the program.
      class seminar
      {
      char topic[30];
      int charges;
      public:
      seminar()
      {
      strcpy(topic,"Registration");
      charges=5000;
      }
      seminar(char t[])
      {
      strcpy(topic,t);
      charges=5000;
      }
      seminar(int c)
      {
      strcpy(topic,"Registration with Discount");
      charges=5000-c;
      }
      void regis(char t[],int c)
      {
      strcpy(topic,t);
      charges=charges+c;
      }
      void regis(int c=2000)
      {
      charges=charges+c;
      }
      void subject(char t[],int c)
      {
      strcpy(topic,t);
      charges=charges+c;
```

---

## page 4

```
      }
      void show()
      {
      cout<<topic<<"@"<<charges<<endl;
      }
      };
      void main()
      {
      seminar s1,s2(1000),s3("Genetic Mutation"),s4;
      s1.show();
      s2.show();
      s1.subject("ICT",2000);
      s1.show();
      s2.regis("Cyber Crime",2500);
      s2.show();
      s3.regis();
      s3.show();
      s4=s2;
      s4.show();
      getch();
      }
(f)   Observe the following program carefully and attempt the given   2
      questions:
      #include<iostream.h>
      #include<conio.h>
      #include<stdlib.h>
      void main()
      {
      clrscr();
      randomize();
      char courses[][10]={"M.Tech","MCA","MBA","B.Tech"};
      int ch;
         for(int i=1;i<=3;i++)
            {
               ch=random(i)+1;
               cout<<courses[ch]<<"\t";
            }
      getch();
      }
```

---

## page 5

```
          I. Out of all the four courses stored in the variable courses, which
          course will never be displayed in the output and which course will
          always be displayed at first in the output?
          II. Mention the minimum and the maximum value assigned to the
          variable ch?
2   (a)    What do you understand by Function overloading or Functional          2
           polymorphism? Explain with suitable example.
    (b)     Answer the questions(i) and (ii) after going through the following   2
           class:
           class planet
           {
               char name[20];char distance[20];
           public:
             planet()                               //Function 1
             {
                  strcpy(name, "Venus");
                  strcpy(distance,"38 million km");
             }
              void display(char na[],char d[])               //Function 2
             {
                  cout<<na<<"has "<<d<<" distance from Earth"<<endl;
             }
             planet(char na[], char d[])              //Function 3
             {
                  strcpy(name,na);
                  strcpy(distance,d);
             }
             ~planet()                                  //Function 4
             {
                  cout<<"Planetarium time over!!!"<<endl;
             }
           };
           I. What is Function 1 referred as? When will it be executed?
           II. Write suitable C++ statement to invoke Function 2.
    (c)    Define a class DanceAcademy in C++ with following description:        4
           Private Members
                     ● Enrollno of type int
```

---

## page 6

```
               ●    Name of type string
               ●    Style of type string
               ●    Fee of type float
               ●    A member function chkfee( ) to assign the value of fee
                    variable according to the style entered by the user
                    according to the criteria as given below:


          Style             Fee

        Classical          10000

         Western           8000

        Freestyle          11000

      Public Members
               ● A function enrollment() to allow users to enter values
                 for Enrollno,Name, Style and call function chkfee()to
                 assign value of fee variable according to the Style
                 entered by the user.
               ● A function display() to allow users to view the details of
                 all the data members.
(d)   Answer the questions (i) to (iv) based on the following:                4
      class indoor_sports
      {
        int i_id;
        char i_name[20];
        char i_coach[20];
      protected:
        int i_rank,i_fee;
        void get_ifee();
      public:
        indoor_sports();
        void iEntry();
        void ishow();
      };
      class outdoor_sports
      {
        int o_id;
        char o_name[20];
```

---

## page 7

```
            char o_coach[20];
          protected:
            int orank,ofee;
            void get_ofee();
          public:
            outdoor_sports();
            void oEntry();
            void oshow();
          };
          class sports:public indoor_sports,protected outdoor_sports
          {
           char rules[20];
           public:
                 sports();
             void registration();
             void showdata();
          };
          (i) Name the type of inheritance illustrated in the above C++ code.
          (ii) Write the names of all the members, which are accessible from
          the objects belonging to class outdoor_sports.
          (iii) Write the names of all the member functions, which are
          accessible from the member function of class sports.
          (iv) What will be the size of the object belonging to class
          indoor_sports?
3   (a)   Write the definition of a function grace_score (int score [], int size) in   3
          C++, which should check all the elements of the array and give an
          increase of 5 to those scores which are less than 40.

          Example: if an array of seven integers is as follows:
                45, 35, 85, 80, 33, 27, 90
          After executing the function, the array content should be changed as
          follows:
                45, 40, 85, 80, 38, 32, 90
    (b)   An array P[30][20] is stored along the column in the memory with             3
          each element requiring 2 bytes of storage. If the base address of the
          array P is 26500, find out the location of P[20][10].
```

---

## page 8

```
(c)   Write the definition of a member function push() for a class Library in   4
      C++ to insert a book information in a dynamically allocated stack of
      books considering the following code is already written as a part of
      the program:
      struct book
      {
      int bookid;
      char bookname[20];
      book *next;
       };
      class Library
      {
      book *top;
      public:
      Library()
      {
      top=NULL;
      }
      void push();
      void pop();
      void disp();
      ~Library();
      };
(d)   Write a user-defined function swap_row(int ARR[ ][3],int R,int C) in      2
      C++ to swap the first row values with the last row values:

      For example if the content of the array is:


      10       20        30

      40       50        60

      70       80        90

      Then after function call, the content of the array should be:


      70       80        90
```

---

## page 9

```
          10       20       30

    (e)   Evaluate the following POSTFIX expression. Show the status of           2
          Stack after execution of each operation separately:
                        45, 45, +, 32, 20, 10, /, -,*
4   (a)   Find the output of the following C++ code considering that the binary   1
          file sp.dat already exists on the hard disk with 2 records in it.
          class sports
          {
            int id;
            char sname[20];
            char coach[20];
            public:
            void entry();
            void show();
            void writing();
            void reading();
          }s;

           void sports::reading()
           {
           ifstream i;
           i.open("sp.dat");
           while(1)
           {
           i.read((char*)&s,sizeof(s));
           if(i.eof())
           break;
           else
           cout<<"\n"<<i.tellg();
           }
           i.close();
           }
           void main()
           {
           s.reading();
           }
    (b)   Write a user defined function word_count() in C++ to count how          2
          many words are present in a text file named “opinion.txt”.
```

---

## page 10

```
      For example, if the file opinion.txt contains following text:


       Co-education system is necessary for a balanced society. With
       co-education system, Girls and Boys may develop a feeling of
       mutual respect towards each other.


      The function should display the following:
      Total number of words present in the text file are: 24

(c)   Write a function display () in C++ to display all the students who have      3
      got a distinction(scored percentage more than or equal to 75) from a
      binary file “stud.dat”, assuming the binary file is containing the objects
      of the following class:
      class student
      {
             int rno;
             char sname [20];
             int percent;
             public:
           int retpercent()
            {
             return percent;
             }
             void getdetails()
             {
             cin>>rno;
                gets(sname);
             cin>>percent;
             }
           void showdetails()
           {
             cout<<rno;
               puts(sname);
             cout<<percent;
             }
      };
```

---

## page 11

```
                              Section - B (Python)
1   (a)   Carefully observe the following python code and answer the questions   2
          that follow:




          On execution the above code produces the following output.
          6
          3
          Explain the output with respect to the scope of the variables.
    (b)   Name the modules to which the following functions belong:              1
           a. uniform()      b. fabs()
    (c)   Rewrite the following code after removing the syntactical errors (if   2
          any). Underline each correction.




    (d)   Observe the following Python code carefully and obtain the output,     2
          which will appear on the screen after execution of it.
```

---

## page 12

```
    (e)   What output will be generated when the following Python code is         3
          executed?




    (f)   Observe the following program and answer the questions that follow:     2
          import random




            a. What is the minimum and maximum number of times the loop
               will execute?
            b. Find out, which line of output(s) out of (i) to (iv) will not be
               expected from the program?
               i. 0#1
               ii. 1#2
               iii. 2#3
               iv. 3#4
2   a     Explain the two strategies employed by Python for memory                2
          allocation.
    b     Observe the following class definition and answer the questions that    2
          follow:
```

---

## page 13

```
     i. Write statement to invoke Function 1.
     ii. On Executing the above code , Statement 2 is giving an error
     explain.
c   Define a class PRODUCT in Python with the following specifications            4
    Data members:
    Pid       – A string to store productid.
    Pname       - A string to store the name of the product.
    Pcostprice – A decimal to store the cost price of the product
    Psellingprice – A decimal to store Selling Price
    Margin      - A decimal to be calculated as Psellingprice - Pcostprice
    Remarks        - To store”Profit” if Margin is positive else “Loss” if
                  Margin is negative
    Member Functions:
       ● A constructor function to initialize All the data members with
             valid default values.
       ● A        method     SetRemarks()      that    assigns   Margin      as
             Psellingprice - Pcostprice and sets Remarks as mentioned
             below:


     Margin            Remarks

     <0 ( negative) Loss
```

---

## page 14

```
     >0(positive)      Profit


       ● A          method      Getdetails()   to   accept     values   for
           Pid,Pname,Pcostprice,Psellingprice and invokes SetRemarks()
           method.
       -   A method Setdetails() that displays all the data members.
d   Answer the questions (i) to (iv) based on the following:                  4
```

---

## page 15

```
        i.     Which type of Inheritance is demonstrated in the above code?
        ii. Explain Statement 1 and 2.
        iii. Name the methods that are overridden along with their class name.
        iv. Fill Blank1 with a statement to display variable category of class
        Brand.
3   a        Consider the following unsorted list                                       3
             95 79 19 43 52 3
              Write the passes of bubble sort for sorting the list in ascending order
             till the 3rd iteration.
    b    Kritika was asked to accept a list of even numbers but she did not put         3
        the relevant condition while accepting the list of numbers. You are
        required to write a code to convert all the odd numbers into even by
        multiplying them by 2.
    c        Aastha wants to create a program that accepts a string and display the     4
             characters in the reverse order in the same line using a Stack. She has
             created the following code , help her by completing the definitions on
             the basis of requirements given below :
             class mystack:
                   def __init__(self):
                        self.mystr= ________________ # Accept a string
                        self.mylist =________________ # Convert mystr to a list
              # Write code to display while removing elements from the stack.
                   def disp(self):
                      :
                      :


    d   Write a generator function generatesq() that displays the squareroots of        2
        numbers from 100 to n where n is passed as an argument .
    e        Evaluate the following Postfix expression:                                 2
                    20,10,-,15,3,/,+,5,*
4   a     Observe the following code and answer the questions that follow:              1
          File = open("Mydata","a")
          _____________________ #Blank1
          File.close()
        i. What type (Text/Binary) of file is Mydata?
```

---

## page 16

```
          ii. Fill the Blank 1 with statement to write “ABC” in the file “Mydata”


    b     A text file “Quotes.Txt” has the following data written in it:              2

          Living a life you can be proud of
          Doing your best
          Spending your time with people and activities that are important to you
          Standing up for things that are right even when it’s hard
          Becoming the best version of you

          Write a user defined function to display the total number of words
          present in the file.


    c      Consider the following class declaration and answer the question that      3
           follows:




                                                                                A
          nuj has been asked to display all the students who have scored less than
          40 for Remedial Classes.
          Write a user defined function to display all those students who have
          scored less than 40 from the binary file “Student.dat” assuming it stores
          all the object of the class Student mentioned above.
                                     Section – C
5   (a)    Observe the table ‘Club’ given below:                                      2

                                             Club
           Member_id      Member_Name Address             Age    Fee
```

---

## page 17

```
      M002             Nisha              Gurgaon     19    3500

      M003             Niharika           New Delhi   21    2100

      M004             Sachin             Faridabad   18    3500

      i.    What is the cardinality and degree of the above given table?
      ii. If a new column contact_no has been added and three more
      members have joined the club then how these changes will affect the
      degree and cardinality of the above given table.
(b)   Write SQL commands for the queries (i) to (iv) and output for (v) to      6
      (viii) based on the tables ‘Watches’ and ‘Sale’ given below.

      Watches
      Watchid          Watch_Name           Price     Type          Qty_Store
      W001             HighTime             10000     Unisex        100
      W002             LifeTime             15000     Ladies        150
      W003             Wave                 20000     Gents         200
      W004             HighFashion          7000      Unisex        250
      W005             GoldenTime           25000     Gents         100

      Sale
       Watchid             Qty_Sold           Quarter
       W001                10                 1
       W003                5                  1
       W002                20                 2
       W003                10                 2
       W001                15                 3
       W002                20                 3
       W005                10                 3
       W003                15                 4
      i. To display all the details of those watches whose name ends with
         ‘Time’

      ii. To display watch’s name and price of those watches which have price
           range in between 5000-15000.

      iii. To display total quantity in store of Unisex type watches.

      iv. To display watch name and their quantity sold in first quarter.

      v.       select max(price), min(qty_store) from watches;
```

---

## page 18

```
           vi.   select quarter, sum(qty_sold) from sale group by quarter;

           vii. select watch_name,price,type from watches w, sale s where
             w.watchid!=s.watchid;

           viii. select watch_name, qty_store, sum(qty_sold), qty_store-
             sum(qty_sold) “Stock” from watches w, sale s where
             w.watchid=s.watchid group by s.watchid;

6   (a)   Correct the following boolean statements:                              2
             1. X+1 = X
             2. (A')'=A'
             3. A+A'=0
             4. (A+B)' = A.B


    (b)    Draw the equivalent logic circuit for the following Boolean           1
           expression:
                       (A.B)+C
    (c)    Write the POS form of a Boolean Function F, which is represented in   2
           a truth tale as follows:


           P         Q         R          F

           0         0         0          0

           0         0         1          1

           0         1         0          1

           0         1         1          1

           1         0         0          0

           1         0         1          1

           1         1         0          0

           1         1         1          1

    (d)    Reduce the following Boolean Expression using K Map:                  3
           F(A,B,C,D)=
7   (a)    Identify the type of topology on the basis of the following:          2
             1. Since every node is directly connected to the server, a large
```

---

## page 19

```
           amount of cable is needed which increases the installation cost
           of the network.
        2. It has a single common data path connecting all the nodes.
(b)   Expand the following:                                                    1
        a. VOIP
        b. SMTP
(c)   Who is a hacker?                                                         1
(d)   The following is a 32 bit binary number usually represented as 4         1
      decimal values, each representing 8 bits, in the range 0 to 255 (known
      as octets) separated by decimal points.
                      140.179.220.200
      What is it? What is its importance?
(e)   Daniel has to share the data among various computers of his two          1
      offices branches situated in the same city. Name the network (out of
      LAN, WAN, PAN and MAN) which is being formed in this process.

(f)   Rehaana Medicos Center has set up its new center in Dubai. It has
      four buildings as shown in the diagram given below:




      Distances between various buildings are as follows:


        Accounts to Research Lab               55 m

        Accounts to Store                      150 m

        Store to Packaging Unit                160 m

        Packaging Unit to Research Lab         60 m
```

---

## page 20

```
 Accounts to Packaging Unit           125 m

 Store to Research Lab                180 m


Number of Computers


Accounts          25

Research Lab      100

Store             15

Packaging Unit    60

As a network expert, provide the best possible answer for the
following queries:
i) Suggest a cable layout of connections between the buildings.        1
ii) Suggest the most suitable place (i.e. buildings) to house the server of this
organization.                                                          1
iii) Suggest the placement of the following device with justification:
        a) Repeater                   b) Hub/Switch                    1
iv) Suggest a system (hardware/software) to prevent unauthorized
                                                                   1
access to or from the network.
```