---
title: "Computer Science (2016-17) Set MS"
source_pdf: "Computer_Science_(2016-17)_Set_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2016_17/Computer Science set-ii/Computer Science (2016-17) Set MS.pdf"
pages: 38
pdf_bytes: 263725
pdf_sha256: "038af1daa0a43daf77cffdccca1aa62a851178acbc59a3b3feba449f653c7895"
text_chars: 41981
low_text_pages: 0
converter: "pdftotext -layout"
---

# Computer Science (2016-17) Set MS


---

## page 1

```
                Marking Scheme- Computer Science (Code: 083)
                            Class XII (2016-17)
Time: 3 Hrs.                                                                       MM: 70
Instructions:
i.    All Questions are Compulsory.
ii.   Programming Language : Section – A : C++
iii. Programming Language : Section – B : Python
iv. Answer either Section A or B and Section C is compulsory.
                                     Section – A
1   (a)        Explain conditional operator with suitable example?                          2
    Ans        Conditional operator is also known as ternary operator because it
               requires three operands and can be used to replace simple if-else
               code. It is used to check the condition and execute first expression if
               condition is true else execute other.

               Syntax:
               Conditional expression? Expression 1 : Expression 2;

               Explanation:

               If the conditional expression is true then expression 1 executes
               otherwise expression 2 executes.

               Example:
               int y=10,x;
               x=y>10?1:0;
               cout<<x;

               Output: 0

               (1 Mark for correct explanation)
               (1 Mark for correct example)
    (b)        Which C++ header file(s) are essentially required to be included to          1
               run/execute the following C++ code :
               void main()
               {
```

---

## page 2

```
      char *word1="Hello",*word2="Friends";
      strcat(word1,word2);
      cout<<word1;
      }
Ans   iostream.h
      string.h

      (½ Mark each for writing correct header file)
(c)   Rewrite the following program after removing the syntactical errors   2
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
Ans   #include<conio.h>
```

---

## page 3

```
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
                      strcpy(name,NULL);
                      }
         void entry()
         {
          cout<<"\n Enter code,qty,price";
          cin>>product_code>>qty>>price;
          gets(name);
         }
          int tot_price() {return qty*price;}
       };
       void main()
       {
         product p;
         p.entry();
         cout<<p.tot_price();
       }


      (½ Mark for each correction upto a maximum of four corrections)
        OR
      (1 Mark for only identifying any 4 errors without suggesting
      corrections)
(d)    Write the output of the following C++ program code:                    2
       Note: Assume all required header files are already being included in
       the program.
       void change(int *s)
       {
        for(int i=0;i<4;i++)
        {
          if(*s<40)
```

---

## page 4

```
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
        int score[]={25,60,35,53};
        change(score);
       }
Ans   36 50 46 42
      (½ Mark for each correct value of output)
(e)    Write the output of the following C++ program code:                    3
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
```

---

## page 5

```
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
```

---

## page 6

```
       getch();
       }
Ans    Registration@5000
       Registration with Discount@4000
       ICT@7000
       Cyber Crime@6500
       Genetic Mutation@7000
       Cyber Crime@6500

       (½ Mark for each correct line of output)
       Note:
       Deduct ½ Mark for not considering any “@” symbol.
(f)    Observe the following program carefully and attempt the given         2
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

      I. Out of all the four courses stored in the variable courses, which
      course will never be displayed in the output and which course will
      always be displayed at first in the output?
      II. Mention the minimum and the maximum value assigned to the
      variable ch?

Ans   I. M.Tech will never be displayed in the output.
       MCA will always be displayed at first in the output.
```

---

## page 7

```
          II. Minimum value of ch=1
             Maximum value of ch=3

           (½ Mark for each correct answer)
           Note:
           Deduct ½ Mark for writing any additional option.

2   (a)   What do you understand by Function overloading or Functional             2
          polymorphism? Explain with suitable example.
    Ans   It is a method of using the same function or method to work using
          different sets of input. Function overloading is one of the example of
          polymorphism, where more than one function carrying same name
          behave differently with different set of parameters passed to them.

          void show()
          {
          cout<<”\n Hello World!”;
          }
          void show(char na[])
          {
          cout<<”\n Hello World! Its ”<<na;
          }

          (1 Mark for correct explanation of Function overloading)
          (1 Mark for suitable example of Function overloading)
    (b)    Answer the questions(i) and (ii) after going through the following      2
          class:
          class planet
          {
              char name[20];char distance[20];
          public:
            planet()                                       //Function 1
            {
                 strcpy(name, "Venus");
                 strcpy(distance,"38 million km");
            }
             void display(char na[],char d[])               //Function 2
            {
                 cout<<na<<"has "<<d<<" distance from Earth"<<endl;
```

---

## page 8

```
        }
        planet(char na[], char d[])          //Function 3
        {
            strcpy(name,na);
            strcpy(distance,d);
        }
        ~planet()                              //Function 4
        {
            cout<<"Planetarium time over!!!"<<endl;
        }
       };
       I. What is Function 1 referred as? When will it be executed?
       II. Write suitable C++ statement to invoke Function 2.
Ans   I. Constructor
         It will be executed at the time of object creation.
      (½ Mark for each correct answer)
       II. planet p;
          p.display(“Pluto”,”7.5 Billion Km”);
       (½ Mark for each correct answer)
(c)    Define a class DanceAcademy in C++ with following description:       4
       Private Members
                 ● Enrollno of type int
                 ● Name of type string
                 ● Style of type string
                 ● Fee of type float
                 ● A member function chkfee( ) to assign the value of fee
                     variable according to the style entered by the user
                     according to the criteria as given below:


            Style              Fee

          Classical           10000

           Western             8000

          Freestyle           11000

       Public Members
```

---

## page 9

```
              ● A function enrollment() to allow users to enter values
                for Enrollno,Name, Style and call function chkfee()to
                assign value of fee variable according to the Style
                entered by the user.
              ● A function display() to allow users to view the details
                of all the data members.

Ans   class DanceAcademy
      {
      int Enrollno;
      char Name[20];
      char Style[20];
      float Fee;
      void chkfee()
      {
      if(strcmpi(Style, "Classical")==0)
         Fee=10000;
      else if(strcmpi(Style, "Western")==0)
         Fee=8000;
      else if(strcmpi(Style, "Freestyle")==0)
         Fee=11000;
      }
      public:
             void enrollment()
             {
              cout<<"Please enter Enrollno,Name,Style";
              cin>>Enrollno;
              gets(Name);
              gets(Style);
              chkfee();
             }
             void display()
             {
             cout<<"\n Entered Enrollno, Name, Style and Fee is:
      "<<Enrollno<<"\t"<<Name<<"\t"<<Style<<"\t"<<Fee;
             }
      };


      ( ½ Mark for correct syntax of class header)
      ( ½ Mark for correct declarations of data members)
```

---

## page 10

```
      (1 Mark for correct definition of chkfee() function)
      (1 Mark for correct definition of enrollment () function)
      (1 Mark for correct definition of display () function)

      Note:
      Deduct ½ Mark if chkfee() is not invoked properly inside
      enrollment() function.

(d)   Answer the questions (i) to (iv) based on the following:     4
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
```

---

## page 11

```
               void registration();
               void showdata();
          };
          (i) Name the type of inheritance illustrated in the above C++ code.
    Ans   Multiple Inheritance

          (1 Mark for correct answer)
          (ii) Write the names of all the members, which are accessible from
          the objects belonging to class outdoor_sports.
    Ans   Data Members: None
          Member Functions: oEntry(), oShow()

          (1 Mark for correct answer)
          Note:
          No marks to be awarded for any partial or additional answer(s)
          (iii) Write the names of all the member functions, which are
          accessible from the member function of class sports.
    Ans   registration(), showdata(), oEntry(), oShow(), get_ofee(), iEntry(),
          iShow(), get_ifee()

          (1 Mark for correct answer)
          Note:
          No marks to be awarded for any partial or additional answer(s)
          (iv) What will be the size of the object belonging to class
          indoor_sports?
    Ans   46 Bytes
          (1 Mark for correct answer)
3   (a)   Write the definition of a function grace_score (int score [], int size)   3
          in C++, which should check all the elements of the array and give an
          increase of 5 to those scores which are less than 40.

          Example: if an array of seven integers is as follows:
                45, 35, 85, 80, 33, 27, 90
          After executing the function, the array content should be changed as
          follows:
                45, 40, 85, 80, 38, 32, 90
```

---

## page 12

```
Ans    void grace_score(int score[],int size)
       {
       for(int i=0;i<size;i++)
             {
             if(score[i]<40)
                     score[i]=score[i]+5;
             cout<<score[i]<<" ";
             }
       }


      (½ Mark for correct function header)
      (1 Mark for correct loop)
      (½ Mark for correct checking of array elements for less than 40)
      (1 Mark each for Adding value 5 to the array elements which has
      value less than 40)

(b)    An array P[30][20] is stored along the column in the memory with        3
       each element requiring 2 bytes of storage. If the base address of the
       array P is 26500, find out the location of P[20][10].

Ans   Total number of rows= 30
      Total size= 2 bytes
      Base Address= 26500

      LOC (P[I][J]) = BaseAddress+((I-LBR) + (J-LBC) * R)*W
      Assuming Lower Bound of Row(LBR)=0
             Lower Bound of Column(LBC)=0
             Total number of Rows(R)=30
             Size of each element(W)=2

      LOC(P[20][10])= 26500 +((20-0)+(10-0)*30)*2
      LOC(P[20][10])= 26500 +640
      LOC(P[20][10])= 27140

      (1 Mark for using correct formula for column major)
      (1 Mark for substituting formula with correct values)
      (1 Mark for correct final answer)

(c)    Write the definition of a member function push() for a class Library    4
       in C++ to insert a book information in a dynamically allocated stack
```

---

## page 13

```
       of books considering the following code is already written as a part
       of the program:
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
Ans   void Library::push()
      {
      book *nptr;
      nptr=new book;
      cout<<"Enter values for bookid and bookname";
      cin>>nptr->bookid;
      gets(nptr->bookname);
      nptr->next=NULL;
      if(top==NULL)
      top=nptr;
      else
        {
          nptr->next=top;
          top=nptr;
        }
      }

      (1 Mark for creating new node)
```

---

## page 14

```
      (½ Mark for taking values from user)
      (½ Mark for storing NULL in the variable responsible for linking in
      newly created node)
      (1 Mark for correct checking of top to be NULL or not and
      associate statement)
      (1 Mark for correct else part)
(d)    Write a user-defined function swap_row(int ARR[ ][3],int R,int C) in   2
       C++ to swap the first row values with the last row values:

       For example if the content of the array is:


       10       20        30

       40       50        60

       70       80        90

       Then after function call, the content of the array should be:


       70       80        90

       40       50        60

       10       20        30

Ans    void swap_row(int ARR[][3],int R,int C)
       {
       for(int i=0,j=0;j<C;j++)
             {
             int temp=ARR[i][j];
             ARR[i][j]=ARR[R-1][j];
             ARR[R-1][j]=temp;
             }
       }

      (1 Mark for correct loop)
      (1 Mark for correct swapping)
(e)    Evaluate the following POSTFIX expression. Show the status of          2
       Stack after execution of each operation separately:
                     45, 45, +, 32, 20, 10, /, -,*
```

---

## page 15

```
    Ans
           Element Scanned        Stack Status
           45                     45
           45                     45, 45
           +                      90
           32                     90, 32
           20                     90,32,20
           10                     90,32,20,10
           /                      90,32,2
           -                      90,30
           *                      2700

          Hence the final result is 2700
          (½ Mark for evaluating till + operator)
          (½ Mark for evaluating till / operator)
          (½ Mark for evaluating till - operator)
          (½ Mark for evaluating till * operator)

          Note:
           (1 Mark to be given for writing correct answer as 2700 without
           showing the Stack Status)
4   (a)    Find the output of the following C++ code considering that the             1
           binary file sp.dat already exists on the hard disk with 2 records in it.

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
```

---

## page 16

```
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
Ans    42
       84

       (½ Mark for each correct answer)
(b)    Write a user defined function word_count() in C++ to count how   2
       many words are present in a text file named “opinion.txt”.

       For example, if the file opinion.txt contains following text:


        Co-education system is necessary for a balanced society. With
        co-education system, Girls and Boys may develop a feeling of
        mutual respect towards each other.


       The function should display the following:
       Total number of words present in the text file are: 24
Ans   void word_count()
      {
      ifstream i;char ch[20];int c=0;
      i.open("opinion.txt ");
      while(!i.eof())
      {
      i>>ch;
      c=c+1;
      }
```

---

## page 17

```
      cout<<" Total number of words present in the text file are: “<<c;
      }

      (½ Mark for opening opinion.txt correctly)
      (½ Mark for fetching each word from the file correctly)
      (½ Mark for counting each word)
      (½ Mark for correct display)

(c)    Write a function display () in C++ to display all the students who have   3
       got a distinction(scored percentage more than or equal to 75) from a
       binary file “stud.dat”, assuming the binary file is containing the
       objects of the following class:
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

## page 18

```
     Ans   void display()
           {
           student s;
           ifstream i(“stud.dat”);
           while(i.read((char*)&s,sizeof(s)))
           {
           if(s.retpercent()>=75)
           s.showdetails();
           }
           i.close();
           }
           (½ Mark for opening stud.dat correctly)
           (1 Mark for reading all records from the file)
           (1 Mark for comparing desired value with obtained data)
           (½ Mark for calling showdetails() function)

                               Section - B (Python)
1    (a)   Carefully observe the following python code and answer the                  2
           questions that follow:




           On execution the above code produces the following output.
           6
           3
           Explain the output with respect to the scope of the variables.
    Ans:   Names declared with global keyword have to be referred at the file
           level. This is because the global statement indicates that the particular
           variable lives in the global scope. If no global statement is being
           used, the variable with the local scope is accessed.

           Hence, in the above code the statement succeeding the statement
           global x informs python to increment the global variable x

           Hence the output is 6 i.e 5+1 which is also the value for global x.
```

---

## page 19

```
        When x is reassigned with the value 3 the local x hides the global x
        and hence 3 is printed.

        (2 marks for explaining the output)

        (Only 1 mark for explaining global and local namespace.)
 (b)    Name the modules to which the following functions belong:              1
         a. uniform()      b. fabs()
Ans:      a. random()
          b. math()
       (½ mark each for the correct modules)
 (c)    Rewrite the following code after removing the syntactical errors (if   2
        any). Underline each correction.




Ans:    def chksum():
              x= input("Enter a number")
              if (x%2 == 0):
                 for i in range(2*x):
                        print i
              else:
                       print "#"
        (½ mark for each correction)
        (1 mark to be given if only the errors are identified)


 (d)    Observe the following Python code carefully and obtain the output,     2
        which will appear on the screen after execution of it.
```

---

## page 20

```
Ans:   EA3n
       (½ mark for each correct character of the output)
 (e)   What output will be generated when the following Python code is       3
       executed?




Ans:   [11, 10, 9, 8, 7, 4]

       (½ mark for each correct value)
       (Deduct ½ mark if output not displayed as a list i.e. missing [])
 (f)   Observe the following program and answer the questions that follow:   2




         a. What is the minimum and maximum number of times the loop
            will execute?
```

---

## page 21

```
              b. Find out, which line of output(s) out of (i) to (iv) will not be
                 expected from the program?
                 I. 0#1
                 ii. 1#2
                 iii. 2#3
                 iv. 3#4
    Ans:        a. Minimum Number = 1
                   Maximum Number = 3
               b. Line iv is not expected to be a part of the output.
           ( 1 mark for correct Minimum and Maximum value)
           ( 1 mark for identifying iv as the answer)
2    a      Explain the two strategies employed by Python for memory                    2
            allocation.

    Ans:    Python uses two strategies for memory allocation-
            i. Reference counting
            ii. Automatic garbage collection.
            Reference Counting: works by counting the number of times an
            object is referenced by other objects in the system. When an object's
            reference count reaches zero, Python collects it automatically.
            Automatic      Garbage     Collection:    Python    schedules     garbage
            collection based upon a threshold of object allocations and object de-
            allocations. When the number of allocations minus the number of
            deallocations are greater than the threshold number, the garbage
            collector is run and the unused block of memory is reclaimed.


            (1 mark for writing the names of both the strategies)
            (1 mark for explaining any one strategy)
            (2 mark for explaining both the strategies)


     b      Observe the following class definition and answer the questions that        2
            follow:
```

---

## page 22

```
        i. Write statement to invoke Function 1.
        ii. On Executing the above code , Statement 2 is giving an error
        explain.

Ans:    i. print I
        ii. The statement 2 is giving an error because __Systemdate is a
        private variable and hence cannot be printed outside the class.


        (1 mark for correct answer of i.)
        (½ mark for identifying __Systemdate as private variable and
        ½ mark for correct explanation)

 c     Define a class PRODUCT in Python with the following specifications         4
       Data members:
       Pid           – A string to store productid.
       Pname         - A string to store the name of the product.
       Pcostprice – A decimal to store the cost price of the product
       Psellingprice – A decimal to store Selling Price
       Margin        - A decimal to be calculated as Psellingprice - Pcostprice
       Remarks          - To store”Profit” if Margin is positive else “Loss” if
                       Margin is negative
       Member Functions:
```

---

## page 23

```
         ● A constructor function to initialize All the data members with
             valid default values.
         ● A      method          SetRemarks()    that   assigns   Margin   as
             Psellingprice - Pcostprice and sets Remarks as mentioned
             below:


       Margin            Remarks

       <0 ( negative) Loss

       >0(positive)      Profit


         ● A          method       Getdetails()   to     accept    values   for
             Pid,Pname,Pcostprice,Psellingprice and invokes SetRemarks()
             method.
         ● A method Setdetails() that displays all the data members.

Ans:
```

---

## page 24

```
    (½ mark for correct syntax of class)
    (1 mark for correct __init__() method )
    ( 1 mark for correct definition of SetRemarks())
    (1 mark for correct definition of Getdetails() )
    (½ mark for correct definition of Setdetails() )

d   Answer the questions (i) to (iv) based on the following:            4




    i.   Which type of Inheritance is demonstrated in the above code?
```

---

## page 25

```
           ii. Explain Statement 1 and 2.

           iii. Name the methods that are overridden along with their class name.

           iv. Fill Blank1 with a statement to display variable category of class
           Brand.

    Ans:   i. Multiple Inheritance
           (1 mark for the correct answer)


           ii. Statement 1 and 2 invoke the getSdata() function of class Shop and
           getData() function of class Brand respectively.
           (1 mark for the correct answer)


           iii. getdata() method of class Brand is overridden.When object of class
           Mall is created,
           M = Mall()
           M.getdata()
           getdata() method of class Mall is invoked and not of class Brand is
           called.
           (1 mark for the correct answer)


           iv. print Brand().category
           (1 mark for the correct answer)

3    a      Consider the following unsorted list                                       3
             95 79 19 43 52 3
             Write the passes of bubble sort for sorting the list in ascending order
            till the 3rd iteration.

    Ans:   [79, 19, 43, 52, 3, 95]
           [19, 43, 52, 3, 79, 95]
           [19, 43, 3, 52, 79, 95]


           (1 mark for each correct iteration in sequence.)

     b     Kritika was asked to accept a list of even numbers but she did not put      3
```

---

## page 26

```
       the relevant condition while accepting the list of numbers. You are
       required to write a user defined function oddtoeven(L) that accepts the
       List L as an argument and convert all the odd numbers into even by
       multiplying them by 2 .

Ans:



       (1 mark for the correct loop)
       (1 mark for the correct condition)
       (1 mark for converting the number to even)

 c      Aastha wants to create a program that accepts a string and display the   4
        characters in the reverse order in the same line using a Stack. She
        has created the following code , help her by completing the
        definitions on the basis of requirements given below :
        class mystack:
              def __init__(self):
                 self.mystr= ________________ # Accept a string
                 self.mylist =________________ # Convert mystr to a list
       # Write code to display while removing element from the stack.
              def display(self):
                 :
                 :


Ans:




        (½ mark for accepting the string)
```

---

## page 27

```
        (1 mark for converting the string to list)
        (1 mark for checking whether the stack is empty)
        (½ mark for the correct loop)
        ( 1 mark for the correct use of pop() method)

 d     Write a generator function generatesq() that displays the squareroots of   2
       numbers from 100 to n where n is passed as an argument .

Ans:




       (½ mark for import math)
       (½ correct use of sqrt() function)
       (1 mark for yield())

 e      Evaluate the following Postfix expression:                                2
                 20,10,-,15,3,/,+,5,*



        Symbol     Operation                Stack       Resul
                                                        t

        20         Push                     20

        10         Push                     20,10

        -          Pop(10)                  10
                   Pop(20)
                   Push(20-10)
                   =10

        15         Push                     10,15

        3          Push                     10,15,3

        /          Pop(3)                   10,5
                   Pop(15)
                   Push(15/3)=5

        +          Pop(5)                   15
                   Pop(10)
                   Push(10+5)=15
```

---

## page 28

```
            5         Push                     15,5

            *         Pop(5)                   75           75
                      Pop(15)
                      Push(15*5)=5



            (½ mark for correct stack status till ‘-’)
            (½ mark for correct stack status till ‘/’)
            (½ mark for correct stack status till ‘+’)
            (½ mark for correct stack status till ‘*’)


            (½ mark for writing the correct result without working of Stack)

4    a      Observe the following code and answer the questions that follow:         1
            File = open("Mydata","a")
            _____________________ #Blank1
            File.close()
           i. What type (Text/Binary) of file is Mydata?
           ii. Fill the Blank 1 with statement to write “ABC” in the file “Mydata”


    Ans:    i. Text File
            (½ mark for the correct answer)
            ii. File.write("ABC")
            (½ mark for the correct statement)

     b     A text file “Quotes.Txt” has the following data written in it:            2

           Living a life you can be proud of
           Doing your best
           Spending your time with people and activities that are important to you
           Standing up for things that are right even when it’s hard
           Becoming the best version of you

           Write a user defined function to display the total number of words
```

---

## page 29

```
       present in the file.


Ans:




       (½ mark for reading the file using read)
       (½ mark for correctly using split())
       (½ mark for the correct loop)
       (½ mark for displaying the correct value of count)

 c      Consider the following class declaration and answer the question that     3
        follows:




                                                                            A
       nuj has been asked to display all the students who have scored less than
       40 for Remedial Classes.
       Write a user defined function to display all those students who have
       scored less than 40 from the binary file “Student.dat” assuming it
       stores all the object of the class Student mentioned above.
```

---

## page 30

```
    Ans:




            (½ Mark for opening the file in “rb” mode)
           (½ Mark for creating the object of the class student)
           (½ Mark for the loop)
           (½ Mark for loading the object from the file)
           (½ Mark for calling returnpercent()to check percentage<40 )
           (½ Mark for displaying records)
                                    Section – C
5    (a)    Observe the table ‘Club’ given below:                                 2

                                           Club
            Member_id    Member_Name Address            Age Fee

            M001         Sumit             New Delhi    20     2000

            M002         Nisha             Gurgaon      19     3500

            M003         Niharika          New Delhi    21     2100

            M004         Sachin            Faridabad    18     3500

            i.    What is the cardinality and degree of the above given table?
            ii. If a new column contact_no has been added and three more
            members have joined the club then how these changes will affect the
            degree and cardinality of the above given table.
     Ans   i. Cadinality: 4
               Degree: 5
           (½ Mark for each correct answer)
           ii. Cardinality: 7
               Degree: 6
           (½ Mark for each correct answer)
```

---

## page 31

```
(b)    Write SQL commands for the queries (i) to (iv) and output for (v) to      6
       (viii) based on the tables ‘Watches’ and Sale given below.
      Watches
      Watchid        Watch_Name         Price      Type        Qty_Store
      W001           HighTime           10000      Unisex      100
      W002           LifeTime           15000      Ladies      150
      W003           Wave               20000      Gents       200
      W004           HighFashion        7000       Unisex      250
      W005           GoldenTime         25000      Gents       100

      Sale
       Watchid               Qty_Sold            Quarter
       W001                  10                  1
       W003                  5                   1
       W002                  20                  2
       W003                  10                  2
       W001                  15                  3
       W002                  20                  3
       W005                  10                  3
       W003                  15                  4


       i. To display all the details of those watches whose name ends with
         ‘Time’

       ii. To display watch’s name and price of those watches which have price
            range in between 5000-15000.

       iii. To display total quantity in store of Unisex type watches.

       iv. To display watch name and their quantity sold in first quarter.

       v.       select max(price), min(qty_store) from watches;

       vi.      select quarter, sum(qty_sold) from sale group by quarter;

       vii. select watch_name,price,type from watches w, sale s where
         w.watchid!=s.watchid;

       viii. select watch_name, qty_store, sum(qty_sold), qty_store-
         sum(qty_sold) “Stock” from watches w, sale s where
         w.watchid=s.watchid group by s.watchid;

Ans   i. select * from watches where watch_name like ‘%Time’
```

---

## page 32

```
(½ mark for SELECT query)
(½ mark for where clause)

ii. select watch_name, price from watches where price between 5000
and 15000;

(½ mark for SELECT query)
(½ mark for where clause)

iii. select sum(qty_store) from watches where type like ’Unisex’;

(½ mark for SELECT query)
(½ mark for where clause)

iv. select watch_name,qty_sold from watches w,sale s where
w.watchid=s.watchid and quarter=1;

(½ mark for SELECT query)
(½ mark for where clause)
v.
 max(price)              min(qty_store)
 25000                   100

(½ mark for correct output)

vi.
         quarter              sum(qty_sold)
           1                       15
           2                       30
           3                       45
           4                       15

(½ mark for correct output)

vii.
 watch_name        price              type
 HighFashion       7000               Unisex

(½ mark for correct output)

viii.
```

---

## page 33

```
            watch_name         qty_store     qty_sold   Stock
            HighTime           100           25         75
            LifeTime           150           40         110
            Wave               200           30         170
            GoldenTime         100           10         90

           (½ mark for correct output)
6    (a)   Correct the following boolean statements:                              2
              1. X+1 = X
              2. (A')'=A'
              3. A+A'=0
              4. (A+B)' = A.B


    Ans:        1.   X+1 =1 or X+0=X
                2.   ((A’)’) = A
                3.   A + A’= 1 or A . A’=0
                4.   (A+B)’ = A’ . B’

           (½ mark for each corrected statement)
     (b)    Draw the equivalent logic circuit for the following Boolean           1
            expression:
                        (A.B)+C
    Ans:




            (½ mark for correct placement of each gate)
     (c)    Write the POS form of a Boolean Function F, which is represented in   2
            a truth table as follows:


            P        Q    R    F

            0        0    0    0

            0        0    1    1
```

---

## page 34

```
            0     1     0     1

            0     1     1     1

            1     0     0     0

            1     0     1     1

            1     1     0     0

            1     1     1     1

    Ans:    (P+Q+R).(P’+Q+R).(P’+Q’+R)

            (½ mark each for correct maxterms)
            (½ mark for the correct representation as POS)
     (d)    Reduce the following Boolean Expression using K Map:                    3
            F(A,B,C,D)=
    Ans:




           A'B'C' + D + BC

           (½ mark for correct K MAP format)
           (½ mark for putting 1 at the right place)
           (½ mark for each correct groups)
           (½ mark for the correct answer)
7    (a)    Identify the type of topology on the basis of the following:            2
              a. Since every node is directly connected to the server, a large
                  amount of cable is needed which increases the installation cost
                  of the network.
              b. It has a single common data path connecting all the nodes.
```

---

## page 35

```
Ans:      a. Star Topology
          b. Bus Topology

       (1 mark for each correct answer)
 (b)    Expand the following:                                                    1
          a. VOIP
          b. SMTP
Ans:      a. Voice Over Internet Protocol
          b. Simple Mail Transfer Protocol
       (½ mark for each correct answer)
 (c)    Who is a hacker?                                                         1
Ans:    A computer enthusiast, who uses his computer programming skills to
        intentionally access a computer without authorization is known as
        hacker. A hacker accesses the computer without the intention of
        destroying data or maliciously harming the computer.
        (1 mark for the correct answer)
 (d)    The following is a 32 bit binary number usually represented as 4         1
        decimal values, each representing 8 bits, in the range 0 to 255
        (known as octets) separated by decimal points.
                      140.179.220.200
       What is it? What is its importance?
Ans:    It is an IP Address.It is used to identify the computers on a network.

        (½ mark for identification)
        (½ mark for the importance)
 (e)    Daniel has to share the data among various computers of his two          1
        offices branches situated in the same city. Name the network (out of
        LAN, WAN, PAN and MAN) which is being formed in this process.
 Ans   MAN

       (1 mark for correct answer)

 (f)     Rehaana Medicos Center has set up its new center in Dubai. It has
         four buildings as shown in the diagram given below:
```

---

## page 36

```
Distances between various buildings are as follows:


 Accounts to Research Lab             55 m

 Accounts to Store                    150 m

 Store to Packaging Unit              160 m

 Packaging Unit to Research Lab       60 m

 Accounts to Packaging Unit           125 m

 Store to Research Lab                180 m


Number of Computers


Accounts             25

Research Lab         100

Store                15

Packaging Unit       60
                                                                  1
As a network expert, provide the best possible answer for the     1
following queries:
                                                                  1
i) Suggest a cable layout of connections between the buildings.
ii) Suggest the most suitable place (i.e. buildings) to house the server of this
organization.
                                                                  1
```

---

## page 37

```
       iii) Suggest the placement of the following device with justification:
               a) Repeater                   b) Hub/Switch
       iv) Suggest a system (hardware/software) to prevent unauthorized
       access to or from the network.

Ans      (i) Layout 1




              Layout 2




      (Any of the above)

      (1 mark for drawing correct layout)

      (ii)The most suitable place/ building to house the server of this
      organization would be building Research Lab, as this building contains
      the maximum number of computers.

      (1 mark for correct answer)
```

---

## page 38

```
(iii)
a) For layout1, since the cabling distance between Accounts to Store is
quite large, so a repeater would ideally be needed along their path to
avoid loss of signals during the course of data flow in this route. For
layout2, since the cabling distance between Store to Recresearch Lab
is quite large, so a repeater would ideally be placed.

b) In both the layouts, a Hub/Switch each would be needed in all the
buildings to interconnect the group of cables from the different
computers in each building.

(½ mark for each correct answer)

(iv) Firewall

(1 mark for correct answer)
```