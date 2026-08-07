---
title: "Computer Science SQP (2015-16) Set 2"
source_pdf: "Computer_Science_SQP_(2015-16)_Set_2.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2015_16/Computer Science SQP/Computer Science SQP (2015-16) Set 2.pdf"
pages: 14
pdf_bytes: 67013
pdf_sha256: "70507a22e5a1292d152cd07f858e08f618d938bb64717572f425f9e60e70683d"
text_chars: 22550
low_text_pages: 0
converter: "pdftotext -layout"
---

# Computer Science SQP (2015-16) Set 2


---

## page 1

```
                                Sample Question Paper – Set II
                                    Computer Science (083)
                                      Class- XII (2015-16)
Time: 3hrs                                                                     M.M: 70
Instructions:
  i.     All Questions are Compulsory.
 ii.     Programming Language: Section A : C++
iii.     Programming Language: Section B: Python
 iv.     Answer either Section A or B, and Section C is compulsory
                                            Section : A (C++)
Q1 a. Define Macro with suitable example.                                              2

   b. Which C++ header file (s) will be included to run /execute the following C++ code? 1
                   void main( )
                   {        int Last =26.5698742658;
                            cout<<setw(5)<<setprecision(9)<<Last;          }


   c. Rewrite the following program after removing any syntactical errors. Underline each
      correction made.                                                             2
         #include<iostream.h>
         void main( )
                int A[10];
                A=[3,2,5,4,7,9,10];
                        for( p = 0; p<=6; p++)
                                {      if(A[p]%2=0)
                                       int S = S+A[p];     }
                                cout<<S;         }
       d. Find the output of the following C++ program:                                2
         #include<iostream.h>
         void repch(char s[])

                                                     1
```

---

## page 2

```
           {
               for (int i=0;s[i]!='\0';i++)
                {
                        if(((i%2)!=0) &&(s[i]!=s[i+1]))
                        {
                                s[i]='@';
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
e. Find the output of the following :                         3
        #include<iostream.h>
               void switchover(int A[ ],int N, int split)
                        {
                               for(int K = 0; K<N; K++)
                                       if(K<split)
                                               A[K] += K;
                                       else
                                               A[K]*= K;
                        }

                                                          2
```

---

## page 3

```
                    void display(int A[ ] ,int N)
                       {
                         for(int K = 0; K<N; K++)
                               (K%2== 0) ?cout<<A[K]<<"%" : cout<<A[K]<<endl;
                       }
                 void main( )
                                       {        int H[ ] = {30,40,50,20,10,5};
                                                switchover(H,6,3);
                                                display(H,6);
                                       }

f. Observe the following C++ code and find out , which out of the given options i) to iv) are the
expected correct output.Also assign the maximum and minimum value that can be assigned to
the variable ‘Go’.                                                        2
               void main()
                   { int X [4] ={100,75,10,125};
int Go = random(2)+2;
                      for (inti = Go; i< 4; i++)
cout<<X[i]<<”$$”;

                   }

   i. 100$$75           ii. 75$$10$$125$$     iii. 75$$10$$ iv.10$$125$

Q2a. Differentiate between data abstraction and data hiding.          2


 b. Answer the questions (i) and (ii) after going through the following class :            2
      class Exam
      {
             int Rollno;
             char Cname[25];
            float Marks ;
          public :
             Exam( )           //Function 1
             {
                       Rollno = 0 ;
                       Cname=””;
                       Marks=0.0;

                                                 3
```

---

## page 4

```
             }
             Exam(int Rno, char candname)           //Function 2
             {
                    Rollno = Rno ;
                    strcpy(Cname,candname);


             }
             ~Exam( )                                 //Function 3
             {
                    cout << “Result will be intimated shortly” << endl ;
             }
             void Display( )                                           //Function 4
             {
                    cout << “Roll no :”<<Rollno;
                     cout<<”Name :” <<Cname;
                     cout <<” Marks:”<<Marks;
             }
             };
(i)Which OOP concept does Function 1 and Function 2 implement.Explain?
(ii)What is Function 3 called? When will it be invoked?
c. Define a class Candidate in C++ with the following specification :         4
Private Members :
                A data members Rno(Registration Number) type long
                A data member Cname of type string
                A data members Agg_marks (Aggregate Marks) of type float
                A data members Grade of type char
                A member function setGrade () to find the grade as per the aggregate marks
obtained by the student. Equivalent aggregate marks range and the respective grade as shown
below.
                Aggregate Marks             Grade
                >=80                        A
                Less than 80 and >=65       B

                                                4
```

---

## page 5

```
               Less than 65 and >=50          C
               Less than 50                   D
Public members:
      A     constructor       to     assign     default     values       to     data    members:
Rno=0,Cname=”N.A”,Agg_marks=0.0
        A function Getdata () to allow users to enter values for Rno. Cname, Agg_marks and call
function setGrade () to find the grade.
        A function dispResult( ) to allow user to view the content of all the data members.

d. Give the following class definition answer the question that is follow:       4
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
                       {      int regno;
                              protected
                              char principal()
                       public :
                              int no_of_students;
                              void readdata();
                              void dispdata ( );
                       };
               class Department : public College
                              char name[20];

                                                   5
```

---

## page 6

```
                                 char HOD[20];
                       public :
                                 void fetchdata(int);
                                 void displaydata( );    }
i). Name the base class and derived class of college.                               1
ii) Name the data member(s) that can be accessed from function displaydata().
iii)What type of inheritance is depicted in the above class definition?
iv) What will be the size of an object (in bytes) of class Department?
Qs. 3a. An integer array A [30][40] is stored along the column in the memory. If the element
A[20][25] is stored at 50000, find out the location of A[25][30].                    3
 b. Write the definition of functions for the linked implemented queue containing passenger
informationas follows:                                                              4
       struct NODE
               {       int Ticketno;
                       char PName[20];
                       NODE * NEXT;             };
       class Queueofbus
               {       NODE *Rear, *Front;
                       public:
                                 Queueofbus()
                       {         Rear = NULL;
                       Front = NULL;                     };
               void Insert();
               void Delete();
               ~Queueofbus()
               {                 cout<<"Object destroyed";    }
};



                                                     6
```

---

## page 7

```
c. Write a function to sort any array of n elements using insertion sort . Array should be passed
as argument to the function.                                                       3
d. Write a function NewMAT(int A[][],int r,int c ) in C++, which accepts a 2d array of integer and
its size as parameters divide all those array elements by 6 which are not in the range 60 to
600(both values inclusive) in the 2d Array . 2
e.Evaluate the following postfix expression using stack and show the contents after execution of
each Operations:470,5,4,^,25,/,6,*                                       2
Q4a.Consider a file F containing objects E of class Emp.                             1
        i)Write statement to position the file pointer to the end of the file
       ii)Write statement to return the number of bytes from the beginning of the file to the
       current position of the file pointer.
b. Write a function RevText() to read a text file “ Input.txt “ and Print only word starting with ‘I’
in reverse order .                                                                   2
       Example: If value in text file is: INDIA IS MY COUNTRY
       Output will be: AIDNI SI MY COUNTRY
c. Write a function in C++ to search and display details, whose destination is “Chandigarh”from
      binary file “Flight.Dat”. Assuming the binary file is containing the objects of the
      following class:                                                            3
       class FLIGHT
       {         int Fno;              //      Flight Number
                 char From[20];        //      Flight Starting Point
                 char To[20];          //      Flight Destination
       public:
                 char * GetFrom ( );   {       return from;    }
                 char * GetTo( );      {       return To;      }
                 void input()          {       cin>>Fno>>; gets(From); get(To);      }
                 void show( )          {       cout<<Fno<< “:”<<From << “:” <<To<<endl; }
       };
Section : B (Python)
Q1. a. List one similarity and one difference between List and Dictionary datatype           2


                                                  7
```

---

## page 8

```
b. Observe the following Python functions and write the name(s) of the module(s) to which they
belong:                                                                 1
        a. uniform() b. findall()
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
               if x % 2 = = 0 :
                  print x,”is even”
               elif x<0 :
                   print x,”should be positive”
               else :
                   print x,”is odd”


d. Find the output of the following Python program:                                     3
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

                                                8
```

---

## page 9

```
                        count +=1
                  newstr = newstr+mystr[:1]
                  print "The new string is :",newstr
 makenew(“sTUdeNT")
e. Find the output of the following program                                          2
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
f. Observe the following Python code and find out , which out of the given options i) to iv) are
the expected correct output(s).Also assign the maximum and minimum value that can be
assigned to the variable ‘Go’.                                             2
               import random
               X =[100,75,10,125]
               Go = random.randint(0,3)
               for i in range(Go):
                  print X[i],"$$",
   i. 100$$75$$10 ii. 75$$10$$125$$iii. 75$$10$$             iv.10$$125$$100


Q2 a. Discuss the strategies employed by python for memory allocation?                     2
b. Answer the questions (i) and (ii) after going through the following class definition:       2
       class Toy :
              tid =0;
              tcat = “ “
               def __init__(self):// Function1


                                                 9
```

---

## page 10

```
       ..................................... // Blank 2
       i. Explain relevance of Function 1.
       ii. a. Fill in the blank2 with a statement to create object of the class TOY.
            b. Write statement to check whether tprice is an attribute of class TOY.

c. Define a class Train in PYTHON with following description:               4
   Data Members

       src of type string
       Tnm of type string
       dest of type string
       charges of float

• A member function Getdata to assign the following values for Charges
       Dest                 Charges
       Mumbai                 1000
       Chennai                 2000
       Kolkatta                2500
Public members
    • A constructor to initialize the data members.
    • A function InputData() to allow the user to enter the values
    • A function displaydata() to display all and call getdata function

d. Observe the following class definition and answer the question that follow:         2
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
        b. What type of inheritance is being demonstrated in the above code?

e. Write a user defined function findname(name) where name is an argument in Python to delete
     phone number from a dictionary phonebook on the basis of the name ,where name is the
     key.                                                             2



                                                10
```

---

## page 11

```
Qs. 3a.Explain try..except…else … with the help of user defined function def divide(x, y)which
raises an error when the denominator is zero while dividing x by y and displays the quotient
otherwise.                                                                              3
b. Write a user defined function arrangelements(X), that accepts a list X of integers and sets all
the negative elements to the left and all positive elements to the right of the list.
Eg: if L =[1,-2,3,4,-5,7] , the output should be: [-2,-5,3,4,7]                   3
c. Consider the following class definition :-                                     3
       class book ():
               bk = []
               def _ init _ (self, bno):
                         self .bno = bno
               def addbook (self):
                         ……………
               def removebook (self):
                         ……………
The class book is implemented using Queue. Keeping the same in mind, complete the function
definitions for adding a book addbook() and deleting a book removebook() .
d. Write a python function generatefibo(n) where n is the limit using a generator function
Fibonacci (max) where max is the limit n that produces Fibonacci series..     3


e. Evaluate the following postfix using stack & show the content of the stack after the execution
of each: 20, 4, +, 3, -, 7, 1                              2


Q4a. Consider the following code :                                         1
       f = open ("mytry", "w+")
       f.write ("0123456789abcdef")
       f.seek (-3,2)     //1
       printf.read(2) //2

Explain statement 1 and give output of 2
b. Write a user defined function in Python that displays the number of lines starting with ‘H’ in
the file Para.txt.Eg: if the file contains:                                               2

                                                  11
```

---

## page 12

```
Whose woods these are I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

Then the line count should be 2.
c. Consider a binary file Employee.dat containing details such as empno:ename:salary (separator
‘ :’). Write a python function to display details of those employees who are earning between
20000 and 40000.(both values inclusive)                                  3

                                          Section : C
Q 5. a. Differentiate between cardinality and degree of a table with the help of an example. 2
b) Consider the following tables FACULTY and COURSES. Write SQL commands for the
statements (i) to (v) and give outputs for SQL queries (vi) to (vii)     6
                                            FACULTY
F_ID        Fname              Lname             Hire_date          Salary
102         Amit               Mishra            12-10-1998         12000
103         Nitin              Vyas              24-12-1994         8000
104         Rakshit            Soni              18-5-2001          14000
105         Rashmi             Malhotra          11-9-2004          11000
106         Sulekha            Srivastava        5-6-2006           10000
                                            COURSES
C_ID       F_ID             Cname                    Fees
C21        102              Grid Computing           40000
C22        106              System Design            16000
C23        104              Computer Security        8000
C24        106              Human Biology            15000
C25        102              Computer Network         20000
C26        105              Visual Basic             6000
    i) To display details of those Faculties whose salary is greater than 12000.
    ii) To display the details of courses whose fees is in the range of 15000 to 50000 (both
         values included).
    iii) To increase the fees of all courses by 500 of “System Design” Course.
    iv) To display details of those courses which are taught by ‘Sulekha’ in descending order of
         courses.
    v) Select COUNT(DISTINCT F_ID) from COURSES;
    vi) Select MIN(Salary) from FACULTY,COURSES where COURSES.F_ID =
         FACULTY.F_ID;
Q6.a. State and Verify Absorption law algebraically.                                     2
  b. Draw a logic circuit for the following Boolean expression: A.B+C.D’.                2




                                               12
```

---

## page 13

```
 c. Write the SOP form of a Boolean function F, which is represented in a truth table as follows:
                                                                                             1
               A B C          F
               0   0   0      0
               0   0   1     1
               0   1   0     1
               0   1   1     0
               1   0   0     1


               1   0   1     1
               1   1   0     0
               1   1   1     0
d. Obtain a simplified from for a Boolean expression:                                       3
       F (U, V, W, Z) = II (0, 1, 3, 5, 6, 7, 15)

Q 7.a Write any 1 advantage and 1 disadvantage of Bus topology.                             1

    b. SunRise Pvt. Ltd. is setting up the network in the Ahmadabad. There are four departments
       named as     MrktDept, FunDept, LegalDept, SalesDept.                            4


                                                                   SalesDept
      MrktDept



                           Legal Dept           Fun Dept




                                                13
```

---

## page 14

```
Distance between various buildings is given as follows:

MrktDept to FunDept                     80 m

MrktDept to LegalDept                   180m

MrktDept to SalesDept                   100 m

LegalDept to SalesDept                  150 m

LegalDept to FunDept                    100 m

FunDept to SalesDept                    50 m

Number of Computers in the buildings:

MrktDept                                20

LegalDept                               10

FunDept                                 08

SalesDept                               42



   i) Suggest a cable layout of connections between the Departments and specify topology.
   ii) Suggest the most suitable building to place the server with a suitable reason.
   iii) Suggest the placement of i) modem ii) Hub /Switch in the network.
   iv)                                         The organization is planning to link its sale
        counter situated in various part of the same city/ which type of network out of LAN,
        WAN, MAN will be formed? Justify.
 c. Name the protocol                                                               1
       i. Used to transfer voice using packet switched network.
       ii.Used for chatting between 2 groups or between 2 individuals.
d. What is an IP Address?                                                           1
e. What is HTTP?                                                                    1
f. Explain the importance of Cookies.                                               1
g. How is 4G different from 3G?                                                     1




                                                14
```