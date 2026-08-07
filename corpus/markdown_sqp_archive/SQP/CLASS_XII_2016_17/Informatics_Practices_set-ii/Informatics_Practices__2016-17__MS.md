---
title: "Informatics Practices  2016-17  MS"
source_pdf: "Informatics_Practices__2016-17__MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2016_17/Informatics Practices set-ii/Informatics Practices _2016-17_ MS.pdf"
pages: 17
pdf_bytes: 112710
pdf_sha256: "85855809ba19cd0ab2c1f2791a12e42e653df59d0b102455cc7e78e527f1d984"
text_chars: 30127
low_text_pages: 0
converter: "pdftotext -layout"
---

# Informatics Practices  2016-17  MS


---

## page 1

```
                                  Sample Question Paper
                              Subject:Informatics Practices
                                           Class: XII
                                       Session 2016-17
Time: 3 Hrs.                                                                           M.M. – 70

1 (a)     After realizing the issues with proprietary software, Ms. Sunita has decided to use 1
           only Open Source Software. Suggest any one suitable open source software to
           her, for each of the following categories:
              i. Operating System
             ii. Browser
   Ans    i. Linux or Google Chrome OS or any other open source OS

          (½ Mark for correct answer)

          ii. Mozilla Firefox or Google Chrome or any other open source browser

          (½ Mark for correct answer)
   (b)     Expand the following:                                                                   1
           i. ODF       ii. PPP
   Ans     i. Open Document Format
           ii. Point to Point Protocol

          (½ Mark for each correct answer)
   (c)    What is Domain Name Resolution?                                                1
   Ans    Domain Name Resolution is the process of getting corresponding IP address from
          a domain name.

          (1 Mark for correct answer)
   (d)    How a Phonetic text entry is different from Keymap based text entry?                     1
   Ans    Phonetic text entry is different from keymap based text entry as in the keymap
          based text entry keyboard keys are mapped to specific characters using a keymap
          whereas in phonetic text entry text translation is done by some software based on
          probable pronunciation of the entered text.

          (1 Mark for correct difference)
   (e)    Which of the following activity can be termed as Eavesdropping:                          2
                 i. If Jack sets up an unauthorized parallel telephone line to capture the data.
                ii. If Jill has stolen his friend’s keyboard.
               iii. If Martina installs some receiver hardware to capture the data while on its
                    way.
               iv. If Kim gets someone’s login information by casually watching what
```

---

## page 2

```
             he/she is typing.

      Select the best suitable option from the following:
           i. Option i only
           ii. Option ii only
           iii. Option i and ii both
           iv. Option i and iii both
      How Eavesdropping is different from snooping by mentioning any one activity
      which will be termed as snooping?
Ans   iv. Option i and iii both
      (1 Mark for correct answer)
      Snooping refers to gaining unauthorized access to another person’s or
      organisation’s data: For e.g. Reading the files on someone’s computer in an
      unauthorized manner.
      (1 Mark for correct answer)
(f)   It’s an era of networking! Almost everyone and everything is connected through one way    4
      or the other, hats off to the technology. We have never been so much linked as we are
      today.
      Daniel has just started his hands on practice of networking. Help him in the following:
           I. He has just connected 10 computers of his resource room to establish a
                network. Name the network (LAN/MAN/PAN/WAN) which will be
                formed. Mention any two main benefits which Daniel could achieve
                by establishing a network.
         II. Help him in identifying the correct topology which has following
                characteristics:
                        Its very easy to diagnose the fault in this topology.
                        Failure of central hub/switch leads to failure of the entire
                            network.

                 Depict the topology by drawing the diagram showing 4 interconnected
                 computers through central hub/switch..
Ans      i. LAN

      (1 Mark for correct answer)

      Benefits of Networking:
          Resource sharing
          Cost saving
      (½ Mark for each correct benefit)

         ii. Star Topology

      (1 Mark for correct answer)
```

---

## page 3

```
        (1 Mark for correct diagram)
2 (a)   Shalini is learning Java programming language, as it allows developers to write 4
        code that can run on any machine, regardless of architecture or platform. Help her
        in finding solutions of her problems:
             I. She wants to compare two integer values for equality in her java code. Out
                    of (=) and (= =), which operator she should use and why?
             II. Help her in writing Java code to initialize two integer variables named
                    num1 and num2 with values 5 and 10 respectively. Increase the value
                    of num1 by 5 and decrease the value of num2 by 5.
  Ans   I.
        = = operator
        As = operator is assignment operator which will be used to assign the values to
        any variable/constant while = = is comparison operator for equality.

        (1 Mark for correct answer)
        (1 Mark for correct explanation)

        II.
        int num1=5, num2=10;
        num1=num1+5;
        num2=num2-5;

        (½ Mark for each correct statement)
  (b)   Mr. Sahil, a programmer in a VISA processing company, has written the 2
        following code:

        int ch=Integer.parseInt(jTextField1.getText());
        switch(ch)
        {
        case 1:
            jTextField2.setText(“Short Term Single Entry Visa Granted”);
        case 2:
            jTextField2.setText(“Short Term Multiple Entry Visa Granted”);
        case 3:
            jTextField2.setText(“Long Term Single Entry Visa Granted”);
        case 4:
            jTextField2.setText(“Long Term Multiple Entry Visa Granted”);
        default:
```

---

## page 4

```
          jTextField2.setText(“Invalid Entry”);
      }

      No matter what value is being entered in the text field jTextField1, this program
      always give a message “Invalid Entry”. Help Mr. Sahil in identifying the problem
      and its reason. Also suggest him a suitable correction in the code.
Ans   In absence of break ‘fall through’ condition occurs. As a result control will not
      be able to come out of the switch block after first matching. So all the messages
      will be overwritten by the last message i.e. “Invalid Entry” due to setText()
      method.

      He should use break statement in each case.

      (1 Mark for correct identification of the problem and reason)
      (1 Mark for correct correction)
(c)   Realizing the importance of the Internet, Ms. Shikha a Mathematics teacher, has 4
      decided to use Internet as a medium to teach her students Mathematics in an
      interesting way.

      I. She wants to design a webpage as shown below to create a mathematics tutorial
      on the topic “Shapes” using HTML.
               Mathematics in a fun way
        Shapes           Images
        Circle




       Square




      She has written following HTML code for the same but she is not getting the
      desired output. Help her in identifying the error(s) and suggest the suitable
      corrections:

       <html>
       <head><title>Shapes</title></head>
       <body>
       <table>
       <tr>
       <table heading>Mathematics in a fun way</table heading>
```

---

## page 5

```
       </tr>
       <tr>
       <td>Shapes</td>
       <td>Images</td>
       </tr>
       <tr>
       <td>Circle</td>
       <td><img source=“circle.jpg”></td>
       </tr>
       <tr>
       <td>Square</td>
       <td><img source=“square.jpg”></td>
       </tr>
       </table>
       </body>
       </html>


      II. Help her in matching Column A with suitable statements of Column ‘B’

       Column A                    Column B
       XML                         We use predefined tags to design
                                   webpages.
       It is designed to store and HTML
       transport data
       Tags are not case sensitive XML
       HTML                        Elements must have a closing
                                   tag.
Ans
       <html>
       <head><title>Shapes</title></head>
       <body>
       <table border=1>                                         //Correction 1
       <tr>
       <th colspan=2>Mathematics in a fun way</th>               //Correction 2 & 3
       </tr>
       <tr>
       <td>Shapes</td>
       <td>Images</td>
       </tr>
       <tr>
       <td>Circle</td>
       <td><img src=“circle.jpg”></td>                         //Correction 4
       </tr>
       <tr>
       <td>Square</td>
```

---

## page 6

```
          <td><img src=“square.jpg”></td>                               //Correction 4
          </tr>
          </table>
          </body>
          </html>

         (½ Mark for each correct correction)

         II.

          Column A                                     Column B
          XML                                          Elements must have a closing tag.
          It is designed to store and transport data   XML
          Tags are not case sensitive                  HTML
          HTML                                         We use predefined tags to design
                                                       webpages.

         (½ Mark for each correct matching)

3 (a)    In today’s digitized world with a need to store data electronically, it is very           4
         important to store the data in the databases. SQL is used to interact with the
         Database Management System.

         I. Classify the following commands according to their type :(DDL/DML)
                        i. INSERT INTO            ii. ALTER TABLE
         II. Which clause would you use with Select to achieve the following:
                i. To select the values that match with any value in a list of specified values.
               ii. Used to display unrepeated values of a column from a table.
         III. Chhavi has created a table named Orders, she has been asked to increase the
         value of a column named salesamount by 20. She has written the following query
         for the same.
                         Alter table Orders Add salesamount =salesamount+20;

         Is it the correct query? Justify.

  Ans:   I.
               i. INSERT INTO : DML command
               ii. ALTER TABLE : DDL command

         (½ Mark for each correct answer)
         II.
             a. IN
             b. Distinct

         (½ Mark for each correct answer)
```

---

## page 7

```
       III.
       No, Alter command is used to make changes to the structure of the table, but
       Chhavi has to make changes in the data stored in the table. Hence, she should
       write the following query:

                       Update Orders set salesamount =salesamount+20;

       (1 Mark for the justification)

       (1 Mark for the correct query)
(b)       I. Name any one Single row function and any one Aggregate function. Also 4
                 mention the difference in their working.

          II. Explain why the following queries give different outputs on execution:

                      i. SELECT COUNT(ENAME) FROM EMP;
                         Output:
                         5

                      ii. SELECT Count(*) FROM EMP;
                         Output:
                          8
Ans:   I.
       Single row function : Length() (any single row function)
       Aggregate Function : Max() (any other aggregate function)

       A single row functions works on every row of the table and hence gives output for
       each row in the table.
       An Aggregate function also known as Multiple row function works on a group of
       rows and returns only 1 output.

       (1 Mark for the writing any 1 valid Single row and Aggregate function)
       (1 Mark for writing the difference in their working)

       II.
       Aggregate functions ignore NULL values. The first query counts the Not Null
       values in the column ENAME hence the output is 5.

       But the second query counts all the records present in the table EMP which gives
       the output as 8.

       Hence this implies that there are 8 rows in the table and the Ename column
       contains the name of only 5 employees. 8-5 = 3, i.e. 3 names have been left blank.
       This means that there are 3 null values in the column ENAME.

       (1 Mark for giving individual explanation of the queries)
```

---

## page 8

```
         (2 Marks for giving individual explanation of the queries along with the reason
         for difference in the output)

         (½ Mark for identifying the error)
  (c)    Geetanjali had created a table “Customer” in the database “Test”. Immediately 2
         after the successful creation of the database, she wrote the Rollback command to
         undo the creation of the table. Did she execute rollback successfully? Explain.
  Ans:   A table in MYSQL is created using CREATE TABLE command which is a DDL
         command. A DDL command cannot be rolled back hence she needs to use the
         DROP TABLE command to remove the table.

         (2 Marks for the correct answer)

         (½ mark only for the identification of CREATE TABLE as a DDL command)

         (½ Mark only for suggesting the use of DROP TABLE command )
4 (a)    Ms. Meena is not able to understand the statement “Java is a case sensitive 1
         language”. Help her in understanding the above mentioned statement by giving
         suitable example.
  Ans    Java is a case sensitive language as java distinguish between uppercase and
         lowercase very strictly. For example:

         int num1, Num1;

         Although both variable have same name in the above statement but java will treat
         them two different variables due to first character in different case.

         (1 Mark for correct answer)
  (b)    Ms. Rachel is designing a frame in Netbeans in which she has used four Radio 1
         Button controls. She want that only one radio button out of four should be
         selected at a time. Which property of the Radio Button should be selected to
         acheive the same?
  Ans    buttonGroup

         (1 Mark for correct answer)
  (c)    What will be displayed in jTextArea1 after the following code is executed:         1

         int i;
         for(i=10;i<50;i=i+30)
         {
         i=i+15;
         jTextArea1.append(""+i);
         }
         jTextArea1.append("\n"+i);
  Ans    25
```

---

## page 9

```
      55

      (½ Mark for each correct output)
(d)   Do as directed :                                                                     4

      I. Find the output of the following Java code snippet after execution of each java
      statement labelled as Stmt 1, Stmt 2, Stmt 3, Stmt 4:

      String str1="VASUDHAIVA",str2="KUTUMBAKAM";
      jTextArea1.append((str1.substring(0,4))); //Stmt 1
      jTextArea1.append((str2.substring(4)));   //Stmt 2
      jTextArea1.setText(jTextArea1.getText()+jTextArea1.getText().length());//Stmt 3
      jOptionPane1.showMessageDialog(null,jTextArea1.getText().length()); //Stmt 4

      II. Rewrite the following code using do while loop:
      int num=Integer.parseInt(jTextField1.getText());
      while(num<=40)
      {
      jOptionPane1.showMessageDialog(null,num);
      num=num*20;
      }
      jOptionPane1.showMessageDialog(null,"Bye Bye");
Ans   I.
      VASU
      VASUMBAKAM
      VASUMBAKAM10
      12

      (½ Mark for each correct output)

      II.
      int num=Integer.parseInt(jTextField1.getText());
      do
      {
      jOptionPane1.showMessageDialog(null,num);
      num=num*20;
      } while(num<=40);
      jOptionPane1.showMessageDialog(null,"Bye Bye");

      (2 Mark for correct code in do while)
(e)   The following code has error(s). Rewrite the correct code underlining all the 2
      corrections made :
         value1=1, value2=2;
         while(value1<value2)
         jTextArea1.append ("\n"+value1*value2;
                     value1++
```

---

## page 10

```
         }

Ans     int value1=1, value2=2;                       //Correction 1
        while(value1<value2)
        {jTextArea1.append ("\n"+value1*value2);       //Correction 2 & 3
              value1++;                               //Correction 4
         }

      (½ Mark for each correct correction)
(f)   Mr. Ashish works as a programmer in “Universal Technologies Pvt. Ltd.”. He has
      designed a Library software to generate the member ship fee depending upon the
      membership type considering discount eligibility as well. A screenshot of the
      same is shown below:




      Help him in writing the code to do the following:

      i. After selecting appropriate Radio Button, when ‘Check Fee’ button is clicked,
      fee should be displayed in the respective text field according to the following
      criteria:

             Membership Type           Fee

                Monthly                500

               Quarterly              1000
```

---

## page 11

```
                Yearly                   1500

      ii. After selecting appropriate Radio Button, when ‘Check Discount’ button is 6
      clicked, appropriate discount should be displayed in the respective text field
      according to the following criteria:

          Discount Eligibility          Discount

               Students                   200

                Other                     100

      iii. When ‘Calculate’ button is clicked, Net Fee should be calculated and
      displayed in the respective text field as per the given formula:

                      Net Fee = Fee – Discount
      iv. When ‘Clear All’ button is clicked, All the text fields should be cleared.
Ans   i. Code for ‘Check Fee’ button:
      if (jRadioButton1.isSelected())
            jTextField3.setText("500");
      else if (jRadioButton2.isSelected())
            jTextField3.setText("1000");
      else if (jRadioButton3.isSelected())
            jTextField3.setText("1500");

      (2 Mark for correct code)

      ii. Code for ‘Check Discount’ button
      if(jRadioButton4.isSelected())
      jTextField4.setText("200");
      else if(jRadioButton5.isSelected())
      jTextField4.setText("100");

      (2 Mark for correct code)

      iii. Code for ‘Calculate’ button
      int fee=Integer.parseInt(jTextField3.getText());
      int disc=Integer.parseInt(jTextField4.getText());
      int net=fee-disc;
      jTextField5.setText(""+net);

      (1 Mark for correct code)

      iv. Code for ‘Clear All’ button
```

---

## page 12

```
         jTextField1.setText("");
         jTextField2.setText("");
         jTextField3.setText("");
         jTextField4.setText("");
         jTextField5.setText("");

         (1 Mark for correct code)
5 (a)    Write the output of the following SQL queries:                                      1
                SELECT POW(INSTR(‘My_Database’,’_’),2);
  Ans:   Output:
         9

         (1mark for the correct output)
  (b)    Is NULL and 0(zero) same?Jusify your answer.                                        1
  Ans:   No, it’s not the same as null means a value that is unavailable, unassigned or
         unknown and zero is a defined value.

         (1 mark for the correct answer)
  (c)    Observe the given table carefully and answer the following questions:               2

          PanNo            Name                   Phoneno          Address
          CIZPW123A        Rajesh Kumar           9599123456       WZ11 – Rajouri
                                                                   Garden, Delhi
          ABWQ2341B Hemant Kumar                  9812345678       Modern
                                                                   Apartments,
                                                                   Pitampura, Delhi
          DERA9786T        Naveen Sharma          7868654235       CA 22, Sector 21
                                                                   Rohini,Delhi
          PARD3457L        Sourabh Verma          8933217645       JD 61,
                                                                   Sector20,Gurgaon
          GDTF8762P        Nishant Kumar          NULL             Modern
                                                                   Apartments,
                                                                   Pitampura, Delhi
          MERT2376G        Hemant Kumar           9811110891       F40, Sector 19,
                                                                   Rohini, Delhi

           i.    Name the column that might have a Primary Key constraint. Justify your
                 answer.
          ii.    Name the column that might have a Unique constraint. Justify your
                 answer.
  Ans:        1. PanNo must be a Primary Key as it contains unique and NOT NULL
                 values.
              2. Phoneno must have a Unique constraint as it contains non repeating values
                 and a Unique constraint allows NULL values.

         (1 Mark each for correct identification of the column and the correct reason.)
```

---

## page 13

```
        (1 Mark for the correct identification of the columns)
(d)     Consider the following table:                                                     4
                                        Table: PharmaDB

         RxID     Drug DrugName          PricePharmacy           PharmacyLocation
                  ID                          Name
         R1000    5476 Amlodipine      100.00 Rx                 Pitampura, Delhi
                                              Pharmacy
         R1001    2345   Paracetamol 15.00 Raj                   Bahadurgarh,
                                              Medicos            Haryana
         R1002    1236   Nebistar      60.00 MyChemi             Rajouri Garden,
                                              st                 Delhi
         R1003    6512   VitaPlus      150.00 MyChemi            Gurgaon,Haryana
                                              st
         R1004    5631   Levocitrezine 110.00 RxPharma           South
                                              cy                 Extension,Delhi

        Write commands in SQL for (i) to (iv):
          i. To increase the price of “Amlodipine” by 50.
          ii. To display all those medicines whose price is in the range 100 to 150.
          iii. To display the Maximum price offered by pharmacy located in
                  “Gurgaon”
          iv. To display the Drug ID, DrugName and Pharmacy Name of all the
                  records in descending order of their price.
Ans :     i. Update PharmaDB set price = price+50 where DrugName =
                  “Amlodipine”;

        (½ Mark for correct usage of update )
        (½ Mark for correct condition )


           ii. Select * from PharmaDB where price between 100 and 150;

        (½ Mark for correct use of Select)
        (½ Mark for correct condition )

           iii. Select Max(Price) from PharmaDB where PharmacyLocation
                    like”%Gurgaon%”;
        (½ Mark for correct Select statement )
        (½ Mark for correct condition )

           iv. Select Drug ID, DrugName,PharmacyName from PharmaDB order by
                   Price desc;
        (½ Mark for correct use of Select )
        (½ Mark for order by )
(e)     On the basis of the Table Pharma ,write the output(s) produced by executing the   2
```

---

## page 14

```
         following queries:
             i. SELECT RxID, DrugName, Price from PharmaDB where PharmacyName
                    IN (“Rx Parmacy”, “Raj Medicos”);
            ii. SELECT PharmacyName, COUNT(*) FROM PharmaDB GROUP BY
                   PHARMACY NAME
  Ans
            i.

          RxID     DrugName        Price
          R1000    Amlodipine      100.00
          R1001    Paracetamol     15.00
          R1004    Levocitrezine   110.00

         (1 mark for the correct output)

            ii. Pharmacy Name | COUNT(*)
                   Rx Pharmacy   |   2
                   Raj Medicos    |  1
                   My Chemist    |   2

         (1 mark for the correct output)
6 (a)     Write SQL query to create a table “Job” with the following structure:            2
                                             Table: Job
           Field name         Datatype              Size Constraint
           J_Code             Integer               3     Primary Key
           J_Description      Varchar               25    Not Null
           J_Chg_Hr           Integer
           J_Lastupdate       Date
  Ans:   Create table Job
         (J_Code Integer(3) Primary Key,
          J_Description Varchar(25) Not Null,
          J_Chg_Hr Integer ,
         J_Lastupdate Date);

         (½ Mark for create table statement)
         (½ Mark for all the fieldnames with datatypes )
         (½ Mark for correct placement of Primary key constraint )
         (½ Mark for correct placement of Not null constraint )

  (b)     Consider the tables given below which are linked with each other and maintains   6
         referential integrity:
                                           Table: SAP

          SAPID               ItemCode             ItemName            ItemStorage
                                                                       Location
```

---

## page 15

```
         S1001                1001                 Receiver           W12-B3-R24
         S1002                1002                 Transponder        W13-B7-R87
         S1003                1003                 Battery Bank       W21-B1-R87
         S1004                1004                 Inverter           W21-B11-R2
         S1005                1005                 Genset             W22-B15-R16

                                            Table : Store

         StoreID              Item Code            StoreLocation      ReceivedDate
         1201                 1001                 Hauz Khas          2016/05/20
         1202                 1002                 Rajouri Garden     2016/06/14
         1203                 1003                 Rohini             2016/05/06
         1204                 1004                 Hauz Khaas         2016/07/15
         1205                 1005                 Rajendra Place     2016/05/27


        With reference to the above given tables, write commands in SQL for (i) and (ii)
        and output for (iii) below:
 i.     To display the ItemCode,ItemName and ReceivedDate of all the items .
Ans:    Select SAP.ItemCode,ItemName , ReceivedDate
         From SAP sa,Store st
         Where sa.ItemCode=st.ItemCode

        (½ Mark for correct usage of Select )
        (½ Mark for correct From statement )
        (1 Mark for the correct condition)
 ii.    To display SAPID,ItemName,ItemStorageLocation of all the items whose
        Received date is after 2nd May 2016.
Ans:    Select sa.SAPID,ItemName,ItemStorageLocation
         From SAP sa,Store st
         Where sa.ItemCode=st.ItemCode and Receiveddate >”2016/05/02”;

        (½ Mark for correct usage of Select )
        (½ Mark for correct From statement )
        (½ Mark for the correct join condition)
        (½ Mark for the correct condition on Receiveddate)
 iii.   SELECT sa.SAPID,ItemName,STOREID FROM SAP sa,Store st WHERE
        sa.ItemCode=st.ItemCode AND StoreLocation = “Hauz Khas”
Ans:     SAPID ItemNa        StoreID
                  me
         S1001 Receiver           1201

         S1004     Inverter          1204
```

---

## page 16

```
         (1 Mark for each row)
  (c)    What will be the degree and cardinality of the cartesian product formed while         1
         combining both the above given tables ‘SAP’ and ‘Store’ ?
  Ans:   Degree: 8
         Cardinality: 25

         (½ mark for each correct answer)
   (d)   Sangeeta is not able to add a new record in the table ‘Store’ through the following   1
         query:
         Insert into store values (1206,1006,’Karol Bagh’, ‘2016/07/25’);
         Identify the error if there is any.
  Ans:   As referential integrity is being maintained in between both the tables, ItemCode
         1006 cannot be inserted in the table store as there is no corresponding matching
         entry in the table SAP.

         (1 Mark for correct error finding)
7 (a)    Observe the given domains carefully and identify the category it belongs out of e-    1
         Governance/e-Business/e-Learning:
            i. AMAZON: www.amazon.in
            ii. PMO(Prime Minister’s office): www.pmo.gov.in
  Ans:      i. e- Business
            ii. e-Governance

         (½ Mark each for correct answer )
  (b)    Mention any one social and economic benefit of ICT.                                   2
  Ans:   Social Benefit :
            i. Social networking sites help people to stay in touch with their near and
                   dear ones.
         Economic Benefit:
            i. It helps economy grow at faster rate as it provides transparency in the
                   process and increases accountability.

         (1 Mark each for correct Social and Economic Benefit )
  (c)    Ms. Rachna, works as a programmer in ‘Plan My Trip’ travel company. She 2
         wishes to design a Flight booking page. Help her in choosing appropriate controls
         for the specified task from Text field, Label, Radio button, Check box, List box,
         Combo box, Button and write in the third column.
          S. No.     Control used to                  Control

          1          Traveler’s Name

          2          Source City/Destination City

          3          Trip Type (One Way Trip /
                     Round Trip / Multi City or
                     Stop Over)
```

---

## page 17

```
       4          Booking Class
                  (Economy/Premium
                  Economy/Business)
Ans
       S. No.     Control used to                Control

       1          Traveler’s Name                Text Field

       2          Source City/Destination City   Combo box

       3          Trip Type (One Way Trip /      Radio button
                  Round Trip / Multi City or
                  Stop Over)

       4          Booking Class                  Combo box/ Radio button
                  (Economy/Premium
                  Economy/Business)

      (1/2 mark for each correct answer)
```