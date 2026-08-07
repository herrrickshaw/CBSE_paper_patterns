---
title: "Computer Science SQP (2015-16) Set 2 MS"
source_pdf: "Computer_Science_SQP_(2015-16)_Set_2_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2015_16/Computer Science SQP/Computer Science SQP (2015-16) Set 2 MS.pdf"
pages: 35
pdf_bytes: 125404
pdf_sha256: "465b693d03c5c4df7b4c1b690f1f2f1e6ce31118025ea9a1f9326dbea235177c"
text_chars: 44438
low_text_pages: 0
converter: "pdftotext -layout"
---

# Computer Science SQP (2015-16) Set 2 MS


---

## page 1

```
                                 Computer Science (083)

                               Marking Scheme - Set - II

                                   Class- XII (2015-16)


Time: 3hrs                                                                      M.M: 70

Instructions:

  i.    All Questions are Compulsory.

 ii.    Programming Language: Section A : C++

 iii.   Programming Language: Section B: Python

 iv.    Answer either Section A or B, and Section C is compulsory



                                          Section : A (C++)

Q1 a. Define Macro with suitable example.                                       2

Ans: Macros are preprocessor directive created using # define that serve as symbolic
constants.They are created to simplify and reduce the amount of repetitive coding
For instance,
#define max (a, b) a>b? a: b
Defines the macro max, taking two arguments a and b. This macro may be called like any
function.Therefore, after preprocessing

A = max(x, y);

Becomes A = x>y?x :y ;

[1 mark for definition]
[1 mark for example]

b. Which C++ header file (s) will be included to run /execute the following C++ code?    1
                    void main( )
                    {        int Last =26.5698742658;
                             cout<<setw(5)<<setprecision(9)<<Last;         }

Ans:     iostream.h
        iomanip.h
```

---

## page 2

```
[1/2 mark for each module name]


c. Rewrite the following program after removing any syntactical errors. Underline each
correction made.                            2

       #include<iostream.h>

       void main( )

               int A[10];

               A=[3,2,5,4,7,9,10];

                       for( p = 0; p<=6; p++)

                              {      if(A[p]%2=0)

                                     int S = S+A[p];       }

                              cout<<S;          }

Ans :- #include<iostream.h>

       void main( )

       {       int A[10] = {3,2,5,4,7,9,10};

               int S = 0,p;

                       for(p = 0; p<=6; p++)

                              {      if(A[p]%2==0)

                                     S = S+A[p];    }

                              cout<<S;

       }

[1/2 mark for each correction]

d. Find the output of the following C++ program:                                 2

#include<iostream.h>

void repch(char s[])

{
```

---

## page 3

```
    for (int i=0;s[i]!='\0';i++)

          {

              if(((i%2)!=0) &&(s[i]!=s[i+1]))

               {

                s[i]='@';

                cout<<"Hello";

                }

              else if (s[i]==s[i+1])

               {

                   s[i+1]='!';

                   i++;

                       }

                   }

}

void main()

{

    char str[]="SUCCESS";

cout<<”Original String”<<str

    repch(str);

    cout<<"Changed String"<<str;

}

Ans:

Original String SUCCESS

Changed String S@C!ES!

[1/2 mark for original String]
```

---

## page 4

```
[1/2 mark for ‘@’ in place of U ]

[1/2 mark for ‘!’ in place of second C ]

[1/2 mark for ‘!’ in place of second S ]



e. Find the output of the following :                                          3
        #include<iostream.h>
               void switchover(int A[ ],int N, int split)
                        {
                                for(int K = 0; K<N; K++)
                                        if(K<split)
                                                A[K] += K;
                                        else
                                                A[K]*= K;              }
                   void display(int A[ ] ,int N)
                        {
                        for(int K = 0; K<N; K++)
                                (K%2== 0) ?cout<<A[K]<<"%" : cout<<A[K]<<endl;
                        }
               void main( )
                                        {       int H[ ] = {30,40,50,20,10,5};
                                                switchover(H,6,3);
                                                display(H,6);
                                        }
Ans 3: 30%41
        52%60
        40%25
[1/2 mark for each value in the above order]
[deduct ½ mark for not putting ‘%’ in between values]

f. Observe the following C++ code and find out , which out of the given options i) to iv) are the
expected correct output.Also assign the maximum and minimum value that can be assigned to
the variable ‘Go’.                                                        2
                void main()
                   { int X [4] ={100,75,10,125};
                     int Go = random(2)+2;
                      for (int i = Go; i< 4; i++)
                         cout<<X[i]<<”$$”;

                   }

   i. 100$$75          ii. 75$$10$$125$$     iii. 75$$10$$ iv.10$$125$
```

---

## page 5

```
    Ans : iv is the correct option.
                Minimum value of Go = 2
                Maximum value of Go = 3

 [½ mark each for Minimum and Maximum value]

 [1 mark for correct option]

Q2a. Differentiate between data abstraction and data hiding.          2
Ans : Data hiding can be defined as the mechanism of hiding the data of a class from the outside
world. This is done to protect the data from any accidental or intentional access..
Data hiding is achieved by making the members of the class private.

Data abstraction refers to, providing only essential information to the outside world and hiding
their background details.
Members defined with a public label are accessible to all parts of the program. The data-
abstraction view of a type is defined by its public members.

[1/2 mark each for definition of Data Hiding and Data Abstraction]

[1/2 mark each for the difference in their implementation]
                Or
[ 2 marks for explanation through an example.


b. Answer the questions (i) and (ii) after going through the following class :             2
                            class Exam
                            {
                                   int Rollno;

                                   char Cname[25];
                                   float Marks ;
                                public :
                                   Exam( )                                //Function 1
                                           Rollno = 0 ;
                                           Cname=””;
                                           Marks=0.0;
                                   }
                                   Exam(int Rno, char candname)           //Function 2
                                   {
```

---

## page 6

```
                                           Rollno = Rno ;
                                           strcpy(Cname,candname);


                                    }
                                    ~Exam( )                              //Function 3
                                    {
                                           cout << “Result will be intimated shortly” << endl ;
                                    }
                                    void Display( )                       //Function 4
                                    {
                                           cout << “Roll no :”<<Rollno;

                                            cout<<”Name :” <<Cname;
                                            cout <<” Marks:”<<Marks;
                                    }
                                    };
(i)Which OOP concept does Function 1 and Function 2 implement.Explain?
Ans: i. Constructor Overloading /Polymorphism , as multiple definitions for Constructors are
given in the same scope. Function 1 is a Default constructor and function 2 is a Parameterized
constructor.
[1/2 mark for the concept]
[1/2 mark for explanation]
(ii)What is Function 3 called? When will it be invoked?
ii. Function 3 is a Destructor which is invoked when the object goes out of scope.
[1/2 mark for identification]
[1/2 mark for time of invocation]
c. Define a class Candidate in C++ with the following specification :                4
Private Members :
                A data members Rno(Registration Number) type long
                A data member Cname of type string
                A data members Agg_marks (Aggregate Marks) of type float
```

---

## page 7

```
               A data members Grade of type char
               A member function setGrade () to find the grade as per the aggregate marks
obtained by the student. Equivalent aggregate marks range and the respective grade as shown
below.
               Aggregate Marks               Grade
               >=80                          A
               Less than 80 and >=65         B
               Less than 65 and >=50         C
               Less than 50                  D
Public members:
      A constructor to assign default values to data members:
Rno=0,Cname=”N.A”,Agg_marks=0.0
       A function Getdata () to allow users to enter values for Rno. Cname, Agg_marks and call
function setGrade () to find the grade.
       A function dispResult( ) to allow user to view the content of all the data members.

Ans : class Candidate
        { long Rno;
           char Cname[20];
          float Agg_marks;
          char Grade;
         void setGrade()
        { if (Agg_marks>= 80)
                  Grade = ‘A’;
           else if(Agg_marks<80 && Agg_marks>=65)
                  Grade = ‘B’;
           else if (Agg_marks<65 && Agg_marks>=50)
                  Grade =’C’;
           else
                  Grade=’D’;
        }
      public:
        Candidate()
                  {
                     Rno=0;
                    Strcpy(Cname,”N.A.”);
                    Agg_marks=0.0;
                    }

              void Getdata ()
              {
                     cout<<”Registration No”;
                     cin>>Rno;
                     cout<<”Name”;
                     cin>>Cname;
                     cout<<Aggregate Marks”;
```

---

## page 8

```
                       cin>>Agg_marks;
                       setGrade();
               }

               void dispResult()
               {
                      cout<<”Registration No”<<Rno;
                      cout<<”Name”<<Cname;
                      cout<<Aggregate Marks”<<Agg_marks;
               }

[1/2 mark for correct syntax for class header]

[1/2 mark for correct declaration of data members]

[1/2 mark for correct definition of the constructor Candidate()]

[1 mark for correct definition of setGrade()

[1mark for correct definition of Getdata () with proper invocation of setGrade()]]

[1/2 mark for correct definition of dispresult]

d. Give the following class definition answer the question that is follow:           4

               class University

                       {

                               char name [20];

                               protected :

                               char vc[20];

                       public :

                               void estd();

                               void inputdata();

                               void outputdata();

                       }

               class College : protected University

                       {       int regno;
```

---

## page 9

```
                              protected

                              char principal()

                       public :

                              int no_of_students;

                              void readdata();

                              void dispdata ( );

                       };

                class Department : public College

                              char name[20];

                              char HOD[20];

                       public :

                              void fetchdata(int);

                              void displaydata( );      }

i). Name the base class and derived class of college.                               1

Ans: Base class: University

     Derived class: Department

[1/2 mark for each correct class name]

ii) Name the data member(s) that can be accessed from function displaydata.

Ans: char name[20],char HOD[20], char principal(),int no_of_students, char vc[20]

[1 mark for each class]

iii)What type of inheritance is depicted in the above class definition?

Ans. Multilevel Inheritance

[1 mark for the correct answer]

iv) What will be the size of an object (in bytes) of class Department?

Ans: 85 bytes
```

---

## page 10

```
[1 mark for the correct answer]



Qs. 3a. An integer array A [30][40] is stored along the column in the memory.If the element
A[20][25] is stored at 50000, find out the location of A[25][30].                       3

Ans : A[i][j] = B+W x [No.of rows x(I-Lr)+(J-Lc)]

       A[20][25] = B+ 2x[30x(20-0)+(25-0)]
       50000= B+2x[30x(20-0)+(25-0)]
       B = 48750

       A[7][10] = 48750+ 2x[30x(7-0)+(10-0)]
               = 49190


      [1 mark for writing correct formula or substitution with correct values]

      [1 mark for calculating correct base address.]

      [1 mark for calculating correct address of A[7][10].]



b. Write the definition of functions for the linked implemented queue containing passenger
informationas follows:                                                                   4

       struct NODE

              {       int Ticketno;

                      char PName[20];

                      NODE * NEXT;             };

       class Queueofbus

              {       NODE *Rear, *Front;

                      public:

                                Queueofbus()

                      {         Rear = NULL;

                      Front = NULL;                    };
```

---

## page 11

```
               void Insert();

               void Delete();

               ~Queueofbus()

               {                cout<<"Object destroyed";    }

};


Ans: void Queueofbus::Insert()
{      NODE *p = new NODE;
       cout<<”Enter Ticket no”
       cin>>p->ticketno;
       cout<<”Enter Name”;
       cin>>p->Pname;
       p->NEXT = NULL;
       if (rear == NULL)
       { Rear = p;
       Front = Rear;
       }
       else
       { Rear -> NEXT = p;
          Rear = Rear -> NEXT;
       }
}

[1 mark for creating a node]

[1/2 mark for accepting details]

[1/2 mark for assigning NULL to NEXT pointer of the Node]

[1/2 mark for checking rear==NULL]

[1/2 mark for setting front and rear on the node when rear == NULL]

[1/2 mark for inserting the node at rear]

[1/2 for shifting rear to the new node]


c. Write a function to sort any array of n elements using insertion sort . Array should be passed
as argument to the function.                                                         3
```

---

## page 12

```
void insertsort( int a[],int n)
{

         int p,ptr;
        //Assuming a[0]=int_min i.e. smallest integer
        for(p=1;p<=n;p++)
        {
        temp=a[p];
        ptr=p-1;
        while(temp<a[ptr])
        {
        a[ptr+1]=a[ptr];       // Move Element Forward
        ptr--;
        }
        a[ptr+1]=temp;         // Insert Element in Proper Place

}

[1/2 mark for correct for loop]

[1/2 mark for assigning first element to temp]

[1/2 mark for setting ptr = p-1]

[1/2 mark for correct while]

[1/2 mark for moving element forward]

[1/2 mark for inserting at the proper place]



d. Write a function NewMAT(int A[][],int r,int c ) in C++, which accepts a 2d array of integer and
its size as parameters divide all those array elements by 6 which are not in the range 60 to
600(both values inclusive) in the 2d Array . 2

Ans:

void NewMAT(int A[][],int r,int c )

{

for (int i = 0;i<r;i++)

        for(j=0;j<c;j++)
```

---

## page 13

```
                if ((A[i][j]>=60 )&&(A[i][j]<=600))

                  A[i][j]/=6 ;
                      or
                 A[i][j] = A[i][j]/6;
}

[1 mark for correct loops]

[1/2 mark for the condition]

[1./2 mark for changing the element value by dividing it by 6]



e. Evaluate the following postfix expression using stack and show the contents after execution of
each

Operations:470,5,4,^,25,/,6,*                                         2

S.No.       Symbol       Operation                Stack          Result
        1       470      push(470)                        470
        2          5     push(5)                      470,5
        3          4     push(4)                    470,5,4
        4                pop(4)                       470,5
            ^
0                      pop(5)                             470
                       perform(5^4)
                       push(625)                       470,625
        5           25 push(25)                   470,625,25
        6              pop(25)                         470,625
            /
                        pop(625)                         470
                        perform(625/25)                  470
                        push(25)                    470,25
        7            6 push(6)                  470,25,6
        8            * pop(6)                   470,25
                        pop(25)                          470
                        perform(25*6)                    470
[1/2 mark for finding result upto ‘^’ operator]

[1/2 mark for finding result upto ‘/’ operator]

[1/2 mark for finding result upto ‘*’ operator]
```

---

## page 14

```
[1/2 mark for correct answer]

[1/2 mark for only writing the answer]

Q4a)Consider a file F containing objects E of class Emp.

i)Write statement to position the file pointer to the end of the file

Ans: F.seekg(0,ios::end);

[1/2 mark for the statement]

ii)Write statement to return the number of bytes from the beginning of the file to the current
position of the file pointer.

Ans: F.tellg();

[1/2 mark for the statement]

b) Write a function RevText() to read a text file “ Input.txt “ and Print only word starting with
‘I’ in reverse order .                                                               2

       Example: If value in text file is: INDIA IS MY COUNTRY

       Output will be: AIDNI SI MY COUNTRY

Ans: void RevText()
       { ifstream in (“Input.txt”);
         char word[25];
         while(in)
               { in>>word;


             if (word[0]==’I’)
                     cout<<strrev(word);
             else
       cout<<word;

}

[1/2 mark for opening the file in input mode]

[1/2 mark for reading a word]

[1 mark for displaying words starting with ‘I’ in reverse order]
```

---

## page 15

```
c. Write a function in C++ to search and display details, whose destination is “Chandigarh”from
   binary file “Flight.Dat”. Assuming the binary file is containing the objects of the following
   class:                                                                     3

        class FLIGHT

        {         int Fno;              //       Flight Number

                  char From[20];        //       Flight Starting Point

                  char To[20];          //       Flight Destination

        public:

                  char * GetFrom ( );   {        return from;    }

                  char * GetTo( );      {        return To;      }

                  void input()          {        cin>>Fno>>; gets(From); get(To);   }

                  void show( )          {        cout<<Fno<< “:”<<From << “:” <<To<<endl; }

        };

 Ans : void Dispdetails()
        { ifstream fin(“Flight.Dat”);
          Flight F;
          while (fin)
         { fin.read((char*)&F,sizeof(F))
           if (strcmp(F.GetTo(),”Chandigarh”))
                 F.show();
 }

 }

 [1/2 mark for opening the file in input mode]

 [1/2 mark for creating the object of Flight]

 [1 mark for reading the record in object of Flight]

 [1/2 mark for comparing record’s destination with ‘Chandigarh’]

 [1/2 mark for displaying the record]

                                        Section : B (Python)
```

---

## page 16

```
Q1. a. List one similarity and one difference between List and Dictionary datatype      2

Ans: Similarity : Both List and Dictionary are mutable datatypes.

     Dissimilarity: List is a sequential data type i.e. they are indexed.

     Dictionary is a mapping datatype. It consists of key: value pair.

     Eg: L =[1,2,3,4,5] is a list

     D= {1:”Ajay”,2:”Prashant,4:”Himani”} is a dictionary where 1,2,4 are keys and
     “Ajay”,Prashant,”Himani” are their corresponding values.

[1 mark for similarity]

[1 mark for any one point of dissimilarity]

or

[2 mark for explanation using example]

b. Observe the following Python functions and write the name(s) of the module(s) to which they
belong:                                                                  1
        a. uniform() b. findall()

Ans: a. random b.re

[1/2 mark each for writing the correct module names]



c. Rewrite the following Python program after removing all the syntactical errors (if
any),underlining each correction.:                                                      2

       def checkval:
              x = raw_input(“Enter a number”)
              if x % 2 = 0 :
                 print x,”is even”
              else if x<0 :
                  print x,”should be positive”
              else ;
                  print x,”is odd”



       def checkval():
              x = raw_input(“Enter a number”)
```

---

## page 17

```
               if x % 2 = = 0 :
                  print x,”is even”
               elif x<0 :
                   print x,”should be positive”
               else :
                   print x,”is odd”

       [1/2 mark for each error]


d. Find the output of the following Python program:        3

   def makenew(mystr):

                  newstr = " "

                  count = 0

                  for i in mystr:

                    if count%2 !=0:

                       newstr = newstr+str(count)

                    else:

                       if islower(i):

                            newstr = newstr+upper(i)

                        else:

                         newstr = newstr+i

                    count +=1

                 newstr = newstr+mystr[:1]

                 print "The new string is :",newstr

 makenew(“sTUdeNT")

Ans:The new string is: S1U3E5Ts

[1/2 mark for each change i.e. S 1 3 E 5 s ]

e. Find the output of the following program            2
```

---

## page 18

```
def calcresult () :

        i=9

        while i> 1 :

                if (i % 2 == 0):

                         x = i%2

                         i = i-1

                else :

                         i = i-2

                         x=i

                print x**2

                49

                25

                9

                1

       [½ mark for each correct line of output.]
       [Deduct ½ mark for showing output in same line]

f. Observe the following Python code and find out , which out of the given options i) to iv) are
the expected correct output(s).Also assign the maximum and minimum value that can be
assigned to the variable ‘Go’.                                             2

                import random
                X =[100,75,10,125]
                Go = random.randint(0,3)
                for i in range(Go):
                   print X[i],"$$",

    i. 100$$75$$10 ii. 75$$10$$125$$iii. 75$$10$$            iv.10$$125$$100

Solution :100 $$ 75 $$ 10 $$
        Minimum Value that can be assigned to Go is 0
        Maximum Value that can be assigned to Go is 3
```

---

## page 19

```
[1 mark for correct option.]

[½ mark each for correct minimum and maximum value.]


Q2 a. Discuss the strategies employed by python for memory allocation?                     2

Ans: Python uses two strategies for memory allocation- Reference counting and Automatic
garbage collection:
Reference Counting: works by counting the number of times an object is referenced by other
objects inthe system. When an object's reference count reaches zero, Python collects it
automatically.
Automatic Garbage Collection: Python schedules garbage collection based upon a threshold of
objectallocations and object de-allocations. When the number of allocations minus the number of
deallocations are greater than the threshold number, the garbage collector is run and the unused
block ofmemory is reclaimed.


[1 mark for naming the strategies]
[1 mark for explanation]
b. Answer the questions (i) and (ii) after going through the following class definition:       2
       class Toy :
              tid =0;
              tcat = “ “

               def __init__(self):// Function1

       ..................................... // Blank 2
       i. Explain relevance of Function 1.
       ii. a. Fill in the blank2 with a statement to create object of the class TOY.
            b. Write statement to check whether tprice is an attribute of class TOY.

:i . __init__ function is used to initialize the members of a class. It is automatically
        invoked when the object of the class is created.

      [1 mark for mentioning the relevance of __init__()]

  ii.a. T=Toy()

     b. hasattr(T,tprice)

      [1 mark for mentioning the relevance of __init__()]

      [½ mark each for correct answer of ii.a. and ii.b.]
```

---

## page 20

```
c. Define a class Train in PYTHON with following description:             4
   Private Members

       src of type string
       Tnm of type string
       dest of type string
       charges of float

• A member function Getdata to assign the following values for Charges
       Dest               Charges
       Mumbai               1000
       Chennai               2000
       Kolkatta              2500
Public members
    • A parameterized constructor to initialize the data members.
    • A function InputData() to allow the user to enter the values
    • A function displaydata() to display all and call getdata function

Ans:
  class train:
       def __init__(self):
            _src=""
            _tnm=""
            _dest=""
            _charges=0.0
       def getdata(self):
               if self._dest=="mumbai" or self._dest=="MUMBAI":
                        self._charges=1000
               elif self._dest=="chennai" or self._dest=="CHENNAI":
                        self._charges=2000
               elif self._dest=="kolkata" or self._dest=="KOLKATA":
                        self._charges=2500
       def inputdata(self):
            self._src=raw_input("enter the source of journey")
            self._tnm=raw_input("enter the train name")
            self._dest=raw_input("enter the destination")
       def displaydata(self):
               print "the source of journey is",self._src
               print "the name of the train is",self._tnm
               print "the destination of the train is",self._dest
               t.getdata()
               print "the charges for your journey",self._charges

       [ 1 mark for the correct syntax of class]
       [1/2 mark for __init__()]
       [1 mark for correct definition of getdata()]
```

---

## page 21

```
        [1/2 mark for correct definition of inputdata()]
        [1 mark for correct definition of displaydata() with proper invocation of getdata()]

.
 d. Observe the following class definition and answer the question that follow:                2

  class ParentClass(objects):
    def__init__(self)
       self,x = 1
       self.y = 10


  def print(self):
        print(self.x, self.y)
  class ChildClass(ParentClass):
  def__init__(self):
        super(ChildClass, self).init_() # Line 1
        self,x = 2
  self.y = 20
  c = ChildClass()
  c.print()
  a. Explain the relevance of Line1.
  Ans: super() function is used to call the methods of base class which have
        been extended in derived class.Also it is the importance of derived class __init__() to
        invoke the base class __init__()
  [1 mark for correct explanation]
  b. What type of inheritance is being demonstrated in the above code?
  Ans. Single level Inheritance
  [1 mark for correct answer]

e. Write a user defined function findname(name) where name is an argument in Python to delete
     phone number from a dictionary phonebook on the basis of the name ,where name is the
     key.                                                             2

Ans:
       def findname(name):
             if phonebook.has_key():
               del phonebook[name]
             else:
               print”Name not found”
             print "Phonebook Information"
```

---

## page 22

```
             print "Name",'\t',"Phone number"
             for i in phonebook.keys():
                 print i,'\t',phonebook[i]

     [1/2 mark for checking whether the name is a valid key]

     [1/2 mark for using del() to delete the corresponding entry]

     [1/2 mark for the correct loop to display all the values corresponding to all keys]

     [1/2 mark for displaying the phonebook values correctly]


Qs. 3a. Explain try..except…else … with the help of user defined function def divide(x, y)which
raises an error when the denominator is zero while dividing x by y and displays the quotient
otherwise.

Ans: def divide(x, y):

               try:

                         result = x / y

               except ZeroDivisionError:

                         print "division by zero!"

               else:

                         print "result is", result

In the above example:

try block consists of code that can raise an error.When y(denominator) gets a 0 value,
ZeroDivisionError is raised which is handled by except clause.In case of no exception else
statement is executed.

In case there is no error the statement(s) in else clause are executed .
[1/2 mark for correct try block]

[1 mark for handling zero division error using except clause]

[1/2 mark for else clause]

[1 mark for explanation]
```

---

## page 23

```
b. Write a user defined function arrangelements(X),that accepts a list X of integers and sets all
the negative elements to the left and all positive elements to the right of the list.

Eg: if L =[1,-2,3,4,-5,7] , the output should be: [-2,-5,3,4,7]             3

Ans: def arrangelements(X):

       L=len(X)

       for i in range(L):

               if a[i]<0 and i!=0:

                         j=i

                         while j!=0 and a[j-1]>0 :

                                  a[j],[j-1]=a[j-1],a[j]

                                  j=j-1

[1/2 mark for correct for loop]

[1/2 mark for correct if statement]

[1/2 mark for assigning I to j]

[1/2 mark for correct while loop]

[1/2 mark for exchanging with the adjacent value to the left]

[1/2 mark for decrementing j]

c. Consider the following class definition :-                                      3

       class book ():

               bk = []

               def _ init _ (self, bno):

                         self .bno = bno



               def addbook (self):

                         ……………
```

---

## page 24

```
                  def removebook (self):

                         ……………

The class book is implemented using Queue. Keeping the same in mind, complete the function
definitions for adding a book addbook() and deleting a book removebook() .

Solution :def addbook(self):
               a=input("enter book number: ")
               book.bk.append(a)
         def removebook (self):
               if (book.bk==[]):
                       print "Queue empty"
               else:
                       print "deleted element is: ",book.bk[0]
                       del book.bk[0]


  [½ mark for accepting a book no]

   [1 mark for book.bk.append(a)]

   [½ mark for checking whether Q is empty]

   [½ mark for displaying the element being deleted.]

   [½ mark for deleting the element]


d. Write a python function generatefibo(n) where n is the limit, using a generator function
Fibonacci (max)( where max is the limit n) that produces Fibonacci series..             3

Ans: def Fibonacci (max):

        a, b = 0, 1

            while a <= max:

                   yield a

                    a, b = b, a + b

      def generatefibo(n)

        for i in Fibonacci (n):

       print i,
```

---

## page 25

```
[1/2 mark for assigning 0,1 respectively to a,b]

[1/2 mark for correct loop]

[1 mark for yield a ]

[1/2 mark for assigning b to a ans a+b to b]

[1/2 mark for’ for loop ‘ and print to display the fibonacci series]




e. Evaluate the following postfix using stack & show the content of the stack after the execution
of each:                                                                           2
       20, 4, +, 3, -, 7, 1

Ans:

 S.no Symbol        Operation        Stack         Result
  1     20           push(20)         20
  2      4            push(4)        20,4
  3     +             pop(4)          20
  4                  pop(20)
                  perform(20+4)
                    push (24)          24
  5        3          push(3)         24,3
  6        -          pop(3)           24
                     pop(24)
                  perform(24-3)
                    push (21)          21
  7        7         push (7)         21,7
  8        /          pop(7)           21
                     pop(21)
                  perform(21/7)
                     push (3)           3
                                               Result =
  9                     pop(3)                    3


       [½ mark each for correctly evaluating expression up to each operator.]

       [½ mark for correct answer]
```

---

## page 26

```
       Qs.4 a. Consider the following code :                                        1

       f = open ("mytry", "w+")

       f.write ("0123456789abcdef")

       f.seek (-3,2)      //1

       printf.read(2) //2

Explain statement 1 and give output of 2

Ans: Statement 1 uses seek()method can be used to position the file object at particular place in
the file. It's syntax is :fileobject.seek(offset [, from_what]).
So,f.seek(-3,2) positions the fileobject to 3 bytes before end of file.

Output of 2 is :de (It reads 2 bytes from where the file object is placed.)


       [½ mark each for correct explanations for i and ii]



b. Write a user defined function in Python that displays the number of lines starting with ‘H’ in
the file Para.txt.Eg: if the file contains:                                                 2

Whose woods these are I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

Then the line count should be 2.

Ans: def countH():
              f = open ("Para.txt", "r")

               lines =0

               l =f.readlines()

               for i in l:

                        ifi[0]=='H':

                        lines+=1

               print "no. of lines is",lines
```

---

## page 27

```
   [½ mark for opening PARA.TXT in input mode.]

   [½ mark for reading lines from the file]

   [½ mark for iterating through lines and checking whether they start with ‘H’]

   [½ mark for incrementing and displaying the no. of lines.]

c. Consider a binary file Employee.dat containing details such as empno:ename:salary (separator
‘ :’). Write a python function to display details of those employees who are earning between
20000 and 40000.(both values inclusive)                                     3

Ans: def Readfile():

       i = open("Employee.dat","rb+")

       x = i.readline()

       while(x):

          I = x.split(':')

          if (20000>=float(I[2])<=5000):

             print x

          x = i.readline()

      [½ mark for opening “Employee.Dat” correctly.]

      [½ mark for reading records from Employee.Dat.]

      [½ for iterating through the file.]

      [½ mark for using split().]

      [½ mark for if statement to check the condition.]

      [½ for printing the relevant record.]



                                              Section : C

Qs. 5 a. Differentiate between cardinality and degree of a table with the help of an example.2

Ans : Cardinality is defined as the number of rows in a table.

       Degree is the number of columns in a table.
```

---

## page 28

```
Eg:Consider the following tables:

Table : Account

Acno     Cname
Ac100    Sheela
Ac101    Darsh
Ac102    Kathy

Cardinality of Account table is : 3
Degree of Account table is :2

[1/2 mark each for definition of cardinality and degree]

[1 mark for correct demonstration using example]

 b. Consider the following tables FACULTY and COURSES. Write SQL commands for the
statements (i) to (v) and give outputs for SQL queries (vi) to (vii)           6


                                         FACULTY
 F_ID     Fname               Lname           Hire_date             Salary
 102      Amit                Mishra          12-10-1998            12000
 103      Nitin               Vyas            24-12-1994            8000
 104      Rakshit             Soni            18-5-2001             14000
 105      Rashmi              Malhotra        11-9-2004             11000
 106      Sulekha             Srivastava      5-6-2006              10000
                                         COURSES
 C_ID    F_ID             Cname                    Fees
 C21     102              Grid Computing           40000
 C22     106              System Design            16000
 C23     104              Computer Security        8000
 C24     106              Human Biology            15000
 C25     102              Computer Network         20000
 C26     105              Visual Basic             6000
   i) To display details of those Faculties whose salary is greater than 12000.
      Ans: Select * from faculty
            where salary > 12000
      [1/2 mark for Select and from]
      [1/2 mark for where]

   ii) To display the details of courses whose fees is in the range of 15000 to 50000 (both
       values included).
       Ans: Select * from Courses
            .where fees between 15000 and 50000
```

---

## page 29

```
       [1/2 mark for Select and from]
       [1/2 mark for where]

   iii) To increase the fees of all courses by 500 of “System Design” Course.
        Ans: Update courses set fees = fees + 500
               where Cname = “System Design”
        [1/2 mark for correct usage of update and set]
        [1/2 mark for where]

   iv) To display details of those courses which are taught by ‘Sulekha’ in descending order of
       courses.
       Ans: Select * from faculty fac,courses cour
              where fac.f_id = cour.f_id
              and fac.fname = 'Sulekha'
              order by cname desc
       [1/2 mark for select and from ]
       [1/2 mark for join condition]
       [1/2 mark for checking fname =”Sulekha”]
       [1/2 mark for order by]



   v) Select COUNT(DISTINCT F_ID) from COURSES;
      Ans: 4

       [1/2 mark for the correct answer]
   vi) Select MIN(Salary) from FACULTY,COURSES where COURSES.F_ID =
       FACULTY.F_ID;
       Ans: 6000


       [1/2 mark for the correct answer]

6.a. State and Verify Absorption law algebraically   2

Ans: Absorption law states that:
      A + AB = A and A . (A + B) = A
      Algebraic method:
      Taking LHS
      A + AB = (A.1) + (A.B) by Identity
      = A. (1+B) by Distribution
      = A.1 by Null Element
      =A

[1 mark for the statement]

[1 mark for proving it algebraically]
```

---

## page 30

```
b. Draw a logic circuit for the following Boolean expression: ab+c.d’.           2




[1/2 mark for correct representation of each gate]

c. Write the SOP form of a Boolean function F, which is represented in a truth

table as follows:                                                                1



                A B C        F

                0   0   0    0

                0   0   1    1

                0   1   0    1

                0   1   1    0

                1   0   0    1

                1   0   1    1

                1   1   0    0

                1   1   1    0

Ans: A’B’C+A’BC’+AB’C’+AB’C

[1 mark for all the terms]

d. Obtain a simplified from for a Boolean expression:                            3
F (U, V, W, Z) = II (0, 1, 3, 5, 6, 7, 15)
```

---

## page 31

```
            w+z                w+z’                  w’+z’               w’+z



 u+v




u+v’




u’+v’



u’+v




        (u+v+w).(u+z’).(v’+w’).(u’+w’+z)

        [1mark for correct K- Map representation]
        [1/2 mark for 2 correct group, 1 for all 4 groups]
        [1 mark for correct answer, ½ mark for two correct terms]


        7.a. Write any 1 advantage and 1 disadvantage of Bus topology.          1


        Ans: Advantage: Since there is a single common data path connecting all the nodes, the bus
        topology uses a very short cable length which considerably reduces the installation cost.
        Disadvantage: Fault detection and isolation is difficult. This is because control of the network is
        not centralized in any particular node. If a node is faulty on the bus, detection of fault may have to
        be performed at many points on the network. The faulty node has then to be rectified at that
        connection point.

        [1/2 mark each foradvantage and disadvantage]

        b. SunRise Pvt. Ltd. is setting up the network in the Ahmadabad. There are four departments
        named as    MrktDept, FunDept, LegalDept, SalesDept.
                                                      4

                                                             Fun Dept
                  MrktDept
```

---

## page 32

```
             Legal Dept                           SalesDept




Distance between various buildings is as given:

 MrktDept to FunDept                 80 m

 MrktDept to LegalDept               180m

 MrktDept to SalesDept               100 m

 LegalDept to SalesDept              150 m

 LegalDept to FunDept                100 m

 FunDept to SalesDept                50 m

                Number of Computers in the buildings:

 MrktDept                            20

 LegalDept                           10

 FunDept                             08

 SalesDept                           42
```

---

## page 33

```
i) Suggest a cable layout of connections between the Departments and specify topology.


                                                               FunDept




                                                                Sales Dept
    fs MrktDept




                                                                   LegalDept




    Star Topology should be used.
    [1/2 mark for cable layout]
    [1/2 mark for topology]
ii) Suggest the most suitable building to place the server a suitable reason with a suitable
    reason.
    Ans: As per 80 – 20 rule, MrktDept beacause it has maximium no. of computers.
    [1 mark for the correct Answer]



iii) Suggest the placement of i) modem ii) Hub /Switch in the network.
     Ans: Each building should have hub/switch and Modem in case Internet connection is
     required.
     [1 mark for the correct Answer]
```

---

## page 34

```
     iv)                                             The organization is planning to link its sale
           counter situated in various part of the same city/ which type of network out of LAN,
           WAN, MAN will be formed? Justify.

     Ans : MAN (Metropolitan Area Network)

           [1 mark for the correct Answer]



c.Name the protocol                                                                             1

           i. Used to transfer voice using packet switched network.

           Ans: VOIP (Voice Over Internet Protocol)

           [1 mark for the correct Answer]

           ii.Used for chatting between 2 groups or between 2 individuals.
           Ans: IRC(Internet Relay Chat)

           [1 mark for the correct Answer]

d. What is an IP Address?
An IP address is a unique identifier for a node or host connection on an IP network. An IP address is
a 32 bit binary number usually represented as 4 decimal values, each representing 8 bits, in the
range 0 to 255 (known as octets) separated by decimal points. This is known as "dotted decimal"
notation.
Example:140.179.220.200
                                                                                      1

[1 mark for correct definition]

or

[1 mark for example with explanation]

or

[1/2 mark for only writing a correct IP address]

e. What is HTTP?                                                                                1

Solution: HTTP is a protocol that is used for transferring hypertext(i.e.
text,graphic,image,sound,video,etc,)between 2 computers and is particularly used on the Worldd
Wide Web (WWW).

[1 mark for definition/explanation]
```

---

## page 35

```
f. Explain the importance of Cookies.                                                           1

Ans : When the user browses a website, the web server sends a text file to the web browser. This
small text file is a cookie. They are usually used to track the pages that we visit so that information
can be customised for us for that visit.

[1/2 mark for definition]
[1/2 mark for its usage]


g. How is 4G different from 3G?                                                                 1

Ans: 3G technology adds multimedia facilities such as video,audio and graphics applications
whereas 4G will provide better than TV quality images and video-links.

[1 mark for difference]
```