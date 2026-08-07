---
title: "Informatics Practices SQP (2015-16) Set 2"
source_pdf: "Informatics_Practices_SQP_(2015-16)_Set_2.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS XII_2015_16/Informatics Practices SQP/Informatics Practices SQP (2015-16) Set 2.pdf"
pages: 12
pdf_bytes: 534350
pdf_sha256: "15da3773383880dc8769ff22cb806b3b599f3bcf5f79cfbfe3bf036e98c7f325"
text_chars: 15239
low_text_pages: 1
converter: "pdftotext -layout"
---

# Informatics Practices SQP (2015-16) Set 2


---

## page 1

```
                         Informatics Practices (Code: 065)
                                          Sample Paper 2
                                           Class XII (2015-16)
        Time: 3Hrs.                                                                         MM: 70
1 (a)     The ‘Chalchitra’ theatre has a computer network. The network is in one building. (2)
          (i) Name this type of network( out of LAN/MAN/WAN).
          (ii) Name one communication channel that can be used for fast communication
          between workstations of the network.
  (b)     Explain in brief any 2 security threats to Computer networks.                          (2)
  (c)     Write the advantages of using Unicode to represent text.                               (2)
  (d)     Write one example each of URL and IP address.                                          (2)
  (e)     Identify the topology shown below. Write 2 advantages of this topology.                (2)




2 (a)     While working in Netbeans, Ms. Sonia has designed a login page where she wants to      (1)
          display “Welcome” or “Try again” message depending on the password entered by
          the user in text field named ‘jTexField1’. If password entered is “India”, ‘Welcome’
          message should be displayed otherwise ‘Try again’ message should be displayed. Help
          her in choosing more appropriate statement out of 'If statement' and 'Switch
          statement'. Give reason for your choice.




                                                1
```

---

## page 2

```
  (b)   Write Java code to assign the value 10 to variable x and store its square value in    (1)
        another variable y.

  (c)   Deepti works as a programmer in a travel company. She has developed the following     (2)
        code to display travel detail according to user’s choice. Help her in rewriting the
        same code using SWITCH CASE:

              if(choice==1)
                jTextField1.setText(“New Delhi to Goa”);
              else if(choice==2)
                jTextField1.setText(“New Delhi to Paris”);
              else if(choice==3)
                jTextField1.setText(“New Delhi to Bangkok”);
              else
                jTextField1.setText(“Pl. choose valid option”);
  (d)   Shambhavi has to design two web pages with following specifications:                  (2)
           i.   One web page should have an unordered list.
           ii.   Another web page should have background “Yellow” in colour.

        Suggest her suitable tag(s) and attribute(s) for the above specifications.
  (e)   Albert works as a website developer in Global Website Designers company. Currently    (2)
        he has created following tags in XML:
        <STUDENT>...</STUDENT>
        <Student>....</Student>

        Are these tags part of HTML code or XML code?
        Are these same same or different?
  (f)   How many times will the loop execute?                                                 (2)

        int value1 =7,value2=19;
        do
        {
             JOptionPane.showMessageDialog(null,value1+value2);
             value1=value1+2;
             value2=value2-2;
        }while(value1<=value2);
3 (a)   Consider the table ‘empsalary’.                                                       (1)


                                               2
```

---

## page 3

```
      ID           Salary


      101         43000

      102         NULL

      104         56000

      107         NULL

      To select tuples with some salary ,Siddharth has written the following erroneous SQL
      statement:
      SELECT ID, Salary FROM empsalary WHERE Salary = something;

      Write the correct SQL statement.

(b)   Consider the table ‘Employee’.                                                         (1)
      Employee


       Name                   Location


       Gurpreet               Mumbai

       Jatinder               Chennai

       Deepa                  Mumbai

       Harsh                  Chennai

       Simi                   New Delhi

       Anita                  Bengaluru

      Write the SQL command to obtain the following output :



                                           3
```

---

## page 4

```
       Location

       Mumbai

       Chennai

       New Delhi

       Bengaluru


(c)   While creating the table Student last week, Ms. Sharma forgot to include the column (1)
      Game_Played. Now write a command to insert the Game_Played column with
      VARCHAR data type and 30 size into the Student table?

(d)   In Marks column of ‘Student’ table, for Rollnumber 2, the Class Teacher entered the   (1)
      marks as 45. However there was a totaling error and the student has got her marks
      increased by 5. Which MySQL command should she use to change the marks in
      ‘Student’ table.

(e)   Consider the table ‘Teacher’ given below.                                             (2)

         TeacherId         Department           Periods

         T101              SCIENCE              32

         T102              NULL                 30

         T103              MATHEMATICS          34


      What will be the output of the following queries on the basis of the above table:
      (i)Select count(Department) from Teacher;
      (ii)Select count(*) from Teacher;




                                            4
```

---

## page 5

```
(f)   Consider the Stu table                                                           (2)

              ROLLNO           NAME



             1           Ashi



             2           Bimmi



             4           Aakash


      The following SQL queries are executed on the above table

      INSERT INTO Stu VALUES(5,'Gagan');
      COMMIT;
      UPDATE Stu SET name='Abhi' WHERE Rollno = 4

      SAVEPOINT A;
      INSERT INTO Stu VALUES(6,'Chris');
      SAVEPOINT B;
      INSERT INTO Stu VALUES(7,'Babita');
      SAVEPOINT C;

      ROLLBACK TO B;

      What will be the output of the following SQL query now:
      SELECT * FROM Stu;


(g)   An attribute A of datatype varchar(20) has the value “Amit” . The attribute B of (2)
      datatype char(20) has value ”Karanita” .
                                              5
```

---

## page 6

```
        How many characters are occupied in attribute A ? How many characters are occupied
        in attribute B?
4 (a)   Following is a list of programming languages:                                        (1)
        BASIC, COBOL, C, JAVA
        Help Sandhya in identifying Object Oriented language(s) from the above given list.
  (b)   Satyam is designing a frame in Netbeans containing list box. Help him in writing (1)
        suitable Java statement to extract selected item from a given listbox named “jList1.”
  (c)   What will be displayed in jTextField1 and jTextField2 after the following code is (1)
        executed:

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
  (d)   Find output of the following Java code snippet:                                      (2)

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
  (e)   Rewrite the following code using WHILE loop:                                         (2)
         int x=100;
        for(int i=2;i<=22;i=i+4)
        {
                                                6
```

---

## page 7

```
       jTextArea1.append("\n"+(i+x));
       x=x-2;
      }
(f)   The following code has error(s). Rewrite the correct code underlining all the           (2)
      corrections made :
            int n=5,int i=1,f=1;
            do;
            {
            f=f*i;
            i++;
            while(i<=n)
            jTextField1.setText(""+f);
(g)   Mr. Pawan works as a programmer in “ABC Marketing Company” where he has
      designed a Salary generator software to generate the salary of salesman in which
      Name and Salary are entered by the user. A screenshot of the same is shown below:




      Help him in writing the code to do the following:

      i. After selecting appropriate Radio Button, when ‘Commission’ button is clicked,       2
      commission should be displayed in the respective text field as each Salesman will get
      a commission based on the units sold according to the following criteria:

                                            7
```

---

## page 8

```
                                       Units Sold    Commission
                                                     (in Rs)

                                    1 to 20          500

                                    20 to 40         1000

                                    >40              2000

        ii. When ‘Gross Salary’ button is clicked, Gross Salary should be calculated and
        displayed in the respective text field as per the given formula:                         1
                           Gross Salary= Salary+Commission

        iii. After required selection of Checkbox(es), when ‘Facility Charges’ button is
        clicked, Facility charges will be displayed in the respective text field according to the 2
        following criteria:

                                    Facility         Charges

                                    Transport        500

                                    Mess             2000

        iv. Money will be deducted from the Gross Salary according to the facilities opted by    1
        the employee. When ‘Net Salary’ button is clicked, Net Salary should be calculated
        and displayed in the respective text field as per the given formulae:
                          Net Salary= Gross Salary-Deductions
5 (a)   Mrs. Sharma is the classteacher of Class ‘XII A’ She wants to create a table ‘Student’   2
        to store details of her class.
        i) Which of the following can be the attributes of Student table?
        a) RollNo b) “Amit” c) Name d) 25

        ii) Name the Primary key of the table ‘Student’. State reason for choosing it.

  (b)   Write the output of the following SQL queries:                                           (2)
               i) SELECT TRUNCATE(8.975,2);

                                                8
```

---

## page 9

```
            ii) SELECT MID(‘HONESTY WINS’,3,4);
            iii) SELECT RIGHT(CONCAT(‘PRACTICES’,’INFORMATICS’),5);
            iv) SELECT DAYOFMONTH(‘2015-01-16’);
(c) Table “Emp” is shown below. Write commands in SQL for (i) to (iv) and output for (v)   (6)
    and (vi)

      ID       NAME          AGE       ADDRESS                   SALARY     PHONE

      1        Siddharth     25        A-4, Ashok Vihar, Delhi   62000      98110766656

      2        Chavi         23        B-21, Model Town,         71000      99113423989
                                       Mumbai



      3        Karan         26        KC-24, North Avenue,      65000      98105393578
                                       Bhopal

      4        Raunaq        22        A-152, Gomti Nagar,       89000      99101393576
                                       Lucknow

      5        Kunal         27        B-5/45, Uday Park,        80000      97653455654
                                       Delhi

     i. To display list of all employees below 25 years old.

     ii. To list names and respective salaries in descending order of salary.
     iii. To count the number of employees with names starting with ‘K’
     iv. To list names and addresses of those persons who have ‘Delhi’ in their address.
     v. SELECT Name, Salary FROM Emp where salary between 50000 and 70000;

     vi. SELECT Name, phone from emp where phone like ‘99%’;




                                            9
```

---

## page 10

```
6 (a)   Write SQL query to create a table ‘Player’ with the following structure:   2

                                  Field         Type          Constraint
                                  playerid      Integer       Primary key
                                  name          Varchar(50)
                                  height        Integer
                                  weight        Integer
                                  datebirth     Date
                                  teamname      Varchar(50)
  (b)   Consider the tables given below.                                           2

        Salesperson


          SalespersonId       Name     Age     Salary

          1                   Ajay     61      140000

          2                   Sunil    34      44000

          5                   Chris    34      40000

          7                   Amaaya   41      52000


        Orders

           OrderId        SalespersonId       Amount

         10               2                   54000

         20               7                   18000

         30               1                   46000



                                                 10
```

---

## page 11

```
         40                5               24000


        i. The SalespersonId column in the "Salesperson" table is the _________ KEY.The
        SalespersonId column in the "Orders" table is a ___________ KEY.

        ii. Can the ‘SalespersonId’ be set as the primary key in table ‘Orders’. Give reason.

  (c)   With reference to the above given tables (in Q6 b), Write commands in SQL for (i) and     6
        (ii) and output for (iii) below:
             i. To display SalespersonID, names, orderids and order amount of all salespersons.

             ii. To display names ,salespersons ids and order ids of those sales persons whose
             names start with ‘A’ and sales amount is between 15000 and 20000.

             iii. SELECT SalespersonId, name, age, amount FROM Salesperson, orders
             WHERE Salesperson.salespersonId= Orders.salespersonId AND AGE
             BETWEEN 30 AND 45;
7 (a)   ‘Bachpan Toys’ is a small company manufacturing toys. They have decided that it           (2)
        would be beneficial to the company to create a website which would allow customers
        to order toys on-line. State how ‘Bachpan Toys’ would benefit from the website.
  (b)   Which of the following is/are the advantage(s) of e-Governance                       (1)
        i) technology makes governance speedier
        ii) Computer literacy and basic Internet usage is not required.
        iii) governance is made transparent, that is most of the information is available to
        public.
  (c)   Lakshmi works for a school. She wishes to create controls on a form for the following     (2)
        functions. Choose appropriate controls from Text field, Label, Radio button, Check
        box, List box, Combo box, Button and write in the third column.
         S. No.     Control used to             Control

         1          Enter Admission number

         2          Select Stream


                                              11
```

---

## page 12

```
3   Select Subject

4   Clear the Form




                     12
```