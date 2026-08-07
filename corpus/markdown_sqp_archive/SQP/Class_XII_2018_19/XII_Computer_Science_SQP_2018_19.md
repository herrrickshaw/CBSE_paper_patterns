---
title: "XII Computer Science SQP 2018 19"
source_pdf: "XII_Computer_Science_SQP_2018_19.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/Class_XII_2018_19/XII_Computer_Science_SQP_2018_19.pdf"
pages: 12
pdf_bytes: 175356
pdf_sha256: "1cf960606d680bb576743d9842a7560ef3cfc9f7a456c4afdd079b4dc9b886e5"
text_chars: 22634
low_text_pages: 0
converter: "pdftotext -layout"
---

# XII Computer Science SQP 2018 19


---

## page 1

```
                                             Class XII
                                       Computer Science (083)
                                    Sample Question Paper 2018-19

Time allowed: 3 Hours                                                                  Max. Marks: 70

    General Instructions:

      (a) All questions are compulsory.
      (b)    Programming Language with C++
      (c)    In Question 2(b, d) ,3 and 4 has internal choices.


Q. No.      Part   Question Description                                                         Marks
1           (a)    Write the type of C++ Operators (Arithmetic, Logical, and Relational          (2)
                   Operators) from thefollowing:
                      (i)     !(ii) !=(iii) &&(iv) %

            (b)    Observe the following program very carefully and write the name of those      (1)
                   header file(s), which are essentially needed to compile and execute
                   thefollowing program successfully:
                           void main()
                           {
                                   char text[20], newText[20];
                                   gets(text);
                                   strcpy(newText,text);
                                   for(int i=0;i<strlen(text);i++)
                                            if(text[i] = =’A’)
                                                     text[i] = text[i]+2;
                                   puts(text);
                           }

            (c)    Rewrite the following C++ code after removing any/all Syntactical Error(s)    (2)
                   with each correction underlined.

                   Note: Assume all required header files are already being included in the
                   program.

                   #define float PI 3.14
                   void main( )
                   {
                          float R=4.5,H=1.5;
                          A=2*PI*R*H + 2*PIpow(R,2);
                          cout<<‘Area=’<<A<<endl;
                   }



                                                       1
```

---

## page 2

```
(d)   Find and write the output of the following C++ program code:                (3)
      Note: Assume all required header files are already being included in
      the program.
      void main( )
      {
             int Ar[ ] = { 6 , 3 , 8 , 10 , 4 , 6 , 7} ;
             int *Ptr = Ar , I ;
             cout<<++*Ptr++ << '@' ;
             I = Ar[3] - Ar[2] ;
             cout<<++*(Ptr+I)<<'@'<<"\n" ;
             cout<<++I + *Ptr++ << '@' ;
             cout<<*Ptr++ <<'@'<< '\n' ;
             for( ; I >=0 ; I -=2)
                   cout<<Ar[I] << '@' ;
      }

(e)   Find and write the output of the following C++ program code:                (2)
      typedef char STRING[80];
      void MIXNOW(STRING S)
      {
         int Size=strlen(S);
         for(int I=0;I<Size;I+=2)
         {
                      char WS=S[I];
                      S[I]=S[I+1];
                      S[I+1]=WS;
              }
              for (I=1;I<Size;I+=2)
              if (S[I]>=’M’ && S[I]<=’U’)
                      S[I]=’@’;
      }
      void main()
      {
        STRING Word=”CBSEEXAM2019”;
        MIXNOW(Word);
        cout<<Word<<endl;
      }

(f)   Observe the following program and find out, which output(s) out of (i) to   (2)
      (iv) willbe expected from the program? What will be the minimum and the
      maximum value assigned to the variable Alter?

      Note: Assume all required header files are already being included in the
      program.
             void main( )
             {
                   randomize();
                   int Ar[]={10,7}, N;

                                       2
```

---

## page 3

```
                         int Alter=random(2) + 10 ;
                         for (int C=0;C<2;C++)
                         {
                                  N=random(2) ;
                                  cout<<Ar[N] +Alter<<”#”;
                         }
                  }
          (i) 21#20#                           (ii) 20#18#
          (iii) 20#17#                         (iv) 21#17#

2   (a)   What is a copy constructor? Illustrate with a suitable C++ example.           (2)

    (b)   Write the output of the following C++ code. Also, write the name of feature   (2)
          of Object Oriented Programming used in the following program jointly
          illustrated by the Function 1 to Function 4.
                   void My_fun ( )                               // Function 1
                   {
                          for (int I=1 ; I<=50 ; I++) cout<< "-" ;
                          cout<<end1 ;
                   }
                   void My_fun (int N)                           // Function 2
                   {
                          for (int I=1 ; I<=N ; I++) cout<<"*" ;
                          cout<<end1 ;
                   }
                   void My_fun (int A, int B)                    // Function 3
                   {
                          for (int I=1. ;I<=B ;I++) cout <<A*I ;
                          cout<<end1 ;
                   }
                   void My_fun (char T, int N)                   // Function 4
                   {
                          for (int I=1 ; I<=N ; I++) cout<<T ;
                          cout<<end1;
                   }
                   void main ( )
                   {
                          int X=7, Y=4, Z=3;
                          char C='#' ;
                          My_fun (C,Y) ;
                          My_fun (X,Z) ;
          }

                                               OR

          (b) Write any four differences between Constructor and Destructor function
              with respect to object oriented programming.


                                           3
```

---

## page 4

```
(c)   Define a class Ele_Bill in C++ with the following descriptions:                (4)
      Private members:
           Cname                   of type character array
           Pnumber                 of type long
           No_of_units             of type integer
            Amount                 of type float.
            Calc_Amount( )         This member function should calculate the
                                   amount as No_of_units*Cost .
            Amount can be calculated according to the following conditions:
      No_of_units Cost
                  First 50 units               Free
                  Next 100 units               0.80 @ unit
                  Next 200 units               1.00 @ unit
                  Remaining units              1.20 @ unit
      Public members:
           * A function Accept( ) which allows user to enter Cname,
             Pnumber, No_of_units and invoke function Calc_Amount().
           * A function Display( ) to display the values of all the data members
             on the screen.

(d)   Answer the questions (i) to (iv) based on the following:                     (4)
      class Faculty
      {
         int FCode;
      protected:
              char FName[20];
      public:
              Faculty();
              void Enter();
              void Show();
      };
      class Programme
      {
              int PID;
      protected:
              char Title[30];
      public:
              Programme();
              void Commence();
              void View();
      };
      class Schedule: public Programme, Faculty
      {
              int DD,MM,YYYY;
      public:

                                        4
```

---

## page 5

```
               Schedule();
               void Start();
               void View();
        };
        void main()
        {
              Schedule S;              //Statement 1
              ___________              //Statement 2
        }

(i)     Write the names of all the member functions, which are directly accessible
        by the object S of class Schedule as declared in main() function.

(ii)    Write the names of all the members, which are directly accessible by the
        memberfunction Start( ) of class Schedule.

(iii)   Write Statement 2 to call function View( ) of class Programme from the
        object S of class Schedule.

(iv)    What will be the order of execution of the constructors, when the object S
        of class Schedule is declared inside main()?

                                               OR

(d)     Consider the following class State :
                       class State
                       {
                       protected :
                       int tp;
                       public :
                       State( ) { tp=0;}
                       void inctp( ) { tp++;};
                       int gettp(); { return tp; }
                       };

               Write a code in C++ to publically derive another class ‘District’
               with the following additional members derived in the public
               visibility mode.

               Data Members :
               Dname          string
               Distance     float
               Population   long int

               Member functions :
                    DINPUT( ) : To enter Dname, Distance and population
                    DOUTPUT( ) : To display the data members on the screen.


                                           5
```

---

## page 6

```
3   (a)   Write a user-defined function AddEnd4(int A[][4],int R,int C) in C++ to         (2)
          find and display the sum of all the values, which are ending with 4 (i.e., unit
          place is 4).
          For example if the content of array is:
                                   24 16 14
                                   19 5 4
          The output should be
          42

                                                OR

    (a)   Write a user defined function in C++ to find the sum of both left and right
          diagonal elements from a two dimensional array.

    (b)   Write a user-defined function EXTRA_ELE(int A[ ], int B[ ], int N) in C++       (3)
          to find and display the extra element in Array A. Array A contains all the
          elements of array B but one more element extra. (Restriction: array
          elements are not in order)

          Example        If the elements of Array A is 14, 21, 5, 19, 8, 4, 23, 11
                         and the elements of Array B is 23, 8, 19, 4, 14, 11, 5
                         Then output will be 21

                                                       OR
    (b)
          Write a user defined function Reverse(int A[],int n) which accepts an
          integer array and its size as arguments(parameters) and reverse the array.
          Example : if the array is 10,20,30,40,50 then reversed array is
          50,40,30,20,10

    (c)   An array S[10] [30] is stored in the memory along the column with each of       (3)
          its element occupying 2 bytes. Find out the memory location of S[5][10], if
          element S[2][15] is stored at the location 8200.

                                                OR

    (c)   An array A[30][10] is stored in the memory with each element requiring 4
          bytes of storage ,if the base address of A is 4500 ,Find out memory
          locations of A[12][8], if the content is stored along the row.

    (d)   Write the definition of a member function Ins_Player() for a class               (4)
          CQUEUE in C++, to add a Player in a statically allocated circular queue of
          PLAYERs considering the following code
          is already written as a part of the program:
          struct Player
          {
                long Pid;
               char Pname[20];

                                            6
```

---

## page 7

```
          };
          const int size=10;
          class CQUEUE
          {
               Player Ar[size];
               int Front, Rear;
             public:
               CQUEUE( )
               {
                   Front = -1;
                   Rear = -1;
               }
               void Ins_Player(); // To add player in a static circular queue
               void Del_Player(); // To remove player from a static circular queue
               void Show_Player(); // To display static circular queue
          };

                                                OR

    (d)   Write a function in C++ to delete a node containing Books information
          ,from a dynamically allocated stack of Books implemented with the help of
          the following structure:
          struct Book
          {
          int BNo;
          char BName[20];
          Book *Next;
          };

    (e)   Convert the following Infix expression to its equivalent Postfix expression, (2)
          showing the stack contents for each step of conversion.
                A/B+C*(D-E)

                                                OR

          Evaluate the following Postfix expression :
          4,10,5,+,*,15,3,/,-

4   (a)   Write a function RevText() to read a text file “ Input.txt “ and Print only   (2)
          word starting with ‘I’ in reverse order .
          Example: If value in text file is: INDIA IS MY COUNTRY
          Output will be: AIDNI SI MY COUNTRY

                                                OR

    (a)   Write a function in C++ to count the number of lowercase alphabets present
          in a text file “BOOK..txt".


                                            7
```

---

## page 8

```
(b)   Write a function in C++ to search and display details, whose destination is    (3)
      “Cochin” from binary file “Bus.Dat”. Assuming the binary file is
      containing the objects of the following class:
      class BUS
      {       int Bno;                       // Bus Number
              char From[20];                 // Bus Starting Point
              char To[20];                   // Bus Destination
            public:
               char * StartFrom ( ); { return From; }
               char * EndTo( ); { return To; }
               void input() { cin>>Bno>>; gets(From); get(To); }
               void show( ) { cout<<Bno<< “:”<<From << “:” <<To<<endl; }
      };

                                           OR

(b)   Write a function in C++ to add more new objects at the bottom of a binary
      file "STUDENT.dat", assuming the binary file is containing the objects of
      the following class :
      class STU
      {
      int Rno;
      char Sname[20];
      public: void Enter()
      {
      cin>>Rno;gets(Sname);
      }
      void show()
      {
      count << Rno<<sname<<endl;
      }
      };

(c)   Find the output of the following C++ code considering that the binary file    (1)
      PRODUCT.DAT exists on the hard disk with a list of data of 500 products.
      class PRODUCT
      {
                     int PCode;char PName[20];
             public:
                     void Entry();void Disp();
      };
      void main()
      {
             fstream In;
             In.open("PRODUCT.DAT",ios::binary|ios::in);
             PRODUCT P;
             In.seekg(0,ios::end);
             cout<<"Total Count: "<<In.tellg()/sizeof(P)<<endl;

                                       8
```

---

## page 9

```
                   In.seekg(70*sizeof(P));
                   In.read((char*)&P, sizeof(P));
                   In.read((char*)&P, sizeof(P));
                   cout<<"At Product:"<<In.tellg()/sizeof(P) + 1;
                   In.close();
           }

                                                         OR

    (c)    Which file stream is required for seekg() ?

5   (a)    Observe the following table and answer the parts(i) and(ii) accordingly     (2)
           Table:Product

                   Pno           Name              Qty              PurchaseDate
                   101            Pen              102               12-12-2011
                   102          Pencil             201               21-02-2013
                   103          Eraser              90               09-08-2010
                   109         Sharpener            90               31-08-2012
                   113           Clips             900               12-12-2011

    (i)    Write the names of most appropriate columns, which can be considered as
           candidate keys.

    (ii)   What is the degree and cardinality of the above table?

    (b)    Write SQL queries for (i) to (iv) and find outputs for SQL queries (v) to    (4+2)
           (viii), which are based on the tables.
                                          TRAINER
            TID TNAME                   CITY                 HIREDATE SALARY
            101 SUNAINA                 MUMBAI               1998-10-15 90000
            102 ANAMIKA                 DELHI                1994-12-24 80000
            103 DEEPTI                  CHANDIGARG 2001-12-21 82000
            104 MEENAKSHI               DELHI                2002-12-25 78000
            105 RICHA                   MUMBAI               1996-01-12 95000
            106 MANIPRABHA CHENNAI                           2001-12-12 69000

                                            COURSE
            CID          CNAME         FEES     STARTDATE             TID
            C201         AGDCA         12000    2018-07-02            101
            C202         ADCA          15000    2018-07-15            103
            C203         DCA           10000    2018-10-01            102
            C204         DDTP          9000     2018-09-15            104
            C205         DHN           20000    2018-08-01            101
            C206         O LEVEL       18000    2018-07-25            105


                                             9
```

---

## page 10

```
    (i)      Display the Trainer Name, City & Salary in descending order of their
             Hiredate.

    (ii)     To display the TNAME and CITY of Trainer who joined the Institute in the
             month of December 2001.

    (iii)    To display TNAME, HIREDATE, CNAME, STARTDATE from tables
             TRAINER and COURSE of all those courses whose FEES is less than or
             equal to 10000.

    (iv)     To display number of Trainers from each city.

    (v)      SELECT TID, TNAME, FROM TRAINER WHERE CITY NOT
             IN(‘DELHI’, ‘MUMBAI’);

    (vi)     SELECT DISTINCT TID FROM COURSE;

    (vii)    SELECT TID, COUNT(*), MIN(FEES) FROM COURSE GROUP BY
             TID HAVING COUNT(*)>1;

    (viii)   SELECT COUNT(*), SUM(FEES) FROM COURSE WHERE
             STARTDATE< ‘2018-09-15’;

6   (a)      State any one Distributive Law of Boolean Algebra and Verify it using       (2)
             truth table.

    (b)      Draw the Logic Circuit of the following Boolean Expression:                 (2)
                          ((U + V’).(U + W)). (V + W’)

    (c)      Derive a Canonical SOP expression for a Boolean function F(X,Y,Z)           (1)
             represented by the following truth table:


                                     X Y Z F(X,Y,Z)
                                     0 0 0    1
                                     0 0 1    1
                                     0 1 0    0
                                     0 1 1    0
                                     1 0 0    1
                                     1 0 1    0
                                     1 1 0    0
                                     1 1 1    1

    (d)      Reduce the following Boolean Expression to its simplest form using K-      (3)
             Map:

             F(X,Y,Z,W)= Σ (0,1,2,3,4,5,8,10,11,14)


                                             10
```

---

## page 11

```
7   (a)   Arun opened his e-mail and found that his inbox was full of hundreds of        (2)
          unwanted mails. It took him around two hours to delete these unwanted
          mails and find the relevant ones in his inbox. What may be the cause of his
          receiving so many unsolicited mails? What can Arun do to prevent this
          happening in future?

    (b)   Assume that 50 employees are working in an organization. Each employee         (1)
          has been allotted a separate workstation to work. In this way, all computers
          are connected through the server and all these workstations are distributed
          over two floors. In each floor, all the computers are connected to a switch.
          Identify the type of network?

    (c)   Your friend wishes to install a wireless network in his office. Explain him    (1)
          the difference between guided and unguided media.

    (d)   Write the expanded names for the following abbreviated terms used in           (2)
          Networking and Communications:
          (i) CDMA     (ii) HTTP    (iii)  XML (iv)     URL

                                                                                         (4)
    (e)   Multipurpose Public School, Bangluru is Setting up the network
          between its Different Wings of school campus. There are 4
          wings
          namedasSENIOR(S),JUNIOR(J),ADMIN(A)andHOSTEL(H).

          Multipurpose Public School, Bangluru




                               SENIOR                                 JUNIOR




                              ADMIN                                   HOSTEL




                                          11
```

---

## page 12

```
                      Distancebetweenvariouswingsaregivenbelow:
                       WingAtoWingS                         100m

                       WingAtoWingJ                         200m

                       WingAtoWingH                         400m

                       WingStoWingJ                         300m

                       WingStoWingH                         100m

                       WingJtoWingH                         450m


        Number of Computers installed at various wings are as follows:


                       Wings                  NumberofComputers

                       WingA                  20

                       WingS                  150

                       WingJ                  50

                       WingH                  25



(i)     Suggest the best wired medium and draw the cable layout to efficiently
        connect various wings of Multipurpose PublicSchool, Bangluru.

(ii)    Namethe       most     suitablewing         wherethe       Servershouldbe
        installed.Justifyyour answer.

(iii)   Suggest a device/software and its placement that would provide
        data security for the entire network of the School.

(iv)    Suggest a device and the protocol that shall be needed to provide wireless
        Internet access to all smartphone/laptop users in the campus               of
        Multipurpose Public School, Bangluru.




                                         12
```