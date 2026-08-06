---
title: "ComputerScience-MS"
source_pdf: "ComputerScience-MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/ClassXII_2025_26/ComputerScience-MS.pdf"
pages: 10
pdf_bytes: 527378
pdf_sha256: "278085d0a2e266bbea3a1c9946d6cac074b2b4bdf967e5318c83f20fd6a78e6c"
text_chars: 20852
low_text_pages: 0
converter: "pdftotext -layout"
---

# ComputerScience-MS


---

## page 1

```
                                 COMPUTER SCIENCE – Code No. 083
                                       MARKING SCHEME
                                      Class - XII - (2025-26)
Time Allowed: 3 Hrs.                                                     Maximum Marks: 70

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


  Q No.                                  Section-A (21 x 1 = 21 Marks)                      Marks
    1     Answer:                                                                             1

          True
          (1 mark for correct answer)
    2     Answer:                                                                             1

          c) It
          (1 mark for correct answer)
    3     Answer:                                                                             1

          b) False
          (1 mark for correct answer)
    4     Answer:                                                                             1

          Equi-Join or Cartesian Join
          (1 mark for correct answer)
    5     Answer:                                                                             1

          a) lSf
          (1 mark for correct answer)
    6     Answer:                                                                             1

          Error as unsupported operand type(s) for +: 'int' and ‘str'
          (1 mark for the correct answer)
    7     Answer:                                                                             1

          -59.0
          (1 mark for the correct answer)



SQP-2025-26-XII-Computer Science (083)                                                    Page 1
```

---

## page 2

```
    8    Answer:                                                                                 1

         SELECT department, COUNT(*) FROM employees GROUP BY department
         HAVING COUNT(*) > 5;

         (1 mark for correct answer)
    9    Answer:                                                                                 1

         b) Some other error!
         (1 mark for correct answer)
    10   Answer:                                                                                 1

         d) Not Specified
         (1 mark for correct answer)
    11   Answer:                                                                                 1

         a) 50@70@
         (1 mark for correct answer)
    12   Answer:                                                                                 1

         c) 5@@12##12
         (1 mark for correct answer)
    13   Answer:                                                                                 1

         c) Both a) & b)
         (1 mark for correct answer)
    14   Answer:                                                                                 1

         b) ['Watersk', '', 'ng ', 's thr', 'll', ‘ng!']

         (1 mark for correct answer)
    15   Answer:                                                                                 1

         a) Degree: 7
         (1 mark for correct answer)
    16   Answer:                                                                                 1

         b) ALTER
         (1 mark for correct answer)
    17   Answer:                                                                                 1

         c) POP3
         (1 mark for correct answer)
    18   Answer:                                                                                 1

         a) A hub sends data to all devices in a network, while a switch sends data to the
         specific device
         (1 mark for correct answer)




SQP-2025-26-XII-Computer Science (083)                                                       Page 2
```

---

## page 3

```
    19    Answer:                                                                                1

          b) HTML
          (1 mark for correct answer)
 Q20 and Q21 are Assertion(A) and Reason(R) based questions. Mark the correct choice as:
 a) Both A and R are True and R is the correct explanation for A.
 b) Both A and R are True and R is not the correct explanation for A.
 c) A is True but R is False.
 d) A is False but R is True.
    20 Answer:                                                                                   1

          d) A is False but R is True

          (1 mark for correct answer)
    21    Answer:                                                                                1

          a) Both A and R are true and R is the correct explanation for A

          (1 mark for correct answer)
  Q No.                                  Section-B ( 7 x 2=14 Marks)                           Marks

    22    Answer:                                                                                2
          A. Implicit Conversion: Python automatically converts one data type to another.

          Example:
          x = 10
          y = 3.5
          result = x + y # x is implicitly converted to float
          Explicit Conversion: The user manually converts one data type to another using
          functions like int(), float().
          Example:
          x = "10"
          y = int(x) # Explicit conversion from string to integer

          (1 mark for correct difference)
          (1/2 mark for each correct example)
                                                    OR
          B. Break exits the loop entirely, while continue skips the current iteration and
               moves to the next one.
          Example of break:
          for i in range(5):
             if i == 2:
                 break # Exits the loop
             print(i)
          Output:
          1
          Example of continue:
          for i in range(5):
             if i == 2:




SQP-2025-26-XII-Computer Science (083)                                                       Page 3
```

---

## page 4

```
                continue # Skips printing 2
            print(i)
         Output:
         1
         3
         4
         5
         (1 mark for correct difference)
         (1/2 mark for each correct example)
    23    Answer:                                                                                2
          def remove_first_last(str):
             if len(str) < 2:
                 return str
             new_str = str[1:-1]
             return new_str
          result = remove_first_last("Hello")
          print("Resulting string: ", result)

         (1⁄2 mark each for correcting 4 mistakes)
    24   Answer:                                                                                 2
          A.
             I. index = review.find("good")                    (1 mark for correct answer)
            II. L1.sort(reverse=True)                          (1 mark for correct answer)

                                                       OR
           B. ('Learn Python ', 'with', ' fun and practice')   (1 mark for correct answer)
               3                                               (1 mark for correct answer)
    25   Answer:                                                                                 2
         A.
          def remove_element(L, n):
             if n in L:
                 L.remove(n)
                 print(L)
             else:
                 print("Element not found")
                                                     OR
         B.
         def add_contact(phone_book, name, number):
            if name in phone_book:
                print("Contact already exists")
            else:
                phone_book[name] = number
                print("Contact added successfully")
         (1/2 mark for function definition)
         (1½ marks for the correct/similar logic)
    26   Answer:                                                                                 2
         ['Arv', 'Ria']
         (2 marks for the correct output)




SQP-2025-26-XII-Computer Science (083)                                                       Page 4
```

---

## page 5

```
    27    Answer:                                                                                    2
          A.
             I.    Desc table_name; or describe table_name;
            II. Create database SQP;
          (1 mark for each correct answer.)
                                                   OR
          B. The DELETE query removes all the records or specific records from a table,
                preserving the table structure.
                Example: DELETE FROM Employees WHERE EmployeeID = 5;
                The DROP query removes the entire table or database along with its data.
                Example: DROP TABLE Employees;

          (1 mark for correct difference)
          (1/2 mark for each correct example)
    28    Answer:                                                                                    2
          A.
             I. A modem is a device that helps connect your computer or other devices to
                the internet. It converts digital signals from your device into analog signals
                that can travel through phone lines or other networks, and vice versa.
            II. A gateway is a device that connects two different networks and helps them
                communicate with each other. It translates the data between different
                network types, allowing them to work together.
          (1 mark for each correct definition)
                                                     OR
          B.
             I. HTTP: Hypertext Transfer Protocol and FTP: File Transfer Protocol
                (1/2 mark for each correct expansion.)
            II. A web server stores and delivers web pages to users over the internet. A
                web browser requests and displays these web pages on the user's device.
          (1 mark for correct point of difference)
  Q No.                                  Section-C ( 3 x 3 = 9 Marks)                              Marks

    29    Answer:                                                                                    3
          A.

          def count_python():
            count = 0
            with open("Prog.txt", 'r') as file:
               text = file.read()
               words = text.split()
               for word in words:
                  if word.lower() == "python":
                     count += 1
               print("The word Python appears", count, "times.")

          (1/2 mark for correct function header)
          (1/2 mark for correctly opening the file)
          (1/2 mark for correctly reading from the file)
          (1/2 mark for splitting the text into words)
          (1/2 mark for correct use of counter variable)



SQP-2025-26-XII-Computer Science (083)                                                           Page 5
```

---

## page 6

```
          (1/2 mark for displaying the result)
                                                       OR
          B.
          def display_non_vowel_lines():
             with open("STORIES.TXT", "r") as file:
                print("Lines that don't start with a vowel:")
                lines = file.readlines()
                for line in lines:
                    if line[0].lower() not in 'aeiou':
                        print(line)
          display_non_vowel_lines()
          (1/2 mark for correct function header)
          (1/2 mark for correctly opening the file)
          (1/2 mark for correctly reading from the file)
          (1 mark for correctly displaying the desired lines)
          (1/2 mark for correctly calling the function)
    30    Answer:                                                                             3
          I.
          L = [("Laptop", 90000), ("Mobile", 30000), ("Pen", 50), ("Headphones", 1500)]
          product = []
          def Push_element(L):
             for i in L:
                if i[1] > 50:
                    product.append(i)
             print(product)

          II.
          def Pop_element(product):
              while product:
                 print(product.pop())
              else:
                 print("Stack Emply")

          (1½ marks for each correct part)
    31    Answer:                                                                             3
          A. QP-^14
          (3 marks for the correct output)
                                                     OR
          B. ['K', 'R']
          (3 marks for the correct output)
  Q No.                                  Section-D ( 4 x 4 = 16 Marks)                      Marks

    32    Answer:                                                                             4
          A.
             I. SELECT Product, SUM(Quantity_Sold) FROM SALES GROUP BY Product
                HAVING SUM(Quantity_sold) > 12;
            II. SELECT * FROM SALES ORDER BY Product DESC;
           III. SELECT DISTINCT Product FROM SALES;
          IV. SELECT * from SALES where Customer_Name like "%e";




SQP-2025-26-XII-Computer Science (083)                                                    Page 6
```

---

## page 7

```
         (4 x 1 mark for each correct query)
                                                 OR
         B.

            I.




           II.




          III.




          IV.




         (4 x 1 mark for each correct query)
    33   Answer:                                                                                4
         I.
         import csv
         def Accept():
            product_id = input("Enter Product ID: ")
            product_name = input("Enter Product Name: ")
            quantity_sold = int(input("Enter Quantity Sold: "))
            price_per_unit = float(input("Enter Price Per Unit: "))
            with open('Sales.csv', 'a', newline='') as file:
               writer = csv.writer(file)
               writer.writerow([product_id, product_name, quantity_sold, price_per_unit])
            print("Sales record added successfully.")

         (1⁄2 mark for correctly taking user input)
         (1⁄2 mark for opening the file in append mode)
         (1⁄2 mark for correctly creating the writer object)



SQP-2025-26-XII-Computer Science (083)                                                      Page 7
```

---

## page 8

```
         (1⁄2 mark for correctly using writerow() of writer object)

         II.
         def CalculateTotalSales():
             total_sales = 0.0
             with open('Sales.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                   total_sales += int(row[2]) * float(row[3])
             print("Total Sales is:", total_sales)

         (1⁄2 mark for opening in the file in right mode)
         (1⁄2 mark for correctly creating the reader object)
         (1⁄2 mark for correctly checking the condition)
         (1⁄2 mark for correctly displaying the total sales)

         Note (for both parts (I) and (II)):
         Ignore import csv as it may be considered the part of the complete program.
    34   Answer:                                                                              4
             I.       SELECT Customer_Name FROM Hotels, Bookings WHERE Hotels.H_ID =
                      Bookings.H_ID AND City = 'Delhi';

             II.      SELECT Bookings.* FROM Hotels, Bookings WHERE Hotels.H_ID =
                      Bookings.H_ID AND City IN ('Mumbai', 'Chennai', 'Kolkata');

             III.     DELETE FROM Bookings WHERE Check_In < '2024-12-03';

             IV.      A. SELECT * FROM Hotels, Bookings;

                                                OR
                    B. SELECT Customer_Name, Hotel_Name FROM Hotels, Bookings
                    WHERE Hotels.H_ID = Bookings.H_ID;

         (4 x 1 mark for each correct query)
    35   Answer:                                                                              4
         import mysql.connector
         connection =
         mysql.connector.connect(host='localhost',user='admin_user',password='warehouse
         2024',database='WarehouseDB')
         cursor = connection.cursor()
         update_query = "UPDATE product_inventory SET Quantity = 91 WHERE
         Item_code = 208"
         cursor.execute(update_query)
         connection.commit()
         print("Data updated successfully.")
         cursor.close()
         connection.close()

         (1⁄2 mark for correctly importing the connector object)
         (1⁄2 mark for correctly creating the connection object)
         (1⁄2 mark for correctly creating the cursor object)



SQP-2025-26-XII-Computer Science (083)                                                    Page 8
```

---

## page 9

```
          (1 mark for correct creation of update query)
          (1 mark for correctly executing the query with commit)
          (1⁄2 mark for correctly closing the connection)
  Q No.                                  Section-E (2 X 5 = 10 Marks)                   Marks

    36    Answer:                                                                        2+3
          I.
          import pickle
          def append_data():
             with open("emp.dat", 'ab') as file:
                employee_id = int(input("Enter Employee ID: "))
                employee_name = input("Enter Employee Name: ")
                department = input("Enter Department: ")
                salary = float(input("Enter Salary: "))
                pickle.dump([employee_id, employee_name, department, salary], file)
             print("Employee data appended successfully.")

          (1/2 mark for correctly defining the function header)
          (1/2 mark for correctly opening the file in append mode)
          (1/2 mark for correctly taking user input)
          (1/2 mark for using dump() method of the pickle module)

          II.
          def update_data():
              updated = False
              employees = []
              with open("emp.dat", 'rb') as file:
                  try:
                     while True:
                        employee = pickle.load(file)
                        if employee[2] == "IT":
                            employee[3] = 200000
                            updated = True
                        employees.append(employee)
                  except EOFError:
                     pass
              with open("emp.dat", 'wb') as file:
                  for employee in employees:
                     pickle.dump(employee, file)
              if updated:
                  print("Salaries updated for IT department.")
              else:
                  print("No employee found in the IT department.")

          (1/2 mark for correctly defining the function header)
          (1/2 mark for correctly opening the file)
          (1 mark for using load() with while loop and try-except block)
          (1 mark for checking the condition and updating the value)




SQP-2025-26-XII-Computer Science (083)                                                Page 9
```

---

## page 10

```
         Note: Note (for both parts (I) and (II)): (i) Ignore import pickle as it may be
         considered the part of the complete program.
    37   Answer:                                                                                  5
           I. Block IT should house the server as it has maximum number of computers.
          II. a) Repeater is to be placed between Block IT to Block HR as distance between
              them is more than 100 metres.
              b) Switch is to be placed in each and every building.
         III. Draw the star topology cable layout.

                           HR                     IT               Finance




                                              Logistics
         IV.    Optical Fibre
          V.    A. Voice over Internet Protocol (VoIP) is a technology that allows users to
                make phone calls and other communications over the Internet instead of a
                traditional phone line.
                                                 OR
                B. WAN will be formed.

         (5 x 1 mark for each correct part)




SQP-2025-26-XII-Computer Science (083)                                                        Page 10
```