---
title: "XII Multimedia WebTech SQP 2018-19"
source_pdf: "XII_Multimedia_WebTech_SQP_2018-19.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/Class_XII_2018_19/XII_Multimedia_WebTech_SQP 2018-19.pdf"
pages: 6
pdf_bytes: 496762
pdf_sha256: "0959509a7997ab3a4353689aea14f908523f1b45bc1cafb6b5bdb973d6c5c6a7"
text_chars: 10477
low_text_pages: 0
converter: "pdftotext -layout"
---

# XII Multimedia WebTech SQP 2018-19


---

## page 1

```
                                     Sample Question Paper
                                Multimedia and Web Technology
                                           Class: XII
                                       Session 2018-19
Max. Marks: 70                                                                      Duration: 3 hrs.
General Instructions:
   (i) All questions are compulsory.
   (ii) Answer the questions after carefully reading the text.


Q1.    (a) Shreya wants to work on database management software. Suggest her any two examples of
       common database management system.                                                   (1)
       (b) What is field in a database? Give an example.                                               (1)
       (c) Define and identify the primary key in the following table:                                 (2)
                                Table: Stationary

                 S_No S_Name            S_Qty PurchaseDate
                 101      Pen           102         2011-12-12
                 102      Pencil        201         2013-02-21
                 103      Eraser        90          2011-09-09
                 109      Sharpener 90              2012-08-31
                 113      Clips         900         2011-09-09

       (d) Shweta wants to delete the records where the "FirstName" is "Rahul" in the „Emp‟ Table. She
           has entered the following SQL statement. An error is being displayed. Rewrite the correct
           statement.                                                                                  (1)
                 DELETE „Rahul‟ FirstName FROM Emp;

       (e) Differentiate between JPEG and GIF image.                                                   (2)
        (f) Explain the term “Publishing a Flash Movie”? Name the extension of the file created when a
        Flash movie is published using a Macintosh projector.                                          (2)
       (g) Mention any one use of Multimedia in healthcare.                                            (1)
Q2. Answer the following question based on Macromedia Flash:
    (a) What is Frame rate?                                                                            (1)
    (b) Differentiate between Motion Tweening and Shape Tweening.                                      (2)
    (c) Name any two movie file formats.                                                               (1)
    (d) Define layer. Write one advantage of using layers in Flash.                                    (2)
```

---

## page 2

```
    (e) Observe the figure given below and do as directed:                                               (4)




      The object on the left hand side shows the position and size of the image for frame 1. The colour of
        the object is blue.
     The object on the right hand side shows the position and size of the image for frame 20. The colour
      of the object is green.
     The circle on frame 1 moves and transforms into an ellipse on frame 20.
Write the procedure and property settings for animating the above scenario.
Q3. Answer the following questions based on HTML
(a) Write the HTML command to create a button in a form with the caption “Click Me”                      (1)
(b) Identify the errors in the following HTML code. Also write the correct code.                         (1)
        <OL TYPE= “a” START= “f”>
(c) Write the HTML code to generate a Web Page in the format given below:                                (8)
   Consider the following while writing the HTML code:

          Title of the page should be “Handmade Cards”.
          Background colour should be “Pink”.
          Text style of the main heading should be “Arial Bold” and color should be red.
          Image used is “cards.jpg”.
          Table in the center of the webpage and should have a 3 pixel thick border of color green and the
           spacing between cell content and border is 10 pixels.
          Use the concept of nested lists for creating the specified lists.
          The bottom image (link.jpg) and the text “Personalize The Card” are links to another page
           “person.html”.
```

---

## page 3

```
Q4. Answer the following questions based on PHP:
   (a) Write any two features of PHP.                                        (1)
   (b) Write the output of the given code:                                   (2)
              <?php
              $sum=0;
              for($a=1; $a<=8; $a +=2)
                   $sum = $sum + $a;
              echo($sum);
              echo("<BR>");
              echo($a);
             ?>
   (c) What is a constant? Declare a constant MAX and assign the value 10.   (2)
   (d) Give output of the following statements:                              (3)
       (i) echo 10/5+2*4%8;
       (ii) echo strtolower("PRODUCT ACTIVATED");
       (iii) echo date("M-d-Y", mktime(0,0,0,8,42,2017));

   (e) Rewrite the following code using switch case                          (2)
       if($Type=='T')
          echo "DISCOUNT ON TV";
       else if($Type=='M')
          echo "DISCOUNT ON MOBILE PHONE";
       else if($Type=='C')
          echo "DISCOUNT ON CAMERAS";
       else
          echo "NO DISCOUNT";
```

---

## page 4

```
   Q5. Answer the following questions based on PHP:
   (a) What is PHP global variable $_REQUEST?                                                     (1)
   (b) Following is the code to count total number of characters from a text file.
       Fill in the blanks so that this code can work:                                             (2)
       <? php
       $file = _______(“data.txt”, “r”);
       $ch = 0;
       while(_______($file))
       {
                $letter= ________________________;
                $ch     = ________________________;
       }
       echo “Number of characters:”, $ch;
       fclose($file);
       ?>
   (c) Rewrite the following code after removing errors with each correction                      (2)
       underlined.
       <?
       value=5;
       while($value!= =0)
       {
                $r_digit=$value%10;
                $value/=10;
       }
         ECHO $r_digit;
       ?>
   (d) Name the built-in functions to be used in the following situations:                        (2)
       (i) To remove backslash from a string.
       (ii) To return number of days in a month for specified year.

   (e) What is a cookie? Write the PHP code to set a cookie named “car” and value “BMW”. The cookie
       should expire after two days. Also Display the value stored in $_COOKIE                    (3)

Q6. Answer the following questions based on JavaScript:
(a) Write the code using do while loop without effecting the output:                              (2)
      <script language="javascript">
      var prod,b;
      prod=1;
      for(b=1;b<=10;b+=3)
      {
              document.write(b);
              prod=prod+b*b;
      }
      document.write(“the final prod is” & prod);
(b) Explain Conditional operator with the help of an example.                                     (2)
(c) Analyse the given program segment and determine how many times the                            (2)
     loop will be executed. What will be the value of A after loop is terminated.
     var A , B;
```

---

## page 5

```
        A = 5;
        B = 10;
        while(A>=1)
        {
                 document.Write(A+B);
                 A = A - 1;
                 B = B – 2;
        }
  (d) Write the code to display a form as shown below along with the javascript code to achieve the specified
  task. User should be able to enter the number of calls and the total amount payable gets displayed when he
  presses “calculate” button.



                                                                                                         (4)
The total amount payable will be calculated based on the following rate list:
                Rs. 1.00 per call for the 1st 100 calls
                Rs. 1.20 per call for the next 100 calls
                Rs. 1.50 per call for the next 50 calls
                Rs. 2.00 per call for more than 250 calls

   Q7. Answer the following questions based on Communication and network concepts:

     (a) How firewall protect our network?                                                               (1)
     (b) Write one advantage of Bus Topology of network. Also, illustrate how 4 computers can
         be connected with each other using bus topology of network.                                     (1)

      (c) Explain the following terms:                                                                   (2)
           i. GSM
          ii. CDMA
     (d) Write two advantages of using open source software over proprietary software.                   (1)
     (e) What is the significance of UNICODE?                                                            (1)
     (f) The Cyber Skill Development Organisation has set up its new Branch at Nagaland for its offices and
          web based activities. It has 4 Wings of buildings as shown in the diagram                      (4)




                                Z                                       Y




                                X                                        U
```

---

## page 6

```
           Center to center distance between various blocks
             Wing X to Wing Z                          30m
             Wing Z to Wing Y                          50m
             Wing Y to Wing X                          125m
             Wing Y to Wing U                          60m
             Wing X to Wing U                          155m
             Wing Z to Wing U                          110m

           Number of computers
             Wing X                                  40
             Wing Z                                  120
             Wing Y                                  30
             Wing U                                  10

(i)     Suggest a most suitable cable layout of connections between the Wings and topology.
(ii)    Suggest the most suitable place (i.e. Wing) to house the server of this organization with a suitable
        reason with justification.
(iii)   Suggest the placement of the following devices with justification:
            o Repeater
            o Hub/Switch
(iv)    The organization is planning to link its head office situated in Delhi with offices at Nagaland.
Suggest an economic way to connect it; company is ready to compromise on the speed of connectivity.
Justify your answer.
```