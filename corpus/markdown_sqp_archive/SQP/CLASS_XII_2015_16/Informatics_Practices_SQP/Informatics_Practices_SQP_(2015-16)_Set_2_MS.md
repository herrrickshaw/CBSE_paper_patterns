---
title: "Informatics Practices SQP (2015-16) Set 2 MS"
source_pdf: "Informatics_Practices_SQP_(2015-16)_Set_2_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2015_16/Informatics Practices SQP/Informatics Practices SQP (2015-16) Set 2 MS.pdf"
pages: 15
pdf_bytes: 666696
pdf_sha256: "cf187e37bcec0cc55fd0de44cd423652a07881e07718fd684855bc4d11faa521"
text_chars: 23649
low_text_pages: 0
converter: "pdftotext -layout"
---

# Informatics Practices SQP (2015-16) Set 2 MS


---

## page 1

```
                                   Informatics Practices (Code: 065)
                                        Marking Scheme
                                                     - Sample Paper2
                                            Class XII (2015-16)
Time: 3Hrs.
MM: 70
1   (a)       The ‘Chalchitra’ theatre has a computer network. The network is in one                   (2)
              building.
              (i) Name this type of network( out of LAN/MAN/WAN).
              (ii) Name one communication channel that can be used for fast communication
              between workstations of the network.
    Ans:       i.LAN
              ii. Optical fiber cable
              (1 mark for each correct answer)
    (b)       Explain in brief any 2 security threats to Computer networks.                            (2)
    Ans:         1. Denial of service attack: It is an attempt to make one or more network
                    resources unavailable to their legitimate users.
                 2. Snooping:It is gaining unauthorised access to another person’s or organization’s
                    data.

              (1 mark for each correct explanation)
    (c)       Write the advantages of using Unicode to represent text.                                 (2)
    Ans:      Unicode encoding standard provides the basis for processing, storage and
              interchange of text data in any language in all modern software and
              information technology protocols.

              (2 marks for mentioning correct advantages of Unicode)
    (d)       Write on example each of URL and IP address.                                             (2)
    Ans:      URL
              http://www.cbse.nic.in/welcome.htm

              IP address

              122.176.185.219
              (1 mark for each correct example)
    (e)       Identify the topology shown below. Write 2 advantages of this topology.                  (2)
```

---

## page 2

```
    Ans:   Star Topology
           Two advantages are as follows:
           1. Easy to install
           2. Easy to diagnose the fault
           (1 mark for identifying correct topology)
           (½ mark for mentioning each correct advantage)
2   (a)    While working in Netbeans, Ms. Sonia has designed a login page where she          (1)
           wants to display “Welcome” or “Try again” message depending on the
           password entered by the user in text field named ‘jTexField1’. If password
           entered is “India”, ‘Welcome’ message should be displayed otherwise ‘Try
           again’ message should be displayed. Help her in choosing more appropriate
           statement out of 'If statement' and 'Switch statement'.
    Ans:   IF statement as String matching can only be done through if statement.

           (½ mark for correct statement identification)
           (½ mark for correct reason specification)
    (b)    Write Java code to assign the value 10 to variable x and store its square value   (1)
           in another variable y.
    Ans:   x=10;
           y=x*x;

           (½ mark for each correct statement)
    (c)    Deepti works as a programmer in a travel company. She has developed the (2)
           following code to display travel detail according to user’s choice. Help her in
           rewriting the same code using SWITCH CASE:

                 if(choice==1)
                 jTextField1.setText(“New Delhi to Goa”);
                 else if(choice==2)
                 jTextField1.setText(“New Delhi to Paris”);
                 else if(choice==3)
                 jTextField1.setText(“New Delhi to Bangkok”);
                 else
                 jTextField1.setText(“Pl. choose valid option”);
```

---

## page 3

```
    Ans:    switch(choice)
            {
            case 1:
            jTextField1.setText(“New Delhi to Goa”);
            break;
            case 2:
            jTextField1.setText(“New Delhi to Paris”);
            break;
            case 3:
            jTextField1.setText(“New Delhi to Bangkok”);
            break;
            default:
            jTextField1.setText(“Pl. choose valid option”);
            }
            (2 marks for correct converted code)
    (d)     Shambhavi has to design two web pages with following specifications:         (2)
               i.   One web page should have an unordered list.
               ii.   Another web page should have background “Yellow” in colour.

            Suggest her suitable tag(s) and attribute(s) for the above specifications.
    Ans:    i. <UL> <LI>
            ii. <body> tag and        bgcolor attribute

            (1 mark each for each correct answer)
    (e)     Albert works as a website developer in Global Website Designers company.     (2)
            Currently he has created following tags in XML:
            <STUDENT>...</STUDENT>
            <Student>....</Student>

            Are these tags part of HTML code or XML code?
            Are these same same or different?
    Ans:    These tags are part of XML code.
            These tags are different.

            (1 mark for mentioning XML)
            (1 mark for correct identification)
    (f)     How many times will the loop execute?                                        (2)

            int value1 =7,value2=19;
            do
            {
                 JOptionPane.showMessageDialog(null,value1+value2);
                 value1=value1+2;
                 value2=value2-2;
            }while(value1<=value2);
    Ans :   4 times.
            (2 marks for mentioning correct output)

3   (a)     Consider the table ‘empsalary’.                                              (1)
```

---

## page 4

```
                                ID            Salary


                                101          43000

                                102          NULL

                                104          56000

                                107          NULL
       To select tuples with some salary ,Siddharth has written   the following
       erroneous SQL statement:
       SELECT ID, Salary FROM empsalary WHERE Salary = something;

       Write the correct SQL statement.

Ans:   SELECT ID, Salary FROM empsalary WHERE Salary is NOT NULL;

       (1 mark for correct SQL statement)
(b)    Consider the table ‘Employee’.                                             (1)
       Employee


        Name                    Location

        Gurpreet                Mumbai

        Jatinder                Chennai

        Deepa                   Mumbai

        Harsh                   Chennai

        Simi                    New Delhi

        Anita                   Bengaluru


        Write the SQL command to obtain the following output :

        Location

        Mumbai

        Chennai

        New Delhi

        Bengaluru
```

---

## page 5

```
Ans:   SELECT DISTINCT Location FROM Employee;

       (1 mark for correct SQL statement)
(c)    While creating the table Student last week, Ms. Sharma forgot to include the (1)
       column Game_Played. Now write a command to insert the Game_Played
       column with VARCHAR data type and 30 size into the Student table?
Ans:   Alter Table Student Add (Game_Played VARCHAR(30));

       (1 mark for correct MySQL command)
(d)    In ‘Marks’ column of ‘Student’ table, for Rollnumber 2, the Class Teacher     (1)
       entered the marks as 45. However there was a totaling error and the student
       has got her marks increased by 5. Which MySQL command should she use to
       change the marks in ‘Student’ table.

Ans:
       UPDATE command

       (1 mark for correct SQL answer)
(e)    Consider the table ‘Teacher’ given below.                                     (2)

           TeacherId            Department     Periods

           T101                 SCIENCE        32

           T102                 NULL           30

           T103                 MATHEMATICS    34


       What will be the output of the following queries on the basis of the above
       table:
       (i)Select count(Department) from Teacher;
       (ii)Select count(*) from Teacher;
Ans:   i. 2
       ii. 3
       (1 mark for each correct answer)
(f)    Consider the Stu table                                                        (2)


                ROLLNO          NAME



                1        Ashi
```

---

## page 6

```
                   2          Bimmi



                   4          Aakash


           The following SQL queries are executed on the above table

           INSERT INTO Stu VALUES(5,'Gagan');
           COMMIT;
           UPDATE Stu SET name='Abhi' WHERE Rollno = 4;

           SAVEPOINT A;
           INSERT INTO Stu VALUES(6,'Chris');
           SAVEPOINT B;
           INSERT INTO Stu VALUES(7,'Babita');
           SAVEPOINT C;

           ROLLBACK TO B;

           What will be the output of the following SQL query now:
           SELECT * FROM Stu;


    Ans:   Output:
           1 Ashi
           2 Bimmi
           4 Abhi
           5 Gagan
           6 Chris
           (2 mark for correct output)
    (g)    An attribute A of datatype varchar(20) has the value “Amit” . The attribute B   (2)
           of datatype char(20) has value ”Karanita” .
           How many characters are occupied in attribute A ? How many characters are
           occupied in attribute B?
    Ans:   4, 20
           (1 mark for each correct answer)
4   (a)    Following is a list of programming languages:                                   (1)
           BASIC, COBOL, C, JAVA
           Help Sandhya in identifying Object Oriented language(s) from the above given
           list.
```

---

## page 7

```
Ans:   Java

       (1 mark for correct identification of OOP language )
(b)    Satyam is designing a frame in Netbeans containing list box. Help him in         (1)
       writing suitable Java statement to extract selected item from a given listbox
       named “jList1.”
Ans:   jList1.getSelectedIValue();

       (1 mark for correct answer)
(c)    What will be displayed in jTextField1 and jTextField2 after the following code   (1)
       is executed:

       int number = 12;
       if (number <15)
         {
         jTextField1.setText(""+ number) ;
         number++;
         jTextField2.setText(""+ number) ;
         }
       else
         {
         jTextField1.setText("number1”) ;
         number++;
         jTextField2.setText("number2”) ;
         }

Ans:   12
       13
       (½ mark for each correct answer)
(d)    Find output of the following Java code snippet:                                  (2)

       String City="Delhi",PinCode="110001",Str="";
       City=City+" "+PinCode;
       JOptionPane.showMessageDialog(null,City);
       int l=City.length();
       int i=0;
       while(i<l)
       {
       Str=Str+City.substring(6);
       i=i+15;
       }
       JOptionPane.showMessageDialog(null,Str);
Ans:   Delhi 110001
       110001

       (1 mark for each correct output)
(e)    Rewrite the following code using WHILE loop:                                     (2)
        int x=100;
       for(int i=2;i<=22;i=i+4)
              {
```

---

## page 8

```
              jTextArea1.append("\n"+(i+x));
              x=x-2;
             }
Ans:   int x=100;
          int i = 2;
       while (i<=22)
       {
        jTextArea1.append("\n"+(i+x));
        x=x-2;
        i = i+4;
       }
       (2 mark for correct code through WHILE loop)
(f)    The following code has error(s). Rewrite the correct code underlining all the   (2)
       corrections made :
             int n=5,int i=1,f=1;
             do;
             {
             f=f*i;
             i++;
             while(i<=n)
             jTextField1.setText(""+f);
Ans:         int n=5,i=1,f=1;
             do
             {
             f=f*i;
             i++;
             }while(i<=n);
             jTextField1.setText(""+f);

       (½ mark for each correct error correction)
(g)    Mr. Pawan works as a programmer in “ABC Marketing Company” where he has
       designed a Salary generator software to generate the salary of salesman in
       which Name and Salary are entered by the user. A screenshot of the same is
       shown below:
```

---

## page 9

```
                                                                                     2




                                                                                     1
Help him in writing the code to do the following:

i. After selecting appropriate Radio Button, when ‘Commission’ button is
clicked, commission should be displayed in the respective text field as each
Salesman will get a commission based on the units sold according to the
following criteria:                                                                  2

                                 Units Sold     Commission
                                                (in Rs)

                             1 to 20            500

                             20 to 40           1000

                             >40                2000

                                                                                     1
ii. When ‘Gross Salary’ button is clicked, Gross Salary should be calculated and
displayed in the respective text field as per the given formulae:

                  Gross Salary= Salary+Commission

iii. After required selection of Checkbox(es), when ‘Facility Charges’ button is
clicked, Facility charges will be displayed in the respective text field according
to the following criteria:

                      Facility                Charges

                      Transport               500

                      Mess                    2000

iv. Money will be deducted from the Gross Salary according to the facilities
```

---

## page 10

```
        opted by the employee. When ‘Net Salary’ button is clicked, Net Salary should
        be calculated and displayed in the respective text field as per the given
        formulae:

                           Net Salary= Gross Salary-Deductions
Ans :   i. Code to calculate and display commission:
        int com=0;
        if(jRadioButton1.isSelected())
        com=500;
        else if(jRadioButton2.isSelected())
        com=1000;
        else if(jRadioButton3.isSelected())
        com=2000;
        jTextField3.setText(“”+com);

        (½ mark for each correct if-else if statement)
        ( ½ mark for displaying commission value)

        ii. Code to calculate and display Gross Salary:

        int sal,comm;
        sal=Integer.parseInt(jTextField2.getText());
        comm=Integer.parseInt(jTextField3.getText());
        jTextField4.setText(“”+(sal+comm));

        (½ mark for fetching values)
        ( ½ mark for displaying Gross Salary)

        iii. Code to calculate and display charges for the facilities:
        int extra=0;
        if(jCheckBox1.isSelected())
        extra=extra+500;
        if(jCheckBox2.isSelected())
        extra=extra+2000;
        jTextField5.setText(“”+extra);

        (½ mark for initializing variable extra with 0)
        (½ mark for each correct if statement)
        ( ½ mark for displaying extra facility charges)

        iv. Code to calculate and display the Net Salary
        int amt,extra;
        amt=Integer.parseInt(jTextField4.getText());
        extra=Integer.parseInt(jTextField5.getText());
        jTextField6.setText(“”+(amt-extra));

        (½ mark for fetching values)
        ( ½ mark for displaying Net Salary)
```

---

## page 11

```
5   (a)    Mrs. Sharma is the classteacher of Class ‘XII A’ She wants to create a table     2
           ‘Student’ to store details of her class.
           i) Which of the following can be the attributes of Student table?
           a) RollNo b) “Amit” c) Name d) 25

           ii) Name the Primary key of the table ‘Student’. State reason for choosing it.
    Ans:   i. a) RollNo     b) Name

           (½ mark for each correct answer)
           ii.Primary Key: RollNo as it will be unique for each student of the class.
           (½ mark for identifying Primary key)
           (½ mark for stating correct reason)
    (b)    Write the output of the following SQL queries:                                   2
           i) SELECT TRUNCATE(8.975,2);
           ii) SELECT MID(‘HONESTY WINS’,3,4);
           iii) SELECT RIGHT(CONCAT(‘PRACTICES’,’INFORMATICS’),5);
           iv) SELECT DAYOFMONTH(‘2015-01-16’);
    Ans:   i. 8.97
           ii. NEST
           iii. ATICS
           iv. 16
           (½ mark for each correct output)
    (c)    Table “Emp” is shown below. Write commands in SQL for (i) to (iv) and output     6
           for (v) and (vi)

            ID          NAME        AGE   ADDRESS                 SALARY     PHONE

            1           Siddharth   25    A-4, Ashok Vihar,       62000      98110766656
                                          Delhi

            2           Chavi       23    B-21, Model Town,       71000      99113423989
                                          Mumbai



            3           Karan       26    KC-24, North            65000      98105393578
                                          Avenue, Bhopal

            4           Raunaq      22    A-152, Gomti Nagar,     89000      99101393576
                                          Lucknow

            5           Kunal       27    B-5/45, Uday Park,      80000      97653455654
                                          Delhi
```

---

## page 12

```
           i. To display list of all employees below 25 years old.

           ii. To list names and respective salaries in descending order of salary.
           iii. To count the number of employees with names starting with ‘K’
           iv. To list names and addresses of those persons who have ‘Delhi’ in their
           address.
           v. SELECT Name, Salary FROM Emp where salary between 50000 and
           70000;

           vi. SELECT Name, phone from emp where phone like ‘99%’;
    Ans:   MySQL Commands:

           i. SELECT * FROM Emp WHERE AGE<25;
           ii. SELECT NAME,SALARY FROM Emp ORDER BY SALARY desc;
           iii. SELECT COUNT(*) FROM Emp WHERE NAME LIKE “K%”;
           iv. SELECT NAME,ADDRESS FROM Emp WHERE ADDRESS LIKE”%Delhi%”;

           (1 mark for each correct query)

           OUTPUT
           v.
           Siddharth 62000
           Karan     65000

           vi.
           Chavi     99113423989
           Raunaq   99101393576

           (1 mark for each correct output)
6   (a)    Write SQL query to create a table ‘Player’ with the following structure:     (2)

                                   Field         Type           Constraint
                                   playerid      Integer        Primary key
                                   name          Varchar(50)
                                   height        Integer
                                   weight        Integer
                                   datebirth     Date
                                   teamname      Varchar(50)
    Ans:   CREATE TABLE Player (
                playerID integer PRIMARY KEY,
                name varchar(50),
                height integer,
                weight integer,
                datebirth date,
                teamname varchar(50) );
```

---

## page 13

```
       (½ Mark for CREATE TABLE Player)
       (½ Mark for constraint)
       (½ Mark for correct data types)
       (½ Mark for correct column)
(b)    Consider the tables given below.                                                (2)

       Salesperson


          SalespersonId       Name      Age    Salary

          1                   Ajay      61     140000

          2                   Sunil     34     44000

          5                   Chris     34     40000

          7                   Amaaya    41     52000



       Orders

          OrderId         SalespersonId       Amount

        10                2                   54000

        20                7                   18000

        30                1                   46000

        40                5                   24000


       i. The SalespersonId column in the "Salesperson" table is the _________
       KEY.The SalespersonId column in the "Orders" table is a ___________ KEY.

       ii. Can the ‘SalespersonId’ be set as the primary key in table ‘Orders’. Give
       reason.
Ans:   i. Primary, Foreign
       ii. No as it may be repeated in Orders table.

       (1 mark for correct column name)
(c)    With reference to the above given tables (in Q6 b), Write commands in SQL for   (6)
       (i) and (ii) and output for (iii) below:
```

---

## page 14

```
              i. To display SalespersonID, names, orderids and order amount of all
              salespersons.

              ii. To display names ,salespersons ids and order ids of those sales persons
              whose names start with ‘A’ and sales amount is between 15000 and 20000.

              iii. SELECT SalespersonId, name, age, amount FROM Salesperson,
              orders WHERE Salesperson.salespersonId= Orders.salespersonId
              AND AGE BETWEEN 30 AND 45;
    Ans:   i. SELECT S.SalespersonID, Name, OrderID, Amount FROM Salesperson
           S, Orders O WHERE S.SalespersonID= O.SalespersonID;

            (1 mark for correct use of select and from)
           (1 mark for correct use of where clause)

           ii. SELECT Name,S.SalespersonID,OrderID FROM Salesperson S,
           Orders O WHERE S. SalespersonID=O.SalespersonID AND Name LIKE
           “A%” AND Amount BETWEEN 15000 AND 20000;

            (1 mark for correct use of select, from and where clause)
            (½ mark for correct use of like operator)
           (½ mark for correct use of between operator/checking specified amount range)

           iii.
           2    Sunil     34    54000
           5    Chris     34    24000
           7    Amaaya    41    18000

           (2 mark for correct output)
7   (a)    ‘Bachpan Toys’ is a small company manufacturing toys. They have decided (2)
           that it would be beneficial to the company to create a website which would
           allow customers to order toys on-line. State how ‘Bachpan Toys’ would benefit
           from the website.
    Ans:   Through online marketing (e-business) they can reach to many customers of far away
           places in a cost effective manner. Also there is no need to incur huge cost of setting
           up a shop/store to sell items.

           (1 mark for each correct point)
    (b)    Which of the following is/are the advantage(s) of e-Governance                           (1)
           i) technology makes governance speedier
           ii) Computer literacy and basic Internet usage is not required.
           iii) governance is made transparent, that is most of the information is available
           to public.
    Ans:   i ) and iii)
           (½ mark for each correct advantage of e-Governance)
```

---

## page 15

```
(c)    Lakshmi works for a school. She wishes to create controls on a form for the      (2)
       following functions. Choose appropriate controls from Text field, Label, Radio
       button, Check box, List box, Combo box, Button and write in the third column.
        S. No.     Control used to             Control

        1          Enter Admission number

        2          Select Stream

        3          Select Subject

        4          Clear the Form



Ans:
            S.No             Control used to                        Control

        1             Enter Admission number               Text field

        2             Select Stream                        List box/ Combo box
                                                           /Radio button

        3             Select Subject                       Check box

        4             Clear the Form                       Button

       (½ mark for each correct control)
```