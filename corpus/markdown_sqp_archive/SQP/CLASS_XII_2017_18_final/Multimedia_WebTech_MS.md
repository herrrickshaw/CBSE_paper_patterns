---
title: "Multimedia WebTech MS"
source_pdf: "Multimedia_WebTech_MS.pdf"
source_url: "https://cbseacademic.nic.in/web_material/SQP/CLASS_XII_2017_18_final/Multimedia_WebTech_MS.pdf"
pages: 13
pdf_bytes: 863947
pdf_sha256: "09994139911b80515a2cb495fe6e0cb834bc3de8348b052dcae9110ad38baa18"
text_chars: 30465
low_text_pages: 0
converter: "pdftotext -layout"
---

# Multimedia WebTech MS


---

## page 1

```
                                          Marking Scheme
                                   Multimedia and Web Technology
                                             Class: XII
                                          Session 2017-18
Q1(a)   Shreya wants to work on a database management software. Suggest her any two                 1
        examples of common database management system.

Ans     MySQL, MS Access, MS-SQL Server, Oracle etc.
        (½ mark each for any two example)
  (b)   What is field in a database? Give an example.                                               1
 Ans.   The column of a table is known as field.
        Example: EmpNo, EmpName etc.
        (½ mark for correct answer)
        (½ mark for any one example)
  (c)   Define and identify the primary key in the following table:                                 2
                                      Table: Stationary
                                  S_No S_Name           S_Qty PurchaseDate
                                  101      Pen          102      2011-12-12
                                  102      Pencil       201      2013-02-21
                                  103      Eraser       90       2011-09-09
                                  109      Sharpener    90       2012-08-31
                                  113      Clips        900      2011-09-09

 Ans.   An attribute or set of attributes which are used to identify a tuple uniquely is known as
        Primary key.
        Primary key: S_No or S_Name
        (1 mark for correct definition)
        (1 mark for identification of primary key)
(d)     Shweta wants to delete the records where the "FirstName" is "Rahul" in the „Emp‟            1
        Table. She has entered the following SQL statement. An error is being displayed.
        Rewrite the correct statement.
         DELETE „Rahul‟ FirstName FROM Emp;
Ans     DELETE FROM Emp WHERE FirstName = 'Rahul';
        OR
        DELETE FROM Emp WHERE FirstName like 'Rahul'
        (1 mark for correct answer)
(e)     Differentiate between JPEG and GIF image.                                                   2
Ans.
            JPEG image                                  GIF Image
         1. JPEG stands for Joint Photographic      1. GIF stands for Graphic Interchange
         Experts Group.                             Format.
         2. JPEG images being static images         2. GIF allows animation.
         does not allow animation.
         3. JPEG images are good for                3 GIF is best for images that have
         displaying real world photographs.         solid colors, text and line art.
         4. JPEG files are more compressed          4. GIF files are less compressed
         than GIF files hence JEPG files are        hence take more storage space.
         more compact than GIF files.
```

---

## page 2

```
        (1 mark each for any two correct difference)
(f)     Explain the term “Publishing a Flash Movie”? Name the extension of the file created      2
        when a Flash movie is published using a Macintosh projector.
Ans.    Publishing is the process of preparing movie files to be uploaded on the website for
        users by converting the Flash .FLA file to another format like .swf, .html etc
        The extension of the file created when a Flash movie is published using a
        Macintosh projector is .hqx.

        (1 mark for correct explanation)
        (1 mark for correct extension)
(g)     Mention any one use of Multimedia in healthcare.                                         1
Ans.         Doctors can be trained by looking at a virtual surgery
             They can simulate how human body is affected by diseases spread by viruses or
                bacteria.
        (1 mark for any one use)
Q2      Answer the following question based on Macromedia Flash:
(a)     What is Frame rate?                                                                      1
Ans.    Frame rate is used to set the speed of animation. If frame rate is low then animation
        will be slow otherwise it is fast. Frame rate is expressed in frames per second (FPS).

        (1 mark for the correct answer)
  (b)   Differentiate between Motion Tweening and Shape Tweening.                                2
Ans.               Motion Tweening                      Shape Tweening
             1. Motion tweening is used to        1. Shape tweening is used to
                change the position of an            change the shape of an object.
                object over time.
             2. Motion tween works only           2. Shape tween works with any
                with symbols.                        object.
             3. Example:-                         3. Example:-




         (1 mark each for any two correct differences)
  (c)   Name any two movie file formats.                                                         1
Ans.    Movie file formats are:- AVI, MPEG, MOV, SWF, DAT
        (½ marks each for any two correct Movie Format)
 (d)    Define layer. Write one advantage of using layers in Flash.                              2
Ans.    A layer is like a transparent sheet stacked on top of each other which may contains
        different scenes of a flash movie.
        Advantage: - It is used to organise the artwork, photographs, text and animation in a
        single file.
        (1 mark for correct definition)
        (1 mark for Advantage)
(e)     Observe the figure given below and do as directed:                                       4
```

---

## page 3

```
              The object on the left hand side shows the position and size of the image for
                frame 1. The colour of the object is blue.
             The object on the right hand side shows the position and size of the image for
               frame 20. The colour of the object is green.
             The circle on frame 1 moves and transforms into an ellipse on frame 20.
         Write the procedure and property settings for animating the above scenario.
Ans.   The following steps have to be followed to animate the given scenario:                   ½x8=4
            Select frame 1 from the timeline.
            Create the blue coloured object given on the left hand side.
            Select frame 20 and insert a Keyframe.
            Reposition the object by dragging from left hand side to right hand side.
            Change the size and shape of the object using Free Transform tool.
            Change the colour of the object by using fill color from the toolbox.
            Click on anywhere between frame 1 and frame 20.
            Select shape tween from properties palette.
        (½ mark for each correct step)
       (full marks for any other correct equivalent way for the same animation)
Q3      Answer the following questions based on HTML

(a)    Write the HTML command to create a button in a form with the caption “Click Me”            1

Ans.                      <INPUT TYPE=”BUTTON” VALUE=“Click Me”>
       (½ mark for naming the <INPUT> tag)
       ( ½ mark for TYPE & VALUE attributes)
(b)    Identify the errors in the following HTML code. Also write the correct code.               1
               <OL TYPE= “a” START= “f”>
Ans    The start attribute should be assigned a numeric value.
       Correct code is:
       <OL TYPE= “a” START=6>
       (½ mark for identification of error)
       (½ mark for correction)
(c)     Write the HTML code to generate a Web Page in the format given below:                         8
       Consider the following while writing the HTML code:
                Title of the page should be “Handmade Cards”.
                Background colour should be “Pink”.
                Text style of the main heading should be “Arial Bold” and color should be
                   red.
                Image used is “cards.jpg”.
                Table in the center of the webpage and should have a 3 pixel thick border of
                   color green and the spacing between cell content and border is 10 pixels.
                Use the concept of nested lists for creating the specified lists.
                The bottom image (link.jpg) and the text “Personalize The Card” are links
                   to another page “person.html”.
```

---

## page 4

```
Ans.   <html>                                                                              ½ mark
       <head>                                                                              for
                                                                                           <HTML>
                                                                                           &<BODY
                                                                                           > tags

       <title> Handmade Cards </title>                                                     ½ mark
       </head>                                                                             for correct
                                                                                           use
                                                                                           of <TITL
                                                                                           E>
                                                                                            tag
       <body bgcolor="pink">
       <center>
                                                                                           ½ mark
                                                                                           for
                                                                                           BGCOLO
                                                                                           R
       <font face="Arial Bold" size="5" color ="Red">                                      attribute of
       <b>HANDMADE CARDS</b>                                                               <BODY>
       </font>                                                                             tag)
       <br>
       <font size=3>Handmade cards offers custom made cards as per your requirements for
       everyone </font><BR>                                                                1 mark for
                                                                                           using
       <img src ="cards.jpg" border ="3" height=175 width=175>                             <FONT>
       </center>                                                                           tag
       <font face = "Arial Bold" size=4 color="Red">                                       with face
       Categories of Cards Offered</font>                                                  &
       <font size=3>                                                                       color
                                                                                           attribute
       <ol type = 1>
```

---

## page 5

```
     <li> General Cards </li>
            <ul type="square">
            <li> Thinking of You </li>
            <li> Missing You </li>                                                 1 mark for
            <li> Friends Forever </li>
                                                                                   correct use
            </ul>
     <li> Specific Cards </li>                                                     of <IMG>
            <ul type ="circle">                                                     tag
            <li> Happy Birthday </li>                                              with heigh
            <li> Happy Diwali </li>
            <li> Happy Anniversary </li>                                           t,
            </ul>                                                                  width,
</ol>                                                                              border
<i><center>You can also order flowers through our site</center></i>
<table width =20% align = center border = 3 bordercolor = green cellpadding = 10
cellspacing = 2>                                                                   (1 mark
                                                                                   for proper
                                                                                   use of list
                                                                                   and TYPE
                                                                                   attributes)

<caption>                                                                          1 mark for
   <b>PRICE LIST</b>                                                               using
</caption>                                                                         <TABLE
                                                                                   > tag with
   <tr>                                                                            ALIGN,
     <th> Bouquet Type </th>                                                       BORDER,
     <th> Price </th>                                                              BORDER
   </tr>                                                                           COLOR,
   <tr>                                                                            CELLPA
      <td> Flower Galore </td>                                                     DDING
      <td> Rs. 200 </td>
   </tr>
   <tr>
       <td> Flower Shower </td>
       <td> Rs. 300 </td>
   </tr>                                                                           ½ mark
   <tr>                                                                            for use
       <td> Flower Power </td>                                                     of <CAPT
       <td> Rs. 400 </td>                                                          ION>tag
   </tr>
   </table>
   <br>                                                                            ½ mark
   <center>                                                                        for proper
   <a href ="person.html">
   <img src = "link.jpg" border = 2 height=50 width=50>                            use
                                                                                   of <TR>,
                                                                                   <TH> &
   <br>
                                                                                   <TD> tag
   Personalize The Card
   </a>
   </center>
   </font>
   </body>
```

---

## page 6

```
          </html>

           (½ mark for correct use of <HTML> and <BODY> tags)
           (½ mark for correct use of <TITLE> tag)
           (½ mark for BGCOLOR attribute of <BODY> tag)
           (1 mark for correct use of <FONT> tag with face & color attribute)
           (1 mark for correct use of <IMG> tag with height, width, border)                      ½ mark
           (1 mark for correct use of list and TYPE attributes)                                  for use
          (1 mark for using <TABLE> tag with ALIGN,BORDER,                                       of <CEN
           BORDERCOLOR,CELLPADDING)                                                              ER>
         ( ½ mark for correct use of <CAPTION>tag)                                                tag
         ( ½ mark for proper use of <TR>, <TH> & <TD> tag)                                       ½ mark
         (½ mark for use of <CENER> tag)                                                         for proper
          (1 mark for proper use of <A> tag with HREF attribute )
                                                                                                 use
                                                                                                 of <A> tag
                                                                                                 with HRE
                                                                                                 F attribute


Q4.    Answer the following questions based on PHP:

(a)    Write any two features of PHP.                                                                1
Ans.   Two features of PHP are:-
          1. PHP is platform independent i.e PHP code runs on various platforms like
              Linux, Unix, Windows etc.
          2. PHP is server-side script and executes on web server.
              (½ marks each for any two correct PHP features)

(b)    Write the output of the given code:                                                           2
                    <?php
                     $sum=0;
                     for($a=1; $a<=8; $a +=2)
                          $sum = $sum + $a;
                     echo($sum);
                     echo("<BR>");
                     echo($a);
                    ?>

Ans.   16
       9
       (1 mark for each line of output)
       (Deduct ½ mark if line break is not considered)
(c)    What is a constant? Declare a constant MAX and assign the value 10.                           2
Ans.   A constant is a name or an identifier whose value is fixed and cannot change during the
       execution of the program.
       define('MAX',10);
       (1 mark for correct definition of constant)
       (1 mark for declare a constant MAX with value 10 )
(d)        Give output of the following statements:                                                  3
               (i) echo 10/5+2*4%8;
               (ii) echo strtolower("PRODUCT ACTIVATED");
               (iii) echo date("M-d-Y", mktime(0,0,0,8,42,2017));
```

---

## page 7

```
Ans.   (i) 2
       (ii) product activated
       (iii) Sep-11-2017
       (1 mark for each correct output)
(e)    Rewrite the following code using switch case                                              2
                if($Type=='T')
                   echo "DISCOUNT ON TV";
                else if($Type=='M')
                   echo "DISCOUNT ON MOBILE PHONE";
                else if($Type=='C')
                   echo "DISCOUNT ON CAMERAS";
                else
                   echo "NO DISCOUNT";
Ans.   switch($Type)
       {
              case 'T': echo "DISCOUNT ON TV";
                          break;
             case 'M' : echo "DISCOUNT ON MOBILE PHONE";
                          break;
             case 'C' : echo "DISCOUNT ON CAMERAS";
                         break;
             default : echo "NO DISCOUNT";
       }
       (½ mark for each correct case)
       (Deduct ½ mark if break is not considered)
Q5.    Answer the following questions based on PHP:

(a)    What is PHP global variable $_REQUEST?                                                    1
Ans.   $_REQUEST is a super global variable which is used to collect data after submitting
       an HTML form.
       (1 mark for correct answer)
(b)    Following is the code to count total number of characters from a text file. Fill in the   2
       blanks so that this code can work:
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
Ans.   <? Php
         $file = fopen(“data.txt”, “r”);
         $ch = 0;
       while(!feof($file))
       {
                       $letter=fgetc($file);
                       $ch=$ch+1;
       }
       echo “Number of characters:”, $ch;
       fclose($file);
       ?>
```

---

## page 8

```
       (1/2 mark each for the correct answer)
(c)    Rewrite the following code after removing errors with each correction underlined.          2
       <?
       value=5;
       while($value!= =0)
       {
          $r_digit=$value%10;
       $value/=10;
       }
       ECHO $r_digit;
       ?>

Ans.   <?php
            $value=0;
            while($value!=0)
            {
                  $r_digit=$value%10;
                  $value/=10;
            }
            echo $r_digit;
       ?>
       (½ mark for correcting each error)
(d)    Name the built-in functions to be used in the following situations:                        2
               (i) To remove backslash from a string.
               (ii) To return number of days in a month for specified year.
Ans.   (i) stripslashes()
       (ii) cal_days_in_month()
       (1 mark for each correct function name)
(e)    What is a cookie? Write the PHP code to set a cookie named “car” and value “BMW”.          3
       The cookie should expire after two days. Also Display the value stored in $_COOKIE

Ans.   A cookie is a small piece of data that the web server sends to a web browser so that the
       web server can keep track of user‟s activity on a particular website.
       When a user uses a computer to visit a website, the website stores some basic
       information about the visit on the hard disk of the computer. It records the user‟s
       preferences while using the site. This stored information is called a „cookie‟.

       <?php
       $cookie_name = "car";
       $cookie_value = "BMW";
       setcookie($cookie_name, $cookie_value, time() + (86400 * 2), "/"); // 86400 = 1 day
       ?>
       <html>
       <body>

       <?php
       if(!isset($_COOKIE[$cookie_name])) {
          echo "Cookie named '" . $cookie_name . "' is not set!";
       } else {
          echo "Cookie '" . $cookie_name . "' is set!<br>";
          echo "Value is: " . $_COOKIE[$cookie_name];
       }
```

---

## page 9

```
       ?>

       </body>
       </html>
       (1 mark for correct definition of cookie)
       (1 mark for correct use of setcookie() function )
       (1 mark for displaying the value stored in $_COOKIE )

Q6     Answer the following questions based on JavaScript:
(a)    Write the code using do while loop without effecting the output:                            2
                 <script language="javascript">
                 var prod,b;
                 prod=1;
                 for(b=1;b<=10;b+=3)
                 {
                       document.write(b);
                       prod=prod+b*b;
                 }
                       document.write("the final product is" & prod);
               </script>
Ans.   <script language="javascript">
       var prod,b;
       prod=1;
       b=1;
       do
       {
            document.write(b);
            prod=prod+b*b;
            b+=3;
       }while(b<=10);
       document.write("the final prod is" & prod);
       </script>
       (½ mark each for block { } statements )
       (½ mark for correct do…while )
(b)    Explain Conditional operator with the help of an example.                                   2
Ans.   It is also known as Ternary operator as it requires 3 operands. It checks the condition,
       if it is evaluated as true it goes to True part else the False part. Syntax:
       Condition?True:False
       Example:- Ans=(x>y?x:y);
       If x=5 and y=3
       As x>y i.e. 5>3 condition is true, Ans. is assigned the value of x, else Ans will get the
       value of y.
       1mark for explanation
       1 mark for correct example
       OR
       Full 2 marks if the difference is explained only with the help of an example)
(c)     Analyse the given program segment and determine how many times the loop will be            2
        executed. What will be the value of A after loop is terminated.
               var A , B;
               A = 5;
               B = 10;
               while(A>=1)
               {
                         document.Write(A+B);
                         A = A - 1;
```

---

## page 10

```
                        B = B – 2;
              }
Ans.     Loop will execute 5 times.
         Value of A after the loop terminates is 0.
         (1 mark each for correct answer)
(d)      Write the code to display a form as shown below along with the javascript code to            4
         achieve the specified task. User should be able to enter the number of calls and the total
         amount payable gets displayed when he presses “calculate” button.




       The total amount payable will be calculated based on the following rate list:

                Rs. 1.00 per call for the 1st 100 calls
                Rs. 1.20 per call for the next 100 calls
                Rs. 1.50 per call for the next 50 calls
                Rs. 2.00 per call for more than 250 calls


Ans.     <html>
         <head>
         <SCRIPT language="javascript">
         function calc()
         {
         var consm, amount=0;
         consm=document.form1.f1.value;
         if(consm<=100)
             amount=consm*1.0
         else if(consm<=200)
             amount=100+1.2*(consm-100)
         else if(consm<=250)
             amount=100+1.2*100+1.5*(consm-200)
         else
             amount=100+ 1.2*100 + 1.5*50 +2.0 *(consm-250)
         document.write("amount payable is " + amount);
         }
         </SCRIPT>
         </head>
         <body>
         <form name="form1">
         NUMBER OF CALLS
         <input name=f1 type=text>
         <br>
         <input type=button name=b1 onclick=calc() value=CALCULATE BILL>
         </form>
         </body>
         </html>

          (1 mark for form )
         (2 marks for function)
         (½ mark for handling ONCLICK( ) event)
          (½ mark for displaying output )
Q7       Answer the following questions based on Communication and network concepts:
(a)      How firewall protect our network?                                                            1
Ans.     A firewall is a part of computer system or network that is designed to block
```

---

## page 11

```
       unauthorized access while permitting authorized communications. It is a device or set
       of devices configured to permit, deny, encrypt, or proxy all(in and out) computer traffic
       between different security domains based upon a set of rules and other criteria.
       (1 mark for appropriate explanation)
(b)    Write one advantage of Bus Topology of network. Also, illustrate how 4 computers can        1
       be connected with each other using bus topology of network.
Ans.   Cable length required for this topology is the least compared to other networks.
       Illustration of 4 computers connected with each other using bus topology of network.




       (½ Mark for writing one correct advantage)
       (½ Mark for drawing / writing correct illustration OR any other diagrammatic
       representation for star topology)
(c)        Explain the following terms:                                                            2
              i. GSM
              ii. CDMA
Ans.   GSM: Global System for Mobiles, it is the international standard for wireless
       technology. GSM allows users to utilize one phone and one number in many countries
       throughout the world.
       CDMA: Code Division Multiple Access: a digital wireless telephony transmission
       technique. CDMA is an example of multiple access, where several transmitters can
       send information simultaneously over a single communication channel.
       (1 mark for each correct definition)
(d)    Write two advantages of using open source software over proprietary software.               1

Ans.   (i) Source Code available for modification and redistribution
       (ii) Freely available for usage
       (½ mark for each correct advantage)
(e)    What is the significance of UNICODE?                                                        1
Ans.    UNICODE is a universal coding standard whose main objective is to enable a single,
        unique character set capable of supporting all characters from all scripts, as well as
        symbols, that are commonly utilized for computer processing throughout the globe.
       (1 mark for correct explanation)

(f)    The Cyber Skill Development Organisation has set up its new Branch at Nagaland for
       its offices and web based activities. It has 4 Wings of buildings as shown in the
       diagram




                              Z                               Y




                             X                                 U
```

---

## page 12

```
                  Center to center distance between various blocks
         Wing X to Wing Z                                      30m
         Wing Z to Wing Y                                      50m
         Wing Y to Wing X                                      125m
         Wing Y to Wing U                                      60m
         Wing X to Wing U                                      155m
         Wing Z to Wing U                                      110m


         Number of computers
         Wing X                                             40
         Wing Z                                             120
         Wing Y                                             30
         Wing U                                             10


(i)     Suggest a most suitable cable layout of connections between the Wings and topology.         1

Ans.       (i) Most suitable layout




                          Z                                Y


                                            50m

                               30m         110 m

                          X                                 U




                    (1 mark for correct layout)
(ii)    Suggest the most suitable place (i.e, Wing) to house the server of this organization with   1
        a suitable reason with justification.
Ans.    Wing Z as it has largest number of computers.
        (½ mark for naming the correct block)
        (½ mark for correct justification)
(iii)   Suggest the placement of the following devices with justification:                          1
                    o Repeater
                    o Hub/Switch

Ans.    A repeater needs to be placed along the wire between wings Z to U as the distance
        between them is more than 70 m.
        A hub/switch each would be needed in all the wings, to interconnect the group of
        cables from the different computers in each wing.
```

---

## page 13

```
        (½ mark for correct placement)
       (½ mark for correct justification)


(iv)   The organization is planning to link its head office situated in Delhi with offices at   1
       Nagaland. Suggest an economic way to connect it; company is ready to compromise on
       the speed of connectivity. Justify your answer.
Ans.   TCP/IP Dial Up as it is an economic option with a reasonable speed.
       (½ mark for correct technology)
       (½ mark for correct justification)
```