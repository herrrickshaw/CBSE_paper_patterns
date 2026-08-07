---
title: "Informatics Practices MS"
source_pdf: "Informatics_Practices_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS_XII_2017_18_final/Informatics_Practices_MS.pdf"
pages: 15
pdf_bytes: 401162
pdf_sha256: "ccd5a8b3bebae64ef082ff95b260f8fa0bfdefdb393ce9c1215dd8439c280329"
text_chars: 25492
low_text_pages: 0
converter: "pdftotext -layout"
---

# Informatics Practices MS


---

## page 1

```
                                      Marking Scheme
                             Subject: Informatics Practices
                                           Class: XII
                                       Session 2017-18
Time: 3 Hrs.                                                                          M.M. 70
1 (a)     Mr. Ravi, an IT Help Desk executive needs to remotely login a customer‟s PC to   1
          provide him technical support. Suggest a remote access software to him.
   Ans Teamviewer

          (1 Mark for correct answer)
   (b)    Identify the type of network (out of LAN/PAN/MAN/WAN) formed in the given       1
          diagram:




   Ans    PAN

          (1 Mark for each correct answer)
   (c)    Identify the fastest wired media out of the following:                          1
          Ethernet cable, Optical fiber, Co-axial cable
   Ans    Optical fiber

          (1 Mark for correct answer)
   (d)    Mention any two main advantages of star topology over bus topology.             1
   Ans        i.     It has centralized control.
              ii.    Fault diagnosis is easy.

          (½ Mark for each correct advantage)
   (e)    Discuss the significance of Bluetooth technology.                               2
   Ans    Bluetooth is a wireless technology standard for exchanging data over short
          distances using short-wavelength radio waves.
          It is used in building personal area networks (PANs).
```

---

## page 2

```
        Now a days many gadgets and peripheral devices are Bluetooth enabled like
        Speakers, mouse, headphone, printer etc.
        (2 Mark for correct answer)
  (f)   I. Write down any two advantages of Open Source Software over Proprietary 4
        software.
        II.    Ms. Sita trying to log into your Internet Banking account for online
        transaction activity. However, as strange as it may seem, she is denied of an
        access to the bank‟s website, in spite of having a swift internet connection.

        What do you think the reason behind this problem is and suggest her few simple
        precautions in order to overcome any such type of network security threats.
  Ans   I.
        i. Source code is available.
        ii. Money need not to be paid for procuring the license for usage and further
        distribution.

        (1 Mark for each correct advantage)
        II.
        She could be under a DoS attack!

        She should deploy an antivirus program and firewall into her network if not
        already done. This helps in restricting the bandwidth usage to authenticated users
        only.

        (1 Mark for correct reason identification)
        (1 Mark for suggesting correct precautions)
2 (a)      I.      Help Manish in identifying the incorrect variable name with 4
                   justification from the following:
                  i. unit@price; ii. fee; iii. userid; iv. avg marks;

             II.       Write Java code to declare a variable named Price of integer type.
                       Assign a value 10 to this variable. Overwrite the value of price with its
                       double value. Decrease the value of price by 5.
  Ans   I.
                   i. unit@price; // Special symbols like „@‟ is not allowed in variable name
                   iv. avg marks;// Spaces are not allowed in variable name

        (½ Mark for each correct identification of incorrect variable name)
        (½ Mark for each correct justification)

        II.
        int price;
        price=10;
        price=price*2;
        price=price-5;
```

---

## page 3

```
      (½ Mark for each correct statement)
(b)   Rewrite the following code using switch case:                            2
          int day=Integer.parseInt(jTextField1.getText());
          if(day>=1 && day<=5)
             jOptionPane1.showMessageDialog(this, "Working Day");
          else if(day>=6 && day<=7)
             jOptionPane1.showMessageDialog(this, "Off Day");
          else
             jOptionPane1.showMessageDialog(this, "Invalid Entry");
Ans       int day=Integer.parseInt(jTextField1.getText());

      switch(day)
      {
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
              jOptionPane1.showMessageDialog(this, "Working Day"); break;
      case 6:
      case 7:
              jOptionPane1.showMessageDialog(this, "Off Day"); break;
           default:
              jOptionPane1.showMessageDialog(this, "Invalid Entry");
      }
       (2 Mark for correct conversion of if-else block to switch block)
(c)   i. Ms. Sangeeta wants to add few descriptive lines in the HTML code which 4
      should not be displayed on the webpage rather should remain inactive during
      execution. Suggest her the solution along with example.
      ii. How HTML is different from XML? Mention any two point of difference.
Ans   i.
      She should use comments in HTML.
      Any text to make comments in HTML, should be preceded by <! and should end
      with ->

      Example:

      <body>
      <!-
      This is only used for comment
      ->
      Welcome
      </body>


      (1 Mark for correct solution)
```

---

## page 4

```
         (1 Mark for correct example)

         ii.
                  HTML is used to display data and to focus on formatting of data, whereas
                   XML is used to describe data and focus on what data is.
                  HTML tags are not case sensitive whereas XML tags are case sensitive.
                  HTML tags are predefined, whereas XML tags are not predefined.
                  XML is used to store and transfer the data over different platforms while
                   HTML is used to design webpages.

         (2 Marks for any two correct point for differentiation)
3 (a)    Mention any two example of common Database Management System.                         1

  Ans:   MySQL, Ingres, Postgres, Oracle etc.

         (½ Mark for any two correct example)
  (b)    Write the full forms of the following:                                                1
               i. DDL               ii. DML
  Ans:   i. DDL-Data Definition Language              ii. DML-Data Manipulation Language

         (½ Mark for each correct full form)
  (c)    Ms. Archana, a class XI student has just started learning MySQL. Help her in 4
         understanding the basic difference between Alter and Update command with
         suitable example.
         Also suggest her suitable command for the following purpose:
             i.     To display the list of the databases already existing in MySQL.
             ii.    To use the database named City.
             iii.   To remove the pre-existing database named Clients.
             iv.    To remove all the records of the table named “Club” at one go along
                    with its structure permanently.
  Ans:   Differentiation between ALTER and UPDATE command:

                       ALTER                               UPDATE
          It‟s a DDL command.                  It‟s a DML command.
          It can be used for the following     It‟s used to modify the records
          purpose:                             of the table.
                To add a new column.
                To remove an existing
                   column.
                To modify a column.
                To add/remove a
                   constraint.
          Example:                             Example:
          If a table named emp already         To modify the address to Noida
          exists with following columns:       from “New Delhi”, we may use
```

---

## page 5

```
                                           the following command :
            Empno    Name      Dept
                                           Update emp set address=
        To add an address column, we       “Noida” where city= “New
        may use following command:         Delhi”;

        Alter Table emp add address
        varchar(20);

       (1 Mark for correct differentiation between ALTER and UPDATE command)
       (1 Mark for suitable example)

       suitable command:
       i. Show Databases
       ii. Use City
       iii. Drop Database Clients
       iv. Drop table Club

       (½ Mark for each the correct answer)
(d)    Observe the given table named “Loan” carefully and predict the output of the 4
       following queries:
                                       Loan

        File_No Cust_Name           PhoneNo       Loan_Amt       Bank     Cheque_Dt
        619095 Ms. Roshni           9899965430    809876         HBDC 2017-06-15
                                                                 Ltd.
        234252       Mr. Rajesh       8654327890 745738          ICUCI 2017-07-22
                                                                 Ltd.
        543613       Mrs. Sapna       8883546354 NULL            NBI      2017-07-24
                                                                 Ltd.S
        435467       Mr. Navneet 9764747474 647484               ICUCI 2017-08-13
                                                                 Ltd.
        263427       Ms. Puja         8746454742 546373          HBDC 2017-08-30
                                                                 Ltd.
            i.      select count(file_no)-count(loan_amt) from loan;
            ii.     select Cust_Name, Loan_Amt from loan where month(cheque_dt)=7;
            iii.    SELECT concat(left(file_no,2),right(cust_name,2)) AS “ID” from loan
                    where Bank='ICUCI Ltd.';
            iv.     select round(loan_amt-loan_amt*10/100) As "Discounted Payment"
                    from loan where loan_amt>700000;
Ans.   i.
       +--------------------------------+
       | count(file_no)-count(loan_amt) |
       +--------------------------------+
       |                1               |
       +--------------------------------+
```

---

## page 6

```
        ii.

        +------------+----------+
        | cust_name | loan_amt |
        +------------+----------+
        | Mr. Rajesh | 745738   |
        | Mrs. Sapna | NULL     |
        +------------+----------+

        iii.
        +------+
        | ID   |
        +------+
        | 23sh |
        | 43et |
        +------+

        iv.
        +--------------------+
        | Discounted Payment |
        +--------------------+
        |             728888 |
        |             671164 |
        +--------------------+

        (1 Mark for each the correct output)
4 (a)   Write down the full forms of the following:                                        1
        i. URL            ii. IDE
  Ans   i. Uniform Resource Locator
        ii. Integrated Development Environment

        (½ Mark for each correct full forms)
  (b)   Which property is to be used during design time to add a list of countries in the 1
        list box?
  Ans   Model property

        (1 Mark for correct answer)
  (c)   What will be the final value of variable x after the following code is executed:   1

        int x=10;
        while(x>1)
        {
        x=x/3;
        ++x;
```

---

## page 7

```
      }

Ans   1

      (1 Mark for correct answer)
(d)   i. Find the output of the following Java code snippet after execution of each java 4
      statement labelled as Line 1, Line 2, Line 3, Line 4:

      String userid="INDIA",pwd="";
      pwd=userid.substring(0,2);                   //Line 1
      int L=userid.length();                        //Line 2
      pwd=pwd.toLowerCase();                       //Line 3
      pwd=pwd.concat(""+L);                         //Line 4

      ii. Rewrite the following code using for loop:

      int attempt=0;
      while(attempt<=3)
      {
      String login=jTextField1.getText();
      String pwd=jTextField2.getText();
      if(login.equals("XII") && pwd.equals("IP"))
      {
         jOptionPane1.showMessageDialog(null, "Welcome");
         break;
      }
      else
         jOptionPane1.showMessageDialog(null, "Pl try again");

      attempt++;
      }

Ans   i.
      IN
      5
      in
      in5
      (½ Mark for each correct output)

      ii.

      for(int attempt=0;attempt<=3;attempt++)
      {
      String login=jTextField1.getText();
      String pwd=jTextField2.getText();
      if(login.equals("XII") && pwd.equals("IP"))
```

---

## page 8

```
      {
          jOptionPane1.showMessageDialog(null, "Welcome");
          break;
      }
      else
         jOptionPane1.showMessageDialog(null, "Pl try again");

      }

       (2 Mark for correct code in for loop)
(e)   The following code has error(s). Rewrite the correct code underlining all the 2
      corrections made :
         int start=2;end=20;
         do;
         {
         start=start+start;
               while(start<=end)

Ans     int start=2,end=20; //Correction 1
       do                    //Correction 2
       {
       start=start+start;
       }                    //Correction 3
      while(start<=end);    //Correction 4


      (½ Mark for each correct correction)
(f)   Ms. Neelam works as a programmer in “Kidz Entertainment Zone”. She has
      designed a Registration Page to calculate the total fee of summer camp depending
      upon the number of activities selected by the user considering age eligibility as
      well. A screenshot of the same is shown below:
```

---

## page 9

```
                                                                                          6




Help her in writing the code to do the following:

i. After entering the age in the specified text field, when „Chk Eligibility‟ button is
clicked, a dialogue box should be displayed with a message “Welcome” if age is
in between 3-13 years else the program should be terminated after displaying the
message “Sorry! You are either underage or overage!!”.




ii. After selecting the desirable activities, total fee should be displayed in the
specified text field on the click of “Proceed” button at the rate of Rs. 1000 per
activity.

iii. A discount of 20% is applicable if more than one activity is chosen by the
user.

iv. After clicking on the “Net Fee” button, Net Fee should be calculated and
displayed in the respective text field as per the given formula:

                 NetFee = Fee – Discount
```

---

## page 10

```
Ans   i.
      int age=Integer.parseInt(jTextField2.getText());
      if(age>=3 && age<=13)
      {
      jOptionPane1.showMessageDialog(this, "Welcome");
      }
      else
      {
       jOptionPane1.showMessageDialog(this, "Sorry!You are either underage or
      overage!!");
       System.exit(0);
      }
      (2 Mark for correct code)

      ii.
      int count=0;
      if(jCheckBox1.isSelected())
          count++;
      if(jCheckBox2.isSelected())
          count++;
      if(jCheckBox3.isSelected())
          count++;
      if(jCheckBox4.isSelected())
          count++;
      if(jCheckBox5.isSelected())
          count++;
      if(jCheckBox6.isSelected())
          count++;
      jTextField3.setText(""+(count*1000));

      (2 Mark for correct code)

      iii.
      int fee=Integer.parseInt(jTextField3.getText());
      int disc=0;
      if(fee>1000)
          disc=fee*20/100;
      jTextField4.setText(""+(disc));

      (1 Mark for correct code)

      iv.
      int fee=Integer.parseInt(jTextField3.getText());
      int disc=Integer.parseInt(jTextField4.getText());
      jTextField5.setText(""+(fee-disc));
```

---

## page 11

```
         (1 Mark for correct code)
5 (a)    While creating a table named “Employee”, Mr. Rishi got confused as which data 2
         type he should chose for the column “EName” out of char and varchar. Help him
         in choosing the right data type to store employee name. Give valid justification
         for the same.
  Ans:   Varchar would be the suitable data type for EName column as char data type is a
         fixed length data type while varchar is a variable length data type.

         Any employee‟s name will be of variable length so it‟s advisable to choose
         varchar over char data type.

         (1mark for the correct data type)
         (1mark for the correct Justification)
  (b)    Ms. Shalini has just created a table named “Employee” containing columns 2
         Ename, Department, Salary.

         After creating the table, she realized that she has forgotten to add a primary key
         column in the table. Help her in writing SQL command to add a primary key
         column empid. Also state the importance of Primary key in a table.
  Ans:   SQL command to add a primary key column:

         Alter table employee add empid int primary key;

         Importance of Primary key in a table:
         Primary key column is used to uniquely identify each record of the table. A
         column defined as primary key cannot have a duplicate entry and can‟t be left
         blank.

         (1 mark for correct SQL command to add a primary key column)
         (1 mark for correct importance of Primary key in a table)
  (c)    Consider the following table:                                                        4
                                             Student

          Admn     Name         Stream         Optional     Average
          1001     Shrishti     Science        CS           90
          1002     Ashi         Humanities     Maths        80
          1003     Aditya       Commerce       IP           60
          1004     Ritu Raj     Science        IP           65
          1005     Sonali       Commerce       Maths        60
          1006     Saumya       Science        IP           65
          1007     Ashutosh     Science        IP           95
          1008     Prashant     Commerce       P.ED         80
          1009     Aman         Commerce       IP           70
          1010     Rishabh      Humanities     P.ED         85

         Write commands in SQL for (i) to (iv):
```

---

## page 12

```
            i.     To display the details of all those students who have IP as their optional
                   subject.
             ii.    To display name, stream and optional of all those students whose name
                   starts with „A‟.
            iii. To give an increase of 3 in the average of all those students of humanities
                   section who have Maths as their optional subject.
            iv.    To display a name list of all those students who have average more than
                   75.
  Ans:    i. select * from student where optional=‟IP‟;
          ii. select name, stream, optional from student where name like „A%‟;
          iii. update student set average=average+3 where stream=‟Humanities‟ and
          optional=‟Maths‟;
          iv. select name from student where average>75;

          (1 Mark each correct command)
  (d)     On the basis of the Table Student, write the output(s) produced by executing the      2
          following queries:
               i.    Select max(average), min(average) from students group by stream
                     having stream like „Science‟;
               ii.   Select name from students where optional IN („CS‟,‟IP‟);
  Ans :   i.
            Max(Average)          Min(Average)
            95                    65

          ii.
            Name
            Shrishti
            Aditya
            Ritu Raj
            Saumya
            Ashutosh
            Aman

          (1 Mark for each correct output )

6 (a)      Write SQL query to create a table “Registration” with the following structure:       2
                                         Table: Registration
            Field name          Datatype             Size Constraint
            Reg_Id              Integer              2     Primary Key
            Name                Varchar              20
            Course              Varchar              10
            Join_Dt             Date
  Ans:    Create table Registration
          (
          Reg_Id Integer(2) Primary Key,
          Name varchar(20),
```

---

## page 13

```
        Course varchar(10),
        Join_Dt date
        );

        (½ Mark for create table statement)
        (1 Mark for all the fieldnames with datatypes )
        (½ Mark for correct placement of Primary key constraint )
(b)      Consider the tables given below while attempting the following questions:
                                              Train
         TrainId              TName               Source              Destination
         3402                 Century Express     New Delhi           Mumbai
         4023                 Superfast Express Kanyakumari           Chandigarh
         3424                 Lucknow Mail        Lucknow             New Delhi
         6542                 Capital Express     Chennai             Kolkata
         9876                 Punjab Mail         Patna               Ludhiana
         5400                 Century Express     New Delhi           Kanpur

                                          Reservation
         RefNo                TrainId            Passenger            JourneyDate
         S001                 4023               Shubham Singh        2017-07-02
         C001                 6542               Jishan Mittal        2017-06-25
         S002                 4023               Jessica Raj          2017-07-02
         P001                 9876               Paramjeet Singh      2017-07-22
         S003                 4023               Gurjyot Singh        2017-07-03
         C002                 6542               Akash Mukharjee      2017-06-25
         P002                 9876               Meera Devi           2017-07-22
         L001                 3424               Ruby Lal             2017-06-29
         C003                 5400               Tapshree             2017-07-04
 (i)    Identify the primary key column of Train and Reservation.                          1
Ans:    Train-TrainId
        Reservation-RefNo

        (½ Mark for each correct answer )
 (ii)   Help Mr. Sajal in identifying the wrong statement with reference to UNION          1
        clause:
            a. Each SELECT statement within UNION must have the same number of
                columns
            b. The columns must also have similar data types
            c. The columns in each SELECT statement must also be in the same order
            d. By default, the UNION operator selects all the values.
Ans:    d

        (1 Mark for correct answer )
 (c)    With reference to the above given tables, write commands in SQL for (i) and (ii)   6
        and output for (iii) below:
```

---

## page 14

```
            i.       To display the Train name along with its passenger name.
            ii.      To display Train detail which has no reservation yet.
            iii.     SELECT T.* from Train T, Reservation R where T.TrainId=R.TrainId
                     AND Source LIKE “%Delhi” OR Destination LIKE “%Delhi”;
  Ans:   i. select TName, Passenger from Train T, Reservation R where
         T.TrainId=R.TrainId;

         (½ Mark for correct usage of Select )
         (½ Mark for correct From statement )
         (1 Mark for the correct condition)

         ii. i. select T.* from Train T, Reservation R where T.TrainId!=R.TrainId;

         (½ Mark for correct usage of Select )
         (½ Mark for correct From statement )
         (1 Mark for the correct condition)

         iii.
           TrainId            TName                Source              Destination
           3424               Lucknow Mail         Lucknow             New Delhi
           5400               Century Express      New Delhi           Kanpur

         (1 Mark for each row)
7 (a)    Write down any two benefits of net banking.                                        1
  Ans:   i. Banking can be done anytime i.e. 24x7.
         ii. Its fast and hassle free.
         (½ Mark each for correct benefit )
  (b)    Mr. Sanjay, a banking professional want to enroll himself in an e-Learning course. 2
         Mention him any two challenges of e-Learning.
  Ans:   i. The lack of learner‟s motivation.
         ii. The busy schedule of the learners.

         (1 Mark for each correct challenges with e-Learning )
  (c)    Ms. Juhi, works as an IT Executive in a health insurance company named „Total 2
         Health‟. She has been assigned a task to design a customer registration page. Help
         her in choosing the most appropriate controls for the specified task from
         Textfield, Label, RadioButton, CheckBox, ListBox, ComboBox, Button and write
         in the third column considering the following points:
              Customer can enter his/her name in the control.
              Customer can choose only one city out of given list of city.
              Customer can choose only one type out of given policy types.
              Customer can choose any number of INCLUSIONS out of given
                 inclusions.

          S. No.     Control used to                 Control
```

---

## page 15

```
       1          CUSTOMER‟S NAME

       2          CUSTOMER‟S CITY

       3          POLICY TYPE
                  (Individual/Family)

       4          INCLUSIONS (Critical
                  Illness/Accidental
                  Coverage/Health
                  Checkup/Others)
Ans
       S. No.     Control used to          Control

       1          CUSTOMER‟S NAME          TextField

       2          CUSTOMER‟S CITY          ComboBox

       3          POLICY TYPE              RadioButton
                  (Individual/Family)

       4          INCLUSIONS (Critical     CheckBox/ListBox
                  Illness/Accidental
                  Coverage/Health
                  Checkup/Others)

      (1/2 mark for each correct answer)
```