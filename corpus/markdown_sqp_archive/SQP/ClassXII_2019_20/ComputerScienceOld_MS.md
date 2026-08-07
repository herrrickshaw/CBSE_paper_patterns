---
title: "ComputerScienceOld MS"
source_pdf: "ComputerScienceOld_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/ComputerScienceOld_MS.pdf"
pages: 26
pdf_bytes: 1032474
pdf_sha256: "22df911ecfc73e4ee5fcbd2a92809e0b614fcaf1e2193c3c45e8ee2b2fcedcfa"
text_chars: 42922
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScienceOld MS


---

## page 1

```
                                 SAMPLE QUESTION PAPER 2019-20
                                       Marking Scheme
                                 COMPUTER SCIENCE - OLD (Code: 283)
                                               CLASS:-XII
    Time:3 Hrs.                                                                             M.M.:70
Q. No. Part       Question Description                                                         Marks
1        (a)      Write the type of C++ Operators (Arithmetic, Logical, and Relational           2
                  Operators) from the following:

                  (i) !(ii) !=(iii) &&(iv) %

         Ans.         (i) Logical    (ii) Relational       (iii)Logical   (iv) Arithmetic

                  (1/2 Mark for each correct Operator Type)

         (b)      Observe the following program very carefully and write the name of those       1
                  header file(s), which are essentially needed to compile and execute
                  thefollowing program successfully:
                          void main()
                          {
                                  char text[20], newText[20];
                                  gets(text);
                                  strcpy(newText,text);
                                  for(int i=0;i<strlen(text);i++)
                                           if(text[i]==’A’)
                                                    text[i]=text[i]+2;
                                  puts(text);
                          }

         Ans.            stdio.h
                         string.h

                  (½ Mark for writing each correct header file)
                  NOTE: Any other header file to be ignored

         (c)      Rewrite the following C++ code after removing any/all Syntactical Error(s)     (2)
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
      #define PI 3.14//Error 1
      void main( )
      {
             float R=4.5,H=1.5;
             floatA=2*PI*R*H + 2*PI*pow(R,2);              //Error 2, 3
             cout<<“Area=”<<A<<endl;                        //Error 4
      }

      (½ Mark for each correction)
      OR
      (1 mark for identifying the errors, without suggesting corrections)

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

Ans   7@11@
      6@8@
      11@3@

      (½ Mark for writing each correct value)
      OR
      (Only ½ Mark for writing all ‘@’ at proper places)
      Note:
      ● Deduct only ½ Mark for not considering any or all correct placements of
        @
      ● Deduct only ½ Mark for not considering any or all line break

(e)   Find and write the output of the following C++ program code:                (2)
      typedef char STRING[80];
      void MIXNOW(STRING S)
      {
        int Size=strlen(S);
        for(int I=0;I<Size;I+=2)
        {
                     char WS=S[I];


                                        2
```

---

## page 3

```
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

Ans.   BCE@XEMA0291

       (2 Marks for correct output)
       OR
       (½ Mark for each of two correct consecutive alphabets not exceeding 1½
       marks )

(f)    Observe the following program and find out, which output(s) out of (i) to   (2)
       (iv) willbe expected from the program? What will be the minimum and the
       maximum value assigned to the variable Alter?
       Note: Assume all required header files are already being included in
       the program.
               void main( )
               {
                       randomize();
                       int Ar[]={10,7}, N;
                       int Alter=random(2) + 10 ;
                       for (int C=0;C<2;C++)
                       {
                                N=random(2) ;
                                cout<<Ar[N] +Alter<<”#”;
                       }
               }
               (i) 21#20#                           (ii) 20#18#
              (iii) 20#17#                          (iv) 21#17#

Ans.   The output expected from the program is (iii) 20#17#
       Minimum Value of Alter = 10
       Maximum Value of Alter = 11

       (1 Mark for writing correct option (iii))
       ( ½ Mark for writing correct Minimum Value of Alter)
       ( ½ Mark for writing correct Maximum Value of Alter)



                                        3
```

---

## page 4

```
2   (a)    What is a copy constructor? Illustrate with a suitable C++ example.         (2)
3
    Ans.   A copy constructor is an overloaded constructor in which an object of the
           same class is passed as reference parameter.
           class X
           {
                  int a;
              public:
                  X()
                  {
                    a=0;
                  }
                  X(X &ob)           //copy constructor
                  {
                       a=ob.a;
                }
           };

           (Full 2 Marks to be awarded if the copy constructor is explained with an
           appropriate example)

           OR

           (1 Mark for correct explanation of copy constructor only without an
           example)

    (b)    Write the output of the following C++ code. Also, write the name of         (2)
           feature of Object Oriented Programming used in the following program
           jointly illustrated by the Function 1 to Function 4.

                  void My_fun ( )                              // Function 1
                  {
                        for (int I=1 ; I<=50 ; I++) cout<< "-" ;
                        cout<<end1 ;
                  }
                  void My_fun (int N)                          // Function 2
                  {
                        for (int I=1 ; I<=N ; I++) cout<<"*" ;
                        cout<<end1 ;
                  }
                  void My_fun (int A, int B)                   // Function 3
                  {
                        for (int I=1. ;I<=B ;I++) cout <<A*I ;
                        cout<<end1 ;
                  }
                  void My_fun (char T, int N)                  // Function 4
                  {
                        for (int I=1 ; I<=N ; I++) cout<<T ;
                        cout<<end1;
                                            4
```

---

## page 5

```
              }
              void main ( )
              {
                    int X=7, Y=4, Z=3;
                    char C='#' ;
                    My_fun (C,Y) ;
                    My_fun (X,Z) ;
       }

                                             OR

       Write any four differences between Constructor and Destructor function
       with respect to object oriented programming

Ans.   ####
       71421
       Polymorphism
       OR
       Function Overloading

                                             OR
                    Constructor                            Destructor
        Name of the constructor function is Name of the destructor function is
        same as that of class                  same as that of class preceded by
                                               ~
        Constructor functions are called       Destructor functions are called
        automatically at the time of           automatically when the scope of
        creation of the object                 the object gets over
        Constructor can be overloaded          Destructor ca not be overloaded
        Constructor is used to initialize the Destructor is used to de- initialize
        data members of the class              the data members of the class

       (½ Mark for writing each correct line of output)
       (1 Mark for writing the feature name correctly)

                                             OR

       (½ Mark for writing each correct difference)

(c)    Define a class Ele_Bill in C++ with the following descriptions:               (4)
       Private members:
            Cname                    of type character array
            Pnumber                  of type long
            No_of_units              of type integer
             Amount                  of type float.
             Calc_Amount( )         This member function should calculate the
                  amount asNo_of_units*Cost .


                                         5
```

---

## page 6

```
       Amount can be calculated accordingto the following conditions:

       No_of_units Cost

                    First 50 units            Free
                    Next 100 units            0.80 @ unit
                    Next 200 units            1.00 @ unit
                    Remaining units           1.20 @ unit

       Public members:

           * A function Accept( ) which allows user to enter Cname,
             Pnumber, No_of_units and invoke function Calc_Amount().
           * A function Display( ) to display the values of all the data members
             on the screen.

Ans.
       class Ele_Bill
       {
           char Cname[20];
           long Pnumber;
           int No_of_units;
           float Amount;
           void Calc_Amount( );
         public:
           void Accept();
           void Display();
       };

          void Ele_Bill : : Calc_Amount( )
          {
                  if(No_of_units<=50)
                  {
                           Amount=0;
       }
       else if(No_of_units<=150)
                    {
                            Amount=(No_of_units-50)*0.80;
       }
                   else if(No_of_units<=350)
                     {
                            Amount=80+(No_of_units-150)*1.00;
       }
                      else
                      {
                            Amount=80+200+(No_of_units-350)*1.20;
                      }
              }
         void Ele_Bill :: Accept( )

                                       6
```

---

## page 7

```
           {
                    gets(Cname);
                    cin>Pnumber>>No_of_units;
                    Calc_Amount( );
            }
            void Ele_Bill :: Display( )
           {
                    cout<<Cname<<Pnumber<<No_of_units<<Amount;
           }


      (½ Mark for declaring class header correctly)
      (½ Mark for declaring data members correctly)
      (1 Mark for defining Calc_Amount() correctly)
      (½ Mark for taking inputs of Cname, Pnumber and No_of_units in
         Accept())
      (½ Mark for invoking Calc_Amount() inside Accept())
      (½ Mark for defining Display() correctly)
      (½ Mark for correctly closing class declaration with a semicolon ; )
      NOTE:
      Marks to be awarded for defining the member functions inside or
      outside the class

(d)   Answer the questions (i) to (iv) based on the following:               (4)
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
              Schedule();

                                        7
```

---

## page 8

```
              void Start();
              void View();
       };
       void main()
       {
             Schedule S;            //Statement 1
             ___________            //Statement 2
       }
                                            OR

       Consider the following class State :
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
             Dname               string
             Distance          float
             Population        long int
             Member functions :
                      DINPUT( ) : To enter Dname, Distance and population
                      DOUTPUT( ) : To display the data members on the screen.

(i)    Write the names of all the member functions, which are directly accessible
       by the object S of class Schedule as declared in main() function.

Ans.   Start(), Schedule::View(), Commence(), Programme::View()

       (1 Mark for writing all correct member names )
       NOTE:
       ● Ignore the mention of Constructors

(ii)   Write the names of all the members, which are directly accessible by the
       memberfunction Start( ) of class Schedule.

Ans.   DD,MM,YYYY, Schedule::View()
       Title, Commence( ), Programme::View()
       Fname, Enter(), Show()

       (1 Mark for writing all correct member names )


                                        8
```

---

## page 9

```
        NOTE:
        ● Marks not to be awarded for partially correct answer
        ● Ignore the mention of Constructors

(iii)   Write Statement 2 to call function View( ) of class Programme from the
        object S of class Schedule.

Ans.    S.Programme::View( );

        (1 Mark for writing Statement 2 correctly)

(iv)    What will be the order of execution of the constructors, when the object S
        of class Schedule is declared inside main()?

Ans.    Programme( ), Faculty( ), Schedule( )

                                              OR
Ans.    class District : public State
         {
        public :
        char      Dname[20];
        float      Distance;
        long int Population;
         void DINPUT( )
        {
        gets(Dname);
        cin>>distance;
        cin>>Population;
        }
        void DOUTPUT( )
        {
        cout<<Dname<<endl;
        cout<<Distance<<endl;
        cout<<population<<endl;
        }
        };
        (1 Mark for writing correct order)
        ● No Marks to be awarded for any other combination/order.
        ● Names of the constructor/class without parenthesis is acceptable

                                              OR

        (1 Mark for correct syntax for derived class header)
        (½ Mark for writing public : )
        (½ Mark for correct declaration of data members Dname ,Distance and
        Population)
        (1 Mark for defining the function DINPUT( ) )
        (1 Mark for defining the function DOUTPUT( ) )

                                          9
```

---

## page 10

```
(a)    Write a user-defined function AddEnd4(int A[][4],int R,int C) in C++ to       (2)
Ans.   find and display the sum of all the values, which are ending with 4 (i.e.,
       unit place is 4).
       For example if the content of array is:
                                24 16 14
                                19 5 4
       The output should be 42

                                              OR

       Write a user defined function in C++ to find the sum of both left and right
       diagonal elements from a two dimensional array.

       void AddEnd4(int A[ ][4], int R, int C)
       {
             int I,J,sum=0;
             for(I=0;I<R;I++)
             {
                   for(J=0;J<C;J++)
         if(A[I][J]%10 ==4)
                       sum=sum+A[I][J];
             }
            cout<<sum;
       }

                                              OR
       void Diagsumboth(int A[][4], int n)
       {
       int sumLt=0,sumRt=0;
       for(int i=0;i<n;i++)
       {
       sumLt+=A[i][i];
       else
       sumRt+=A[n-1-i][i];
       }
       cout<<”sum of left diagonal”<<sumlt<<endl;
       cout<<”sum of right diagonal”<<sumRt<<endl;
       }

       (½ Mark for correct loops)
       (½ Mark for correct checking values ending with 4)
       ( ½ Mark for finding sum of values)
       ( ½ Mark for displaying the sum )

                                              OR
       (1/2 Mark for correct loop)
       (1/2 Mark each for calculating sum of left or right diagonals)
       (1/2 Mark for displaying)

                                         10
```

---

## page 11

```
(b)    Write a user-defined function EXTRA_ELE(int A[ ], int B[ ], int N) in C++    (3)
       to find and display the extra element in Array A. Array A contains all the
       elements of array B but one more element extra. (Restriction: array
       elements are not in order)

       Example       If the elements of Array A is 14, 21, 5, 19, 8, 4, 23, 11
                     and the elements of Array B is 23, 8, 19, 4, 14, 11, 5
                     Then output will be 21

                                                  OR

       Write a user defined function Reverse(int A[],int n) which accepts an
       integer array and its size as arguments(parameters) and reverse the array.
       Example : if the array is 10,20,30,40,50 then reversed array is
       50,40,30,20,10

Ans.   void EXTRA_ELE(int A[], int B[],int N)
       {
         int i,j,flag=0;
         for(i=0;i<N;i++)
         {
             for(j=0;j<N;j++)
           {
                 if(A[i]==B[j])
                 {
                         flag=1;
                         break;
                 }
           }
           if(flag==0)
                   cout<<"Extra element"<<A[i];
       flag=0;
         }
       }

                                             OR
       void Reverse( int A[ ] , int n)
       {
       int temp;
       for(int i=0;i<n/2;i++)
       {
       temp=A[i];
       A[i]=A[n-1-i];
       A[n-1-i]=temp;
       }
       }
       (1 Mark for correct loops)
       (1 Mark for checking array elements which are equal)
       ( ½ Mark for display the extra element)

                                        11
```

---

## page 12

```
                                              OR
       (1 Mark for correct loop)
       (2 Marks for swapping elements)

(c)    An array S[10] [30] is stored in the memory along the column with each of     (3)
       its element occupying 2 bytes. Find out the memory location of S[5][10], if
       element S[2][15] is stored at the location 8200.

                                             OR
       An array A[30][10] is stored in the memory with each element requiring 4
       bytes of storage ,if the base address of A is 4500 ,Find out memory
       locations of A[12][8], if the content is stored along the row.


Ans.   OPTION 1:
       ASSUMING LBR=LBC=0
       W=2 BYTES, NUMBER OF ROWS(M)=10, NUMBER OF
       COLUMNS(N)=30
       LOC(S[I][J]) = B +(I + J*M)*W
       LOC(S[2][15]) = B +(2+15*10)* 2
       8200 = B + (152*2)
       B = 8200 - 304
       B = 7896
       LOC(S[5][10]) = 7896 +(5+10*10)* 2
       = 7896 + (105*2)
       = 7896 + 210
       = 8106

       OPTION 2:
       ASSUMING LBR=2,LBC=15 AND B = 8200
       W=2 BYTES, NUMBER OF ROWS(M)=10, NUMBER OF
       COLUMNS(N)=30
       LOC(S[I][J]) = B +((I-LBR) + (J-LBC)*M)*W
       LOC(S[5][10])= 8200 + ((5-2) + (10-15)*10)*2
       = 8200 + (3 + (-5)*10) * 2
       = 8200 + (3 + (-50)) * 2
       = 8200 + (3 – 50) * 2
       = 8200 + (-47) * 2
       = 8200 – 94
       = 8106

                                              OR

       Loc of A[12][8]= B+W*(N*(I-LBR)+(J-LBC))
                       =4500+4*(10*12+8)
                        = 4500 4*(128)
                        =4500 + 512
                        = 5012


                                         12
```

---

## page 13

```
      1 Mark for writing correct formula (for column major)
      OR substituting formula with correct values)
      (1 Mark for correct step calculations)
      (1 Mark for final correct address)

                                           OR

      1 Mark for writing correct formula (for Row major)
      OR substituting formula with correct values)
      (1 Mark for correct step calculations)
      (1 Mark for final correct address)


(d)   Write the definition of a member function Ins_Player() for a class           (4)
      CQUEUE in C++, to add a Player in a statically allocated circular queue of
      PLAYERs considering the following code
      is already written as a part of the program:
      struct Player
      {
            long Pid;
           char Pname[20];
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
               Rear=-1;
            }
            void Ins_Player(); // To add player in a static circular queue
            void Del_Player(); // To remove player from a static circular queue
            void Show_Player(); // To display static circular queue
      };

                                           OR

      Write a function in C++ to delete a node containing Books information
      ,from a dynamically allocated stack of Books implemented with the help of
      the following structure:
      struct Book
      {
      int BNo;
      char BName[20];
      Book *Next;
      };

                                      13
```

---

## page 14

```
Ans.   void CQUEUE : : Ins_Player( )
       {
            if((Front==0 && Rear==size-1) || (Front==Rear+1)
            {
                  cout<< “Overflow”;
                  return;
             }
            else if(Rear = = -1)
            {
                  Front=0;
                  Rear=0;
             }
             else if(Rear= =size-1)
            {
                   Rear=0;
             }
             else
             {
                   Rear++;
             }
          cout<< “Enter Player Id=”;
          cin>>Ar[Rear].Pid;
          cout<< “Enter Player Name=”;
          gets(Ar[Rear].Pname);
       }

                                            OR

       struct Book
       {
       int BNo;
       char BName[20];
       Book *Next;
       }*temp,*top;


       void pop()
       {
       temp=new Book ;
       temp=top;
       top=top->next;
       delete temp;
       }

       (1 Mark for checking if Queue is Full)
       (1 Mark for checking if Queue is Empty)
       (½ Mark for checking Rear is at size-1)
       (½ Mark for incrementing Rear)
       (½ Mark for assigning Values to the Rear location of the Queue)
                                       14
```

---

## page 15

```
                                                        OR
           ( 1 Mark for creating new node Book)
           (1 Mark for assigning top to temp)
           (1 Mark for top=top->next)
           (1 Mark for delete top)

    (e)    Convert the following Infix expression to its equivalent Postfix expression,   (2)
           showing the stack contents for each step of conversion.
                 A/B+C*(D-E)

                                              OR
           Evaluate the following Postfix expression :
             4,10,5,+,*,15,3,/,-

    Ans:
            Element                   Stack                     Postfix
            A                                                   A
            /                         /                         A
            B                         /                         AB
            +                         +                         AB/
            C                         +                         AB/C
            *                         +*                        AB/C
            (                         +*(                       AB/C
            D                         +*(                       AB/CD
            -                         +*(-                      AB/CD
            E                         +*(-                      AB/CDE
            )                         +*                        AB/CDE-
                                      +                         AB/CDE-*
                                                                AB/CDE-*+
                                                   OR
           55

           (½ Mark for conversion upto each operator illustrating through stack)

                                                   OR

           (1/2 Mark for evaluating each operator)

4   (a)    Write a function RevText() to read a text file “ Input.txt “ and Print only    (2)
           word starting with ‘I’ in reverse order .
           Example: If value in text file is: INDIA IS MY COUNTRY
           Output will be: AIDNI SI MY COUNTRY

                                                   OR

           Write a function in C++ to count the number of lowercase alphabets
           present in a text file “BOOK..txt".


                                              15
```

---

## page 16

```
Ans.   void RevText( )
       {
             ifstream Fin(“Input.txt”);
             char Word[20];
             while(!Fin.eof())
           {
       Fin>>Word;
                 if(Word[0]==’I’)
                     strrev(Word);
                 cout<<Word<< “ ”;
             }
         Fin.close( );
       }

                                               OR

       int Countalpha()
       ifstream ifile ("BOOK.txt");
       char ch;
       int count =0;
       while (! ifile.eof())
       {
       ifile.get(ch);                                                                 Ifele.get(ch);
       if(isfower(ch))
       count ++;
       }
       ifile.close();
       return (count)
       }


       (½ Mark for opening Input.txt correctly)
       (½ Mark for reading each Word from the file)
       (½ Mark for checking the word starting with ‘I’ )
       (½ Mark for reversing and displaying the word)

                                               OR

       (½ Mark for opening Input.txt correctly)
       (½ Mark for reading each character from the file)
       (½ Mark for checking the lower character )
       (½ Mark for displaying the count)

(b)    Write a function in C++ to search and display details, whose destination is   (3)
       “Cochin” from binary file “Bus.Dat”. Assuming the binary file is
       containing the objects of the following class:
       class BUS
       {       int Bno;                      // Bus Number
               char From[20];                // Bus Starting Point
                                          16
```

---

## page 17

```
               char To[20];                  // Bus Destination
             public:
       char * StartFrom ( ); { return From; }
                char * EndTo( ); { return To; }
                void input() { cin>>Bno>>; gets(From); get(To); }
                void show( ) { cout<<Bno<< “:”<<From << “:” <<To<<endl; }
       };

                                         OR
       Write a function in C++ to add more new objects at the bottom of a binary
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

Ans.   void Read_File( )
       {
             BUS B;
             ifstream Fin;
             Fin.open(“Bus.Dat”, ios::binary);
             while(Fin.read((char *) &B, sizeof(B)))
             {
                     if(strcmp(B.EndTo(), “Cochin”)==0)
                     {
                            B.show( ) ;
                     }
            }
            Fin.close( );
       }
                                            OR
       void Addrecord()
       {
       ofstream ofile;
       ofile.open("STUDENT.dat", ios ::out);
       STU S;
       char ch='Y';
       while (Ch=='Y' || Ch = = 'y')
       {
                                       17
```

---

## page 18

```
       S.Enter();
       ofile.write (Char*) & S, sizeof(s));
       cout << "more (Y/N)";
       cin>>ch;
       }
       ofile.close();
       }

       (½ Mark for opening Bus.Dat correctly)
       (1 Mark for reading each record from Bus.Dat)
       (1 Mark for comparing value returned by EndTo( ) with “Cochin”)
       (½ Mark for displaying the matching record)

                                              OR

       (1 Mark for opening STUDENT.Dat correctly)
       (1 Mark for S.Enter())
       (1 Mark for writing each record into the file)

(c)    Find the output of the following C++ code considering that the binary file   (1)
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
              In.seekg(70*sizeof(P));
              In.read((char*)&P, sizeof(P));
              In.read((char*)&P, sizeof(P));
              cout<<"At Product:"<<In.tellg()/sizeof(P) + 1;
              In.close();
       }
                                          OR

       Which file stream is required for seekg() ?

Ans.   Total Count:500
       At Product: 73

                                              OR

                                         18
```

---

## page 19

```
           fstream/ ifstream

           (½ Mark for each correct value of In.tellg()/sizeof(P) as 500 and 73
           respectively)

                                                 OR
           (1 Mark for correct stream)

5   (a)    Observe the following table and answer the parts(i) and(ii) accordingly     (2)
           Table:Product

                  Pno            Name              Qty              PurchaseDate
                  101             Pen              102               12-12-2011
                  102           Pencil             201               21-02-2013
                  103           Eraser              90               09-08-2010
                  109          Sharpener            90               31-08-2012
                  113            Clips             900               12-12-2011

    (i)    Write the names of most appropriate columns, which can be considered as
           candidate keys.

    Ans.   Candidate Key: Pno, Name

           (1 Mark for writing correct Candidate Keys)

    (ii)   What is the degree and cardinality of the above table?

    Ans.   Degree:4
           Cardinality:5

           (½ Mark for writing correct value of degree)
           (½ Mark for writing correct value of cardinality)

    (b)    Write SQL queries for (i) to (iv) and find outputs for SQL queries (v) to    (4+2)
           (viii), which are based on the tables.

                                 TRAINER

            TID    TNAME                 CITY                  HIREDATE     SALARY
            101    SUNAINA               MUMBAI                1998-10-15   90000
            102    ANAMIKA               DELHI                 1994-12-24   80000
            103    DEEPTI                CHANDIGARG            2001-12-21   82000
            104    MEENAKSHI             DELHI                 2002-12-25   78000
            105    RICHA                 MUMBAI                1996-01-12   95000
            106    MANIPRABHA            CHENNAI               2001-12-12   69000



                                            19
```

---

## page 20

```
        COURSE

         CID        CNAME          FEES        STARTDATE          TID
         C201       AGDCA          12000       2018-07-02         101
         C202       ADCA           15000       2018-07-15         103
         C203       DCA            10000       2018-10-01         102
         C204       DDTP           9000        2018-09-15         104
         C205       DHN            20000       2018-08-01         101
         C206       O LEVEL        18000       2018-07-25         105


(i)     Display the Trainer Name, City & Salary in descending order of their
        Hiredate.

Ans.    SELECT TNAME, CITY, SALARY FROM TRAINER ORDER BY
        HIREDATE;

        (½ Mark for SELECT TNAME, CITY, SALARY FROM TRAINER)
        (½ Mark for ORDER BY HIREDATE)

(ii)    To display the TNAME and CITY of Trainer who joined the Institute in the
        month of December 2001.

Ans.    SELECT TNAME, CITY FROM TRAINER WHERE HIREDATE
        BETWEEN ‘2001-12-01’ AND ‘2001-12-31’;
        OR
        SELECT TNAME, CITY FROM TRAINER WHERE HIREDATE >=
        ‘2001-12-01’ AND HIREDATE<=‘2001-12-31’;
        OR
        SELECT TNAME, CITY FROM TRAINER WHERE HIREDATE LIKE
        ‘2001-12%’;

        (½ Mark for SELECT TNAME, CITY FROM TRAINER)
        (½ Mark for
        WHERE HIREDATE BETWEEN ‘2001-12-01’ AND ‘2001-12-31’
        OR
        WHERE HIREDATE >= ‘2001-12-01’ AND HIREDATE<=‘2001-12-31
        OR
        WHERE HIREDATE LIKE ‘2001-12%’

(iii)   To display TNAME, HIREDATE, CNAME, STARTDATE from tables
        TRAINER and COURSE of all those courses whose FEES is less than or
        equal to 10000.

Ans.    SELECT TNAME,HIREDATE,CNAME,STARTDATE FROM
        TRAINER, COURSE WHERE TRAINER.TID=COURSE.TID AND
        FEES<=10000;


                                        20
```

---

## page 21

```
        (1 Mark for correct query)
        OR
        (½ Mark for correct SELECT )
        (½ Mark for correct WHERE Clause)

(iv)    To display number of Trainers from each city.

Ans.    SELECT CITY, COUNT(*) FROM TRAINER GROUP BY CITY;

        (1 Mark for correct query)
        OR
        (½ Mark for correct SELECT )
        (½ Mark for GROUP BY CITY)

(v)     SELECT TID, TNAME, FROM TRAINER WHERE CITY NOT
        IN(‘DELHI’, ‘MUMBAI’);

Ans.    TIDTNAME
        103    DEEPTI
        106    MANIPRABHA

        (½ Mark for correct output)

(vi)    SELECT DISTINCT TID FROM COURSE;

Ans.    DISTINCT TID
         101
         103
         102
         104
         105

        (½ Mark for correct output)

(vii)   SELECT TID, COUNT(*), MIN(FEES) FROM COURSE GROUP BY
        TID HAVING COUNT(*)>1;

Ans.    TIDCOUNT(*)MIN(FEES)
        101      2                    12000

        (½ Mark for correct output)

(viii) SELECT COUNT(*), SUM(FEES) FROM COURSE WHERE
       STARTDATE< ‘2018-09-15’;

Ans.    COUNT(*)SUM(FEES)
         4              65000

        (½ Mark for correct output)


                                        21
```

---

## page 22

```
6   (a)    State any one Distributive Law of Boolean Algebra and Verify it using   (2)
           truth table.

    Ans.   Distributive Law:
           A+BC=(A+B)(A+C)
           Verification

            A   B   C BC A+BC (A+B) (A+C) (A+B)(A+C)
            0   0   0 0    0    0     0       0
            0   0   1 0    0    0     1       0
            0   1   0 0    0    1     0       0
            0   1   1 1    1    1     1       1
            1   0   0 0    1    1     1       1
            1   0   1 0    1    1     1       1
            1   1   0 0    1    1     1       1
            1   1   1 1    1    1     1       1

           OR
           A(B+C)=AB+AC

            A   B   C B+C A(B+C) AB AC AB+AC
            0   0   0  0     0    0  0   0
            0   0   1  1     0    0  0   0
            0   1   0  1     0    0  0   0
            0   1   1  1     0    0  0   0
            1   0   0  0     0    0  0   0
            1   0   1  1     1    0  1   1
            1   1   0  1     1    1  0   1
            1   1   1  1     1    1  1   1


           (1 Mark for stating any one Distributive Law correctly)
           (1 Mark for correctly verifying the stated Law using Truth Table)

    (b)    Draw the Logic Circuit of the following Boolean Expression:             (2)
                        ((U + V’).(U + W)). (V + W’)

    Ans.




    (c)    Derive a Canonical SOP expression for a Boolean function F(X,Y,Z)       (1)
           represented by the following truth table:

                                            22
```

---

## page 23

```
                                    X Y Z F(X,Y,Z)
                                    0 0 0    1
                                    0 0 1    1
                                    0 1 0    0
                                    0 1 1    0
                                    1 0 0    1
                                    1 0 1    0
                                    1 1 0    0
                                    1 1 1    1

    Ans.   F(X,Y,Z)= X’Y’Z’+X’Y’Z+XY’Z’+XYZ
           OR
           F(X,Y,Z)=∑(0,1,4,7)

           (1 Mark for the correct SOP form)
           OR
           (½ Mark for writing any two term correctly)


    (d)    Reduce the following Boolean Expression to its simplest form using K-         (3)
           Map:
           F(X,Y,Z,W)= Σ (0,1,2,3,4,5,8,10,11,14)




           Simplified Expression: X’Z’+Y’W’+Y’Z+XZW’

           (½ Mark for drawing K-Map and correctly plotting 1s in the given cells)
           ( ½ Mark each for 4 groupings)
           ( ½ Mark for writing final expression in reduced/minimal form)
           Note:
           ● Deduct ½ mark if wrong variable names are used

7   (a)    Arun opened his e-mail and found that his inbox was full of hundreds of        (2)
           unwanted mails. It took him around two hours to delete these unwanted
           mails and find the relevant ones in his inbox. What may be the cause of his
           receiving so many unsolicited mails? What can Arun do to prevent this
           happening in future?



                                            23
```

---

## page 24

```
Ans.   Arun’s email has been attacked with spam.
       These may be promotional mails from different advertisement groups.
       Arun must have checked some promotional offers while surfing the
       Internet.
       He should create filters in his email to stop receiving these unwanted mails.

       (1 Mark for writing correct Answer)
       (1 Mark for writing correct Justification to prevent Spam)

(b)    Assume that 50 employees are working in an organization. Each employee          (1)
       has been allotted a separate workstation to work. In this way, all computers
       are connected through the server and all these workstations are distributed
       over two floors. In each floor, all the computers are connected to a switch.
       Identify the type of network?

Ans.   LAN(Local Area Network)

       (1 Mark for writing correct Answer)

(c)    Your friend wishes to install a wireless network in his office. Explain him     (1)
       the difference between guided and unguided media.

Ans.   Guided media uses cables to connect computers, whereas unguided media
       uses waves.

       (1 Mark for writing any correct difference between guided and unguided
       media)

(d)    Write the expanded names for the following abbreviated terms used in            (2)
       Networkingand Communications:
       (i) CDMA      (ii) HTTP     (iii)   XML (iv)      URL

Ans.      (i)     Code Division Multiple Access
          (ii)    Hyper Text Transfer Protocol
          (iii)   Extensible Markup Language
          (iv)    Uniform Resource Locator

       ( ½ Mark for writing each correct expansion)

(e)    Multipurpose Public School, Bangluru is Setting up the network                  (4)
       between its Different Wings of school campus. There are 4
       wings

       namedasSENIOR(S),JUNIOR(J),ADMIN(A)andHOSTEL(H).


         Multipurpose Public School, Bangluru


                                         24
```

---

## page 25

```
                          SENIOR                                JUNIOR




                          ADMIN                                 HOSTEL




      Distance between various wings are given below:


                          WingAtoWingS             100m
                          WingAtoWingJ             200m
                          WingAtoWingH             400m
                          WingStoWingJ             300m
                          WingStoWingH             100m
                          WingJtoWingH             450m

      Number of Computers installed at various wings are as follows:


                          Wings            NumberofComputers
                          WingA                      20
                          WingS                     150
                          WingJ                      50
                          WingH                      25


(i)   Suggest the best wired medium and draw the cable layout to efficiently
      connect various wings of Multipurpose PublicSchool, Bangluru.

Ans   Best wired medium: Optical Fibre OR CAT5 OR CAT6 OR CAT7 OR
      CAT8 OR Ethernet Cable


                                      25
```

---

## page 26

```
                       SENIOR
                                                                  JUNIOR




                           ADMIN                                 HOSTEL




        (½ Mark for writing best wired medium)
        (½ Mark for drawing the layout correctly)
(ii)    Name the most suitable wing where the                 Server should be
        installed. Justify your answer.
Ans.    Wing Senior(S)- Because it has maximum number of computers.

        (½ Mark for correct Wing)
        (½ Mark for valid justification)

(iii)   Suggest a device/software and its placement that would provide
        data security for the entire network of the School.

Ans.    Firewall - Placed with the server at Senior
        OR
        Any other valid device/software name

        (½ Mark for writing device/software name correctly)
        (½ Mark for writing correct placement)

(iv)    Suggest a device and the protocol that shall be needed to provide wireless
        Internet access to all smartphone/laptop users in the campus of
        Multipurpose Public School, Bangluru.

Ans.    Device Name: WiFi Router OR WiMax OR RF Router OR Wireless
        Modem OR RFTransmitter
        Protocol : WAP OR 802.16 OR TCP/IP OR VOIP OR MACP OR 802.11

        (½ Mark for writing correct device name)
        (½ Mark for writing correct protocol)



                                           26
```