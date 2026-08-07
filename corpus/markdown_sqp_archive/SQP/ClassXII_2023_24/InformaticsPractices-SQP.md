---
title: "InformaticsPractices-SQP"
source_pdf: "InformaticsPractices-SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/InformaticsPractices-SQP.pdf"
pages: 9
pdf_bytes: 651813
pdf_sha256: "3d63d54a849fd12fe7bf7d8948612d139fda831ebf28c7a6daaffe8d166db3b5"
text_chars: 16890
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPractices-SQP


---

## page 1

```
                             SAMPLE QUESTION PAPER
                                   CLASS XII
                           INFORMATICS PRACTICES (065)
TIME: 03 HOURS                                                                              M.M.: 70
 General Instructions:
           1. This question paper contains five sections, Section A to E.
           2. All questions are compulsory.
           3. Section A has 18 questions carrying 01 mark each.
           4. Section B has 07 Very Short Answer type questions carrying 02 marks each.
           5. Section C has 05 Short Answer type questions carrying 03 marks each.
           6. Section D has 02 questions carrying 04 marks each.
           7. Section E has 03 questions carrying 05 marks each.
           8. All programming questions are to be answered using Python Language only.
                                                     SECTION A

              1.     A ____________is a device that connects the organisation’s network with the   1
                     outside world of the Internet.
                         i. Hub
                         ii. Modem
                         iii. Gateway
                         iv. Repeater

              2.    When e-waste such as electronic circuit boards are burnt for disposal, the     1
                    elements contained in them create a harmful chemical called ________which
                    causes skin diseases, allergies and an increased risk of lung cancer.
                        i. Hydrogen
                        ii. Beryllium
                        iii. Chlorine
                        iv. Oxygen

              3.     Copyright, Patent and Trademark comes under:                                  1
                        i. Intellectual Property Right
                        ii. Individual Property Right
                        iii. Industrial Property Right
                        iv. International Property Right

              4.     Predict the output of the following query:                                    1
                             SELECT MOD (9,0);
                        i. 0
                        ii. NULL
                        iii. NaN
                        iv. 9
```

---

## page 2

```
5.   Which of the following SQL functions does not belong to the Math functions   1
     category?
         i. POWER()
         ii. ROUND()
         iii. LENGTH()
         iv. MOD()

6.    ________ is not a FOSS tool.                                                1
         i. Libre Office
         ii. Mozilla Firefox
         iii. Google Chrome
         iv. Python

7.   CSV stands for:                                                              1
       i. Column Separated Value
       ii. Class Separated Value
       iii. Comma Separated Value
       iv. Comma Segregated Value

8.   Raj, a Database Administrator, needs to display the average pay of workers   1
     from those departments which have more than five employees. He is
     experiencing a problem while running the following query:

     SELECT DEPT, AVG(SAL) FROM EMP WHERE COUNT(*) > 5
     GROUP BY DEPT;

     Which of the following is a correct query to perform the given task?

     i. SELECT DEPT, AVG(SAL) FROM EMP WHERE COUNT(*) > 5
     GROUP BY DEPT;
     ii. SELECT DEPT, AVG(SAL) FROM EMP HAVING COUNT(*) >
     5 GROUP BY DEPT;
     iii. SELECT DEPT, AVG(SAL) FROM EMP GROUP BY DEPT
     WHERE COUNT(*) > 5;
     iv. SELECT DEPT, AVG(SAL) FROM EMP GROUP BY DEPT
     HAVING COUNT(*) > 5;

9.   Predict the output of the following query:                                   1
     SELECT LCASE (MONTHNAME ('2023-03-05'));
          i. May
          ii. March
          iii. may
          iv. march
```

---

## page 3

```
10.     Which of the following command will show the last 3 rows from a Pandas          1
        Series named NP?
            i. NP.Tail( )
            ii. NP.tail(3)
            iii. NP.TAIL(3)
            iv. All of the above

11.    With reference to SQL, identify the invalid data type.                           1
        i. Date
        ii. Integer
        iii. Varchar
        iv. Month

12.   In Python Pandas, while performing mathematical operations on series, index       1
      matching is implemented and all missing values are filled in with _____by
      default.
           i. Null
           ii. Blank
           iii. NaN
           iv. Zero

13.    By restricting the server and encrypting the data, a software company's          1
       server is unethically accessed in order to obtain sensitive information. The
       attacker blackmails the company to pay money for getting access to the data,
       and threatens to publish sensitive information unless price is paid. This kind
       of attack is known as:
               i. Phishing
               ii. Identity Theft
               iii. Plagiarism
               iv. Ransomware

14.      In SQL, the equivalent of UCASE() is:                                          1
             i. UPPERCASE ()
             ii. CAPITALCASE()
             iii. UPPER()
             iv. TITLE ()

15.   Collection of hyper linked documents available on the internet is known           1
      as_______________.
         i. Website
         ii. Webpage
         iii. Web Server
         iv. Web Hosting
```

---

## page 4

```
16.    _______________is a non-profit organization that aims to build a publicly         1
       accessible global platform where a range of creative and academic work is
       shared freely.
          i. Creative Cost
          ii. Critical Commons
          iii. Creative Commons
          iv. Creative Common

17.    Assertion (A):- MODEM stands for modulator-demodulator.                           1
       Reasoning (R): - It is a computer hardware device that converts data from a
       digital format to analog and vice versa.
          i. Both A and R are true and R is the correct explanation for A
          ii. Both A and R are true and R is not the correct explanation for A
          iii. A is True but R is False
          iv. A is false but R is True

18.    Assertion (A):- To use the Pandas library in a Python program, one must           1
       import it.
       Reasoning (R): - The only alias name that can be used with the Pandas library
       is pd.
          i. Both A and R are true and R is the correct explanation for A
          ii. Both A and R are true and R is not the correct explanation for A
          iii. A is True but R is False
          iv. A is false but R is True

                                       SECTION B

19.   Briefly explain the basic concepts of a web server and web hosting.                2
                                            OR
      Rati is doing a course in networking. She is unable to understand the concept of
      URL. Help her by explaining it with the help of suitable example.

20. The python code written below has syntactical errors. Rewrite the correct code       2
    and underline the corrections made.
    Import pandas as pd
    df ={"Technology":["Programming","Robotics","3D
    Printing"],"Time(in months)":[4,4,3]}
    df= Pd.dataframe(df)
    Print(df)

21.    Consider the given SQL string:                                                    2
       “12#All the Best!”
       Write suitable SQL queries for the following:
          i. Returns the position of the first occurrence of the substring “the” in
              the given string.
          ii. To extract last five characters from the string.
```

---

## page 5

```
22.    Predict the output of the given Python code:                                             2
       import pandas as pd
       list1=[-10,-20,-30]
       ser = pd.Series(list1*2)
       print(ser)

23.    Differentiate between the active digital footprint and passive digital footprints.       2

24.    Complete the given Python code to get the required output as: Rajasthan                  2
       import _________ as pd
       di = {'Corbett': 'Uttarakhand', 'Sariska':
       'Rajasthan', 'Kanha': 'Madhya Pradesh’,
       'Gir':'Gujarat'}
       NP = ___________. Series( _____ )
       print(NP[ ___________ ])

25.   What are aggregate functions in SQL? Name any two.                                        2

                                        SECTION C

26.    Based on the SQL table CAR_SALES, write suitable queries for the following:          3
        +--------+-------------------+--------+-------+-------+
        | NUMBER | SEGMENT           | FUEL   | QT1   | QT2   |
        +--------+-------------------+--------+-------+-------+
        |      1 | Compact HatchBack | Petrol | 56000 | 70000 |
        |      2 | Compact HatchBack | Diesel | 34000 | 40000 |
        |      3 | MUV               | Petrol | 33000 | 35000 |
        |      4 | MUV               | Diesel | 14000 | 15000 |
        |      5 | SUV               | Petrol | 27000 | 54000 |
        |      6 | SUV               | Diesel | 18000 | 30000 |
        |      7 | Sedan             | Petrol | 8000 | 10000 |
        |      8 | Sedan             | Diesel | 1000 | 5000 |
        +--------+-------------------+--------+-------+-------+
           i. Display fuel wise average sales in the first quarter.
           ii. Display segment wise highest sales in the second quarter.
           iii. Display the records in the descending order of sales in the second
                quarter.
                                             OR
       Predict the output of the following queries based on the table CAR_SALES
       given above:
       i. SELECT LEFT(SEGMENT,2) FROM CAR_SALES WHERE FUEL=
       "PETROL";
       ii.SELECT (QT2-QT1)/2 "AVG SALE" FROM CAR_SALES WHERE
       SEGMENT= "SUV";
       iii. SELECT SUM(QT1) "TOT SALE" FROM CAR_SALES WHERE
       FUEL= "DIESEL";
```

---

## page 6

```
27.    Create a DataFrame in Python from the given list:                                 3
       [[‘Divya’,’HR’,95000],[‘Mamta’,’Marketing’,97000],[‘Payal’,’IT’,980000],
       [‘Deepak’,’Sales’,79000]]
       Also give appropriate column headings as shown below:




28.    Write MySQL statements for the following:                                         3
          i. To create a database named FOOD.
          ii. To create a table named Nutrients based on the following specification:
                 Column Name         Data Type           Constraints
                 Food_Item           Varchar(20)         Primary Key
                 Calorie             Integer


29.    Richa, recently started using her social media account. Within a few days, she    3
       befriends many people she knows and some that she does not know. After
       some time, she starts getting negative comments on her posts. She also finds
       that her pictures are being shared online without her permission.
       Based on the given information, answer the questions given below.
           i. Identify the type of cybercrime she is a victim of.
           ii. Under which act, she can lodge a complaint to the relevant authorities?
           iii. Suggest her any two precautionary measures which she should take in
                future while being online to avoid any such situations.
                                              OR
       Mention any three health hazards associated with inappropriate and excessive
       use of gadgets.

30.    Consider the given DataFrame ‘Genre’:                                             3
                      Type        Code
            0         Fiction      F
            1         Non Fiction NF
            2         Drama        D
            3         Poetry      P

      Write suitable Python statements for the following:
         i. Add a column called Num_Copies with the following data:
             [300,290,450,760].
         ii. Add a new genre of type ‘Folk Tale' having code as “FT” and 600
              number of copies.
         iii. Rename the column ‘Code’ to ‘Book_Code’.
```

---

## page 7

```
                                        SECTION D

31.    Preeti manages database in a blockchain start-up. For business purposes, she            4
       created a table named BLOCKCHAIN. Assist her by writing the following
       queries:
                                TABLE: BLOCKCHAIN




           i. Write a query to display the year of oldest transaction.
           ii. Write a query to display the month of most recent transaction.
           iii. Write a query to display all the transactions done in the month of May.
           iv. Write a query to count total number of transactions in the year 2022.

32.   Ekam, a Data Analyst with a multinational brand has designed the DataFrame               4
      df that contains the four quarter’s sales data of different stores as shown below:
                 Store Qtr1 Qtr2 Qtr3 Qtr4
               0 Store1 300 240 450 230
               1 Store2 350 340 403 210
               2 Store3 250 180 145 160
      Answer the following questions:
          i. Predict the output of the following python statement:
               a. print(df.size)
               b. print(df[1:3])
          ii. Delete the last row from the DataFrame.
          iii. Write Python statement to add a new column Total_Sales which is the
               addition of all the 4 quarter sales.
                                               OR
                                   (Option for part iii only)
      Write Python statement to export the DataFrame to a CSV file named data.csv
      stored at D: drive.

                                        SECTION E

33.    Write suitable SQL queries for the following:                                       5
          i. To calculate the exponent for 3 raised to the power of 4.
          ii. To display current date and time.
          iii. To round off the value -34.4567 to 2 decimal place.
          iv. To remove all the probable leading and trailing spaces from the
               column userid of the table named user.
          v. To display the length of the string ‘FIFA World Cup’.
```

---

## page 8

```
                                             OR
      Kabir has created following table named exam:
      +-------+---------+------------------+-------+
      | RegNo | Name              | Subject                   | Marks |
      +-------+---------+------------------+-------+
      |       1 | Sanya           | Computer Science |               98 |
      |       2 | Sanchay | IP                                |     100 |
      |       3 | Vinesh | CS                                 |      90 |
      |       4 | Sneha           | IP                        |      99 |
      |       5 | Akshita | IP                                |     100 |
      +-------+---------+------------------+-------+
      Help him in writing SQL queries to the perform the following task:
         i.      Insert a new record in the table having following values:
                 [6,'Khushi','CS',85]
         ii.     To change the value “IP” to “Informatics Practices” in subject
                 column.
         iii.    To remove the records of those students whose marks are less than
                 30 .
         iv.     To add a new column Grade of suitable datatype.
         v.      To display records of “Informatics Practices” subject.

34.   XYZ Media house campus is in Delhi and has 4 blocks named Z1, Z2, Z3 and        5
      Z4. The tables given below show the distance between different blocks and the
      number of computers in each block.
```

---

## page 9

```
      The company is planning to form a network by joining these blocks.
         i. Out of the four blocks on campus, suggest the location of the server that
              will provide the best connectivity. Explain your response.
         ii. For very fast and efficient connections between various blocks within the
              campus, suggest a suitable topology and draw the same.
         iii. Suggest the placement of the following devices with justification
              (a) Repeater
              (b) Hub/Switch
         iv. VoIP technology is to be used which allows one to make voice calls
              using a broadband internet connection. Expand the term VoIP.
         v. The XYZ Media House intends to link its Mumbai and Delhi centers.
              Out of LAN, MAN, or WAN, what kind of network will be created?
              Justify your answer.

35.    The heights of 10 students of eighth grade are given below:                       5

                Height_cms=[145,141,142,142,143,144,141,140,143,144]

       Write suitable Python code to generate a histogram based on the given data,
       along with an appropriate chart title and both axis labels.
       Also give suitable python statement to save this chart.
                                             OR
       Write suitable Python code to create 'Favourite Hobby' Bar Chart as
       shown below:




       Also give suitable python statement to save this chart.
```