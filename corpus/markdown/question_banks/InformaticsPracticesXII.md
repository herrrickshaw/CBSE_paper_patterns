---
title: "InformaticsPracticesXII"
source_pdf: "InformaticsPracticesXII.pdf"
source_url: "https://cbseacademic.nic.in/web_material/QuestionBank/ClassXII/InformaticsPracticesXII.pdf"
pages: 39
pdf_bytes: 623718
pdf_sha256: "c2a40fcf6c08f8fb51adc0c16858494443fbe7ba2985f00d4d78e40e977231e4"
text_chars: 47636
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPracticesXII


---

## page 1

```
                                             INFORMATICS PRACTICES (065)
                                         CASE STUDY BASED QUESTIONS


      Q.1. Mr. Ankit is working in an organisation as data analyst. He uses Python Pandas and Matplotlib for the
      same. He got a dataset of the passengers for the year 2010 to 2012 for January, March and December. His
      manager wants certain information from him, but he is facing some problems. Help him by answering few
      questions given below:




      Code to create the above data frame:
         import pandas as ____________      #Statement 1
         data={"Year":[2010,2010,2012,2010,2012],"Month":["Jan","Mar","Jan","Dec","Dec"]
         ,"Passengers":[25,50,35,55,65]}
         df=pd.____________________(data)         #Statement 2
         print(df)

 i.      Choose the right code from the following for statement 1.
         i.    pd
         ii.   df
         iii.  data
         iv.   p

               Answer: (i) pd
ii.      Choose the right code from the following for the statement 2.
         i.    Dataframe
         ii.   DataFrame
         iii.  Series
```

---

## page 2

```
        iv.      Dictionary
              Answer: (ii) DataFrame
iii.    Choose the correct statement/ method for the required output:
           (5,3)

                 i.   df.index
                 ii. df.shape()
                 iii. df.shape
                 iv.  df.size

               Answer: (iii) df.shape

iv.     He wants to print the details of "January" month along with the number of passengers, Identify the correct
        statement:




              i.     df.loc[['Month','Passengers']][df['Month']=='Jan']
              ii.    df[['Month','Passengers']][df['Month']=='Jan']
              iii.   df.iloc[['Month','Passengers']][df['Month']=='Jan']
              iv.    df(['Month','Passengers']][df['Month']=='Jan')

      Answer: (ii) df[['Month','Passengers']][df['Month']=='Jan']

 v.     Mr. Ankit wants to change the index of the Data Frame and the output for the same is given below. Identify
        the correct statement to change the index.




        i.       df.index[]=["Air India","Indigo","Spicejet","Jet","Emirates"]
        ii.      df.index["Air India","Indigo","Spicejet","Jet","Emirates"]
```

---

## page 3

```
     iii. df.index=["Air India","Indigo","Spicejet","Jet","Emirates"]
     iv. df.index()=["Air India","Indigo","Spicejet","Jet","Emirates"]

         Answer: (iii) df.index=["Air India","Indigo","Spicejet","Jet","Emirates"]


 Q.2.
 Mr. Sharma is working in a game development industry and he was comparing the given chart on the basis of
 the rating of the various games available on the play store.




 He is trying to write a code to plot the graph. Help Mr. Sharma to fill in the blanks of the code and get the
 desired output.


 import__________________________            #Statement 1
 Games=["Subway Surfer","Temple Run","Candy Crush","Bottle                                   Shot","Runner
 Best"]
 Rating=[4.2,4.8,5.0,3.8,4.1]
 plt.______________(Games,Rating)            #Statement 2
 plt.xlabel("Games")
 plt.______________("Rating")                #Statement 3
 plt._______________                         #Statement 4

i.   Choose the right code from the following for statement 1.
     i.     matplotlib as plt
     ii. pyplot as plt
```

---

## page 4

```
       iii. matplotlib.pyplot as plt
       iv.  matplotlib.plt as pyplot

       v.      Answer. (iii) matplotlib.pyplot as plt

 ii.   Identify the name of the function that should be used in statement 2 to plot the above graph.
           i.       line()
           ii. bar()
           iii. hist()
           iv. barh()

            Answer:(ii) bar()

iii.   Choose the correct option for the statement 3.
          i.      title("Rating")
          ii. ytitle("Rating")
          iii. ylabel("Rating")
          iv. yaxis("Rating")


         Answer: (iii) ylabel("Rating”)


iv.    Choose the right function/method from the following for the statement 4.
       i.     display()
       ii. print()
       iii. bar()
       iv. show()

            Answer: (iv) show()

 v.    In case Mr. Sharma wants to change the above plot to the any other shape, which statement, should he change.
       i.      Statement 1
       ii.     Statement 2
       iii.    Statement 3
       iv.     Statement 4
            Answer: Statement 2
```

---

## page 5

```
  Q.3.A School in Delhi uses database management system to store student details. The school maintains a
  database 'school_record' under which there are two tables.


       Student Table : Maintains general details about every student enrolled in school.
       StuLibrary Table : To store details of issued books. BookID is the unique identification number issued to
       each book. Minimum issue duration of a book is one Day.




  i.          Identify the SQL Query which displays the data of StuLibrary table in ascending order of Student-
              ID.
                i) Select * from StuLibrary Order By BookID
                ii) Select * from StuLibrary Order By StuID
                 iii) Select * from StuLibrary Order By StuID ASC
                 iv) Select * from StuLibrary Order By StuID DESC

              Choose the correct option:
              a. Both Query i) and iv) will display the desired data.
              b. Both Query i) and ii) will display the desired data.
              c. Both Query iii) and iv) will display the desired data.
              d. Both Query ii) and iii) will display the desired data.


 ii.          The Primary Key for StuLibrary Table is/are …….
              a. BookID
              b. BookID,StuID
              c. BookID,Issued_date
              d.Issued_date


iii.          Which of the following SQL Query will fetch ID of those issued books which have not been
              returned?
              a. SELECT BookID from StuLibrary where BookID is NULL;
```

---

## page 6

```
            b. SELECT BookID from StuLibrary where StuID is NULL;
            c. SELECT BookID from StuLibrary where Issued_date is NULL;
            d. SELECT BookID from StuLibrary where Return_date is NULL;


iv.         The Alternate Key for Student Table will be ……….
            a. StuName
            b. StuContact
            c. StuAadhar
            d. StuClass


 v.         Which of the following SQL Query will display dates on which number of issued books is greater
            than 5?
            a. SELECT Issued_date from StuLibrary GROUP BY Issued_datewhere COUNT(*)>5;
            b. SELECT Issued_date from StuLibrary GROUP BY Return_datehaving count(*)>5
            c. SELECT Issued_date from StuLibrary GROUP BY Issued_datehaving count(*)>5
            d. SELECT Issued_date from StuLibrary GROUP BY Return_datewhere COUNT(*)>5


  Solutions:
  I.     d) Both Query ii) and iii) will display the desired data.
 II.     c) BookID,Issued_date
III.     d) SELECT BookID from StuLibrary where Return_date is NULL;
IV.      c) StuAadhar
 V.      c) SELECT Issued_date from StuLibrary GROUP BY Issued_datehaving count(*)>5




  Q. 4.
       Tejasvi Sethi, a car dealer has stored the details of all cars in her showroom in a table called CARMARKET.
       The table CARMARKET has attributes CARCODE which is a primary key, CARNAME, COMPANY,
       COLOR, COST (in lakh rupees) of the car and DOM which is the Date of Manufacture of the car.

       Answer any four questions based on the table CARMARKET from the below mentioned questions.

       Table: CARMARKET

       CARCODE        CARNAME         COMPANY        COLOR          COST            DOM
       C01            BALENO          SUZUKI         BLUE           5.90            2019-11-07
       CO2            INDIGO          TATA           SILVER         12.90           2020-10-15
       C03            GLC             MERCEDES       WHITE          62.38           2020-01-20
       C04            A6              AUDI           RED            58.55           2018-12-29
```

---

## page 7

```
     C05            INNOVA           TOYOTA          BLACK           32.82           2017-11-10
     C06            WAGON-R          SUZUKI          WHITE           12.11           2016-11-11
     C07            BREZZA           SUZUKI          GOLDEN          9.80            2016-10-03

  Choose the correct SQL query to do the following (for parts 1 to 4)

       i.   Display the carname along with the charges rounded off to 1 digit afterdecimal place.
            a. Select carname,round(cost) from carmarket;
            b. Select carname,round.cost(1) from carmarket;
            c. Select carname,round.cost() from carmarket;
            d. Select carname, round(cost,1) from carmarket;

                CORRECT ANSWER – d




     ii.    Display the carname, color and position of the character ‘E’ in the color ofall the cars.
            a. select carname,color from carmarket where color like “%E%”;
            b. select carname,color,instr(color,'E') from carmarket;
            c. select carname,color from carmarket where color = “%E%”;
            d. select carname,color,substr(color,1,’E’) from carmarket;

                CORRECT ANSWER – b

     iii.   Display the carname ,name of the company in lower case of all cars whoseyear (of dom) is 2020.
            a. select carname,lcase(company) from carmarket where year(dom) = 2020;
            b. select carname,lcase(company) from carmarket where yearof(dom) like'2020%';
            c. select carname,lower(company) from carmarket where dom from'2020-01-01' to '2020-
               12-31';
            d. select carname,lower(company) from carmarket where yearfrom(dom) =2020;

                CORRECT ANSWER - a



     iv.    Display the number of cars manufactured each year.
                a. select count(*),year(dom) from carmarket where year(dom) = distinct;
                b. select count(*),year(dom) from carmarket group by year(dom);
                c. select count(carmarket),year(dom) from carmarket group by year(dom);
                d. select count(distinct *),year(dom) from carmarket group by year(dom);

            CORRECT ANSWER - b


v.     What is the cardinality and degree of the table CARMARKET?
```

---

## page 8

```
       a. Cardinality = 8 and Degree = 6
       b. Cardinality = 6 and Degree = 7
       c. Cardinality = 7 and Degree = 6
       d. Cardinality = 7 and Degree = 8

           CORRECT ANSWER – c



Q.5.
         Samarth is the harware engineer of “Happy School”. He has been given the task of installing a
         network in the school lab which has around 40 computers.
          i.     Suggest the most suitable type of network topology he should use in order to maximise speed and
                 make each computer indepenent of network breakdowns.
               a. Bus Topology
               b. Star Topology
               c. Ring Topology
               d. Mesh Topology
         answer : b


         ii.     In order to allow data transfer from server to only the intended computers which network device
                 is required in the lab to connect the computers?
               a. Switch
               b. Hub
               c. Router
               d. Gateway
         answer : a


        iii.     After setting up the lab and internet in the lab, Samarth is now required to enable videos and
                 animations to be played on the web browser for students of multimedia class. Which browser tool
                 /service can be used for the same?
               a. Plug ins
               b. Add ons
               c. Control Panel
               d. Download Settings
         answer: b
        iv.     During an international exchange programme the students need to connect to a classroom in
                Russia using Skype. Samarth helps the students to connect. Which type of network service is
                being used ?
```

---

## page 9

```
              a.   Instant messaging
              b.   Email messaging
              c.   VoIP
              d.   WWW
        answer: c
        v.      Samarth has asked students of class 7 to identify different parts of URL. Help the students to
                choose the correct option for label 1 and 2.

              1                          2


        https://www.cbse.gov.in/newsite/index.html

                                       Uniform Resource Locator
       a. 1- Domain Name
             2-Protocol
       b. 1- Protocol
             2-Domain Name
       c. 1. Domain name
             2. subdomain
       d. 1-Protocol
             2-subdomain
        answer : b


Q.6. Answer the following based on the series given below.
import pandas as pd
list1=[1,2,3,4,5,6,7,8]
list2=['swimming','tt','skating','kho kho', 'bb', 'chess', 'football',"cricket"]
school=pd.Series(list1,index=list2)
school.name=("little")
print (school*2)                       #statement 1
print (school.tail(3))                # statement 2
print (school["tt"])                  # statement 3
print (school[2:4])                  # statement 4
```

---

## page 10

```
i.     Choose the correct name of the series object given above.

 a) list1
 b) list2
 c) school
 d) little

ii.    Choose the correct output for the statement:
        print (school.tail(3))             # statement 2
       a.
        swimming             1
        tt                   2
        skating              3
       b.
        chess        6
        football         7
        cricket      8
       c.    4
       d.
        kho kho          4
        bb           5
        chess        6
        football         7
        cricket      8


iii.   Choose the correct output for the statement:
       print (school["tt"]).                          # statement 3
       a. 2
       b. 3
       c. tt     2
       d. true



iv.     Identify the correct output for:
```

---

## page 11

```
     print (school[2:4])                          # statement 4.
     a.
      skating       3
      kho kho           4
     b.
      tt        2
      skating       3
      kho kho           4
     c.
      skating       3
      kho kho 4
      bb            5
     d.
      skating           3
      kho kho           4
      bb            5
      chess         6
      football          7
      cricket       8



v.   The correct output of the statetment:
     print (school*2)                  # statement 1 will be .
          a.
      swimming              3
      tt                    4
      skating               5
      kho kho               6
      bb                    7
      chess                 8
      football              9
```

---

## page 12

```
       cricket     10
        b.
       swimming    2
       tt          4
       skating     6
       kho kho    8
       bb         10
       chess      12
       football   14
       cricket    16
        c.
       swimming    False
       tt         False
       skating    True
       kho kho    True
       bb         True
       chess      True
       football   True
       cricket    True
        d.
       swimming    1
       tt          4
       skating     9
       kho kho     16
       bb         25
       chess       36
       football    49
       cricket    64



Solution:
```

---

## page 13

```
       i.         d) little
       ii.        b)

              chess      6

              football    7

              cricket     8

       iii.       a) 2


       iv.        a)

                  skating     3

                  kho kho     4

       v.         b)

                  swimming         2

                  tt              4

                  skating          6

                  kho kho          8

                  bb              10

                  chess           12

                  football        14

                  cricket         16



Q.7.

Smridh has recently changed his school so he is not aware of the people, but someone is posting negative ,
demeaning comments on his social media profile. He is also getting repeated mails from unknown people.
Everytime he goes online, he finds someone chasing him online.
```

---

## page 14

```
  i.     Smridh is a victim of …………. :
         a. Eavesdropping
         b. Stolen identity
         c. Phishing
         d. Cyber stalking

         Answer(d)




ii.      The action that Smridh should take :
         a. He should ONLY share with his friends
         b. He should NOT share with anyone as it can cause serious problem
         c. He should immediately report to the police
         d. He should bring to the notice of his parents and school authorities.

          Answer : (d)

iii.     …………………….. is a set of moral principles that governs the behaviour of a group or individual and
         regulates the use of computers.
       a. Copyright
       b. Computer ethics
       c. Property rights
       d. Privacy law

       Answer: (b)

iv.      Smridh needs to protect his personal information or data from unintentional and intentional attacks and
         disclosure which is termed as ………...
         a. Digital right
         b. Copyright
         c. Privacy
         d. Intellectual property
```

---

## page 15

```
       Answer : (c)

 v.    The act of fraudulently acquiring someone’s personal and private information, such as online account
       names, login information and passwords is called as ……………
       a. Phishing
       b. Fraud
       c. Scam
       d. Plagiarism

       Answer : (a)

Q.8.
A Departmental store ‘Iconic’ is planning to automate its system so that they can store all the records on computer.
They contacted a Software Company to make the software for the same. The company suggested that there is
need of a front end and back-end software. The major challenge was to keep the record of all the items available
in the store. To overcome the problem, the software company has shown the glimpses of the database and table
required to resolve their problem:
Database Name: Iconic
Table Name: Garment
Attributes of the table: Gcode – Numeric, Gname – Character 25, Size - Character 5, Colour – Character 10,
Price – Numeric
Consider the following records in ‘Garment’ table and answer the given questions:




                                               Table: GARMENT
 GCODE         GNAME        SIZE          COLOUR        PRICE
 111           Tshirt       XL            Red           1400.00
 112           Jeans        L             Blue          1600.00
 113           Skirt        M             Black         1100.00
 114           Jacket       XL            Blue          4000.00
 115           Trousers     L             Brown         1500.00
 116           LadiesTop    L             Pink          1200.00
```

---

## page 16

```
i.         Choose the command that will give the output as:
              COLOUR
              Blu
              Bla
              Blu
              Bro
        a.   Select left(COLOUR,3) from GARMENT where COLOUR like “B%”;
        b.   Select COLOUR from GARMENT where COLOUR not like “%B%”;
        c.   Select mid(COLOUR,3) from GARMENT where COLOUR like “B%”;
        d.   Select COLOUR from GARMENT where COLOUR = ‘B%’;
             Answer: a
ii.        Choose the correct command for the following purpose.
To delete the record with GCode as 116
        a. Delete * from GARMENT where GCode=’116’;
        b. Delete from GARMENTS where GCode =116;
        c. Delete from GARMENT where GCode =116;
        d. Delete from GARMENT where GCode is ’116’;
          Answer: b

iii.     Give the output of :
Select GName, Price from GARMENT
order by Price Desc;
     a.
  GNAME           PRICE
  Tshirt          1400.00
  Jeans           1600.00
  Skirt           1100.00
  Jacket          4000.00
  Trousers        1500.00
  LadiesTop       1200.00


      b.
 GNAME              PRICE
 Skirt              1100.00
 LadiesTop          1200.00
 Tshirt             1400.00
 Trousers           1500.00
 Jeans              1600.00
 Jacket             4000.00
```

---

## page 17

```
          c.
      GNAME              PRICE
      Jacket             4000.00
      Jeans              1600.00
      Trousers           1500.00
      Tshirt             1400.00
      LadiesTop          1200.00
      Skirt              1100.00




          d.
      GNAME              PRICE
      Jacket             4000.00
      Jeans              1600.00
      LadiesTop          1200.00
      Skirt              1100.00
      Trousers           1500.00
      Tshirt             1400.00


     Answer: c

iv.    Choose the correct command for the following purpose.
  To change the colour of GARMENT with code as 116 to “Orange”.

     a.    Update GARMENTS set COLOUR=”Orange” where Gcode=116;
     b.    Update GARMENT set COLOUR =”Orange” where Gcode=116;
     c.    Update GARMENT set COLOUR =”Orange” where Gcode is ”116”;
     d.    Update GARMENT where Gcode=116 set COLOUR =Orange;
     Answer: b



v.             What is the degree and cardinality of ‘GARMENT’ table?
               a. Degree=5 & Cardinality=6
               b. Degree=6 & Cardinality=5
               c. Degree=5 & Cardinality=7
               d. Degree=7 & Cardinality=5
     Answer: a
```

---

## page 18

```
vi.          Suggest a free software for managing the database
              a. Oracle
              b. MySQL
              c. Sybase
              d. Microsoft SQL Server

      Answer: b




      Q.9.
      Sanyukta is the event incharge in a school. One of her students gave her a suggestion to use Python Pandas and
      Matplotlib for analysing and visualising the data, respectively. She has created a Data frame “SportsDay” to keep
      track of the number of First, Second and Third prizes won by different houses in various events.




      Write Python commands to do the following:

 i.      Display the house names where the number of Second Prizes are in the range of 12 to 20.
         a. df['Name'][(df['Second']>=12) and (df['Second']<=20)]
         b. df[Name][(df['Second']>=12) & (df['Second']<=20)]
         c. df['Name'][(df['Second']>=12) & (df['Second']<=20)]
         d. df[(df['Second']>=12) & (df['Second']<=20)]

      Answer: c. df['Name'][(df['Second']>=12) & (df['Second']<=20)]

ii.      Display all the records in the reverse order.
         a.       print(df[::1])
         b.       print(df.iloc[::-1])
         c.       print(df[-1:]+df[:-1])
         d.       print(df.reverse())
```

---

## page 19

```
      Answer: b. print(df.iloc[::-1])


iii.     Display the bottom 3 records.
         a. df.last(3)
         b. df.bottom(3)
         c. df.next(3)
         d. df.tail(3)
      Answer: d. df.tail(3)


iv.      Choose the correct output for the given statements:

      x=df.columns[:1]
      print(x)

         a.      0
         b.      Name
         c.      First
         d.      Error

      Answer: b. Name

 v.      Which command will give the output 24:
         a. print(df.size)
         b. print(df.shape)
         c. print(df.index)
         d. print(df.axes)


      Answer: a. df.size




      Q.10.

      The school offers Wi-Fi to the students of Class XII. For communication, the network security-staff of the school
      is having a registered URL "schoolwifi.edu". On 17th September 2017, emails were received by all the students
      regarding expiry of their passwords. Instructions were also given renew their password within 24 hours by
      clicking on particular URL provided.
      On the bases of the above case study, answer the questions given below:
```

---

## page 20

```
   i. Specify which type of cybercrime is it.
      a) Spamming
      b) Phishing
      c) Identity Theft
      d) Hacking
Answer: (b) Phishing

   ii.    URL stands for____________
      a) Universal Resource Loader
      b) Uniform Resource Locator
      c) United Research Loader
      d) Uniform Resource Loader
Answer: (b) Uniform Resource Locator



   iii.   Unsolicited commercial email is known as:
   a) Malware
   b) Virus
   c) Spam
   d) Spyware
Answer: (c) Spam



  iv.    WiFi stands for ___________
   a) Wireless Internet Frequent Interface
   b) Wireless Functioning
   c) Wireless Fidelity
   d) Wire Free Internet
Answer: c Wireless Fidelity



  v.    Ideally, what characters should be used in a password to make it strong?
   a) Letters and numbers only
   b) Mixed Case (Upper and Lower)
   c) Special characters
   d) All of above

Answer: (d) All of the above
```

---

## page 21

```
Q.11.

 Pushp, a student of class-XII, has been assigned a code to create a panda series S1, as shown below.

 a 100
 b 200
 c 300
 d 400
 e 500
 dtype: int64
With reference to the above answer given questions:
     i.   Choose the command that will give the following output-

          b   200
          c   300
          dtype: int64

    a. print(S1[:3])
    b. print(S1[0:3])
    c. print(S1[1:3])
    d. print(S1[2:4])




   ii.    Help him to identify the correct statement that can be used to extract t h e value with the index 'c'

    a. print(S1[c])
    b. print(S1(c))
    c. print('S1' ['c'])
    d. print(S1 ['c'])




  iii.    W h i c h of the following command will give the following output-

          b    200
          d    400
          dtype: int64

    a. print(S1.iloc[1:4])
    b. print(S1.iloc[2:4])
    c. print(S1.iloc(1:4))
    d. print(S1.iloc[1:4:2])



  iv.   Which of the following command will display the series by adding 10 in eachvalue.
    a. print(S1 [+10])
```

---

## page 22

```
    b. print(S1+10)
    c. print(S1)+10
    d. print(S1)+print(10)



   v.      Pushp wants to delete the value against index 'd'. Help him to choose the suitable option to do so:

    a. S1=S1.drop(d)
    b. S1=S1.drop('d')
    c. S1=drop('d')
    d. S1=S1.drop['d']



Solution:

   i.     c) print(s1[1:3])
  ii.     d) print(S1 ['c'])
 iii.     d) print(S1.iloc[1:4:2])
 iv.      b) print(S1+10)
 v.       b) S1=S1.drop('d')




Q.12.

Gaurav has written a Python Code to create a bar plot as given below using the following data :

   City               Happiness_Index Male     Happiness_Index Female

   Delhi              60                       30

   Beijing            40                       60

   Washington         70                       70

   Tokyo              65                       55

   Moscow             85                       75
```

---

## page 23

```
 import    as                                           #Statement 1
 City=['Delhi','Beijing','Washington','Tokyo','Moscow']
 Gender=['Male','Female'] Happiness_Index_Male=[60,40,70,65,85]
 Happiness_Index_Female=[30,60,70,55,75]
 plt.bar([0.25,1.25,2.25,3.25,4.25],Happiness_Index_Male,color='blue',label="
 Male",width=.5)
 plt.      ([.75,1.75,2.75,3.75,4.75],Happiness_Index_Female,color='Green',w
 idth=.5,label="Female")                          #Statement 2
 pos=range(len(City)) print(pos)
 plt.xticks(pos,City,fontsize=10) plt.xlabel('City', fontsize=16)
 plt.ylabel('Happiness_Index', fontsize=16)
_______                                                              #Statement 3
_______                                                              #Statement 4
_______                                                              #Statement 5




   i.   Identify the suitable code to be used in the blank space in line marked as Statement 1.
        a.matplotlib as plt
        b.numpy as np
        c.pandas as pd
        d.matplotlib.pyplot as plt


  ii.   What is the name of the function to plot the required bar graph in the line marked as Statement 2
        a. hist()
        b. pie()
        c. bar()
```

---

## page 24

```
        d. scatter()

 iii.   Fill in the blank in statement 3 to set Chart Title as “ Happiness Index across cities by gender
        “and font size as 18.
        a. plt.xtitle("Happiness Index across cities by gender",fontsize=18)
        b. plt.title("Happiness Index across cities by gender",fontsize=18)
        c. plt.ytitle("Happiness Index across cities by gender",fontsize=18)
        d. plt.show("Happiness Index across cities by gender",fontsize=18)

  iv.   Identify the suitable code for line marked as Statement 4 to display the legends as shown in the plot.
        a. plt.showlegend()
        b. plt.legend()
        c. plt.display()
        d. plt.show()

  v.    Fill in the blank marked in Statement 5 to display the plot.
        a. plt.plot()
        b. plt.showplot()
        c. plt.display()
        d. plt.show()

Solution:
i.   d. matplotlib.pyplot as plt
ii. c. bar()
iii. b. plt.title("Happiness Index across cities by gender",fontsize=18)
iv. b. plt.legend()
v. d. plt.show()



Q.13.
Refer to the following diagram and answer the questions given below.
```

---

## page 25

```
 i.        Which of the following devices acts as a server?
           a. A
           b. B
           c. C
           d. D

  Answer : (d) D

 ii.       The arrow from device D to pointing to A represents?
       a. HTTP request
       b. HTTP response
       c. HTTP request & response
       d. All of the above

 Answer (b) HTTP response

 iii.    Which of the following device(s) can have IP Addresses?
     a. A
     b. D
     c. F
     d. All of the above

 Answer: (d) All of the above

 iv.    Identify the network topology of the above network :
    a. Ring
    b. Star
    c. Bus
    d. None of the above

 Answer: (b) Star

 v.           is a protocol (set of rules) used when transmitting files (data) over theworld wide web.
  a. FTP
  b. HTTP
  c. SMP
  d. None of the above
Answer: (b) HTTP

Q.14.
Vidya Devi, a retired school principal, was inspired by her granddaughter who uses technology for her day to
day activities. Beinga learner and teacher all her life, she wanted to open an emailaccount and interact with her
friends and family. Her granddaughter created an email account for her and gradually she started sending mails
```

---

## page 26

```
to her friends and family. This was a big achievement for her. Her granddaughter explained how emails are
sent, how to create an email address, what protocols are used. Some of these details weretoo technical for
her, but she never gave up. There are few doubts/misconceptions in her mind which you can help her with.

 i.        Unsolicited e-mail advertising is known as

   a. newsgroup
   b. junk ads
   c. spam
   d. none of the above
 answer (c) spam

 ii.       Which of the following is the correct format of email address?

       a. name@website@info
       b. name@website.info
       c. www.nameofwebsite.com
       d. name.website.com

 answer: (b) name@website@info

 iii.      Mail access starts with client when user needs to download email fromthe

     a. mail box
     b. mail server
     c. IP server
     d. Internet
 Answer:(a) mail box
 iv.     To use email service, one needs to register with

       a. Internet Service Provider
       b. Email Service Provider
       c. A company
       d. No need to register

          Answer: (a) Internet Service Provider

 v.        Bcc stands for        to send the copy of mail.

       a. Black carbon copy
       b. Blue carbon copy
       c. Blind carbon copy
       d. Block chain copy
```

---

## page 27

```
        Answer: (c ) Blind Carbon Copy



Q.15.
A Gift Gallery has different stores in India. Database Administrator Abhay wants to maintain database of their
Salesmen in SQL to store the data, He has decided that
Name of the database: GiftGallery
Name of the table: Salesman
Attributes of the tables: Scode – Numeric, Sname – Character 25, Address - Character 25, Dojoin - Date, Sales
– Numeric and Area – Character 10
Consider the following records in ‘Salesman’ table and answer the given questions:
                                                 Table : Salesman

 Scode         Sname         Address        Dojoin       Sales        Area
 100           Amit          Delhi          2017/09/29   5000.90      East
 101           Sushant       Gurgaon        2018/01/01   7000.75      East
 102           Priya         Noida          2018/04/25   3450.45      West
 103           Mohit         Delhi          2018/11/03   6000.50      North
 104           Priyanshi     Delhi          2019/12/15   8000.62      North

   i.        State the command that will give the output as :
               Sname
               Sushant
               Priya
             a. Select Sname from Salesman Where Not Address =”Delhi”;
             b. Select Sname from Salesman Where Address NOT IN(“Delhi”);
             c. Select Sname from Salesman Where Address !=“Delhi”;
             d. All of the above;
             Answer: (d) All of the above


   ii.       Which of the following commands will display the details of all sales record of North Area, regardless
             of case (whether North / NORTH / north):
             a. Select * from salesman where area like upper ‘north’;
             b. Select * from salesman where area = ‘North’ or ‘NORTH’ or north;
             c. Select * from salesman where upper(area)=’NORTH’;
             d. Select * from salesman where area= =upper(’North”)’;
```

---

## page 28

```
            Answer : (c) Select * from salesman where upper(area)=’NORTH’;




iii.        Help Priya to display sname and sales of east and west areas
            a. Select sname, sales from Salesman where area=”East” and area=”West”;
            b. Select sname, sales from Salesman where area=”East” or area=”West”;
            c. Select sname, sales from Salesman where area in ”East” and ”West”;
            d. Select sname, sales from Salesman where area=”East” , ”West”;
            Answer:(b) Select sname, sales from Salesman where area=”East” or area=”West”;
iv.         The command to display the name of the salesman along with the sales amount rounded off to one
            decimal point will be:
            a. Select sname, round(sales,1) from salesman;
            b. Select sname, round(sales,0.1) from salesman;
            c. Select sname, trunc(sales,1) from salesman;
            d. Select sname, trunc(sales,0.1) from salesman;
        answer:(a) Select sname, round(sales,1) from salesman;
v.          What will be the output of the following command?
            Select Right(Sname,3), Round(Sales) from Salesman Where Sname Like “P%”;
            a.

                 Right(Sname,3) Round(Sales)
                 Pri            3450
                 Pri            8000


            b.

                 Right(Sname,3) Round(Sales)
                 iya            3450
                 shi            8000




       c.

             Right(Sname,3) Round(Sales)
```

---

## page 29

```
               iya               3450
               shi               8001




        d.

              Right(Sname,3) Round(Sales)
              Pri            3450
              Pri            8001


Answer : (d)


Q.16.
A Fashion Store MyStore is considering to maintain database of their Customers in SQL to store the data, As a
Database Administrator Hina has decided that
Name of the database: MyStore
Name of the table: Customer
Attributes of the tables: Acc_No – Numeric, Cust_Name – Character 25, Cust_City - Character 25, Cust_Phone
- Character 11, Open_Bal – Numeric
Consider the following records in ‘Customer’ table and answer the given questions:
                                                Table : Customer

 Acc_No              Cust_Name      Cust_City       Cust_Phone       Open_Bal
 1001                Dhashmesh      Ambala          9710557614       10000
 1002                Sanya          Patna           8223545233       15000
 1003                Joe            NewDelhi        9972136576       13000
 1004                Mrinal         NewDelhi        9321305453       12000
 1005                Ishaan         Agra            9809876798       19000


   i.        With reference to the above given table, give query for generating following output
              Cust_Name
              Dhashmesh
              Sanya
```

---

## page 30

```
        Ishaan
      a. Select Name from Customer where Open_bal<20000;
      b. Select Name from Customer where Cust_City like ‘%a’;
      c. Select Cust_Name from Customer where Cust_City like ‘%a’;
      d. Select Cust_name from Customer where Cust_Name like “a%;
      Answer : (c) Select Cust_Name from Customer where Cust_City like ‘%a’;


ii.   Give the output of :
      Select Cust_Name, Open_Bal from Customer order by Open_bal;
      a.
         Cust_Name        Open_Bal
         Dhashmesh        10000
         Mrinal           12000
         Joe              13000
         Sanya            15000
         Ishaan           19000

      b.
           Cust_Name   Open_Bal
           Ishaan      19000
           Sanya       15000
           Joe         13000
           Mrinal      12000
           Dhashmesh   10000

      c.
           Cust_Name    Open_Bal
           Dhashmesh    10000
           Ishaan       19000
           Joe          13000
           Mrinal       12000
           Sanya        15000




      d.

           Cust_Name   Open_Bal
```

---

## page 31

```
              Dhashmesh        10000
              Sanya            15000
              Joe              13000
              Mrinal           12000
              Ishaan           19000


  Answer : (a)
  iii.      Pranay has given the following command to obtain Highest Opening Balance of each City
            Select max(Open_Bal) from Customer where group by Cust_City;
            but he is not getting the desired result. Help him by writing the correct command.
            a. Select Max(Open_Bal) group by Cust_City;
            b. Select Max(Open_Bal) from Customer where group by Cust_City;
            c. Select Cust_City, Max(Open_Bal) from Customer group by Cust_City;
            d. Select max(Open_Bal) from Customer group by Cust_name;

Answer : (c) Select Cust_City, Max(Open_Bal) from Customer group by Cust_City;


  iv.       Help Pranay find the total no. of records having open_bal between 15000 to 20000 by selecting the
            right command:
            a. Select total from customer having open_bal between 15000 and 20000;;
            b. Select count(*) from customer where open_bal between 15000 to 20000;;
            c. Select count(*) from customer where open_bal between 15000 and 20000;
            d. Select count(*) from customer order by open_bal;
             Answer: (c) Select count(*) from customer where open_bal between 15000 and 20000;


  v.        Choose the correct command to display the first two letters of each customer’s name.
            a. select right(cust_name,2) from customer;
            b. select left(cust_name,2) from customer;
            c. select right(cust_name,0,2) from customer;
            d. select left(cust_name,2) from customer;


         Answer: (b) select left(cust_name,2) from customer;
```

---

## page 32

```
 Q.17.
Ramanpreet has to work on his science project which deals with electromagnetic waves. A lot of research
workis required by him for the same. He uses Google Chrome to search for the relevant matter.
  i.     Google chromeis an example of a
         a. Website
         b. Web browser
         c. Web Page
         d. Web Page
Ans. (b)
 ii.       He finally locates some useful information and clicks on the link provided to access the website. The
           link is actually known as a_____________.
         a. Domain name
         b. Web Page
         c. URL
         d. IP address
Ans. (c)
 iii.      As Ramanpreet works on his project, he collects and curates information. Whenever he clicks on the
           link the same piece of information is shown and the content is not clickable. Ramanpreet is accessing
           a/an _______ website.
           a. Dynamic
           b. Textual
           c. Outdated
           d. Static
Ans. (d)
 iv.       A web cookie is a small piece of data that is __________
           a. sent from a website and stored in user’s web browser while a user is browsing a website
           b. sent from user and stored in the server while a user is browsing a website
           c. sent from root server to all servers
           d. sent from the root server to other root servers
Ans. (a)
 v.        HTML stands for________
           a. Hyper Text Markup Link
           b. Hyper Text Markup Language
           c. Hybrid Text Markup Language
           d. Hyper Text Manipulation Language
```

---

## page 33

```
Ans. (c)



Q.18.

Zeenat has created the following data frame dataframe1 to keep track of data Rollno, Name, Marks1 and
Marks2 for various students of her class where row indexes are taken as the default values:



 Rollno                 Name                Marks1              Marks2
 1                      Swapnil Sharma      30                  50
 2                      Raj Batra           75                  45
 3                      Bhoomi Singh        82                  95
 4                      Jay Gupta           90                  95


i.          Which among the following option will give 90, 95 as output
     a)        print(max(dataframe1['Marks1','Marks2'])
     b)        print((dataframe1.Marks1.max(),(dataframe1.Marks2.max())))
     c)        print(max(dataframe1['Marks1'])
     d)        print(max(dataframe1['Marks2'])



Answer: (b) print((dataframe1.Marks1.max(),(dataframe1.Marks2.max())))

     ii.       She needs to know the marks scored by Rollno 2. Help her to identify the correct set of statement/s
               from the given options:
     a. print(dataframe1[dataframe1['Rollno']= =2])
     b. print(dataframe1['Rollno']= =2)
     c. print(dataframe1[dataframe1. Rollno = =2])
     d. print(dataframe1[dataframe1['Rollno']])

     Answer : (c) print(dataframe1[dataframe1. Rollno = =2])

     iii.      Which of the following statement/s will delete the 3rd column?
     a. del dataframe1['Marks1']
```

---

## page 34

```
   b. dataframe1.pop('Marks1')
   c. drop dataframe1['Marks1']
   d. pop dataframe1['Marks1']

Choose the correct option:

   a) both (a) and (b)
   b) only (b)
   c) (a), (b) and (c)
   d) (a), (b) and (d)
         Answer : (a) both (a) and (b)
   iv.      Which of the following command will display the total number of elements in the dataframe?
   a. print(dataframe1.shape)
   b. print(dataframe1.num)
   c. print(dataframe1.size)
   d. print(dataframe1.elements)

   answer (c) print(dataframe1.size)

   v.       Now she wants to add a new column Marks3 with relevant data. Help her choose the command to
            perform this task.
   a. dataframe1.column=[ 45,52,90,95]
   b. dataframe1 ['Marks3']= [ 45,52,90,95]
   c. dataframe1.loc['Marks3']= [ 45,52,90,95]
   d. Both (b) and (c) are correct
   Answer: (b) dataframe1 ['Marks3']= [ 45,52,90,95]
```

---

## page 35

```
Q.19.
Naman has created the following dataframe “Climate” to record the data about climatic conditions of four years.

                   Year               MaxTemp            MinTemp            Rainfall
                   2017               32                 20                 123
                   2018               33                 22                 140
                   2019               35                 21                 135
                   2020               34                 23                 160


   i.      Which of the following code snippets will return the MaxTemp and Rainfall for year 2018 and
           2019?
   a. Climate[['MaxTemp','Rainfall']][1:3]
   b. Climate['MaxTemp', 'Rainfall'][1:3]
   c. Climate.iloc[1:3]
   d. Climate.iloc[1:3,1:2]

   Answer: (c) Climate.iloc[1:3]

   ii.     Display the temperature difference between MaxTemp and MinTemp for all the rows in the
           dataframe Climate.
           a. Climate=Climate["MaxTemp"]-Climate["MinTemp"]
           b. print(Climate["maxt"]-Climate["mint"])
           c. print(Climate["MaxTemp"]-Climate["MinTemp"])
           d. print(Climate.Climate["MaxTemp"]-Climate["MinTemp"])


           e. Answer : (c) print(Climate["MaxTemp"]-Climate["MinTemp"])
   iii.    To display 2 rows from the top in the dataframe, which of the following statement is correct:
   a. print (Climate.head()=2 )
   b. print (Climate.head(n==2) )
   c. print (Climate.head(range(2)) )
   d. print (Climate.head(2)            )

   answer: (d) print (Climate.head(2)           )
```

---

## page 36

```
  iv.      Which of the following statement/s will give the exact number of values in each column of the
           dataframe?
  a.       print(Climate.count())
  b.       print(Climate.count(0))
  c.       print(Climate.count)
  d.       print(Climate.count(axis='index'))

  Choose the correct option:

  a) both (a) and (b)
  b) only (b)
  c) (a), (b) and (c)
  d) (a), (b) and (d)

        Answer: (d) (a), (b) and (d)



  v.       To display 2 rows from the bottom in the dataframe, which of the following statement is correct:
  a.       print     (Climate.tail()=2 )
  b.       print (Climate.tail(n==2) )
  c.       print(Climate.tail(range(2)))
  d.       print (Climate.tail(2) )



Answer: (d) print (Climate.tail(2) )
```

---

## page 37

```
Q.20.
Sumit has to prepare a project on “Swachh Bharat Shreshth Bharat”.
He decides to get information from the Internet. He downloads three web pages (webpage1, webpage 2, webpage
3) containing information on the given topic.
1. He read a paragraph on from webpage 1 and rephrased it in his own words. He finally pasted the rephrased
paragraph in his project.
2. He downloaded three images of from webpage 2. He made a collage for his project using these images.
3. He also downloaded an icon from web page 3 and pasted it on the front page of his project report.


i.      Step1 An Example of __________
        a. Plagiarism
        b. Paraphrasing
        c. copyright infringement
        d. Intellectual Property right
        Answer:(b) :Paraphrasing


ii.     Step 2 An act of __________
        a. plagiarism
        b. copyright infringement
        c. Intellectual Property right
        d. Digital Footprints
         Answer: (a) Plagiarism


 iii.    Step 3 An act of _________
        a. Plagiarism
        b. Paraphrasing
        c. copyright infringement
        d. Intellectual Property right
     Answer : (c) Copyright Infringement


 iv.     A website is a collection of ___________
         a.   Web Servers
```

---

## page 38

```
             b.    Web pages
             c.    Browsers
             d.    Hyperlinks
           Answer : (b)
      v.     The process of getting web pages, images and files from a web server to local computer is called
             a. FTP
             b. Uploading
             c. Downloading
             d. Remote access
           Answer : (c) Downloading



     Q.21.
     HR Department of ABCTech has created following dataframe to store data about salaries and bonus paid to
     their employees:

     import pandas as pd
     import numpy as np
     d1={'EName':[ 'Kavita', 'Sudha',
     'Garima’]'],'Sal':[50000,60000,55000],'Bonus':[3000,4000,5000]}
     Df1=pd.DataFrame(d1)

     Choose the python statement using suitable functions for the following tasks:


i.      Display the columns Sal and Bonus

           a. df1 [:Sal :Bonus]
           b. df1.loc(['Sal','Bonus'])
           c. df1.iloc(['Sal','Bonus'])
           d. df1[['Sal','Bonus']]
           Answer: (b) df1.loc(['Sal','Bonus'])

ii.     Display the details of employee Kavita.
        a. df1[df1.EName='Kavita']
        b. df1.loc[df1.EName=='Kavita']
        c. df1.iloc[df1.EName=='Kavita']
        d. df1[EName='Kavita']

        Answer (b) df1.loc[df1.EName=='Kavita']
```

---

## page 39

```
iii.     Display the details of the last employee.
         a. Df1.tail(1)
         b. Df1.tail (-1)
         c. Df1.head(n=1)
         d.     Df1.head()

       Answer: (a) Df1.tail(1)
 iv.      Add a new column named ‘Email’ with the value “abc@gmail.com”.
         a. Df1[‘Email’]= ‘abc@gmail.com’
         b. Df1[Email]=’abc@gmail.com’
         c. Df1.loc[‘Email’]=’abc@gmail.com’
         d.      Df1(‘Email’)=’abc@gmail.com’
         Answer : (a) Df1[‘Email’]= ‘abc@gmail.com’



  v.      Write a python statement to print the details of employees having Sal more than 50000
              a. df1.Sal>=5000
              b. df1[df1.Sal>=5000]
              c. df1[df1.'Sal'>=5000]
              d. df1.iloc[df1.Sal>=5000]

              answer: (b) df1[df1.Sal>=5000]
```