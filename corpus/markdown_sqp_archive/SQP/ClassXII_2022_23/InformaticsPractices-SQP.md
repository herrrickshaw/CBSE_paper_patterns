---
title: "InformaticsPractices-SQP"
source_pdf: "InformaticsPractices-SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/InformaticsPractices-SQP.pdf"
pages: 9
pdf_bytes: 531123
pdf_sha256: "f3bb139920a33f37dd22a2c83bb849f1e55203adae3a0f042b09cfcca3de1cc2"
text_chars: 16721
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
TIME: 3 HOURS                                                               M.M.70

General Instructions:
          1. This question paper contains five sections, Section A to E.
          2. All questions are compulsory.
          3. Section A have 18 questions carrying 01 mark each.
          4. Section B has 07 Very Short Answer type questions carrying 02 marks each.
          5. Section C has 05 Short Answer type questions carrying 03 marks each.
          6. Section D has 03 Long Answer type questions carrying 05 marks each.
          7. Section E has 02 questions carrying 04 marks each. One internal choice is
             given in Q35 against part c only.
          8. All programming questions are to be answered using Python Language only.



                                            PART A
1.   Television cable network is an example of:                                    1
         i.   LAN
        ii.   WAN
       iii.   MAN
       iv.    Internet
2.   Which of the following is not a type of cyber crime?                          1
        i. Data theft
       ii. Installing antivirus for protection
     iii. Forgery
      iv. Cyber bullying
3.   What is an example of e-waste?                                                1
        i. A ripened mango
       ii. Unused old shoes
     iii. Unused old computers
      iv. Empty cola cans
4.   Which type of values will not be considered by SQL while executing the 1
     following statement?

     SELECT COUNT(column name) FROM inventory;

        i.   Numeric value
       ii.   text value
      iii.   Null value
      iv.    Date value
```

---

## page 2

```
5.    If column “Fees” contains the data set (5000,8000,7500,5000,8000), what will 1
      be the output after the execution of the given query?

      SELECT SUM (DISTINCT Fees) FROM student;

            i.      20500
            ii.      10000
            iii.     20000
            iv.      33500
6.    ‘O’ in FOSS stands for:                                                        1
         i.      Outsource
        ii.      Open
       iii. Original
       iv.       Outstanding

7.    Which SQL statement do we use to find out the total number of records present 1
      in the table ORDERS?

        i.     SELECT * FROM ORDERS;
        ii.    SELECT COUNT (*) FROM ORDERS;
        iii.   SELECT FIND (*) FROM ORDERS;
        iv.    SELECT SUM () FROM ORDERS;
8.    Which one of the following is not an aggregate function?                       1
        i.  ROUND()
       ii.  SUM()
      iii. COUNT()
      iv.   AVG()
9.    Which one of the following functions is used to find the largest value from the 1
      given data in MySQL?
         i.  MAX( )
        ii.  MAXIMUM( )
       iii. BIG( )
       iv.   LARGE( )
10.   To display last five rows of a series object ‘S’, you may write:               1
         i.  S.Head()
        ii.  S.Tail(5)
       iii. S.Head(5)
       iv.   S.tail()
11.   Which of the following statement will import pandas library?                   1
        i.  Import pandas as pd
       ii.  import Pandas as py
      iii. import pandas as pd
      iv.   import panda as pd
```

---

## page 3

```
12.   Which of the following can be used to specify the data while creating a 1
      DataFrame?
         i.  Series
        ii.  List of Dictionaries
       iii. Structured ndarray
       iv.   All of these
13.   Which amongst the following is not an example of a browser?                         1
            i.      Chrome
            ii.     Firefox
            iii.    Avast
            iv.     Edge
14.   In SQL, which function is used to display current date and time?                    1
         i.      Date ()
        ii.      Time ()
       iii. Current ()
       iv.       Now ()
15.   Legal term to describe the rights of a creator of original creative or artistic work 1
      is:
          i. Copyright
        ii.  Copyleft
       iii. GPL
       iv.   FOSS
16.   __________is the trail of data we leave behind when we visit any website (or use 1
      any online application or portal) to fill-in data or perform any transaction.
         i.  Offline phishing
        ii.  Offline footprint
       iii. Digital footprint
       iv.   Digital phishing
Q17 and 18 are ASSERTION AND REASONING based questions. Mark the correct choice as
           i. Both A and R are true and R is the correct explanation for A
          ii. Both A and R are true and R is not the correct explanation for A
         iii. A is True but R is False
         iv. A is false but R is True
17. Assertion (A): - Internet cookies are text files that contain small pieces of data, 1
     like a username, password and user’s preferences while surfing the internet.

      Reasoning (R):- To make browsing the Internet faster & easier, its required to
      store certain information on the server’s computer.

18.   Assertion (A):- DataFrame has both a row and column index.                          1

      Reasoning (R): - A DataFrame is a two-dimensional labelled data structure like
      a table of MySQL.
```

---

## page 4

```
                                       PART B
19.   Explain the terms Web page and Home Page.                                          2

                                              OR
      Mention any four networking goals.

20.   Rashmi, a database administrator needs to display house wise total number of 2
      records of ‘Red’ and ‘Yellow’ house. She is encountering an error while
      executing the following query:

      SELECT HOUSE, COUNT (*) FROM STUDENT GROUP BY HOUSE
      WHERE HOUSE=’RED’ OR HOUSE= ‘YELLOW’;

      Help her in identifying the reason of the error and write the correct query by
      suggesting the possible correction (s).
21.   What is the purpose of Order By clause in SQL? Explain with the help of suitable 2
      example.

22.   Write a program to create a series object using a dictionary that stores the number 2
      of students in each house of class 12D of your school.

      Note: Assume four house names are Beas, Chenab, Ravi and Satluj having
      18, 2, 20, 18 students respectively and pandas library has been imported as
      pd.

23.   List any four benefits of e-waste management.                                      2
                             OR
      Mention any four net etiquettes.

24.   What will be the output of the following code:                                     2
            >>>import pandas as pd
            >>>A=pd.Series(data=[35,45,55,40])
            >>>print(A>45)

25.   Carefully observe the following code:                                              2

      import pandas as pd
      Year1={'Q1':5000,'Q2':8000,'Q3':12000,'Q4': 18000}
      Year2={'A' :13000,'B':14000,'C':12000}
      totSales={1:Year1,2:Year2}
      df=pd.DataFrame(totSales)
      print(df)

      Answer the following:

        i.   List the index of the DataFrame df
       ii.   List the column names of DataFrame df.
```

---

## page 5

```
                                     SECTION C
26.   Write outputs for SQL queries (i) to (iii) which are based on the given table 3
      PURCHASE:

                          TABLE: PURCHASE
       CNO        CNAME     CITY         QUANTITY                      DOP
       C01        GURPREET NEW DELHI     150                           2022-06-11
       C02        MALIKA    HYDERABAD    10                            2022-02-19
       C03        NADAR     DALHOUSIE    100                           2021-12-04
       C04        SAHIB     CHANDIGARH 50                              2021-10-10
       C05        MEHAK     CHANDIGARH 15                              2021-10-20

           i.   SELECT LENGTH(CNAME) FROM PURCHASE WHERE
                QUANTITY>100;
          ii.   SELECT CNAME FROM PURCHASE WHERE
                MONTH(DOP)=3;
       iii.     SELECT MOD (QUANTITY, DAY(DOP)) FROM PURCHASE
                WHERE CITY= ‘CHANDIGARH’;
27.   Write a Python code to create a DataFrame with appropriate column headings 3
      from the list given below:

      [[101,'Gurman',98],[102,'Rajveer',95],[103,'Samar' ,96],[104,'Yuvraj',88]]

28.   Consider the given DataFrame ‘Stock’:                                         3

                 Name                             Price
      0          Nancy Drew                       150
      1          Hardy boys                       180
      2          Diary of a wimpy kid             225
      3          Harry Potter                     500

      Write suitable Python statements for the following:
        i.   Add a column called Special_Price with the following data:
             [135,150,200,440].
       ii.   Add a new book named ‘The Secret' having price 800.
      iii. Remove the column Special_Price.
29.   Nadar has recently shifted to a new city and school. She does not know many 3
      people in her new city and school. But all of a sudden, someone is posting
      negative, demeaning comments on her social networking profile etc.

      She is also getting repeated mails from unknown people. Every time she goes
      online, she finds someone chasing her online.

         i.     What is this happening to Nadar?
        ii.     What immediate action should she take to handle it?
       iii.     Is there any law in India to handle such issues? Discuss briefly.
```

---

## page 6

```
                                             OR
      What do you understand by plagiarism? Why is it a punishable offence? Mention
      any two ways to avoid plagiarism.
30.   Based on table STUDENT given here, write suitable SQL queries for the 3
      following:

             Roll No      Name       Class       Gender City            Marks
                 1        Abhishek      XI          M          Agra     430
                 2        Prateek       XII         M        Mumbai 440
                 3        Sneha         XI           F         Agra     470
                 4        Nancy         XII          F       Mumbai 492
                 5        Himnashu      XII         M          Delhi    360
                 6        Anchal        XI           F        Dubai     256
                 7        Mehar          X           F       Moscow 324
                 8        Nishant        X          M        Moscow 429
      i. Display gender wise highest marks.
      ii. Display city wise lowest marks.
      iii. Display total number of male and female students.
                                            OR
      Discuss the significance of Group by clause in detail with the help of suitable
      example.
                                        SECTION D
31.   Write suitable SQL query for the following:                                       5
          i.   Display 7 characters extracted from 7th left character onwards from the
               string ‘INDIA SHINING’.
         ii.   Display the position of occurrence of string ‘COME’ in the string
               ‘WELCOME WORLD’.
        iii. Round off the value 23.78 to one decimal place.
        iv.    Display the remainder of 100 divided by 9.
         v.    Remove all the expected leading and trailing spaces from a column userid
               of the table ‘USERS’.
                                           OR
      Explain the following SQL functions using suitable examples.
         i.      UCASE()
         ii.     TRIM()
         iii.    MID()
         iv.     DAYNAME()
         v.      POWER()

32.   Prime Computer services Ltd. is an international educational organization. It is 5
      planning to set up its India campus at Mumbai with its head office in Delhi. The
      Mumbai office campus has four main buildings-ADMIN, ACCOUNTS,
      EXAMINATION and RESULT.
```

---

## page 7

```
You as a network expert have to suggest the best network related solutions for
their problems raised in (i) to (v), keeping in mind the distances between the
buildings and other given parameters.

                               MUMBAI CAMPUS
DELHI HEAD OFFICE
                                                        ACCOUNTS
                               EXAMINATION

                               ADMIN                             RESULT



Shortest distances between various buildings:
 ADMIN TO ACCOUNTS                        55 m
 ADMIN TO EXAMINATION                     90 m
 ADMIN TO RESULT                          50 m
 ACCOUNTS TO EXAMINATION                  55 m
 ACCOUNTS TO RESULT                       50 m
 EXAMINATION TO RESULT                    45 m
 DELHI Head Office to MUMBAI              2150 m
 campus

Number of computers installed at various buildings are as follows:
 ADMIN                                       110
 ACCOUNTS                                    75
 EXAMINATION                                 40
 RESULT                                      12
 DELHI HEAD OFFICE                           20
   (i)    Suggest the most appropriate location of the server inside the
          MUMBAI campus (out of the four buildings) to get the best
          connectivity for maximum number of computers. Justify your answer.
   (ii)   Suggest and draw cable layout to efficiently connect various buildings
          within the MUMBAI campus for a wired connectivity.
  (iii)    Which networking device will you suggest to be procured by the
           company to interconnect all the computers of various buildings of
           MUMBAI campus?
  (iv)     Company is planning to get its website designed which will allow
           students to see their results after registering themselves on its server.
           Out of the static or dynamic, which type of website will you suggest?
  (v)      Which of the following will you suggest to establish the online face
           to face communication between the people in the ADMIN office of
           Mumbai campus and Delhi head office?
               a)     Cable TV
               b)     Email
               c)     Video conferencing
               d)     Text chat
```

---

## page 8

```
33.   Write Python code to plot a bar chart for India’s medal tally as shown below:       5




      Also give suitable python statement to save this chart.
                                           OR
      Write a python program to plot a line chart based on the given data to depict the
      changing weekly average temperature in Delhi for four weeks.

      Week=[1,2,3,4]
      Avg_week_temp=[40,42,38,44]
                                         SECTION E
34.   Shreya, a database administrator has designed a database for a clothing shop.       1+1+2
      Help her by writing answers of the following questions based on the given
      table:                       TABLE: CLOTH

       CCODE      CNAME          SIZE COLOR             PRICE DOP
       C001       JEANS          XL       BLUE          990       2022-01-21
       C002       T SHIRT        M        RED           599       2021-12-12
       C003       TROUSER M               GREY          399       2021-11-10
       C004       SAREE          FREE GREEN             1299      2019-11-12
       C005       KURTI          L        WHITE         399       2021-12-07
         i.   Write a query to display cloth names in lower case.
         ii.  Write a query to display the lowest price of the cloths.
         iii. Write a query to count total number of cloths purchased of medium
              size.
```

---

## page 9

```
                                    OR (Option for part iii only)

                Write a query to count year wise total number of cloths purchased.
35.   Mr. Som, a data analyst has designed the DataFrame df that contains data about
      Computer Olympiad with ‘CO1’, ‘CO2’, ‘CO3’, ‘CO4’, ‘CO5’ as indexes shown
      below. Answer the following questions:

                    School         Tot_students     Topper          First_Runnerup
       CO1          PPS            40               32              8                  1+1+2
       CO2          JPS            30               18              12
       CO3          GPS            20               18              2
       CO4          MPS            18               10              8
       CO5          BPS            28               20              8

         A. Predict the output of the following python statement:
            i.      df.shape
            ii.     df[2:4]
         B. Write Python statement to display the data of Topper column of indexes
            CO2 to CO4.
                                      OR (Option for part iii only)
            Write Python statement to compute and display the difference of data of
            Tot_students column and First_Runnerup column of the above given
            DataFrame.
```