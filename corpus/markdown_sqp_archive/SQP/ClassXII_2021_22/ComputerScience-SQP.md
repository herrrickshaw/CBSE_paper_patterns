---
title: "ComputerScience-SQP"
source_pdf: "ComputerScience-SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/ComputerScience-SQP.pdf"
pages: 13
pdf_bytes: 271759
pdf_sha256: "6b648a8e02e71793c2b60dc58c55ca6905a27b7d2c46b333735db33b5a467d83"
text_chars: 21651
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-SQP


---

## page 1

```
                                     Sample Question Paper
                                    Class: XII Session: 2021-22
                                   Computer Science (Code 083)
                                         (Theory: Term-1)
Maximum Marks: 35                                                      Time Allowed: 90 Minutes

General Instructions:

   The question paper is divided into 3 Sections - A, B and C.
   Section A, consist of 25 Questions (1-25). Attempt any 20 questions.
   Section B, consist of 24 Questions (26-49). Attempt any 20 questions.
   Section C, consist of 6 case study based Questions (50-55). Attempt any 5 questions.
   All questions carry equal marks.
  Q.N.                                      Section-A

         This section consists of 25 Questions (1 to 25). Attempt any 20 questions from this
         section. Choose the best possible option.

  1      Find the invalid identifier from the following
                a. none
                b. address
                c. Name
                d. pass
  2      Consider a declaration L = (1, 'Python', '3.14').
         Which of the following represents the data type of L?
                a. list
                b. tuple
                c. dictionary
                d. string
  3      Given a Tuple tup1= (10, 20, 30, 40, 50, 60, 70, 80, 90).
         What will be the output of print (tup1 [3:7:2])?
                a. (40,50,60,70,80)
                b. (40,50,60,70)
                c. [40,60]
                d. (40,60)
  4      Which of the following option is not correct?
                a. if we try to read a text file that does not exist, an error occurs.
                b. if we try to read a text file that does not exist, the file gets created.
                c. if we try to write on a text file that does not exist, no error occurs.
                d. if we try to write on a text file that does not exist, the file gets
                    Created.
  5      Which of the following options can be used to read the first line of a text file Myfile.txt?
                a. myfile = open('Myfile.txt'); myfile.read()
                b. myfile = open('Myfile.txt','r'); myfile.read(n)
                c. myfile = open('Myfile.txt'); myfile.readline()
                d. myfile = open('Myfile.txt'); myfile.readlines()
```

---

## page 2

```
6    Assume that the position of the file pointer is at the beginning of 3rd line in a text file. Which
     of the following option can be used to read all the remaining lines?
             a. myfile.read()
             b. myfile.read(n)
             c. myfile.readline()
             d. myfile.readlines()
7    A text file student.txt is stored in the storage device. Identify the correct option out of the
     following options to open the file in read mode.
             i. myfile = open('student.txt','rb')
             ii. myfile = open('student.txt','w')
             iii. myfile = open('student.txt','r')
             iv. myfile = open('student.txt')

            a. only i
            b. both i and iv
            c. both iii and iv
            d. both i and iii
8    The return type of the input() function is
            a. string
            b. integer
            c. list
            d. tuple
9    Which of the following operator cannot be used with string data type?
            a. +
            b. in
            c. *
            d. /
10   Consider a tuple tup1 = (10, 15, 25, and 30). Identify the statement that will result in an
     error.
            a. print(tup1[2])
            b. tup1[2] = 20
            c. print(min(tup1))
            d. print(len(tup1))
11   Which of the following statement is incorrect in the context of binary files?
            a. Information is stored in the same format in which the information is held in
                 memory.
            b. No character translation takes place
            c. Every line ends with a new line character
            d. pickle module is used for reading and writing
12   What is the significance of the tell() method?
            a. tells the path of file
            b. tells the current position of the file pointer within the file
            c. tells the end position within the file
            d. checks the existence of a file at the desired location
```

---

## page 3

```
13   Which of the following statement is true?
           a. pickling creates an object from a sequence of bytes
           b. pickling is used for object serialization
           c. pickling is used for object deserialization
           d. pickling is used to manage all types of files in Python

14   Syntax of seek function in Python is myfile.seek(offset, reference_point) where myfile is
     the file object. What is the default value of reference_point?
             a. 0
             b. 1
             c. 2
             d. 3
15   Which of the following components are part of a function header in Python?
             a. Function Name
             b. Return Statement
             c. Parameter List
             d. Both a and c
16   Which of the following function header is correct?
             a. def cal_si(p=100, r, t=2)
             b. def cal_si(p=100, r=8, t)
             c. def cal_si(p, r=8, t)
             d. def cal_si(p, r=8, t=2)
17   Which of the following is the correct way to call a function?
             a. my_func()
             b. def my_func()
             c. return my_func
             d. call my_func()
18   Which of the following character acts as default delimiter in a csv file?
             a. (colon) :
             b. (hyphen) -
             c. (comma) ,
             d. (vertical line) |
19   Syntax for opening Student.csv file in write mode is
     myfile = open("Student.csv","w",newline='').

     What is the importance of newline=''?
           a. A newline gets added to the file
           b. Empty string gets appended to the first line.
           c. Empty string gets appended to all lines.
           d. EOL translation is suppressed
20   What is the correct expansion of CSV files?
           a. Comma Separable Values
           b. Comma Separated Values
           c. Comma Split Values
           d. Comma Separation Values
```

---

## page 4

```
21   Which of the following is not a function / method of csv module in Python?
            a. read()
            b. reader()
            c. writer()
            d. writerow()
22   Which one of the following is the default extension of a Python file?
            a. .exe
            b. .p++
            c. .py
            d. .p
23   Which of the following symbol is used in Python for single line comment?
            a. /
            b. /*
            c. //
            d. #
24   Which of the following statement opens a binary file record.bin in write mode and writes
     data from a list lst1 = [1,2,3,4] on the binary file?
            a. with open('record.bin','wb') as myfile:
                            pickle.dump(lst1,myfile)

           b. with open('record.bin','wb') as myfile:
                         pickle.dump(myfile,lst1)

           c. with open('record.bin','wb+') as myfile:
                         pickle.dump(myfile,lst1)

           d. with open('record.bin','ab') as myfile:
                         pickle.dump(myfile,lst1)
25   Which of these about a dictionary is false?
           a) The values of a dictionary can be accessed using keys
           b) The keys of a dictionary can be accessed using values
           c) Dictionaries aren’t ordered
           d) Dictionaries are mutable
                                              Section-B

     This section consists of 24 Questions (26 to 49). Attempt any 20 questions.
26   What is the output of following code:
                        T=(100)
                        print(T*2)
           a. Syntax error
           b. (200,)
           c. 200
           d. (100,100)
```

---

## page 5

```
27   Suppose content of 'Myfile.txt' is:

                                     Twinkle twinkle little star
                                     How I wonder what you are
                                     Up above the world so high
                                     Like a diamond in the sky

     What will be the output of the following code?
                          myfile = open("Myfile.txt")
                          data = myfile.readlines()
                          print(len(data))
                          myfile.close()
             a. 3
             b. 4
             c. 5
             d. 6
28   Identify the output of the following Python statements.
            x = [[10.0, 11.0, 12.0],[13.0, 14.0, 15.0]]
            y = x[1][2]
            print(y)
             a. 12.0
             b. 13.0
             c. 14.0
             d. 15.0
29   Identify the output of the following Python statements.
                 x = 2
                 while x < 9:
                     print(x, end='')
                     x = x + 1
            a. 12345678

            b. 123456789
            c. 2345678

            d. 23456789

30   Identify the output of the following Python statements.
                    b = 1
                    for a in range(1, 10, 2):
                          b += a + 2
                    print(b)
             a. 31
             b. 33
             c. 36
             d. 39
```

---

## page 6

```
31   Identify the output of the following Python statements.
                    lst1 = [10, 15, 20, 25, 30]
                    lst1.insert( 3, 4)
                    lst1.insert( 2, 3)
                    print (lst1[-5])
             a. 2
             b. 3
             c. 4
             d. 20
32   Raghav is trying to write a tuple tup1 = (1,2,3,4,5) on a binary file test.bin. Consider the
     following code written by him.
                  import pickle
                  tup1 = (1,2,3,4,5)
                  myfile = open("test.bin",'wb')
                  pickle._______ #Statement 1
                  myfile.close()
     Identify the missing code in Statement 1.
             a. dump(myfile,tup1)
             b. dump(tup1, myfile)
             c. write(tup1,myfile)
             d. load(myfile,tup1)
33   A binary file employee.dat has following data
                                     Empno empname          Salary
                                     101      Anuj          50000
                                     102      Arijita       40000
                                     103      Hanika        30000
                                     104      Firoz         60000
                                     105      Vijaylakshmi 40000

               def display(eno):
                   f=open("employee.dat","rb")
                   totSum=0
                   try:
                       while True:
                            R=pickle.load(f)
                            if R[0]==eno:
                                     __________      #Line1
                                     totSum=totSum+R[2]
                   except:
                       f.close()
                   print(totSum)

     When the above mentioned function, display (103) is executed, the output displayed is
     190000.
     Write appropriate jump statement from the following to obtain the above output.
```

---

## page 7

```
        a. jump
        b. break
        c. continue
        d. return
34   What will be the output of the following Python code?
                      def add (num1, num2):
                            sum = num1 + num2
                      sum = add(20,30)
                      print(sum)
           a. 50
           b. 0
           c. Null
           d. None
35   Evaluate the following expression and identify the correct answer.
         16 - (4 + 2) * 5 + 2**3 * 4
       a. 54
       b. 46
       c. 18
       d. 32
36   What will be the output of the following code?
                  def my_func(var1=100, var2=200):
                        var1+=10
                        var2 = var2 - 10
                        return var1+var2
                  print(my_func(50),my_func())
           a. 100 200
           b. 150 300
           c. 250 75
           d. 250 300
37   What will be the output of the following code?
                   value = 50
                   def display(N):
                          global value
                          value = 25
                          if N%7==0:
                               value = value + N
                          else:
                               value = value - N
                   print(value, end="#")
                   display(20)
                   print(value)
           a. 50#50
           b. 50#5
           c. 50#30
           d. 5#50#
```

---

## page 8

```
38   What will be the output of the following code?
                   import random
                   List=["Delhi","Mumbai","Chennai","Kolkata"]
                   for y in range(4):
                        x = random.randint(1,3)
                        print(List[x],end="#")
           a. Delhi#Mumbai#Chennai#Kolkata#
           b. Mumbai#Chennai#Kolkata#Mumbai#
           c. Mumbai# Mumbai #Mumbai # Delhi#
           d. Mumbai# Mumbai #Chennai # Mumbai
39   What is the output of the following code snippet?
                        def ChangeVal(M,N):
                              for i in range(N):
                                     if M[i]%5 == 0:
                                          M[i]//=5
                                     if M[i]%3 == 0:
                                          M[i]//=3
                        L = [25,8,75,12]
                        ChangeVal(L,4)
                        for i in L:
                              print(i,end="#")
               a) 5#8#15#4#
               b) 5#8#5#4#
               c) 5#8#15#14#
               d) 5#18#15#4#

40   Suppose content of 'Myfile.txt' is
                             Humpty Dumpty sat on a wall
                             Humpty Dumpty had a great fall
                             All the king's horses and all the king's men
                             Couldn't put Humpty together again
     What will be the output of the following code?
                      myfile = open("Myfile.txt")
                      record = myfile.read().split()
                      print(len(record))
                      myfile.close()
            a. 24
            b. 25
            c. 26
            d. 27
41   Find the output of the following code:
                          Name="PythoN3.1"
                          R=""
                          for x in range(len(Name)):
                                 if Name[x].isupper():
                                     R=R+Name[x].lower()
```

---

## page 9

```
                              elif Name[x].islower():
                                   R=R+Name[x].upper()
                              elif Name[x].isdigit():
                                   R=R+Name[x-1]
                              else:
                                   R=R+"#"
                          print(R)

            a. pYTHOn##@
            b. pYTHOnN#@
            c. pYTHOn#@
            d. pYTHOnN@#
42   Suppose content of 'Myfile.txt' is
                                     Honesty is the best policy.
     What will be the output of the following code?
              myfile = open("Myfile.txt")
              x = myfile.read()
              print(len(x))
              myfile.close()
            a. 5
            b. 25
            c. 26
            d. 27
43   Suppose content of 'Myfile.txt' is
      Culture is the widening of the mind and of the spirit.
     What will be the output of the following code?
                    myfile = open("Myfile.txt")
                    x = myfile.read()
                    y = x.count('the')
                    print(y)
                    myfile.close()
            a. 2
            b. 3
            c. 4
            d. 5
44   What will be the output of the following code?
                 x = 3
                 def myfunc():
                     global x
                     x+=2
                     print(x, end=' ')
                 print(x, end=' ')
                 myfunc()
                 print(x, end=' ')
```

---

## page 10

```
          a. 3 3 3
          b. 3 4 5
          c. 3 3 5
          d. 3 5 5
45   Suppose content of 'Myfile.txt' is
                                    Ek Bharat Shreshtha Bharat

     What will be the output of the following code?
                       myfile = open("Myfile.txt")
                       vlist = list("aeiouAEIOU")
                       vc=0
                       x = myfile.read()
                       for y in x:
                             if(y in vlist):
                                   vc+=1
                       print(vc)
                       myfile.close()
           a. 6
           b. 7
           c. 8
           d. 9
46   Suppose content of 'Myfile.txt' is

                                  Twinkle twinkle little star
                                  How I wonder what you are
                                  Up above the world so high
                                  Like a diamond in the sky
                                  Twinkle twinkle little star


     What will be the output of the following code?
                    myfile = open("Myfile.txt")
                    line_count = 0
                    data = myfile.readlines()
                    for line in data:
                         if line[0] == 'T':
                                 line_count += 1
                    print(line_count)
                    myfile.close()
           a. 2
           b. 3
           c. 4
           d. 5
```

---

## page 11

```
47   Consider the following directory structure.




     Suppose root directory (School) and present working directory are the same. What will
     be the absolute path of the file Syllabus.jpg?
            a. School/syllabus.jpg
            b. School/Academics/syllabus.jpg
            c. School/Academics/../syllabus.jpg
            d. School/Examination/syllabus.jpg

48   Assume the content of text file, 'student.txt' is:

                                             Arjun Kumar
                                             Ismail Khan
                                             Joseph B
                                             Hanika Kiran

     What will be the data type of data_rec?
                     myfile = open("Myfile.txt")
                     data_rec = myfile.readlines()
                     myfile.close()
           a. string
           b. list
           c. tuple
           d. dictionary

49   What will be the output of the following code?
                tup1 = (1,2,[1,2],3)
                tup1[2][1]=3.14
                print(tup1)
           a. (1,2,[3.14,2],3)
           b. (1,2,[1,3.14],3)
           c. (1,2,[1,2],3.14)
           d. Error Message
```

---

## page 12

```
                                           Section-C
                                 Case Study based Questions
             This section consists of 6 Questions (50 -55) Attempt any 5 questions.

     Rohit, a student of class 12, is learning CSV File Module in Python. During examination,
     he has been assigned an incomplete python code (shown below) to create a CSV File
     'Student.csv' (content shown below). Help him in completing the code which creates the
     desired CSV File.

                                               CSV File
                                               1,AKSHAY,XII,A
                                               2,ABHISHEK,XII,A
                                               3,ARVIND,XII,A
                                               4,RAVI,XII,A
                                               5,ASHISH,XII,A

     Incomplete Code
     import _____                                                 #Statement-1
     fh = open(_____, _____, newline='')                          #Statement-2
     stuwriter = csv._____                                        #Statement-3
     data = [ ]
     header = ['ROLL_NO', 'NAME', 'CLASS', 'SECTION']
     data.append(header)
     for i in range(5):
               roll_no = int(input("Enter Roll Number : "))
               name = input("Enter Name : ")
               Class = input("Enter Class : ")
               section = input("Enter Section : ")
               rec = [ _____ ]                                #Statement-4
               data.append(_____)                             #Statement-5
     stuwriter. _____ (data)                                  #Statement-6
     fh.close()
50   Identify the suitable code for blank space in the line marked as Statement-1.
             a) csv file
             b) CSV
             c) csv
             d) cvs
51   Identify the missing code for blank space in line marked as Statement-2.
          a) "Student.csv","wb"
          b) "Student.csv","w"
          c) "Student.csv","r"
          d) "Student.cvs","r"
52   Choose the function name (with argument) that should be used in the blank space of line
     marked as Statement-3.
             a) reader(fh)
             b) reader(MyFile)
             c) writer(fh)
             d) writer(MyFile)
```

---

## page 13

```
53   Identify the suitable code for blank space in line marked as Statement-4.
           a) 'ROLL_NO', 'NAME', 'CLASS', 'SECTION'
           b) ROLL_NO, NAME, CLASS, SECTION
           c) 'roll_no','name','Class','section'
           d) roll_no,name,Class,section

54   Identify the suitable code for blank space in the line marked as Statement-5.
           a) data
           b) record
           c) rec
           d) insert

55   Choose the function name that should be used in the blank space of line marked as
     Statement-6 to create the desired CSV File?
           a) dump()
           b) load()
           c) writerows()
           d) writerow()
```