---
title: "InformaticsPractices-MS"
source_pdf: "InformaticsPractices-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/InformaticsPractices-MS.pdf"
pages: 7
pdf_bytes: 318222
pdf_sha256: "73fc17619e119331874d55418e896b539aab6d15527119eaad22bce8b14c0ac5"
text_chars: 12989
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPractices-MS


---

## page 1

```
                                MARKING SCHEME
                             SAMPLE QUESTION PAPER
                                   CLASS XII
                           INFORMATICS PRACTICES (065)
TIME: 03 HOURS                                                                            M.M.: 70
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

               1.   iii. Gateway                                                                 1
                    (1 mark for correct answer)

               2.   ii. Beryllium                                                                1
                    (1 mark for correct answer)

               3.   i. Intellectual Property Right                                               1
                    (1 mark for correct answer)

               4.   iv. NULL                                                                     1
                    (1 mark for correct answer)

               5.   iii. LENGTH ()                                                               1
                    (1 mark for correct answer)

               6.   iii. Google Chrome                                                           1
                    (1 mark for correct answer)

               7.   iii. Comma Separated Value                                                   1
                    (1 mark for correct answer)

               8.   iv. SELECT DEPT, AVG(SAL) FROM EMP GROUP BY DEPT HAVING                      1
                    COUNT(*) > 5;
                    (1 mark for correct answer)

               9.   iv. march                                                                    1
                    (1 mark for correct answer)

              10.     ii. NP.tail(3)                                                             1
                      (1 mark for correct answer)
```

---

## page 2

```
11.   iv. Month                                                                          1
      (1 mark for correct answer)

12.   iii. NaN                                                                           1
      (1 mark for correct answer)

13.   iv. Ransomware                                                                     1
      (1 mark for correct answer)

14.   iii. UPPER( )                                                                      1
      (1 mark for correct answer)

15.   i. Website                                                                         1
      (1 mark for correct answer)

16.   iii. Creative Commons                                                              1
      (1 mark for correct answer)

17.   i. Both A and R are true and R is the correct explanation for A                    1
      (1 mark for correct answer)

18.   iii. A is True but R is False                                                      1
      (1 mark for correct answer)

                                       SECTION B

19.    Web server: A web server is used to store and deliver the contents of a website   2
       to clients such as a browser that request it. A web server can be software or
       hardware.
       Web hosting: It is a service that allows to put a website or a web page onto
       the Internet, and make it a part of the World Wide Web.
      (1 mark each for each correct explanation)
                                              OR
      URL: It stands for Uniform Resource Locator. It provides the location and
      mechanism (protocol) to access the resources over the internet.

      URL is sometimes also called a web address. It not only contains the domain
      name, but other information as well that completes a web address.

      Examples:
      https://www.cbse.nic.in, https://www.mhrd.gov.in, http://www.ncert.nic.in,
      http://www.airindia.in, etc.
      (1 mark for correct explanation)
      (1 mark for correct example)
```

---

## page 3

```
20.   import pandas as pd                                                                  2
      df ={"Technology":["Programming","Robotics","3D
      Printing"],"Time(in months)":[4,4,3]}
      df= pd.DataFrame(df)
      print(df)
      (1/2 mark for each correction)

21.     i. SELECT INSTR("12#All the Best!","the");                                         2
        ii. SELECT RIGHT("12#All the Best!",5);
        (1 mark for each correct query)

22.           0 -10                                                                        2
              1 -20
              2 -30
              3 -10
              4 -20
              5 -30
       (2 marks for correct output)

23.    Active Digital Footprints: Active digital footprints include data that we           2
       intentionally submit online. This would include emails we write, or responses or
       posts we make on different websites or mobile Apps, etc.
       Passive Digital Footprints: The digital data trail we leave online
       unintentionally is called passive digital footprints. This includes the data
       generated when we visit a website, use a mobile App, browse Internet, etc.
       (2 marks for correct differentiation)

24.    import pandas as pd                                                                 2
       di = {'Corbett': 'Uttarakhand', 'Sariska':'Rajasthan', 'Kanha': 'Madhya
       Pradesh','Gir':'Gujarat'}
       NP = pd.Series( di)
       print(NP[ 'Sariska'])
       (1/2 mark for each correct fill-up)

25.    Aggregate functions: These are also called multiple row functions. These            2
       functions work on a set of records as a whole, and return a single value for each
       column of the records on which the function is applied.

       Max(), Min(), Avg(), Sum(), Count() and Count(*) are few examples of multiple
       row functions.
       (1 mark for correct explanation)
       (½ mark each for two correct names)
                                             SECTION C
```

---

## page 4

```
26.   i. SELECT FUEL, AVG(QT1) FROM CAR_SALES GROUP BY FUEL;   3
      ii. SELECT SEGMENT, MAX(QT2) FROM CAR_SALES GROUP BY
      SEGMENT;
       iii. SELECT * FROM CAR_SALES ORDER BY QT2 DESC;
      (1 mark for each correct query)
                                      OR
       i.
       +-----------------+
       | LEFT(SEGMENT,2) |
       +-----------------+
       | Co                     |
       | MU                     |
       | SU                     |
       | Se                     |
       +-----------------+
       ii.
       +------------+
       | AVG SALE        |
       +------------+
       | 13500.0000 |
       | 6000.0000 |
       +------------+
       iii.
       +----------+
       | TOT SALE |
       +----------+
       |     67000 |
       +----------+
       (1 mark each correct output)

27.   import pandas as pd #Statement 1                             3
      df=[["Divya","HR",95000],["Mamta","Marketing",97000
      ],["Payal","IT",980000], ["Deepak","Sales",79000]]
      #Statement 2
      df=pd.DataFrame(df,columns=["Name","Department",
      "Salary"])#Statement 3
      print(df) #Statement 4
      (#Statement 1 & 4 – ½ mark each)
      (#Statement 2 & 3 – 1 mark each)
```

---

## page 5

```
28.   i. CREATE DATABASE FOOD;                                                       3
       (1 mark for correct answer)
      ii. CREATE TABLE NUTRIENTS(NAME VARCHAR(20) PRIMARY
      KEY,CALORIES INTEGER);

       (½ mark for CREATE TABLE NUTRIENTS
       ½ mark each for correctly specifying each column
       ½ mark for correctly specifying primary key)

29.       i. She is a victim of Cyber Bullying.                                      3
          ii. Information Technology Act, 2000 (also known as IT Act).
          iii. a. Need to be careful while befriending unknown people on the
               internet.
               b. Never share personal credentials like username and password with
               others.
       (1 mark for each correct answer)
                                           OR
      Simran needs to be made aware of the following consequences:
          i) Eye strain      ii) Painful muscles and joints    iii) Poor memory
          iv) Lack of sleep v) Back pain and neck pain
       (1 mark each for writing any 3 correct health hazards)

30.        i. Genre["Num_Copies"]=[300,290,450,760]                                  3
           ii. Genre.loc[4]=["Folk Tale","FT",600]
          iii.Genre=Genre.rename({"Code":"Book_Code"},
          axis=1)
              OR
          Genre=Genre.rename({"Code":"Book_Code"},
          axis="columns")
       (1 mark for each correct statement)

                                      SECTION D

31.       i.  SELECT YEAR(MIN(TRANSACTION_DATE)) FROM                                4
             BLOCKCHAIN;
         ii. SELECT MONTH(MAX(TRANSACTION_DATE)) FROM
         BLOCKCHAIN;
         iii. SELECT * FROM BLOCKCHAIN WHERE MONTHNAME
      (TRANSACTION_DATE)='MAY';
         iv. SELECT COUNT(ID) FROM BLOCKCHAIN WHERE
         YEAR(TRANSACTION_DATE)=2022;
         (1 mark for each correct query)
```

---

## page 6

```
32.    i. a. 15                                                                      4
       b. Store Qtr1 Qtr2 Qtr3 Qtr4
          1 Store2 350 340 403 210
           2 Store3 250 180 145 160
       ( ½ mark for each correct output/statement)
       ii. df=df.drop(2)
                   OR
                df.drop(2,axis=0)
       (1 mark for correct statement)
       iii.
       df["total"]=df["Qtr1"]+df["Qtr2"]+df["Qtr3"]+df["Qtr
       4"]
                                            OR
                 df.to_csv(“D:\data.csv”)
         (2 mark for correct statement)

                                       SECTION E

33.        i. SELECT POWER(3,4);                                                     5
           ii. SELECT NOW();
           iii.SELECT ROUND(-34.4567,2);
           iv. SELECT TRIM(USERID) FROM USER;
            v. SELECT LENGTH("FIFA World Cup");
       (1 mark for each correct query)
                                         OR
       Ans:
        i. INSERT INTO EXAM VALUES(6,'Khushi','CS',85);
       ii. UPDATE EXAM SET subject= "Informatics
             Practices" where subject = "IP";
      iii. DELETE FROM EXAM WHERE marks<30;
       iv. ALTER TABLE EXAM ADD COLUMN grade varchar(2);
        v. Select * from exam where subject="Informatics
             Practices";
               (1 mark for each correct query)

34.      i. Z2 as it has maximum number of computers.                                5
         ii. For very fast and efficient connections between various blocks within
             the campus suitable topology: Star Topology
```

---

## page 7

```
          iii. Repeater: To be placed between Block Z2 to Z4 as distance between
               them is more than 100 metres.
               Hub/Switch: To be placed in each block as each block has many
               computers that needs to be included to form a network.
         iv. Voice Over Internet Protocol
         v. WAN as distance between Delhi and Mumbai is more than 40kms.
      (1 mark for each correct answer)

35.     import matplotlib.pyplot as plt #Statement 1                               5
        Height_cms=[145,141,142,142,143,143,141,140,143,144]
                                                       #Statement 2
        plt.hist(Height_cms)                           #Statement 3
        plt.title("Height Chart")                      #Statement 4
        plt.xlabel("Height in cms")                    #Statement 5
        plt.ylabel("Number of people") #Statement 6
        plt.show()                                     #Statement 7
      (½ mark each for each correct statement 1,2,4,5,6,7)
      (1 mark for correct statement 3)

       plt.savefig("heights.jpg")

      (1 mark for the correct statement)
                                          OR
      import matplotlib.pyplot as plt #Statement 1
      hobby = ('Dance', 'Music', 'Painting', 'Playing
      Sports')                               #Statement 2
      users = [300,400,100,500]              #Statement 3
      plt.bar(hobby, users)                  #Statement 4
      plt.title("Favourite Hobby")           #Statement 5
      plt.ylabel("Number of people")         #Statement 6
      plt.xlabel("Hobbies")                  #Statement 7
      plt.show()                             #Statement 8
      (½ mark for each correct statement)
      plt.savefig("hobbies.jpg")
      (1 mark for the correct statement)
```