---
title: "InformaticsPracticesOld SQP"
source_pdf: "InformaticsPracticesOld_SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2019_20/InformaticsPracticesOld_SQP.pdf"
pages: 8
pdf_bytes: 436015
pdf_sha256: "01d1e035c545977623b3aa639e99709bc52001495b72819ff33e9fe10b11a180"
text_chars: 17788
low_text_pages: 0
converter: "pdftotext -layout"
---

# InformaticsPracticesOld SQP


---

## page 1

```
                                                  Class XII
                                         Informatics Practices - OLD (265)
                                          Sample Question Paper 2019-20

Time allowed: 3 Hours                                                              Max. Marks: 70

General Instructions:
All questions are compulsory, however question number 2, 4 and 6 have internal choices.


                                                  Section-A

1.   (a) Which of the following are open standards?                                             1
         .OGG              .DOC           .BMP             .ODF

     (b) Ms. Ivana, a leading marketing professional working in a multinational company, is 1
        most of the time on move to cater her profession demands. Although she carries her
        laptop with her all the time but many a times she require to take some data from her
        office PC. She has to make several requesting phone calls to her colleague Ms. Barbara
        to send her required documents from her office PC. Suggest her any one popular
        software name so that she can herself remotely access her office PC anytime from
        anywhere.




     (c) Write the URL of any one e-Governance website.                                         1

     (d) International Tour and Travels company has set up its new branch office in Jaipur where 1
         different buildings are spanned over in the radius of 900 meter in Jaipur. Name the
         network formed in the following situations :
     (i) The branch office is connected with the regional office in New Delhi.
     (ii) All the buildings of branch office are connected to each other.

     (e) Deepti is confused between the terms ASCII and Unicode. Help her by differentiating    2
         between ASCII and Unicode.

     (f) Many of the programming brains has shifted their focus from Proprietary software to 4
         Free and Open software. Mention any two freedom offered by Free software.
         Going with the flow, Sandhya has downloaded a software from the internet which can
         be freely distributed and used by anyone but the source code is not available. Is it
         Freeware or free software? Justify your answer as well.
         Similarly Premjith wants to install a software on his system that can help him to create,
         edit and save office documents but he does not want to purchase the software. Suggest
         him a good software for the same.

                                                    1
```

---

## page 2

```
2.   (a) Ruby, a class XI student has just started learning java programming. Help her in the 4
         following:
         i. Explain her the concept of variable and data type by suitable example.
         ii. Help her in understanding the difference between assignment operator and
         comparison operator with the help of appropriate example.

     (b) Will the output from the following two code be any different?                           2
         First Code:
          int x=2,y=40;
         while(y<=x) {
                 jTextField1.setText(""+x);
                 x=x+8;
                     }

         Second Code :
            int x=2,y=40;
         do {
                   jTextField1.setText(""+x);
                   x=x+8;
                  } while(y<=x);

        Give reasons for your answer.

                                                     OR
     (b) Predict the output of the following code:
         int n=4,f=0,i;
         for(i=1;i<=n;i++)
         {
         f=f*i;
         }
         jTextField1.setText(""+f);
         jTextField2.setText(""+i);

     (c) Dev, a website designer with “Creative Designers Pvt. Ltd.” has written the following   4
        code. Observe the code given below and answer the following questions:

        <company>
              <employee eid=1>
                      <name>Albert</name>
                      <dept deptid=“d1”>Computer</dept>
              </employee>
              <employee eid=2>
                      <name>Manisha</name>
        <dept deptid=“d2”>Accounts</dept>
              </employee>
        </company>
           i. Are these tags part of HTML code or XML code?
          ii. Identify the root element.
         iii. Mention any two child elements.
         iv. Mention any two attributes

                                                     OR

                                                      2
```

---

## page 3

```
     (c) Mention any two main differences between HTML and XML. Also mention any two
         main features of XML for which it’s used extensively now a days.

3.   (a) What is the purpose of SQL?                                                             1

     (b) Mr. Manav, a database administrator in “Global Educational and Training Institute” has 4
         created following table named “Training” for the upcoming training schedule:

                                              Training

         Training_Id Name           Email_Id             Topic         City        Fee
         ND01        Mr. Rajan      raj@gmail.com        Cyber         New Delhi   10000
                                                         Security
         GU01         Ms. Urvashi   urv@yahoo.com        ICT      in   Gurugram    15000
                                                         Education
         FD01         Ms. Neena     neenarediff.com      Cyber         Faridabad   12000
                                                         Security
         ND02         Mr. Vinay     NULL                 ICT      in   New Delhi   13000
                                                         Education
         GU02         Mr. Naveen    nav@gmail.com        Cyber         Gurugram    NULL
                                                         Security
        Help him in writing SQL query for the following purpose:
        i.     To count how many female candidates will be attending the training.
        ii.    To display list of free trainings.
        iii.   To display all the cities where Cyber Security training is scheduled along with
               its fee.
        iv.    To add a column feedback with suitable data type.

     (c) Observe the table named “Training” given above carefully and predict the output of the 4
         following queries:
           i. select city from training where topic = 'Cyber Security';
          ii. select count(Training_Id) from training where email_id like '%gmail% ';
         iii. select AVG (Fee) from training where Topic = 'Cyber Security';
         iv. select name from training where INSTR (Email_Id, '@’)=0;

     (d) What is the degree and cardinality of the above given table named ‘Training’.           1

4.   (a) Shiva has placed two radio button on a payment form designed in NetBeans to accept 1
         mode of payment one out of cash or card. To his surprise, during runtime, a customer is
         able to select both the options for a single transaction. What went wrong?

                                              OR
     (a) Mention any one advantage of jCheckBox control over jRadioButton control.

     (b) Prachi is working with following swing controls:                                        1

         jButton, jLabel, jTextField, jCheckBox.
         Suggest her any two basic methods commonly available with all the four controls
         mentioned above.
                                                 OR
     (b) How jLabel is different from jTextField control at run time?


                                                    3
```

---

## page 4

```
(c) What will be an output of the following code if value of variable application is 1?        1
    Switch (application)
      {
    case 0 : jTextField1.setText("RDBMS");
    case 1 : jTextField1.setText("BROWSER");
    case 2 : jTextField1.setText("OS"); break;
    case 3 : jTextField1.setText("PHOTO EDITOR"); break;
    default : jTextField1.setText("Application Software"); break;
          }
                                              OR
(c) Re-write the above given code through if-else statements.

(d) Anju, a beginner in java programming has written following code with some mistakes:        4
     int k=0;
     string s="Save Earth";
     int l=s.length;
     for(int i=0;k<l;i++)
     {
     jTextArea1.append(s+\n);
     k++;
     };
    Help her in identifying and correcting the errors.
    Convert the correct code into do while looping statement.
                                             OR
(d) Observe the given code:
     int ctr=10;
    while(ctr>5)
    {
    ctr=ctr-2;
    }
    Attempt the following questions based on the above given code:
    i. How many times the above given loop will run and what will be the value of ctr,
    immediately after exiting from the loop.
   ii. Out of entry controlled or exit controlled loop, above given loop will come under
    which category and why?

(e) Study the following code and answer the questions that follow:                             2
    String str="Green World, Clean World";
    int len=str.length(),remain;
    remain=100-len;
    jTextField2.setText(str.toUpperCase());
    jTextField3.setText(Integer.toString(remain)+" more charachters can be entered");

      i. Predict the output displayed in text fields named jTextField2 and jTextField3 after
         running the above code.
     ii. Identify and name any two method of String class used in the above code.

                                             OR

(e) Explain the purpose of pow() method with the help of suitable java code. Also mention
    that pow() method belongs to which class?


                                               4
```

---

## page 5

```
     (f) Mr. Suman, a programmer in New Era Programming World has designed a registration 6
         page for a hobby club as shown below:




        Fee for different hobbies are as follows:
        Hobby          Fee
        Dancing        1000
        Drawing        1500
        Music           2000
        Singing         2500
        Help him in writing the code to do the following:

        i.       As per the hobby chosen in the hobby combo box, fee should be displayed in the
                 respective text field named t1 as per the criteria given above after clicking on
                 “Check Fee” button.
         ii.     If a candidate belongs to “Jr. Category” then a discount of 10% should be given
                 in displayed in the text field.
         iii.    After clicking on the “Net Fee” button, Net Fee should be calculated and
                 displayed in the respective text field as per the given formula:
                           Net Fee = Fee – Discount
         iv.     Write suitable java code to close the application.
         v.      Write java statement to add a new hobby “Reading” in the combo box at run
                 time.
                                                          OR
     (f) Write java statement to make the Net Fee text field named txtNetFee un-editable at run
         time.

5.   (a) Write any one similarity and one difference between primary key and unique Constraint      2

     (b) Ms. Pari, a beginner in SQL is not able to understand the meaning of “Cancelling a 2
        Transaction”. Help her in understanding the same. Also mention suitable command for it

     (c) Consider the following tables Library given below:                                         4


                                                   5
```

---

## page 6

```
                                               Library

         Bid Name             Author        Price   Mem_name Issue_Date Status
         B01 Wings of         A.P.J         550     Sarita   2018-05-   Returned
             Fire             Abdul                          20
                              Kalam
         B02 The Monk         Robin         340     Simmi          2018-03-     Not
             who sold         Sharma                               15           Returned
             his Ferrari
         B03 You can          Shiv Khera    230     Rajat          2018-04-     Returned
             win                                                   16
         B04 Who              Spencer       450     Ram            2018-03-     Not
             moved my         Jhonson                              17           Returned
             cheese
         B05 Real             Patrick       250     Sia            2018-06-     Not
             Success          Mather-                              18           Returned
                              Pike

        i. Suggest the suitable data type for Issue_Date column.
        ii. Suggest the suitable SQL command to change the size of column name from 30
        character to 50 characters.
        iii. Mention the significance of Bid column in table Library.
        iv. Suggest the suitable command to display a list of the books in a sequence so that first
        all the book’s name should be displayed which has not been returned and after that all
        the book’s name which has been returned should be displayed.

     (d) Rishi, a class XII student has given following commands for the given purposes:              2
        i. To add a new column “Rating” :
        update table library add column rating varchar(20);
        ii. To give an increase of 50 Rs. to all the books:
        alter library set price=price+50;
        Check if above given SQL commands will be able to achieve desired task or not. Justify
        your answer. Suggest the correction (s) if required.

6.   (a) Write SQL query to create a table “BOOKS” with the following structure:                      2

                                           Table: BOOKS

         Field name           Datatype              Size Constraint
         BOOK_ID              Integer               2    Primary Key
         BOOK_NAME            Varchar               20
         CATEGORY             Varchar               10
         ISSUE_DATE           Date

                                     OR

     (a) Help Ramesh in identifying any two columns for a table named student along with their
         suitable data type



                                                    6
```

---

## page 7

```
     (b) In a Bank’s database, there are two tables ‘Customer’ and ‘Transaction’ as shown
         below.
                            Customer

         Acc_No      Cust_Name     Cust_City      Cust_Phone      Open_Bal
         2101001     Sunita        Ambala         9710557614      10000
         2201002     Sandhya       Patna          8223545233      15000
         2301003     Vivek         New Delhi      9972136576      13000
         2401004     Meena         New Delhi      9321305453      10000

                             Transaction

         Trans_Id       Acc_No        Transaction_Type      Amount
         Tr001          2301003       Credit                15000
         Tr002          2201002       Credit                20000
         Tr003          2101001       Debit                 3500
         Tr004          2301003       Credit                26000
         Tr005          2301003       Credit                24000

        Consider these tables while attempting the questions given below:

        (i) Identify the candidate keys of Customer table.                                            1
                                                   OR
        (i) Briefly explain the concept of Candidate keys.

         (ii) Which column can be considered as foreign key column in Transaction table?              1
                                                  OR
        (ii) Identify Primary Key column of Transaction table.

     (c) With reference to the above given tables, attempt the questions given below:                 9

        (i) Write a query to display customer’s name who has withdrawn the money.
                                                   OR
        (i) Write a query to display customer’s name along with their transaction details.

        (ii) Write a query to display customer’s name who have not done any transaction yet.
                                                  OR
        (ii) How many rows and column will be there in the Cartesian product of the above
             given tables. Also mention the degree and cardinality of the Cartesian product of
             the above given tables.

        (iii) Select Acc_No, sum(Amount) from Customer c, Transaction t where
              c.Acc_No=t.Acc_No group by c.Acc_No having Transaction_Type="Credit";
                                                OR
        (iii) Discuss the significance of having clause with group by statement with suitable
              example

7.   (a) It’s an era of online financial transactions. Help Julie in identifying any two challenges   2
        which a common man may face for the same.


                                                     7
```

---

## page 8

```
(b) Mention any one major environmental benefits of ICT to Ms. Megha so that she can     1
   utilize it in her future “Save Earth” campaign

(c) Ms. Achla, works as a Programmer in a survey firm named “National Survey 2
    Foundation”. In her current project, she is supposed to design a survey page for an
    online educational training program. Help her in choosing the most appropriate controls
    for the specified task from Textfield, Label, RadioButton, CheckBox, ListBox,
    ComboBox, Button and write in the third column:

    S. No.     Control used to input               Control

    1          TRAINEE’S NAME

    2          TRAINING LOCATION

    3          GRADE THE SESSION
               (Excellent, Good,
               Satisfactory, Unsatisfactory)

    4          SUGGESTIONS




                                               8
```