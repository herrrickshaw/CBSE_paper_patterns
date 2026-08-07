---
title: "InformaticsPractices-MS"
source_pdf: "InformaticsPractices-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/InformaticsPractices-MS.pdf"
pages: 8
pdf_bytes: 524842
pdf_sha256: "866832a0e3620087b8e3d3c81d4bbbd9b86ac562c4fd9cec1df3aa2bc4ae4b19"
text_chars: 11900
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPractices-MS


---

## page 1

```
                                           MARKING SCHEME

                                                CLASS XII

                                    INFORMATICS PRACTICES (065)

TIME: 3 HOURS                                                     M.M.70



 1.        iii. MAN                                                  1

           1 mark for correct answer

 2.        ii. Installing antivirus for protection                   1

           1 mark for correct answer

 3.        iii. Unused old computers                                 1

           1 mark for correct answer

 4.        iii. Null value                                           1

           1 mark for correct answer

 5.        i. 20500                                                  1

           1 mark for correct answer

 6.        ii. Open                                                  1

           1 mark for correct answer

 7.        ii. SELECT COUNT (*) FROM ORDERS;                         1

           1 mark for correct answer

 8.        i. ROUND( )                                               1

           1 mark for correct answer

 9.        i. MAX ()                                                 1

           1 mark for correct answer

 10.       iv. S.tail()                                              1

           1 mark for correct answer

 11.       iii. import pandas as pd                                  1

           1 mark for correct answer

 12.       iv. All of these                                          1
```

---

## page 2

```
      1 mark for correct answer

13.   iii. Avast                                                              1

      1 mark for correct answer

14.   iv. Now()                                                               1

      1 mark for correct answer

15.   i. Copyright                                                            1

      1 mark for correct answer

16.   iii. Digital footprint                                                  1

      1 mark for correct answer

17.   iii. A is True but R is False                                           1

18.   i. Both A and R are true and R is the correct explanation for A         1

19.   Web Page: A Web Page is a part of a website and is commonly written 2
      in HTML. It can be accessed through a web browser.

      Home Page: It is the first web page you see when you visit a website.

      1 mark for correct explanation of each term

                                      Or

      Four networking goals are:
         i.     Resource sharing
         ii.    Reliability
         iii.   Cost effective
         iv.    Fast data sharing

      ½ mark for each goal

20.   The problem with the given SQL query is that WHERE clause should not be 2
      used with Group By clause.

      To correct the error, HAVING clause should be used instead of WHERE.

      Corrected Query:

      SELECT HOUSE, COUNT(*) FROM STUDENT GROUP BY HOUSE HAVING
      HOUSE= ‘RED’ OR HOUSE=’YELLOW’;



      1 Mark for error identification
      1 Mark for writing correct query
```

---

## page 3

```
21.   Order By clause:                                                                2

      The ORDER BY command is used to sort the result set in ascending or
      descending order.

      The following SQL statement displays all the customer’s names in alphabetical
      order:

      SELECT Cname FROM Customers ORDER BY Cname;

      1 mark for correct purpose
      1 mark for correct example
22.   St={‘Beas’ :18, ‘Chenab’ :20 , ‘ Ravi’ :20, ‘ Satluj’ :18}                      2
      S1=pd.Series(St)

      1 mark for each correct python statement
23.   The e-waste management-                                                         2

             i.        Saves the environment and natural resources
             ii.       Allows for recovery of precious metals
             iii.      Protects public health and water quality
             iv.       Saves landfill space

      ½ mark for each benefit

                                   Or

      i.            No copyright violation
      ii.           Share the expertise with others on the internet
      iii.          Avoid cyber bullying
      iv.           Respect other’s privacy and diversity

      ½ mark for each net etiquette

24.                                                                                   2




      ½ mark for each correct output

25.          i.        The index labels of df will include Q1,Q2,Q3,Q4,A,B,C          2
             ii.       The column names of df will be: 1,2

      1 mark for each correct answer

26.      i.         8                                                                 3
        ii.         No Output
       iii.         0
                    15
```

---

## page 4

```
      1 mark for each correct output

27.   import pandas as pd                                                                 3
      data=[[101,'Gurman',98],[102,'Rajveer',95],[103,'Samar' ,96],
      [104,'Yuvraj',88]]
      df=pd.DataFrame(data,columns=['Rno','Name', 'Marks'])


      1 mark for each correct python statement

28.       i.        Stock['Special_Price']=[135,150,200,400]                              3
          ii.       Stock.loc['4']=['The Secret',800]
          iii.      Stock=Stock.drop('Special_Price',axis=1)

      1 mark for each correct statement
29.      i.       Nadar has become a victim of cyber bullying and cyber stalking.    3
         ii.      She must immediately bring it into the notice of her parents and
                  school authorities. And she must report this cyber crime to local
                  police with the help of her parents.
         iii.     Yes.
                  The Information Technology Act, 2000 (also known as ITA-2000,
                  or the IT Act) is the primary law in India dealing with cybercrime
                  and electronic commerce.


      1 mark for each correct answer

                                                OR

      Ans. Plagiarism is the act of using or stealing someone else’s intellectual work,
      ideas etc. and passing it as your own work. In other words, plagiarism is a
      failure in giving credit to its source.

      Plagiarism is a fraud and violation of Intellectual Property Rights. Since IPR
      holds a legal entity status, violating its owners right is a legally punishable
      offence.

      Any two ways to avoid plagiarism:

                Be original
                Cite/acknowledge the source


      1 mark for correct definition
      1 mark for correct justification
      ½ mark each for any two ways to avoid plagiarism
```

---

## page 5

```
30.   i. select max(marks) from student group by gender;                            3
      ii. select min(marks) from student group by city;
      iii. select gender,count(gender) from student group by gender;

      1 mark for each correct query

                               OR
      GROUP BY clause is used in a SELECT statement in combination with aggregate
      functions to group the result based on distinct values in a column.

      For example:


      To display total number of male and female students from the table
      STUDENT, we need to first group records based on the gender then we should
      count records with the help of count() function.

      Considering the following table STUDENT:
       RollNo        Name        Class       Gender       City         Marks
           1         Abhishek      XI          M           Agra        430
           2         Prateek       XII         M          Mumbai       440
           3         Sneha         XI           F          Agra        470
           4         Nancy         XII          F         Mumbai       492
           5         Himnashu      XII         M           Delhi       360
           6         Anchal        XI           F          Dubai       256
           7         Mehar          X           F         Moscow       324
           8         Nishant        X          M          Moscow       429

      SQL query for the above-mentioned task is as follows:

      select gender,count(gender) from student group by gender;

      Output:
      Gender      Count(Gender)
      M             4
      F             4

      1 mark for correct significance
      2 marks for correct example
31.      i.       select mid('INDIA SHINING',7,7);                                  5
         ii.      select INSTR('WELCOME WORLD','COME');
         iii.     select round(23.78,1);
         iv.      select mod(100,9);
         v.       select trim(userid) from users;

      1 mark for each correct query
```

---

## page 6

```
                  OR
      1. UCASE(): It converts the string into upper case.
      Example:
              SELECT UCASE(‘welcome world’);
      Output:

      WELCOME WORLD

      2. TRIM(): It removes the leading and trailing spaces from the given string.
      Example:
               SELECT TRIM(‘           Welcome world     ‘ );
      Output:
              Welcome world
      3. MID(): It extracts the specified number of characters from given string.
      Example:
                SELECT MID(‘ Welcome world,4,,4);
      Output:
                Come
      4. DAYNAME(): It returns the weekday name for a given date
      Example:
                SELECT DAYNAME(‘2022-07-22’);
      Output:
                 Friday
      5. POWER(): It returns the value of a number raised to the power of another
      number.
      Example:
              SELECT POW(6,2);
      Output:
              36

      ½ mark for each correct explanation
      ½ mark for each correct example
32.      i.      Server should be installed in Admin department as it has            5
                 maximum number of computers.


          ii.
                                           examination


                 Admin
                                             accounts



                                             Result
                  Star topology
```

---

## page 7

```
          iii.          Hub/Switch
          iv.           Dynamic
          v.            Video conferencing

      1 Mark for each correct answer
33.   import matplotlib.pyplot as plt                                         5
      Category=['Gold','Silver','Bronze']
      Medal=[20,15,18]
      plt.bar(Category,Medal)
      plt.ylabel('Medal')
      plt.xlabel('Medal Type')
      plt.title('Indian Medal tally in Olympics')
      plt.show()

      ½ mark for each correct statement

      Python statement to save the chart:

      plt.savefig("aa.jpg")

      1 mark for the correct statement

                                                OR

      import matplotlib.pyplot as plt
      Week=[1,2,3,4]
      Avg_week_temp=[40,42,38,44]
      plt.plot(Week,Avg_week_temp)
      plt.show()

      1 mark for each correct statement
34.           i.     SELECT LOWER(CNAME) FROM CLOTH;                          1+1+2
              ii.    SELECT MIN(PRICE) FROM CLOTH;

                            1 mark for each correct query

                 iii.       SELECT COUNT(*) FROM CLOTH GROUP BY SIZE HAVING
                            SIZE='M';
                                                   OR
                            SELECT YEAR(DOP),COUNT(*) FROM CLOTH GROUP BY
                            YEAR(DOP);

                            2 marks for correct query

35.   A. Output:                                                              1+1+2

          i.            (5,4)
```

---

## page 8

```
    ii.     School       tot_students        Topper     First_Runner_up
   CO3       GPS           20                18         2
   CO4       MPS           18                10         8

                 1 mark for each correct output

B. Python statement:

print(df.loc['CO2': 'CO4', 'Topper'])
                                        OR

print(df.Tot_students-df.First_Runnerup)

                 2 marks for correct Python statement
```