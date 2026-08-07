---
title: "ComputerScience-MS"
source_pdf: "ComputerScience-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/ComputerScience-MS.pdf"
pages: 7
pdf_bytes: 235478
pdf_sha256: "f1c7a482c74424a18d2c8ad1c60fc8d7b9bb6441e383708405016950642373ce"
text_chars: 13634
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-MS


---

## page 1

```
                                         Sample Question Paper - 2021
                                             Computer Science – 083
                                               MARKING SCHEME
       Maximum Marks: 70                                                Time Allowed: 3 hours
                                                    Part – A
                                                   Section - I
1    b) True                                                                                      1
2    [6,82,5]                                                                                     1
3    Comma Separated Value                                                                        1
4    c) **                                                                                        1
5    b) T[2]= -29 (as tuple is immutable)                                                         1
6    Day={1:'monday',2:'tuesday',3:'wednesday'}                                                   1
7    30
8    abs()                                                                                        1
9    SMTP                                                                                         1
10 Cyber Stalking                                                                                 1
11 ORDER BY                                                                                       1
12 To check if the column has null value / no value                                               1
13 SUM / AVG / COUNT / MAX / MIN                                                                  1
14 b) ALTER                                                                                       1
15 Microwave / Radio wave                                                                         1
16 d. List                                                                                        1
17 puterSc                                                                                        1
18 SHOW TABLES                                                                                    1
19 Wireless Fidelity                                                                              1
20 (c) Primary Key                                                                                1
21 Bps, Kbps, Mbps, Gbps, Tbps                                                                    1
                                                    Part – A
                                                   Section - II
22        (a) ItemNo                                                                              1
          (b) Degree =       4   Cardinality = 7                                                  1
          (c) INSERT INTO store (ItemNo,ItemName,Scode) VALUES(2010, “Note Book”,25);             1
          (d) DROP TABLE store;                                                                   1
          (e) Describe Store;                                                                     1
23        (a) Line 1 : csv                                                                        1
          (b) Line 2 : a                                                                          1
          (c) Line 3 : reader                                                                     1
          (d) Line 4 : close()                                                                    1

                                                                                    Page 1 of 7
```

---

## page 2

```
        (e) Line 5 : Arjun 123@456                                                                         1
                      Arunima aru@nima
                      Frieda myname@FRD


                                                 Part – B
24      a) 13                                                                                              2
        b) False
25 Viruses require an active host program or an already-infected and active operating system in            2
     order for viruses to run, cause damage and infect other executable files or documents
     Worms are stand-alone malicious programs that can self-replicate.
                                                    OR
     Web Browser : A web browser is a software application for accessing information on the
     World Wide Web. When a user requests a web page from a particular website, the web
     browser retrieves the necessary content from a web server and then displays the page on the
     user's device.
     Web Server : A web server is a computer that runs websites. The basic objective of the web
     server is to store, process and deliver web pages to the users. This intercommunication is
     done using Hypertext Transfer Protocol (HTTP).
     Popular web browsers : Google Chrome, Mozilla Firefox, Internet Explorer etc


26               a. SMTP - Simple Mail Transfer Protocol                                                   2
                 b. XML - eXtensible Markup Language
                 c. LAN – Local Area Network
                 d. IPR – Intellectual Property Rights
27 The list of identifiers used in a function call is called actual parameter(s) whereas the list of       2
     parameters used in the function definition is called formal parameter(s).


     Actual parameter may be value / variable or expression.
     Formal parameter is an identifier.


     Example:
     def area(side):             # line 1
        return side*side;


     print(area(5))              # line 2


     In line 1, side is the formal parameter and in line 2, while invoking area() function, the value 5
     is the actual parameter.


                                                                                             Page 2 of 7
```

---

## page 3

```
    A formal parameter, i.e. a parameter, is in the function definition. An actual parameter, i.e. an
    argument, is in a function call.
                                                   OR
    Use of global key word:
    In Python, global keyword allows the programmer to modify the variable outside the current
    scope. It is used to create a global variable and make changes to the variable in local
    context. A variable declared inside a function is by default local and a variable declared
    outside the function is global by default. The keyword global is written inside the function to
    use its global value. Outside the function, global keyword has no effect.
    Example
    c = 10 # global variable
    def add():
       global c
       c=c+2        # global value of c is incremented by 2
       print("Inside add():", c)


    add()
    c=15
    print("In main:", c)


    output:
    Inside add() : 12
    In main: 15
28 CORRECTED CODE:                                                                                        2
            Value=30
            for VAL in range(0,Value) :                  # Error 1
               if val%4==0:                              # Error 2
                  print (VAL*4)
               elif val%5==0:                                 # Error 3
                  print (VAL+3)
               else:                                          # Error 4
                  print(VAL+10)


29 OUTPUT: (ii)                                                                                           2
    Maximum value of Lower: 3
    Maximum value of Upper: 4
30 A table may have more than one such attribute/group of attributes that identifies a tuple              2
   uniquely, all such attribute(s) are known as Candidate Keys.


                                                                                            Page 3 of 7
```

---

## page 4

```
       Table:Item
          Ino      Item               Qty
          I01      Pen               500
          I02      Pencil            700
          I04      CD                500
          I09                        700
          I05      Eraser            300
          I03      Duster            200
     In the above table Item, ItemNo can be a candidate key
31 fetchall() fetches all the rows of a query result. An empty list is returned if there is no record      2
     to fetch the cursor.
     fetchone() method returns one row or a single record at a time. It will return None if no more
     rows / records are available.
     Any example.


32 DDL – Data Definition Language                                                                          2
     DML – Data Manipulation Language
     Any two out of INSERT, DELETE, UPDATE
33 OUTPUT : fUNnpYTHON                                                                                     2
34 def LShift(Arr,n):                                                                                      3
       L=len(Arr)
       for x in range(0,n):
          y=Arr[0]
          for i in range(0,L-1):
             Arr[i]=Arr[i+1]
          Arr[L-1]=y
       print(Arr)
     Note : Using of any correct code giving the same result is also accepted.


35                  def displayMeMy():                                                                     3
                      num=0
                      f=open("story.txt","rt")
                      N=f.read()
                      M=N.split()
                      for x in M:
                        if x=="Me" or x== "My":
                          print(x)
                          num=num+1
                      f.close()
                      print("Count of Me/My in file:",num)


                                                                                             Page 4 of 7
```

---

## page 5

```
                                                          OR
                      def count_A_M():
                        f=open("story.txt","r")
                        A,M=0,0
                        r=f.read()
                        for x in r:
                            if x[0]=="A" or x[0]=="a" :
                              A=A+1
                            elif x[0]=="M" or x[0]=="m":
                              M=M+1
                        f.close()
                        print("A or a: ",A)
                        print("M or m: ",M)
    Note : Using of any correct code giving the same result is also accepted.


36 OUTPUT:                                                                                               3
       i.
                   Department          Count(*)
                   History             3
                   Computer Sc         2
                   Mathematics         3

       ii.        Max - 31/07/2018 or 2018-07-31           Min- 05/09/2007 or 2007-09-05
       iii.
                   name               Department      Place
                    Jugal             Computer Sc     Delhi
                    Shiv Om           Computer Sc     Delhi


37 ANSWER: (Using of any correct code giving the same result is also accepted.)                          3

    def PUSH(Arr,value):
      s=[]
      for x in range(0,len(Arr)):
            if Arr[x]%5==0:
              s.append(Arr[x])
      if len(s)==0:


                                                                                           Page 5 of 7
```

---

## page 6

```
             print("Empty Stack")
       else:
             print(s)


                                                   OR


     def popStack(st) :
       # If stack is empty
       if len(st)==0:
             print("Underflow")
       else:
             L = len(st)
             val=st[L-1]
             print(val)
             st.pop(L-1)


38             a. Most suitable place to install the server is HR center, as this center has maximum     5
                    number of computers.
               b.




               c. Switch
               d. Repeater may be placed when the distance between 2 buildings is more than 70
                    meter.
               e. WAN, as the given distance is more than the range of LAN and MAN.




39      i.          SELECT * FROM teacher WHERE department= “History”;                                   5
        ii.         SELECT name FROM teacher WHERE department= “Mathematics” AND
                    gender= “F”;
        iii.        SELECT name FROM teacher ORDER BY date_of_join;
        iv.         SELECT name, salary, age FROM teacher WHERE gender=’M’;
        v.          SELECT name, salary*0.1 AS Bonus FROM teacher;


                                                                                           Page 6 of 7
```

---

## page 7

```
40 ANSWER: (Using of any correct code giving the same result is also accepted.)                 5

    import pickle
    def createFile():
      fobj=open("Book.dat","ab")
      BookNo=int(input("Book Number : "))
      Book_name=input("Name :")
      Author = input(“Author: “)
      Price = int(input("Price : "))
      rec=[BookNo,Book_Name,Author,Price]
      pickle.dump(rec,fobj)
      fobj.close()

     def CountRec(Author):
       fobj=open("Book.dat","rb")
       num = 0
       try:
          while True:
              rec=pickle.load(fobj)
              if Author==rec[2]:
                 num = num + 1
       except:
          fobj.close()
       return num

                                                        OR

     import pickle
     def CountRec():
       fobj=open("STUDENT.DAT","rb")
       num = 0
       try:
          while True:
              rec=pickle.load(fobj)
              if rec[2] > 75:
                 print(rec[0],rec[1],rec[2],sep="\t")
                 num = num + 1
       except:
          fobj.close()
       return num


                                                                                  Page 7 of 7
```