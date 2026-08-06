---
title: "ComputerScience-SQP"
source_pdf: "ComputerScience-SQP.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2025_26/ComputerScience-SQP.pdf"
pages: 8
pdf_bytes: 695875
pdf_sha256: "f88512f2e8f0316a2d62f45e618e004344fec2ee9f0bc4166b47e2a171036ef6"
text_chars: 21210
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-SQP


---

## page 1

```
                                   COMPUTER SCIENCE – Code No. 083
                                      SAMPLE QUESTION PAPER*
                                         Class - XII - (2025-26)
Time Allowed: 3 Hrs.                                                                  Maximum Marks: 70

General Instructions:
    This question paper contains 37 questions.
    All questions are compulsory. However, internal choices have been provided in some
      questions. Attempt only one of the choices in such questions.
    The paper is divided into 5 Sections- A, B, C, D and E.
    Section A consists of 21 questions (1 to 21). Each question carries 1 Mark.
    Section B consists of 7 questions (22 to 28). Each question carries 2 Marks.
    Section C consists of 3 questions (29 to 31). Each question carries 3 Marks.
    Section D consists of 4 questions (32 to 35). Each question carries 4 Marks.
    Section E consists of 2 questions (36 to 37). Each question carries 5 Marks.
    All programming questions are to be answered using Python Language only.
    In-case of MCQ, text of the correct answer should also be written.


 Q No.                                    Section-A (21 x 1 = 21 Marks)                                        Marks
    1    State if the following statement is True or False:                                                           1
         Using the statistics module, the output of the below statements will be 20:
         import statistics
         statistics.median([10, 20, 10, 30, 10, 20, 30])

    2    What will be the output of the following code?                                                               1
         L = ["India", "Incredible", "Bharat"]
         print(L[1][0] + L[2][-1])

         a) IT            b) it            c) It             d) iT
    3    Consider the given expression:                                                                               1
         print(19<11 and 29>19 or not 75>30)
         Which of the following will be the correct output of the given expression?
         a) True         b) False         c) Null           d) No output
    4    In SQL, which type of Join(s) may contain duplicate column(s)?                                               1
    5    What will be the output of the following Python code?                                                        1
         str= "Soft Skills"
         print(str[-3::-3])
         a) lSf            b) Stkl       c) StKi           d) l
    6    Write the output of the following Python code :                                                              1
         for k in range(7,40,6):
              print ( k + '-' )
    7    What will be the output of the following Python statement:                                                   1
         print(10-3**2**2+144/12)
    8    Consider the given SQL Query:                                                                                1
         SELECT department, COUNT(*) FROM employees HAVING COUNT(*) > 5 GROUP
         BY department;

*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 1
```

---

## page 2

```
         Saanvi is executing the query but not getting the correct output. Write the correction.
    9     What will be the output of the following Python code?                                                       1
         try:
            x = 10 / 0
         except Exception:
            print("Some other error!")
         except ZeroDivisionError:
            print("Division by zero error!")
         a) Division by zero error!            b) Some other error!
         c) ZeroDivisionError                  d) Nothing is printed
   10    What will be the output of the following Python code?                                                        1
         my_dict = {"name": "Alicia", "age": 27, "city": "DELHI"}
         print(my_dict.get("profession", "Not Specified"))
          a) Alicia         b)DELHI             c)None               d)Not Specified
   11    What possible output is expected to be displayed on the screen at the time of execution                      1
         of the Python program from the following code?

         import random
         L=[10,30,50,70]
         Lower=random.randint(2,2)
         Upper=random.randint(2,3)
         for K in range(Lower, Upper+1):
            print(L[K], end="@")

         a) 50@70@              b) 90@                 c) 10@30@50@ d) 10@30@50@70@
   12    What will be the output of the following Python code?                                                        1
         i=5
         print(i,end='@@')
         def add():
          global i
          i = i+7
          print(i,end='##')
         add()
         print(i)
         a) 5@@12##15            b) 5@@5##12            c) 5@@12##12     d)12@@12##12
   13    Which SQL command can change the cardinality of an existing relation?                                        1
         a) Insert        b) Delete          c) Both a) & b)     d) Drop
   14    What is the output of the given Python code?                                                                 1
         st='Waterskiing is thrilling!'
         print(st.split("i"))
         a) ['Watersk', 'ng ', 's thr', 'll', ‘ng!']         b) ['Watersk', '', 'ng ', 's thr', 'll', 'ng!']
         c) ['Watersk', 'i', 'ng ', 's thr', 'll', ‘ng!']    d) Error
   15    In SQL, a relation consists of 5 columns and 6 rows. If 2 columns and 3 rows are added                       1
         to the existing relation, what will be the updated degree of a relation?
         a) Degree: 7                                        b) Degree: 8
         c) Degree: 9                                        d) Degree: 6
   16    Which SQL command is used to remove a column from a table in MySQL?                                          1
         a) UPDATE                 b) ALTER               c) DROP                 d) DELETE

*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 2
```

---

## page 3

```
   17     _________ is a protocol used for retrieving emails from a mail server.                                      1
          a) SMTP              b) FTP             c) POP3               d) PPP
   18    Which of the following is correct about using a Hub and Switch in a computer network?                        1
         a) A hub sends data to all devices in a network, while a switch sends data to the
         specific device.
         b) A hub sends data only to the devices it is connected to, while a switch sends data to
         all devices in a network.
         c) A hub and switch function the same way and can be used interchangeably.
         d) A hub and switch are both wireless networking devices.
   19    Which of the following is used to create the structure of a web page?                                        1
         a) CSS              b) HTML           c) JavaScript              d) FTP
Q20 and Q21 are Assertion(A) and Reason(R) based questions. Mark the correct choice as:
a) Both A and R are True and R is the correct explanation for A.
b) Both A and R are True and R is not the correct explanation for A.
c) A is True but R is False.
d) A is False but R is True.
   20 Assertion (A): The expression (1, 2, 3, 4).append(5) in Python will modify the original                         1
         sequence datatype.
         Reason (R): The append() method adds an element to the end of a list and modifies the
         list in place.
   21 Assertion (A): A primary key must be unique and cannot have NULL values.                                        1
         Reasoning (R): The primary key uniquely identifies each row in the table.

 Q No.                                     Section-B ( 7 x 2=14 Marks)                                          Marks
   22    A. Explain the difference between explicit and implicit type conversion in Python with a                     2
             suitable example.
                                                     OR
         B. Explain the difference between break and continue statements in Python with a
             suitable example.
   23     The code provided below is intended to remove the first and last characters of a                            2
         given string and return the resulting string. However, there are syntax and logical
         errors in the code.
         Rewrite it after removing all the errors. Also, underline all the corrections made.
          define remove_first_last(str):
             if len(str) < 2:
                 return str
             new_str = str[1:-2]
             return new_str
          result = remove_first_last("Hello")
          Print("Resulting string: " result)

   24     A. (Answer using Python built-in methods/functions only):                                                   2

            I.   Write a statement to find the index of the first occurrence of the substring
                 "good" in a string named review.
           II.   Write a statement to sort the elements of list L1 in descending order.



*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 3
```

---

## page 4

```
                                                     OR
          B. Predict the output of the following Python code:
         text="Learn Python with fun and practice"
         print(text.partition("with"))
         print(text.count("a"))

   25    A. Write a function remove_element() in Python that accepts a list L and a number n. If                      2
               the number n exists in the list, it should be removed. If it does not exist, print a
               message saying "Element not found".
                                                    OR
         B. Write a Python function add_contact() that accepts a dictionary phone_book, a
         name, and a phone number. The function should add the name and phone number to
         the dictionary. If the name already exists, print "Contact already exists" instead of
         updating it.
   26    Predict the output of the Python code given below :                                                          2
         emp = {"Arv": (85000,90000),"Ria": (78000,88000),"Jay": (72000,80000),"Tia":
          (80000,70000)}
         selected = [ ]
         for name in emp:
             salary = emp[name]
             average = (salary[0] + salary[1]) / 2
             if average > 80000:
                 selected.append(name)
         print(selected)
   27    A. Write suitable commands to do the following in MySQL.                                                     2
            I.    View the table structure.
           II. Create a database named SQP
                                                         OR
         B. Differentiate between drop and delete query in SQL with a suitable example.
   28    A. Define the following terms:                                                                               2
            I.    Modem
           II. Gateway
                                                         OR
         B.
            I.    Expand the following terms: HTTP and FTP
           II. Differentiate between web server and web browser.
 Q No.                                     Section-C ( 3 x 3 = 9 Marks)                                         Marks
   29    A. Write a Python function that displays the number of times the word "Python"                               3
             appears in a text file named "Prog.txt".
                                                      OR
         B. Write and call a Python function to read lines from a text file STORIES.TXT and
             display those lines which doesn’t start with a vowel (A, E, I, O, U) irrespective of
             their case.
   30    A list containing records of products as                                                                     3
             L = [("Laptop", 90000), ("Mobile", 30000), ("Pen", 50), ("Headphones", 1500)]
         Write the following user-defined functions to perform operations on a stack named
         Product to:


*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 4
```

---

## page 5

```
              I. Push_element() – To push an item containing the product name and price of
                  products costing more than 50 into the stack.
                      Output: [('Laptop', 90000), ('Mobile', 30000), ('Headphones', 1500)]
             II. Pop_element() – To pop the items from the stack and display them. Also, display
         "Stack Empty" when there are no elements in the stack.
                      Output:
                      ('Headphones', 1500)
                      ('Mobile', 30000)
                      ('Laptop', 90000)
                      Stack Emply
   31    A. Predict the output of the following Python code:                                                          3
         s1="SQP-25"
         s2=""
         i=0
         while i<len(s1):
            if s1[i]>='0' and s1[i]<='9':
                Num=int(s1[i])
                Num-=1
                s2=s2+str(Num)
            elif s1[i]>='A' and s1[i]<='Z':
                s2=s2+s1[i+1]
            else:
                s2=s2+'^'
            i+=1
         print(s2)
                                                       OR
         B. Predict the output of the following Python code:
         wildlife_sanctuary = ["Kaziranga", "Ranthambhore", "Jim Corbett", "Sundarbans",
         "Periyar", "Gir", "Bandipur"]
         output = [ ]
         for sanctuary in wildlife_sanctuary:
            if sanctuary[-1] in 'aeiou':
                output.append(sanctuary[0].upper())
         print(output)
 Q No.                                    Section-D ( 4 x 4 = 16 Marks)                                         Marks
   32    Consider the table SALES as given below:                                                                     4




         A. Write the following queries:
           I. To display the total quantity sold for each product whose total quantity sold
              exceeds 12.
          II. To display the records of SALES table sorted by Product name in descending
              order.
*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 5
```

---

## page 6

```
          III.   To display the distinct Product names from the SALES table.
          IV.    To display the records of customers whose names end with the letter 'e'.
                                                    OR
         B. Predict the output of the following:
            I.   SELECT * FROM Sales where product='Tablet';
           II. SELECT sales_id, customer_name FROM Sales WHERE product LIKE 'S%';
          III. SELECT COUNT(*) FROM Sales WHERE product in ('Laptop', 'Tablet');
         IV. SELECT AVG(price) FROM Sales where product='Tablet';
   33    Raj is the manager of a medical store. To keep track of sales records, he has created a                      4
         CSV file named Sales.csv, which stores the details of each sale.

         The columns of the CSV file are: Product_ID, Product_Name, Quantity_Sold and
         Price_Per_Unit.

         Help him to efficiently maintain the data by creating the following user-defined functions:

            I.   Accept() – to accept a sales record from the user and add it to the file Sales.csv.

           II.   CalculateTotalSales() – to calculate and return the total sales based on the
                 Quantity_Sold and Price_Per_Unit.

   34    Pranav is managing a Travel Database and needs to access certain information from the                        4
         Hotels and Bookings tables for an upcoming tourism survey. Help him extract the
         required information by writing the appropriate SQL queries as per the tasks mentioned
         below:
                                              Table: Hotels




                                                  Table: Bookings




*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 6
```

---

## page 7

```
            I.   To display a list of customer names who have bookings in any hotel of 'Delhi'
                 city.
           II.   To display the booking details for customers who have booked hotels in
                 'Mumbai', 'Chennai', or 'Kolkata'.
          III.   To delete all bookings where the check-in date is before 2024-12-03.
          IV.    A.    To    display    the    Cartesian   Product     of   the   two    tables.
                                                  OR
                 B. To display the customer’s name along with their booked hotel’s name.

   35    MySQL database named WarehouseDB has a product_inventory table in MySQL which                                4
         contains the following attributes:
           •   Item_code: Item code (Integer)
           •   Product_name: Name of product (String)
           •   Quantity: Quantity of product (Integer)
           •   Cost: Cost of product (Integer)
         Consider the following details to establish Python-MySQL connectivity:
           •    Username: admin_user
           •    Password: warehouse2024
           •    Host: localhost
         Write a Python program to change the Quantity of the product to 91 whose Item_code is
         208 in the product_inventory table.
 Q No.                                    Section-E (2 X 5 = 10 Marks)                                          Marks
   36    Mr. Ravi, a manager at a tech company, needs to maintain records of employees. Each                      2+3
         record should include: Employee_ID, Employee_Name, Department and Salary.
         Write the Python functions to:
            I.  Input employee data and append it to a binary file.
           II. Update the salary of employees in the "IT" department to 200000.
   37    XYZNova Inc. is planning a new campus in Hyderabad while maintaining its headquarters                        5
         in Bengaluru. The campus will have four buildings: HR, Finance, IT, and Logistics. As a
         network expert, you are tasked with proposing the best network solutions for their needs
         based on the following:
                                   From           To        Distance (in meters)

                           HR        Finance             50
                           HR        IT                 175
                           HR        Logistics           90
                           Finance IT                    60
                           Finance Logistics             70
                           IT        Logistics           60
         Number of Computers in Each Block:
                             Block           Number of Computers
                             HR                        60
                             Finance                   40
                             IT                        90

*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 7
```

---

## page 8

```
                                 Logistics                    35
            I.   Suggest the best location for the server in the Hyderabad campus and explain
                 your reasoning.
           II.   Suggest the placement of the following devices:
                 a) Repeater      b) Switch
          III.   Suggest and draw a cable layout of connections between the buildings inside the
                 campus.
          IV.    The organisation plans to provide a high-speed link with its head office using a
                 wired connection. Which of the cables will be most suitable for this job?
           V.    A. What is the use of VoIP?
                                                  OR
                 B. Which type of network (PAN, LAN, MAN, or WAN) will be formed while
                 connecting the Hyderabad campus to Bengaluru Headquarters?




*Please note that the assessment scheme of the Academic Session 2024-25 will continue in the current session i.e.
2025-26.
                                                                                                             Page 8
```