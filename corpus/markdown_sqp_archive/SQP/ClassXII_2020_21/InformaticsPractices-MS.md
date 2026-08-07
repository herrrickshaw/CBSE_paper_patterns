---
title: "InformaticsPractices-MS"
source_pdf: "InformaticsPractices-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2024_25/InformaticsPractices-MS.pdf"
pages: 12
pdf_bytes: 331973
pdf_sha256: "8e2f843a6dddb143e915e51cc28ade38fe5d04e5d7bc6b754a2dd1c25dad9cad"
text_chars: 15956
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPractices-MS


---

## page 1

```
                                     Class XII
                            INFORMATICS PRACTICES (065)
                          SAMPLE QUESTION PAPER (2020 - 21)
                                  Marking Scheme




Max. Marks: 70                                                    Time: 3 hours

                                           Section A          Total
  Questi
  on No.
  1             i.     True                                   1
                ii.    False

           ½ mark for each correct answer
  2        plt.title()                                        1


           1 mark for correct answer

  3.       50                                                 1

           1 mark for the correct answer

  4        print(Sequences.head(4))                           1

           1 mark for the correct usage of head()

  5        print(S1+S2)                                       1

           1 mark for the correct print() statement

  6        histogram                                          1

           1 mark for the correct answer

  7        Firewall                                           1


           1 mark for the correct answer




                                                                      Page 1 of 12
```

---

## page 2

```
8    column                                       1

     1 mark for the correct answer

9    Bug                                          1

     1 mark for the correct answer

10   Dynamic web page                             1

     1 mark for the correct answer

11   Aggregate Function                           1

     1 mark for the correct answer

12   Plagiarism                                   1


     1 mark for the correct answer

13   isnull()                                     1

     1 mark for the correct answer

14   Cookies                                      1

     1 mark for the correct answer

15   c. Avast                                     1

     1 mark for the correct answer

16                                                1
     spam

     1 mark for the correct answer
17   Buy environmentally friendly electronics     1
     Donate used electronics to social programs
     Reuse , refurbish electronics
     Recycling e-waste
     Any other correct answer to be considered

     1 mark for the correct answer


                                                      Page 2 of 12
```

---

## page 3

```
18                                                                                  1
         update

         1 mark for the correct answer
19       Select now();                                                              1

         1 mark for the correct answer

20       Switch                                                                     1


         1 mark for the correct answer
21       Spam or spamming                                                           1

         I mark for the correct answer
22.(i)      b. print(df.max())                                                      4

         1 mark for the correct answer
(ii)     a. df1=df[df[‘rollno’]==4]
               print(df1)


         d.    df1=df[df.rollno==4]
                print(df1)

         ½ mark for mentioning option(a)

         ½ mark for mentioning option(d)
(iii)

         a. both (i) and (ii)

         1 mark for stating option “a” as correct answer ½ mark for staing option
         “b” as correct answer

(iv)     a. d. print(df.columns)

         1 mark for the correct answer
(v)      b. df [‘Grade’]=[’A’,’B’,’A’,’A’,’B’,’A’]
         1 mark for the correct answer
23 (i)   b. Both (iii) and (iv)                                                     4

         select name from student where city=”Agra” or
         city=”Mumbai”;
         or

                                                                                        Page 3 of 12
```

---

## page 4

```
        select name from student where city IN(“Agra”,
        “Mumbai”);

        d. Only (iii)
        iii. select name from student where city=”Agra” or
        city=”Mumbai”;

        1 mark for stating option b as correct answer
        ½ mark for stating d as correct answer

(ii)
        b.

             Rollno   Name      Class      DOB     Gender    City    Marks
                6     Maakhiy    XI     12/12/94      F      Dubai   256
                7     Neha        X     8/12/95       F     Moscow   324
                3     Geet       XI     6/5/97        F      Agra    470
                4     Preeti     XII    8/8/95        F     Mumbai   492


        1 mark for the correct answer

(iii)   d. Select class, max(marks) from student group
        by class;

        1 mark for the correct answer

(iv)    b. Both (ii) and (iv)


        Select gender, average(marks) from student group
        by gender where class=”XI”;
        or
        Select gender, average(marks) from student group
        by gender having class = “XI”;

        1 mark for the correct answer

(v)     b. select name,max(DOB) from student ;

        1 mark for the correct answer




                                                                             Page 4 of 12
```

---

## page 5

```
                               Section B


24   import pandas as pd                                               2
     m1=pd.Series([45,65,24,89],index=['term1','term2','t
     erm3','term4'])

     ½ mark for import statement
     ½ mark for usage of Series ()
     ½ mark for stating index as a list
     ½ mark for creating object m1

25   Differences between single row functions and multiple row         2
     functions.
     (i) Single row functions work on one row only whereas multiple
     row functions group rows
     (ii) Single row functions return one output per row whereas
     multiple row functions return only one output for a specified
     group of rows.




                                    OR
     The order by clause is used to show the contents of a
     table/relation in a sorted manner with respect to the column
     mentioned after the order by clause. The contents of the
     column can be arranged in ascending or descending order.

     The group by clause is used to group rows in a given column and
     then apply an aggregate function eg max(), min() etc on the
     entire group.
     (any other relevant answer)

     Single row v/s Multiple row functions
     1 mark for each valid point



     Group by v/s Order by
     1 mark for correct explanation
     1 mark for appropriate example

                                                                           Page 5 of 12
```

---

## page 6

```
26   i. select round(8459.2654);                                    2
     ii.select round(8459.2654,-2);

     1 mark each for correct answer of part (i) , (ii)
27   i. print(S_amt[S_amt>250])                                     2

     ii. S_amt.name=        'Furniture'

     1 mark each for correct answer of part (i) , (ii)
28   This is because the column commission contains a NULL value    2
     and the aggregate functions do not take into account NULL
     values. Thus Command1 returns the total number of records in
     the table whereas Command2 returns the total number of non
     NULL values in the column commission.
29                                                                  2
     a. select substr("Preoccupied", 4);
          or
        select substring("Preoccupied", 4);
          or
        select mid("Preoccupied",4);
          or
        select right(("Preoccupied"”, 8);

     b. select substr("Preoccupied" ,6,3);
          or
        select substring("Preoccupied", 6,3);
          or
        select mid(("Preoccupied" ,6,3);

                                     OR


     a. select instr 'Preoccupied' , ‘ 'cup'));
     b. select left 'Preoccupied',4);

     1 mark for each correct answer of part (a) , (b)

30   i.    classframe[‘Activity’]=[‘Swimming’,’Dancing              2
           ’,’Cricket’, ‘Singing’]
     ii.   classframe.loc[‘St5’]=[1,’Mridula’, ‘X’,
           ‘F’, 9.8, ‘Science’]


                                                                        Page 6 of 12
```

---

## page 7

```
     1 mark for each correct answer

31   a. SMTP: Simple Mail Transfer Protocol                                 2
     b. POP: Point to Point Protocol
     c. FTP: File Transfer Protocol
     d. VoIP: Voice over Internet Protocol

     ½ marks for each correct full form

32   The continuous use of devices like smartphones, computer               2
     desktop, laptops, head phones etc cause a lot of health hazards
     if not addressed. These are:
     i. Impact on bones and joints: wrong posture or long hours of
     sitting in an uncomfortable position can cause muscle or bone
     injury.
     ii. Impact on hearing: using headphones or earphones for a
     prolonged time and on high volume can cause hearing problems
     and in severe cases hearing impairments.
     iii. Impact on eyes: This is the most common form of health
     hazard as prolonged hours of screen time can lead to extreme
     strain in the eyes.
     iv. Sleep problem: Bright light from computer devices block a
     hormone called melatonin which helps us sleep. Thus we can
     experience sleep disorders leading to short sleep cycles.

     2 marks for any two correct points

33   We call this type of activity as Digital Footprints                    2


     Risk involved :
     It includes websites we visit emails we send, and any information we
     submit online,
     etc., along with the computer’s IP address, location, and other
     device specific details. Such data could be used for targeted
     advertisement or could also be misused or exploited.

     1 mark for naming the activity
     1 mark for mentioning any one risk .

34   a. will give the output as:                                            3
     [20,40,90,110,20,40,90,110]

     b. will give the output as
                                                                                Page 7 of 12
```

---

## page 8

```
     0     40
     1     80
     2    180
     3    220

     Justification: In the first statement x represents a list so when
     a list is multiplied by a number, it is replicated that many
     number of times.
     The second y represents a series. When a series is multiplied by
     a value, then each element of the series is multiplied by that
     number.

     1 mark for output of list multiplication
     1 mark for output of Series multiplication
     1 mark for the justification
35   Identity theft is the crime of obtaining the personal or financial   3
     information of another person for the sole purpose of assuming
     that person's name or identity to make transactions or use it to
     post inappropriate remarks , comments etc.
     Example:
     Alex likes to do his homework late at night. He uses the
     Internet a lot and also sends useful data through email to many
     of his friends. One Day he forgot to sign out from his email
     account. In the morning, his twin brother, Flex started using
     the computer. He used Flex’s email account to send
     inappropriate messages to his contacts

     Or any other relevant example

     1 ½ mark for explaining Identity theft
     1 ½ nark for suitable example

                                    OR
     Net Ettiquets refers to the proper manners and behaviour we
     need to exhibit while being online.

     These include :
     1. No copyright violation: we should not use copyrighted
     materials without the permission of the creator or owner. We
     should give proper credit to owners/creators of open source
     content when using them.
                                                                              Page 8 of 12
```

---

## page 9

```
     2. Avoid cyber bullying: Avoid any insulting, degrading
     or intimidating online behaviour like repeated
     posting of rumours, giving threats online,
     posting the victim’s personal information,
     or comments aimed to publicly ridicule a victim.

     Or any other relevant answer.

     1 marks for deifition of Net Ettiquettes
     1 mark eachfor the example with explanation.


36   import matplotlib.pyplot as plt                           3
     plt.plot([2,7],[1,6])
     plt.show()
      alternative answer
     import matplotlib.pyplot as plt
     a = [1,2,3,4,5,6]
     b = [2,3,4,5,6,7]
     plt.plot (a,b)
     1 mark for the import statement
     1 mark for appropriate usage of plot()
     1 mark for show()

                                     OR

     import matplotlib.pyplot as plt
     Classes = ['VII','VIII','IX','X']
     Students = [40,45,35,44]
     plt.bar(classes, students)
     plt.show()

     1 mark for the import statement
     1 mark for appropriate usage of pie()
     1 mark for show()

37   a. select Type, avg(Price) from Vehicle group by          3
     Type having Qty>20;
     b. select Company, count(distinct Type) from
     Vehicle group by Company;
     c. Select Type, sum(Price* Qty) from Vehicle
     group by Type;


                                                                   Page 9 of 12
```

---

## page 10

```
        a. ½ mark for the Select with avg(), ½ mark for the having
           clause
        b. ½ mark for the Select with count() , ½ mark for group by
           clause
        c. ½ mark for the Select with sum() , ½ mark for the group
           by clause



38                                                                    5
     import pandas as pd
     d1={'B_NO':[1,2,3,4],
         'Name':["Sunil Pillai","Gaurav
     Sharma","Piyush Goel","Kartik
     Thakur"],'Score1':[90,65,70,80],
     'Score2':[80,45,95,76]
            }
     df=pd.DataFrame(d1)
     print(df)
     df['Total'] = df['Score1']+ df['Score2']
     Alternative Answer
     Scheme
     df['Total'] = sum(df['Score1'], df['Score2'])
     print(df)
     print("Maximum scores are : " ,
     max(df['Score1']), max(df['Score2']))
     1 mark for import statement
     2 marks for creating the dataframe
     1 mark for creating column Total to hold the sum
     of scores
     1 mark for displaying highest scores in Score1 &
     Score2
39   i) monthname(date(now()))                                        5
     ii) trim(“ Panaroma “)
     iii) dayname(date(dob))
     iv)instr(name, fname)
     v) mod(n1,n2)
     1 mark for each correct answer

                                  OR



     i) Select sname, round(bonus,0) from Salesman;

                                                                          Page 10 of 12
```

---

## page 11

```
      ii) Select instr(Sname, “ta”) from Salesman;
      iii) Select mid(Sname,2,4) from Salesman;
      alternative answer
      iii) Select Substring(Sname,2,4) from Salesman;
      iv) Select monthname(DateofJoin) from Salesman;
      v) Select dayname(DateofJoin) from Salesman;
      1/2 mark each for correct usage of Select and round()
      1/2 mark each for correct usage of Select and instr()
      1/2 mark each for correct usage of Select and substr()
      1/2 mark each for correct usage of Select and monthname()
      1/2 mark each for correct usage of Select and dayname()

      Note : Instead of substr() , substring() may be accepted as
      correct



40.   i) Most suitable layout according to distance is :            5




                    W1                               W2




                    W3                                 W4




      1 mark for an appropriate cable layout
      ii) Star Topology
      1 mark for correct topology
      iii) Broadband.
      1 mark for suggesting suitable technology

                                                                        Page 11 of 12
```

---

## page 12

```
iv). a. Not required. Repeaters may be skipped as per above
layout (because distance is less than 100 m)
     b. In every wing

½ mark for placement of repeater ½ mark for placement of hub
/ switch
iv) Radio Waves
1 mark for the appropriate connectivity mode between HQ and
other offices




                                                               Page 12 of 12
```