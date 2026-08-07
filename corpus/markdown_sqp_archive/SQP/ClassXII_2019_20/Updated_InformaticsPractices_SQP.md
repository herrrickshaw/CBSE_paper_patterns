---
title: "Updated InformaticsPractices SQP"
source_pdf: "Updated_InformaticsPractices_SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/Updated_InformaticsPractices_SQP.pdf"
pages: 9
pdf_bytes: 267353
pdf_sha256: "d766977a8200036b49b473367b972e261f413cea86df89805cf5be0902657d9b"
text_chars: 15898
low_text_pages: 0
converter: "pdftotext -layout"
---

# Updated InformaticsPractices SQP


---

## page 1

```
                         CLASS XII INFORMATICS PRACTICES
                           NEW (065) SAMPLE QUESTION
                                   PAPER (2019-20)

    Max Marks: 70                                                                       Time: 3 hrs

    General Instructions:

           All questions are compulsory
           Question Paper is divided into 4 sections A,B,C and D.
           Section A comprises of questions(1 and 2)
           (i) Question 1 comprises Data Handling-2(DH-2) (Series,Numpy)
         (ii) Question 2 comprises of question from Data Handling -2(DH-2)(Data Frames and
          its operations)
        Section B comprises of questions from Basic Software Engineering.
           Section C comprises of questions from Data Management-2(DM-2)
           Section D comprises of questions from Society, Law and Ethics-2(SLE-2)


                                             Section A
Answer the following questions :
1    a)    Find the output of following program.                                                 1
           import numpy as np
           d=np.array([10,20,30,40,50,60,70])
           print(d[-4:])

     b)    Fill in the blank with appropriate numpy method to calculate and print the            1
           covariance of an array.
           import numpy as np
           data=np.array([1,2,3,4,5,6])
           print(np.      (data,ddof=0))

     c) Write a suitable Python code to create an empty dataframe.                               1
                                                  OR

           Consider the following dataframe : student_df
           Name         class        marks
           Anamay       XI           95
           Aditi       XI           82
           Mehak       XI            65
           Kriti      XI            45

           Write a statement to get the minimum value of the column marks.
```

---

## page 2

```
d)   Write the output of the following code :                                                   2

     import numpy as np
     array1=np.array([10,12,14,16,18,20,22])
     print(array1[1:5:2])




e)   Write a code to plot a bar chart to depict the pass percentage of students in CBSE exams   2
     for the years 2015 to 2018 as shown below-




f)   What is series? Explain with the help of an example.                                       2
g)   Write a code in Python to search for a given value in a list of elements(Without using in - 3
     built function)
     Example:
     If the List contains: [20,30,40,50,60,80,120]
     and the element to be searched is:60
     Then the output should be: Found at position 4

     OR

     Write a code in python to find the minimum value in a list.
     Example:
     If the List contains: [100,150,90,65,180,200]
     Then the output should be: Minimum Value is 65
```

---

## page 3

```
 Answer the following questions
2   a) _                 method in Pandas can be used to change the index of                      1
         rows and columns of a Series or Dataframe :
         (i) rename()
         (ii) reindex()
         (iii) reframe()
         (iv) none of the above

    b) Hitesh wants to display the last four rows of the data frame df and has                    1
         written the following code :
         df.tail()
         But last 5 rows are being displayed. Identify the error and rewrite the correct code
         so that last 4 rows get displayed.
                                                     OR
         A dataframe studdf stores data about the students stream, marks. A part of it is shown
         below:

         Class    Stream        Marks
         11       Science        95
         11       Commerce       80
         11       Arts           75
         11       Vocational     65

         Using the above dataframe, write the command to compute Average marks stream wise.

    c)   Consider the following python code and write the output for statement S1                 1
         import pandas as pd K=pd.Series([2,4,6,8,10,12,14])
         K.quantile([0.50,0.75]) ---------------------- S1


    d) Write a small python code to drop a row from dataframe labeled as 0.                       1

    e)   What is Pivoting? Name any two functions of Pandas which support                         2
         pivoting.

    f)   Write a python code to create a dataframe with appropriate headings from                 2
         the list given below :
         ['S101', 'Amy', 70], ['S102', 'Bandhi', 69], ['S104', 'Cathy', 75], ['S105',
         'Gundaho', 82]
                                                         OR
         Write a small python code to create a dataframe with headings(a and b)
         from the list given below : [[1,2],[3,4],[5,6],[7,8]]
```

---

## page 4

```
g)   Consider the following dataframe, and answer the questions given below:              3

     import pandas as pd
     df = pd.DataFrame({“Quarter1":[2000, 4000, 5000, 4400, 10000],
                 "Quarter2":[5800, 2500, 5400, 3000, 2900], "Quarter3":[20000,
                 16000, 7000, 3600, 8200], "Quarter4":[1400, 3700, 1700, 2000,
                 6000]})

     (i)      W rite the code to find mean value from above dataframe df over the index
              and column axis.
     (ii)     Use sum() function to find the sum of all the values over the index axis.
     (iii)    Find the median of the dataframe df.

                                                  OR

     Given a data frame df1 as shown below:

      City              Maxtemp       MinTemp          RainFall

      Delhi             40            32               24.1

      Bengaluru         31            25               36.2

      Chennai           35            27               40.8

      Mumbai            29            21               35.2

      Kolkata           39            23               41.8

     (i)      Write command to compute sum of every column of the data frame.
     (ii)     Write command to compute mean of column Rainfall.
     (iii)    Write command to compute Median of the Maxtemp Column.
h)   Find the output of the following code:                                               3

     import pandas as pd
     data = [{'a': 10, 'b': 20},{'a': 6, 'b': 32, 'c': 22}]
     #with two column indices, values same as dictionary keys
     df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
     #With two column indices with one index with other name
     df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
     print(df1)
     print(df2)
```

---

## page 5

```
    i)                                                                                       4
           Write the code in pandas to create the following dataframes :
                    df1                    df2
               mark1 mark2           mark1 mark2
           0 10         15       0    30        20
           1 40         45       1    20       25
           2 15         30       2    20       30
           3 40         70       3    50       30

           Write the commands to do the following operations on the dataframes given
           above :
            (i) To add dataframes df1 and df2.
            (ii) To subtract df2 from df1
            (iii) To rename column mark1 as marks1in both the dataframes df1 and df2.
            (iv) To change index label of df1 from 0 to zero and from 1 to one.




                                                  Section B

3   a)   Which of this is NOT an advantage of the waterfall model ?                          1
         (a) Simplicity
         (b) Easy to arrange the task
         (c) Clearly defined stages
         (d) Difficult to measure the progress in phases
    b) _                 _ is the process of checking the developed software for its         1
         correctness and error free working
          (i) Specification
          (ii) Design/Implementation
          (iii) Validation/Testing
          (iv) Evolution

    c)   Write down any one benefit of pair programming.                                     1
    d) In the Scrum process, a ScrumMaster differs from a traditional project                2
         manager. Justify the statement.

                                                     OR

         List any two differences between Incremental model and Spiral model in developing
         complex software projects.
```

---

## page 6

```
e)   Write down any one situation where waterfall software process can be        3
     used. Also mention one advantage and one disadvantage of waterfall software
     process.

                                                  OR

     Write down any one situation where spiral delivery model can be used. Also mention
     one advantage and one disadvantage of spiral delivery model.


f)   Gunveen, Marshy and Aloha are three developers working on an exciting                 3
     new app, and the launch day is just a day away. Gunveen creates an unmanaged
     package and saves it Aloha’s folder. Marshy also writes a new piece of code and saves
     it in Aloha’s folder. What could go wrong on the day of the launch? Explain and also
     mention how version control can help teams in this scenario.



g)   Draw a use case diagram and identify the actors for the situations (i) do (ii)              4
     as directed:
      (i) A repair can be made by a master, a trainee or any other repair shop employee.
      (ii) Consider an ATM system. Identify at least three different actors that interact with
             this system.
                                              OR

     (i)   Look at the following use case diagrams and write the actors and the situation
           depicted by the use case diagrams. Also explain the relationship depicted between
           A and B.

                                              A




                                                  B
```

---

## page 7

```
                                                  Section C

4   a)   Write the Django command to start a new app named ‘users’ in an existing                       1
         project?

    b)   What do you understand by Primary Key?                                                         1

                                                      OR

         Write the command to delete a table STUDENT.

    c)   CSV stands for _                                                                               1
    d)   NULL value means :                                                                             1
          (i) 0 value
          (ii) 1 value
          (iii) None value
          (iv) None of the above
    e)    is_connected() is the MYSQL function to :                                                     1
            (i) establish a connection to a mysql database from python.
            (ii) verify whether the python application is connected to mysql database. (iii) traverse
            through records in mysql database.
            (iv) None of the above

    f)    Shewani has recently started working in MySQL. Help her in                                    3
          understanding the difference between the following :
           (i) Where and having clause
           (ii) Count(column_name) and count(*)

    g)    On the basis of following table answer the given questions:                                   3


                                  Table: CUSTOMER_DETAILS

                                         ACCT_TY       ACCUMLT_A
          CUST_ID       CUST_NAME          PE             MT                DOJ         GENDER
          CNR_001           Manoj          Saving          101250       1992-02-19          M
          CNR_002           Rahul          Current         132250       1998-01-11          M
          CNR_004           Steve          Saving          18200        1998-02-21          M
          CNR_005        Manpreet        Current         NULL     1994-02-19      M
          (i)   Write the sql quer y to delete the record of customer
                  Manpreet.
          (ii)  What will be the output of the following query :
                 Select max(DOJ) From Customer_Details;
          (iii) Write the sql query to delete the row from the table where customer has no
                accumulated amount.
```

---

## page 8

```
h)    Write commands in SQL for (i) to (iii) and output for (iv) and (v).                      4
                                            Table : Store
       StoreId Name         Location             City      NoOfEmp DateOpen         SalesAmt

        S101      Planet Fashion Bandra           Mumbai         7     2015-10-16    40000

        S102      Vogue          Karol Bagh       Delhi          8     2015-07-14   120000

        S103      Trends         Powai            Mumbai         10    2015-06-24    30000

        S104      Super Fashion Thane             Mumbai         11    2015-02-06    45000

        S105      Annabelle      South Extn.      Delhi          8     2015-04-09    60000

        S106      Rage           Defence Colony Delhi            5     2015-03-01    20000

       (i) To display names of stores along with Sales Amount of those stores that are
             located in Mumbai.
        (ii) To display the details of store in alphabetical order of name.
       (iii) To display the City and the number of stores located in that City, only if
                number of stores is more than 2.
       (iv) SELECT MIN(DATEOPEN) FROM STORE;
       (v) SELECT COUNT(STOREID), NOOFEMP FROM STORE GROUP BY
             NOOFEMP HAVING MAX(SALESAMT)<60000;
                                                  OR

     (i) Consider the table FANS and answer the following.
                               FANS

      FAN_ID             FAN_NAME        FAN_CITY         FAN_DOB       FAN_MODE
      F001               SUSHANT         MUMBAI           1998-10-02    MAIL
      F002               RIYA            MUMBAI           1997-12-12    LETTER
      F003               ANIKA           DELHI            2001-06-30    BLOG
      F004               RUDRA           AJMER            2005-08-22    MAIL
      F006               MIARA           KOLKATTA         1998-11-01    BLOG


     Write MySQL queries for the following:

        i.     To display the details of fans in decending order of their DOB
        ii.    To display the details of FANS who does not belong to AJMER
        iii.   To count the total number of fans of each fan mode
        iv.    To display the dob of the youngest fan.
```

---

## page 9

```
                                                  Section D
5   a)   Which of the following is not an intellectual property?                           1
         (i) A poem written by a poet
         (ii) An original painting made by a painter
         (iii) Trademark of a Company
         (iv) A remixed song

    b)   Jhilmalini has stolen a credit card. She used that credit card to purchase a      1
         laptop. What type of offence has she committed?

    c)   Name the primary law in India dealing with cybercrime and electronic              1
         commerce.

    d)   Sutapa received an email from her bank stating that there is a problem with       2
         her account. The email provides instructions and a link, by clicking on which she
         can logon to her account and fix the problem. Help Sutapa by telling her the
         precautions she should take when she receives these type of emails.


    e)   Explain any two ways in which technology can help students with                   2
         disabilities.

    f)   Explain the role of online social media campaigns, crowdsourcing and              3
         smart mobs in society.
                                                        OR

         Ms Samtha has many electronics gadgets which are not usable due to outdated
         hardware and software. Help her to find any three best ways to dispose the used
         electronic gadgets.
```