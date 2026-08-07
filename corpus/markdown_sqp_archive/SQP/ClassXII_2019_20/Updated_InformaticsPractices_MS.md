---
title: "Updated InformaticsPractices MS"
source_pdf: "Updated_InformaticsPractices_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/Updated_InformaticsPractices_MS.pdf"
pages: 7
pdf_bytes: 290760
pdf_sha256: "f2ea06c7c1d7ed470505d7c160603edeb370e9979a328e8d6cc29ee35ada0a0f"
text_chars: 23427
low_text_pages: 0
converter: "pdftotext -layout"
---

# Updated InformaticsPractices MS


---

## page 1

```
                         CLASS XII INFORMATICS PRACTICES
                           - New (065) Marking Scheme - SQP
                                        (2019-20)

  Max. Marks: 70                                                                  Time: 3 hrs

                                                   Section A

Q1 a) Ans    [40 50 60 70]                                                       (1 mark for correct
                                                                                 output)

   b) Ans    print(np.cov(data,ddof=0))                                          (1     mark       for
                                                                                 appropriate function var)

   c)Ans    (i)    import pandas as pd                                           (½ mark for import
                  df=pd.DataFrame()                                              statement and ½ mark for
                  print(df)                                                      correct DataFrame create
                                                                                 statement)
                                              OR
              Student_df[‘marks’.min()]                                          (1 mark for correct statement)



   d) Ans    [12 16 ]                                                            (1 mark for correct
                                                                                 output)

   e) Ans   import matplotlib.pyplot as plt                                              2 marks
            import numpy as np                                                   (½ mark for each import
            objects=(‘2015’, 2016’, ‘2017’, ‘2018’)                              statement) (½ mark for
            y_pos=np.arrange(len(objects))                                       using arange())
            percentage=[82,83,85,90]                                             (½ mark for using
                                                                                 plot statement, labeling the
            plt.bar(y_pos, percentage, align=’Centre’, color=’Blue’)
                                                                                 axes and show())
            plt.xticks(y_pos,objects)
            plt.ylabel(“Pass Percentage”)
            plt.xlabel(‘Years’)
            plt.show()

   f) Ans    Pandas Series is a one-dimensional labeled array capable of                2 marks
             holding data of any type (integer, string, float, python objects,
             etc.). The axis labels are collectively called index.Example        (1 mark for definition and 1
             importpandas as pd                                                  mark for example)

             # simple array
             data =pd.Series([1,2,3,4,5])
             print(data)

   g) Ans   List=[20,30,40,60,80,120]                                            ½ Mark to initialize flag
            Flag=0                                                               and pos
            No=int(Input(“Enter a value”))                                       ½ Mark for input statement
            pos=0                                                                ½ Mark for correctly
            for I in List:                                                       writing the loop
                 if no==i:                                                       1 mark for the correct if
                     prnt(“Found at position=”, pos+1)                           statement to search for
                     Flag=1                                                      the number
                     break                                                       ½ Mark for the correct
                 pos=pos+1                                                       print statement-value is
            if Flag==0:                                                          not found
                print(“value not found”)
```

---

## page 2

```
                                                 OR                            ½ Mark to initialize min
              List=[100,150,90,65,180,200]                                     ½ mark for correct loop
              min=List[0]                                                      1 mark for correct if
              for i in List:                                                   construct to find the
                  if i<min:                                                    minimum value in the list
                       min=i                                                   1 Mark for the print
               print(“Minimum Value is”, min)                                  statement


Q2 a) Ans      (ii) reindex                                                    (1 mark for correct
                                                                               answer)


   b) Ans      df.tail(4)                                                      (1 mark for correct
                                                                               answer)
                                                  OR

               Studdf.pivot_table(index=’Stream’, Values=’marks’,
               aggfunc=’mean’)
   c) Ans      0.50    8.0                                                     (1 mark for each
               0.75    11.0                                                    correct    line   of
                                                                               output)
   d) Ans      # Drop rows with label 0                                        ( 1 mark for giving
               df = df.drop(0)                                                 complete        and
               print(df )                                                      correct code)


   e)   Ans    Pivoting means to use unique values from specified              (1 mark for correct
               index/columns to form apex of the resulting dataframe.          definition and ½ mark
               Pivot() and pivot_table() methods                               for        each correct
                                                                               example)

   f) Ans      import pandas as pd

               # initialize list of lists
               data = [['S101', 'Amy', 70], ['S102', 'Bandhi', 69], ['S104',
               'Cathy', 75], ['S105', 'Gundaho', 82]]
                                                                                      2 marks
               # Create the pandas DataFrame
               df = pd.DataFrame(data, columns = ['ID', 'Name', 'Marks'])      (½ mark for correct
                                                                               initialization, 1 mark for
               # printdataframe.                                               correct dataframe and ½
               print(df )                                                      mark         for   printing
                                                                               dataframe)
                                                  OR

              import pandas as pd
              df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b']) df2 =
              pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b']) df =
              df.append(df2)
    g)Ans       (i) print(df.mean(axis = 1))                                          3 marks
                         print(df.mean(axis = 0))
                (ii) print(df.sum(axis = 1))                                   (1 mark for each
                (iii) print(df.median())                                       correct code )




                                                                                         2
```

---

## page 3

```
                                            OR
             (i) df1.sum()
             (ii) df1[‘Rainfall’].mean()
             (iii) df1.loc[:, ‘Maxtemp’].median( )

     h)Ans         a b                                                               3 marks
                                                                              (½ mark for each
             first 10 20                                                      correct output)
             second 6 32
                   a b1
             first 10 NaN
             second 6 NaN

     i)Ans   import numpy as np                                                      4 marks
             import pandas as pd                                              (1 mark for creating
             df1 = pd.DataFrame({'mark1':[30,40,15,40],                       each dataframe and
             'mark2':[20,45,30,70]});                                         ½ mark for each
             df2 = pd.DataFrame({'mark1':[10,20,20,50],                       correct command)
             'mark2':[15,25,30,30]});
             print(df1)
             print(df2)
              (i) print(df1.add(df2))
              (ii) print(df1.subtract(df2))
              (iii) df1.rename(columns={'mark1':'marks1'}, inplace=True)
             print(df1)
              (iv) df1.rename(index = {0: "zero", 1:"one"}, inplace = True)
             print(df1)

                                             Section B
Q3   a)Ans   Difficult to measure the progress in phases                      (1 mark for correct
                                                                              answer)

     b)Ans   Validation/Testing                                               (1 mark for correct
                                                                              answer)

     c)Ans   Improved code quality: As second partner reviews the code        (1 mark for correct
             simultaneously, it reduces the chances of mistake.               answer)


     d)Ans    The ScrumMaster is the servant leader to the Product                   2 marks
             Owner, Development Team and Organization with no                 (1 mark for correct
             hierarchical authority over the team but rather more of a        answer and 1 mark
             facilitator, the ScrumMaster ensures that the team adheres to    for             correct
             Scrum theory, practices, and rules.                              justification)
             The ScrumMaster protects the team by doing anything
             possible to help the team perform at the highest level.

                                             OR

             Incremental model works on the stage-wise development of
             a complex project that involves real time data whereas Spiral
             model works on risk analysis of a real time situation.

             Spiral model is a combination of both Incremental as well as
             Waterfall method.


                                                                                             3
```

---

## page 4

```
e)Ans   Situations to use/apply waterfall model                                  3 marks
        i) When project is small
                                                                           (1 mark for any
        ii) When problem is static.
                                                                           correct area of use 1
        iii) Clear and fixed requirements. Stable problem definition.
                                                                           mark     for   correct
        Technology is static.
                                                                           advantage    and 1
                                                                           mark     for   correct
        Advantage :
                                                                           disadvantage)
        Simple and easy to understand
        Disadvantage :
        No working software till the last phase

        OR

         Situations to use/apply spiral model
         When project is large,When releases are required to be
         frequent,When risk and costs evaluation is important
         For medium to high-risk projects

         Advantage- Additional functionality or changes can be done at
         a later stage
         Cost estimation becomes easy as the prototype building is
         done in small fragments
         Disadvantage-Risk of not meeting

f)Ans   The team members are not working in a systematic way and                3 marks
        they are not saving the versions of their work. Changes made in
        one part of the software can be incompatible with those made (1 mark for identifying
        by another developer working at the same time.                   the problem, 1 mark
        Version control exists to solve these problems, and it’s within for explaining version
        easy reach for every developer. Version control helps teams control and 1 mark
        solve these kinds of problems, tracking every individual change for its advantages)
        by each contributor and helping prevent concurrent work from
        conflicting.
        Further, in all software development, any change can
        introduce new bugs on its own and new software can't be
        trusted until it's tested. So testing and development proceed
        together until a new version is ready.



g)Ans                                                                            4 marks

                                                                           (2 marks for drawing
                                                                           use case and 1
                                                                           mark for each actor)




         Actors : Master, Trainee
         An actor is any entity (user or system) that interacts with the


                                                                                         4
```

---

## page 5

```
              system of interest. For an ATM, this includes:
              • Bank Customer
              • ATM Maintainer
              • Central Bank Computer



                                              OR
              A teacher is conducting an interview with a student. In the           (1½ mark for each
              course of that, the teacher always has to grade the student.          correct explanation
              Father and son cook dinner. In the course of that, one of them        and         1 mark
              always has to load the dishwasher.                                    explaining      the
              1.     B can execute the same use cases as A.                         relationship)
              2.     B inherits all of A's associations.

                                              Section C

Q4   a)Ans    python manage.py startapp users                                       (1 mark for correct
                                                                                    answer)

     b)Ans   The attribute(column) or set of attributes(columns) which is used to   (1 mark for correct
             identify a tuple/ row uniquely is known as Primary Key.                answer)
                                                OR

              DROP TABLE STUDENT


     c)Ans    Comma separated values                                                (1 mark for correct
                                                                                    answer)

     d)Ans    None value                                                            (1 mark for correct
                                                                                    answer)

     e)Ans    verify whether the python application is connected to mysql           (1 mark for correct
              database.                                                             answer)

     f)Ans    (i)Where clause is used to show data set for a table based on a        3 marks
              condition and having clause is used to put condition on the
              result set that comes after using Group by clause.              ( 1 mark for each
                                                                              correct difference)
              (ii)COUNT(*) returns the number of items in a group, including
              NULL values and duplicates. COUNT(expression) evaluates
              expression for each row in a group and returns the number of
              non null values.
              Candidate Key – A Candidate Key can be any column or a
              combination of columns that can qualify as unique key in
              database. There can be multiple Candidate Keys in one table.
              Each Candidate Key can qualify as Primary Key.
              Primary Key – A Primary Key is a column or a combination of
              columns that uniquely identify a record. Only one Candidate
              Key can be Primary Key.
              A table can have multiple Candidate Keys that are unique as
              single column or combined multiple columns to the table. They
              are all candidates for Primary Key.

     g)Ans                                                                               3 marks


                                                                                                5
```

---

## page 6

```
         (i) DELETE FROM CUSTOMER_DETAILS WHERE                         (½ mark for correct
         CUST_NAME=’Manpreet’;                                          Delete Statement
                                                                        and ½ mark for
         (ii)
                                                                        correct where
         +------------+                                                 clause)
         | max(DOJ) |
         +------------+                                                 (1 mark for correct
         | 1998-02-21 |                                                 output)
         +------------+

                                                                        (1 mark for correct
         (iii)Delete from Customer_Details where Accumlt_Amt is NULL;
                                                                        query)
h)Ans   (i) SELECT NAME,SALESAMT FROM STORE W HERE                        4 marks
               CITY=’MUMBAI’;
                                                                   (1 mark for each
        (II) SELECT * FROM STORE O R D E R BY NAME;
                                                                      correct query and
        ( II I) SELECT CIT Y, CO UNT (*) FRO M ST O RE G RO UP B Y
                ST O RE HAVING C O UNT(*)>2 ;                         ½ mark for each
                                                                      correct output)
        (iv)
        +---------------+
        | Min(DateOpen) |
        +---------------+
        | 2015-02-06 |
        +---------------+
        (v)
        +----------------+---------+
        | Count(StoreId) | NoOfEmp |
        +----------------+---------+
        |           1 | 10           |
        |           1 | 11           |
        |           1|5 |
        |           1|7 |
        +----------------+---------+

                                         OR                             (1 mark for each
                i. SELECT * FROM FANS ORDER BY FAN_DOB                     correct query)
                     DESC;
                ii. SELECT * FROM FANS WHERE
                     FAN_CITY<>’AJMER’;
                iii. SELECT FAN_MODE, COUNT(*) FROM FANS
                     GROUP BY FAN_MODE;
                iv. SELECT MAX(FAN_DOB) FROM FANS;




                                                                                      6
```

---

## page 7

```
                                             Section D
Q5   a)Ans    A remixed song is not an intellectual property                   (1 mark for correct
                                                                               answer)

     b) Ans   She has committed a fraud                                         (1 mark for correct
                                                                                answer)
     c) Ans  The  primary   law is Information Technology Act 2000.             (1 mark for correct
                                                                                answer)
     d) Ans She should check whether it is a valid bank site or not by            2 marks
             checking in the url https. It is always better to type the url and (1 mark for correct
             then login to the site. She should not click on the link provided answer)
             in the email.
     e)Ans Different types of ICT tools assist people with learning                   2 marks
            disabilities to achieve positive outcomes. They are :
            Talking Word processors                                            (1 mark for each
            Screen Readers                                                     correct point or any
            Conversion of local language to Braille                            other correct point)
            Eye Tracking mouse

     f)Ans    Role of Social Media Campaigns:-                                        3 marks
              A social media campaign should focus around a singular
                                                                              (1 mark for one
              business goal, whether it's on Facebook or Instagram. Common
                                                                              correct role of social
              goals for a social media campaigns include:
                                                                              media campaign, 1
                   Getting feedback from users.
                                                                              mark for one correct
                   Building email marketing lists
                                                                              role of
                   Increasing website traffic
                                                                              Crowdsourcing and 1
                                                                              mark for one correct
              Crowdsourcing is the practice of engaging a ‘crowd’ or group
                                                                              role of Smart mob)
              for a common goal — often innovation, problem solving, or
              efficiency. It is powered by new technologies, social media and
              web 2.0. Crowdsourcing can take place on many different
              levels and across various industries.

              Smart mobs, so named because each person in the
              group uses technology to receive information on where to go
              and what to do. This ability to stay on top of current events
              makes smart mobs extremely effective

                                            OR
                                                                                 (1 mark for each
              1. Give Your Electronic Waste to a Certified E-Waste Recycler       correct ways of
              2. Donating Your Outdated Technology                              disposing e waste)
              3. Give Back to Your Electronic Companies and Drop Off
              Points.




                                                                                             7
```