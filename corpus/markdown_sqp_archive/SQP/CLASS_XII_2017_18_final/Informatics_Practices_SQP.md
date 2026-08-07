---
title: "Informatics Practices SQP"
source_pdf: "Informatics_Practices_SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS_XII_2017_18_final/Informatics_Practices_SQP.pdf"
pages: 7
pdf_bytes: 97771
pdf_sha256: "c5e63b3b3d875bac94b44140e94bc2dc7b557381b9f83ca885c4020776f78665"
text_chars: 14329
low_text_pages: 0
converter: "pdftotext -layout"
---

# Informatics Practices SQP


---

## page 1

```
                                 Sample Question Paper
                            Subject: Informatics Practices
                                         Class: XII
                                      Session 2017-18
Time: 3 Hrs.                                                                      M.M. 70
1 (a)     Mr. Ravi, an IT Help Desk executive needs to remotely login a customer’s PC to 1
          provide him technical support. Suggest a remote access software to him.
   (b)    Identify the type of network (out of LAN/PAN/MAN/WAN) formed in the given 1
          diagram:




   (c)    Identify the fastest wired media out of the following:                              1
          Ethernet cable, Optical fiber, Co-axial cable
   (d)    Mention any two main advantages of star topology over bus topology.                 1
   (e)    Discuss the significance of Bluetooth technology.                                   2
   (f)    I. Write down any two advantages of Open Source Software over Proprietary 4
          software.
          II.    Ms. Sita trying to log into your Internet Banking account for online
          transaction activity. However, as strange as it may seem, she is denied of an
          access to the bank’s website, in spite of having a swift internet connection.

          What do you think the reason behind this problem is and suggest her few simple
          precautions in order to overcome any such type of network security threats.
2 (a)         I. Help Manish in identifying the incorrect variable name with justification 4
                     from the following:
                    i. unit@price; ii. fee; iii. userid; iv. avg marks;

             II. Write Java code to declare a variable named Price of integer type. Assign
                     a value 10 to this variable. Overwrite the value of price with its double
                     value. Decrease the value of price by 5.
   (b)    Rewrite the following code using switch case:                                        2
               int day=Integer.parseInt(jTextField1.getText());
```

---

## page 2

```
             if(day>=1 && day<=5)
                jOptionPane1.showMessageDialog(this, "Working Day");
             else if(day>=6 && day<=7)
                jOptionPane1.showMessageDialog(this, "Off Day");
             else
                jOptionPane1.showMessageDialog(this, "Invalid Entry");
  (c)   i. Ms. Sangeeta wants to add few descriptive lines in the HTML code which 4
        should not be displayed on the webpage rather should remain inactive during
        execution. Suggest her the solution along with example.
        ii. How HTML is different from XML? Mention any two point of difference.
3 (a)   Mention any two example of common Database Management System.               1

  (b)   Write the full forms of the following:                                           1
                i. DDL                ii. DML
  (c)   Ms. Archana, a class XI student has just started learning MySQL. Help her in 4
        understanding the basic difference between Alter and Update command with
        suitable example.
        Also suggest her suitable command for the following purpose:
            i. To display the list of the database already existing in MySQL.
            ii. To use the database named City.
            iii. To remove the pre-existing database named Clients.
            iv. To remove all the records of the table named “Club” at one go along with
                     its structure permanently.
  (d)   Observe the given table named “Loan” carefully and predict the output of the 4
        following queries:
                                             Loan

         File_No   Cust_Name      PhoneNo        Loan_Amt     Bank      Cheque_Dt
         619095    Ms. Roshni     9899965430     809876       HBDC      2017-06-15
                                                              Ltd.
         234252    Mr. Rajesh     8654327890     745738       ICUCI     2017-07-22
                                                              Ltd.
         543613    Mrs. Sapna     8883546354     NULL         NBI       2017-07-24
                                                              Ltd.S
         435467    Mr. Navneet    9764747474     647484       ICUCI     2017-08-13
                                                              Ltd.
         263427    Ms. Puja       8746454742     546373       HBDC      2017-08-30
                                                              Ltd.
           i. select count(file_no)-count(loan_amt) from loan;
           ii. select Cust_Name,Loan_Amt from loan where month(cheque_dt)=7;
           iii. SELECT concat(left(file_no,2),right(cust_name,2)) AS “ID” from loan
                   where Bank='ICUCI Ltd.';
           iv. select round(loan_amt-loan_amt*10/100) As "Discounted Payment" from
                   loan where loan_amt>700000;
4 (a)   Write down the full forms of the following:                                 1
          i. URL               ii. IDE
```

---

## page 3

```
(b)   Which property is to be used during design time to add a number of countries in 1
      the list box?
(c)   What will be the final value of variable x after the following code is executed: 1

      int x=10;
      while(x>1)
      {
      x=x/3;
      ++x;
      }

(d)   i. Find the output of the following Java code snippet after execution of each java 4
      statement labelled as Line 1, Line 2, Line 3, Line 4:

      String userid="INDIA",pwd="";
      pwd=userid.substring(0,2);                   //Line 1
      int l=userid.length();                       //Line 2
      pwd=pwd.toLowerCase();                       //Line 3
      pwd=pwd.concat(""+l);                        //Line 4


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

(e)   The following code has error(s). Rewrite the correct code underlining all the 2
      corrections made :
        int start=2;end=20;
        do;
        {
        start=start+start;
              while(start<=end)
```

---

## page 4

```
(f)   Ms. Neelam works as a programmer in “Kidz Entertainment Zone”. She has
      designed a Registration Page to calculate the total fee of summer camp depending
      upon the number of activities selected by the user considering age eligibility as
      well. A screenshot of the same is shown below:




      Help her in writing the code to do the following:
                                                                                                6
      i. After entering the age in the specified text field, when ‘Chk Eligibility’ button is
      clicked, a dialogue box should be displayed with a message “Welcome” if age is
      in between 3-13 years else there should be a message “Sorry! You are either
      underage or overage!!”. Additionally the application should be closed if age is
      inappropriate.




      ii. After selecting the desirable activities, total fee should be displayed in the
      specified text field on the click of “Proceed” button at the rate of Rs. 1000 per
      activity.

      iii. A discount of 20% is applicable if more than one activity is chosen by the
      user.
```

---

## page 5

```
        iv. After clicking on the “Net Fee” button, Net Fee should be calculated and
        displayed in the respective text field as per the given formula:

                         Net Fee = Fee – Discount
5 (a)   While creating a table named “Employee”, Mr. Rishi got confused as which data    2
        type he should chose for the column “EName” out of char and varchar. Help him
        in choosing the right data type to store employee name. Give valid justification
        for the same.
  (b)   Ms. Shalini has just created a table named “Employee” containing columns 2
        Ename, Department, Salary.

        After creating the table, she realized that she has forgotten to add a primary key
        column in the table. Help her in writing SQL command to add a primary key
        column empid. Also state the importance of Primary key in a table.
  (c)   Consider the following table:                                                      4
                                              Student

         Admn     Name          Stream         Optional      Average
         1001     Shrishti      Science        CS            90
         1002     Ashi          Humanities     Maths         80
         1003     Aditya        Commerce       IP            60
         1004     Ritu Raj      Science        IP            65
         1005     Sonali        Commerce       Maths         60
         1006     Saumya        Science        IP            65
         1007     Ashutosh      Science        IP            95
         1008     Prashant      Commerce       P.ED          80
         1009     Aman          Commerce       IP            70
         1010     Rishabh       Humanities     P.ED          85

         Write commands in SQL for (i) to (iv):
            i. To display the details of all those students who have IP as their optional
                    subject.
            ii. To display name, stream and optional of all those students whose name
                    starts with ‘A’.
            iii. To give an increase of 3 in the average of all those students of humanities
                    section who have Maths as their optional subject.
            iv. To display a name list of all those students who have average more than
                    75.
  (d)   On the basis of the Table Student, write the output(s) produced by executing the       2
        following queries:
            i. Select max(average), min(average) from students group by stream having
                    stream like ‘Science’;
            ii. Select name from students where optional IN (‘CS’,’IP’);
6 (a)    Write SQL query to create a table “Registration” with the following structure:        2
                                         Table: Registration
         Field name            Datatype              Size Constraint
```

---

## page 6

```
          Reg_Id               Integer              2     Primary Key
          Name                 Varchar              20
          Course               Varchar              10
          Join_Dt              Date
  (b)    Consider the tables given below while attempting the following questions:
                                               Train
          TrainId              TName               Source             Destination
          3402                 Century Express     New Delhi          Mumbai
          4023                 Superfast Express Kanyakumari          Chandigarh
          3424                 Lucknow Mail        Lucknow            New Delhi
          6542                 Capital Express     Chennai            Kolkata
          9876                 Punjab Mail         Patna              Ludhiana
          5400                 Century Express     New Delhi          Kanpur

                                             Reservation
          RefNo                 TrainId            Passenger            JourneyDate
          S001                  4023               Shubham Singh        2017-07-02
          C001                  6542               Jishan Mittal        2017-06-25
          S002                  4023               Jessica Raj          2017-07-02
          P001                  9876               Paramjeet Singh      2017-07-22
          S003                  4023               Gurjyot Singh        2017-07-03
          C002                  6542               Akash Mukharjee 2017-06-25
          P002                  9876               Meera Devi           2017-07-22
          L001                  3424               Ruby Lal             2017-06-29
          C003                  5400               Tapshree             2017-07-04
  (i)    Identify the primary key column of Train and Reservation.                            1
  (ii)   Help Mr. Sajal in identifying the wrong statement with reference to UNION            1
         clause:
             a. Each SELECT statement within UNION must have the same number of
                  columns
             b. The columns must also have similar data types
             c. The columns in each SELECT statement must also be in the same order.
             d. By default, the UNION operator selects all the values.
  (c)    With reference to the above given tables, write commands in SQL for (i) and (ii)     6
         and output for (iii) below:
             i. To display the Train name along with its passenger name.
             ii. To display Train detail which has no reservation yet.
             iii. SELECT T.* from Train T, Reservation R where T.TrainId=R.TrainId
                      AND Source LIKE “%Delhi” OR Destination LIKE “%Delhi”;
7 (a)    Write down any two benefits of net banking.                                          1
  (b)    Mr. Sanjay, a banking professional want to enroll himself in an e-Learning course.   2
         Mention him any two challenges of e-Learning.
  (c)    Ms. Juhi, works as an IT Executive in a health insurance company named ‘Total        2
         Health’. She has been assigned a task to design a customer registration page. Help
         her in choosing the most appropriate controls for the specified task from
```

---

## page 7

```
Textfield, Label, RadioButton, CheckBox, ListBox, ComboBox, Button and write
in the third column considering the following points:
    • Customer can enter his/her name in the control.
    • Customer can choose only one city out of given list of city.
    • Customer can choose only one type out of given policy types.
    • Customer can choose any number of INCLUSIONS out of given
        inclusions.

 S. No.    Control used to               Control

 1         CUSTOMER’S NAME

 2         CUSTOMER’S CITY

 3         POLICY TYPE
           (Individual/Family)

 4         INCLUSIONS (Critical
           Illness/Accidental
           Coverage/Health
           Checkup/Others)
```