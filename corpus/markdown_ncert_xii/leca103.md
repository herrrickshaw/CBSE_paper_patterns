---
title: "leca103"
source_pdf: "leca103.pdf"
source_url: "https://ncert.nic.in/textbook/pdf/leca103.pdf"
pages: 18
pdf_bytes: 2826450
pdf_sha256: "c2eed18213560c801f661501e68b8cb82d1a39b393d374e40e20d38a3c1d453c"
text_chars: 39814
low_text_pages: 0
converter: "pdftotext -layout"
---

# leca103


---

## page 1

```
USE OF SPREADSHEET
IN BUSINESS
                                                                                 3
APPLICATIONS
Learning Objectives                           Introduction
After studying this chapter you will be
able to use spreadsheet for:              In the previous chapter, we have learned about
   •   Computing employee’s gross
                                          the spreadsheet and its several features that can
       salary. Making necessary           be used in business applications. In this chapter,
       deductions to calculate net        we shall discuss the applications of spreadsheet
       salary, payroll accounting.        (using Excel) to Payroll Accounting and some other
   •   Calculation of deprecation by      select applications (Asset Management, and Loan
       various methods.                   Repayment).
   •   Loan repayment, interest
       calculation.                       3.1 PAYROLL ACCOUNTING
                                          Every employee is paid salary on a pre-determined
                                          date within the framework of employee contract
                                          and related personnel policy in force from time to
                                          time in an organisation.
                                             The computation of salary payment is based
                                          on the number of days an employee has worked,
                                          rate per grade of pay, rate of applied allowances
                                          and deductions to be made therefrom.
                                              The preparation of salary bill should provide
                                          for the following :
                                          •   Maintaining payroll related data such as
                                              Employee No., Name, Attendance, Basic Pay,
                                              applicable Dearness and other Allowances,
                                              deductions to be made.
                                          •   Periodic payroll computations: the payroll
                                              computation includes the calculation of various
                                              earning and deduction heads, which are to be
                                              derived from basic values (such as basic salary,
                                              number of days under leave without pay (LWP)
                                              and unauthorised absence, etc) as per the
                                              formulae.



                                              Reprint 2026-27
```

---

## page 2

```
                                                     Computerised Accounting System

     •   Preparation of salary statement and employees salary slips
     •   Generation of advice to bank: It contains the net salary to be
         transferred to individual bank account of employees and other salary
         related statutory payments such as provident fund, tax, etc.

     3.1.1 PAYROLL COMPONENTS
     Every employee is under contractual relationship of service with an
     organisation, and is paid salary accordingly. The following elements
     are important for salary computation and its payment:
     •   CURRENT PAYROLL PERIOD (MONTH AND YEAR)
     •   EARNINGS
         §   Basic Pay (BP) : It is the pay in the pay scale plus Grade Pay,
             but does not include Special Pay.
         §   Grade Pay (GP) : It is the pay to be added to the Basic Pay
             according to the Designation of the employee and applicable pay
             band or scale of pay.
         §   Dearness Pay (DP) : It is that portion of Dearness Allowance,
             which has been declared and deemed to have been merged with
             the Basic Pay.
         §   Dearness Allowance (DA) : It is a compensation for erosion in
             the purchasing power of wage earner due to price rise. It is granted
             by the Government periodically as a percentage of (Basic Pay +
             Dearness Pay, if applicable).
         §   House Rent Allowance (HRA) : It is an amount paid to facilitate
             employee in acquiring on lease of residential accommodation.
         §   Transport Allowance (TRA) : It is an amount to facilitate commuting
             to the the place of work, i.e. Delhi, Bhopal, Haridwar, etc.
         §   Any Other Earning : It may include any other allowance not
             included above but declared from time to time, such as Education
             Allowance, Medical Allowance, Washing Allowance, etc.
     •   DEDUCTIONS
         §   Professional Tax (Applicable in some states) (PT) : It is a
             statutory deduction according to the legislature of the State
             Government.
         §   Provident Fund (PF) : It is a statutory deduction, as part of
             social security. It is decided by the Government under the
             Provident Fund Act and is computed as a percentage of (Basic
             Pay + Dearness Pay, if applicable).
         §   Tax Deduction at Source (TDS) : It is a statutory deduction,
             which is deducted monthly towards Income Tax liability of an
88           employee. It is essentially an apportionment of yearly Income
             Tax liability over 12 months.



                            Reprint 2026-27
```

---

## page 3

```
Use of Spreadsheet in Business Application

    §   Recovery of Loan Instalment (LOAN) : Any amount signified by
        the employee for deduction on account of any loan taken up by
        him/her.
    §   Any Other Deduction : It may include any other deduction not
        included above such as Recovery of “Advance against Salary”,
        deductions on account of “Food Grain Advance”, “Festival
        Advance”, etc.

3.1.2 ELEMENTS USED IN PAYROLL CALCULATION
Basic Pay Earned (BPE) – Basic Pay Earned of an employee is the
Basic Pay calculated with reference to Number of Effective Days present
(NOEDP) during the month.
        BPE     =   BP * NOEDP/NODM

  Number of Effective Days Present (NOEDP) – is the Number of Days
  in a Month Minus Leave without Pay minus Unauthorised Absence, i.e.
  NOEDP = (Number of Days in a Month) – (Leave without Pay) –
  (Unauthorised Absence) ; where (Number of Days in a Month) may be
  denoted by NODM.

Dearness Allowance (DA) –
    DA = BPE * (Applicable Rate of DA for the Month)
House Rent Allowance (HRA) –
    HRA = BPE * (Applicable Rate of HRA for the Month)
Transport Allowance (TRA) –
    TRA = (Fixed Amount) or (On Percentage Basis)
Total Earnings (TE) – It is the aggregate of all the above earning
elements. Thus,
    TE = BPE + DA + HRA + TRA
Provident Fund (PF) : This can be calculated as PF = BPE * PF Rate
Tax Deduction at Source (TDS) : It is usually a fixed amount deducted
every month on account of TDS. In the last quarter of a year, the
investment details, which are permissible for tax deduction, are
received from employees to compute the quarterly and yearly income
tax liability more accurately.
Recovery of Loan Instalments (LOAN) : It is a fixed amount to be
deducted on account of Loan Installment as part of loan recovery.
Total Deductions (TD) : It is the total of all the above deductions.
Thus,
                                                                          89
    TD = PF + TDS + LOAN




                                             Reprint 2026-27
```

---

## page 4

```
                                                   Computerised Accounting System

     The Net Salary (NS) is the amount payable to an employee. It is obtained
     by deducting Total Deductions (TD) from Total Earnings (TE) as given
     below :
       Net Salary (NS) = Total Earnings (TE) – Total Deductions (TD)
     3.1.2.1 Template Design
     Whenever we have to use a spreadsheet for any computations, the first
     step is to plan its layout and the template specifying the sequence of
     various columns, etc. The template also includes identification of cells,
     which will contain formulae. The advantage of preparing the template
     is that as a user puts in the values in the spreadsheet, the calculated
     results are shown correspondingly. A table giving the contents of various
     columns is a helpful tool to represent the template of a spreadsheet.
     The following example will explain this process.
     Example
     There are 14 employees in M/s XYZ Enterprise. The payroll calculations
     of these employees are given in the spreadsheet shown in Figure 3.3 (a)
     and Figure 3.3 (b). These figures show the layout of the spreadsheet. In
     a column, either a value is entered directly or else it is computed using
     a formula. Such data are given in Figure 3.1. The rules for computing
     some of the payroll elements used above are given in Figure 3.2.
     Different data elements are arranged in the spreadsheet as follows:
     • No. of Days in a Month (NODM) is entered in the cell G3
     • DA Rate (in %) is entered in the cell G4
     • HRA Rates (in %) for Supervisory (Emp Type = “Sup”) and Non-
         supervisory (Emp Type = “Nsup”) are entered in the cells G5 and
         G6, respectively.
     • Transport Allowance for Supervisory (Emp Type = “Sup”) and Non-
         supervisory (Emp Type = “Nsup”) are entered in the cells G7 and
         G8, respectively.
     • PF Rate (in %) is entered in the cell G9.

      Notes
      • In columns I and J, nested-if function (i.e. an “IF” function within
        another “IF” function) has been used. If function has been introduced
        in Chapter 2.
      • The formulae in column-F and column-G use absolute address ($G$3)
        for cell G3 rather than using the relative address (G3). The absolute
        address is used for those cells whose reference should not change
        while the formula is to be copied into other cells. The concept of
        relative and absolute addressing of cells has been explained in
        Chapter 2 earlier. Absolute addresses are also used in the formulae
90      used in columns H, I, and J.




                          Reprint 2026-27
```

---

## page 5

```
Use of Spreadsheet in Business Application

 Column           Column Heading              Abbrev Ref              First line shows Required Formula
                                                                      Second line refers the cell content

     A         Employee No                    Emp No            Value entered directly
     B         Employee Name                  Emp Name          Value entered directly
     C         Employee Type                  Emp Type          Value entered directly
     D         Deduction Days                 Ded Days          Value entered directly
     E         Basic Pay                      BP                Value entered directly
     F         No. of Effective Days          NOEP              = NODM – (Ded Days)
               Present                                          = $I$3-D12
     G         Basic Pay Earned               BPE               = BP * NOEP/NODM = E12*F12/$I$3
     H         Dearness Allowance             DA                = BPE * DA Rate (in %) = G12*$I$4
     I         House Rent Allowance           HRA               = If (Emp Typ = “Sup” then 40% of BPE
                                                                else if (Emp Typ = “Nsup” then 30% of
                                                                BPE else 0))
                                                                = IF(C12=”Sup”, G12*$I$5,
                                                                IF(C12 =”Nsup”, G12*$I$6,0))
     J         Transport Allowance            TRA               = If (Emp Typ = “Sup” then 1000 else if
                                                                (Emp Typ = “Nsup” then 500 else 0))
                                                                = IF(C12=”Sup”,$I$7,IF(C12
                                                                =”Nsup”,$I$8,0))
     K         Gross Salary                   TE                = BPE + DA + HRA + TRA
                                                                = G12+H12+I12+J12
     N         Provident Fund                 PF                = BPE * PF Rate (in %)
                                                                = G12*$I$9
     O         Tax Deduction at Source        TDS               Value entered directly
     P         Loan Repayment Inst.           LOAN              Value entered directly
     Q         Total Deductions               TD                = PF + TDS + LOAN= N12+O12+P12
     R         Net Salary                     NS                = TE – TD= K12-Q12
          Figure 3.1: Spreadsheet Columns and the Cells Content in Spreadsheet shown in Figure 3.3 A


         Variable/Type of Employee                 Value in % or Fix Value                 Remark
 Dearness Allowance (DA)                              35% of Basic Pay                       I4
 House Rent Allowance (HRA) –:
 Supervisory Employee (Sup)                           40% of Basic Pay                       I5
 Non-supervisory Employee (Nsup)                      30% of Basic Pay                       I6
 Consultant or Contract Employee                      Nil
 Provident Fund (PF)                                  12% of BP +DA                          I9
                                                                                                            91
                            Figure 3.2: Rules for Computing Some of Payroll Elements




                                                    Reprint 2026-27
```

---

## page 6

```
                                                                   Computerised Accounting System

       The following spreadsheet shows columns A to K in Figure 3.3 a; while
       columns L to P are shown in Figure 3.3 b. For reference, columns A
       and B are repeated in columns L and M in Figure 3.3 b for reference
       only.




           Figure 3.3 a : Partial Spreadsheet Showing Payroll List upto Gross Salary




92
     Figure 3.3 (b) : Partial Spreadsheet for calculation of Deductions & Net Salary




                                   Reprint 2026-27
```

---

## page 7

```
Use of Spreadsheet in Business Application

3.2 ASSET ACCOUNTING
In this section, we shall be discussing the computation of amount of
depreciation to be charged on assets.

3.2.1 INTRODUCTION
Assets are resources of the organisation, which can be classified into
fixed and current assets. Fixed assets are long-term assets and provide
productive capability to the firm. The examples of fixed assets are
land, building, plant & machinery, etc. It includes both tangible and
intangible assets. Tangible assets are physical in nature, which have
form, shape and size. Intangible assets are resources capable of adding
value but do not have a physical dimension such as patents, copyrights,
trade mark, etc.
   The depreciation on fixed assets is provided to recognise the cost of
the asset consumed during an accounting period since the life of such
assets extends beyond single accounting year. Usually, depreciation is
not provided on free hold land.
Total Amount of Depreciation                 = Acquisition Cost – Salvage Value
(Over Life of the Asset)

    Year-to-date depreciation is the accumulated depreciation from the
    date to which the asset is put to use till the current accounting year.

   Year-to-date depreciation is the accumulated depreciation from the
date to which the asset is put to use till the current accounting year.
   Depreciation is calculated according to the policy of the organisation.
There are basically two methods, namely the Straight Line Method
(SLM) and the Written Down Value Method (WDV). We had studied
depreciation in our previous standard (XIth Standard) in Accountancy
Book Part I.
    We will recall that asset accounting requires maintenance of asset
register, computation of depreciation and preparation of schedule of
fixed assets for reporting in the balance sheet as part of the annual
accounts. In order to prepare this report the depreciation calculation
sheet is also to be prepared.

3.2.2 COMPUTERISED ASSET ACCOUNTING
Assets are classified into the following categories:
•    Goodwill
•    Land: Free-hold land and Lease-hold land
                                                                                  93
•    Building: Factory building, Office building, and Residential building




                                                  Reprint 2026-27
```

---

## page 8

```
                                                          Computerised Accounting System

     •    Plant and Machinery
     •    Furniture and Fixtures
     •    Vehicles
     •    Capital work in progress
     •    Others

     The Companies Act, 1956 in Schedule-14 lists the rate of depreciation
     to be used for different class of assets under Straight Line Method
     (SLM) and Written Down Value Method (WDV). The prescribed rates
     are different under two methods. For reporting purposes, corporate
     enterprises may use either of the method and applicable rates. Let us
     now understand the computation of depreciation using the two methods.
     3.2.2.1 Straight Line Method (SLM)
     The following is the formula for computation of depreciation:
     •    Acquisition Cost = Purchase Value + Other expenses, such as
          Transportation Expenses, Installation Expenses and Pre-operating
          Expenses
     •    Total Depreciable Amount = Acquisition Cost - Salvage Value

         The salvage value of an asset is the value, which is realisable at the
         end of its useful life.

                                              Total Depreciable Amount
     •    Straight Line Depreciaion =
                                                Expected Useful Life

                                   Straight Line Depreciation
     •    Rate of Depreciaion =                                   × 100
                                    Total Depreciable Amount

     Example
     The depreciation calculation (using SLM) is done using the Excel
     spreadsheet, which is shown in Fig. 3.5 a and Fig. 3.5 b in two parts
     due to the limitation of the page width. In each of the spreadsheet
     column, either a value is entered directly or else it is computed using
     a formula. Such data are given in Figure 3.4.
     Different data elements are arranged in the spreadsheet as follows:
     •    Year Beginning Date is entered in cell-C3
     •    Year End Date is entered in cell-F3
     •    First-Half Year End Date is entered in cell-E3
94




                            Reprint 2026-27
```

---

## page 9

```
Use of Spreadsheet in Business Application

 Column      Column Heading              Abbrev Ref       First line shows Required Formula
                                                          Second line refers the cell content

    A        Asset Name                  Asset Name       Value entered directly
    B        Date of Purchase            Pur. Date        Value entered directly
    C        Date of Installation        Inst. Date       Value entered directly
    D        Cost of Purchase            Pur. Cost        Value entered directly
    E        Installation Expenses       Inst. Exp.       Value entered directly
    F        Pre-operating               Pre-op Exp       Value entered directly
             Expenses
    G        Cost to Use                 Cost to Use      = (Cost of Purchase) + (Installation Expenses)
                                                          + (Pre-operating Expenses) = D5+E5+F5
    H        Salvage Value               Salvage Val      Value entered directly
     I       Life of Asset in Years      Life in Yrs      Value entered directly
    K        Depreciation Amount         Depr.            =SLN(G5,H11,I11)
                  Figure 3.4: Column Items and their contents referred to in the Spreadsheet


The depreciation is computed by straightline method using the built-
in spreadsheet function SLN in column-K. The spreadsheets are shown
in Figure 3.5(a) and Figure 3.5(b).




            Figure 3.5(a) : Partial Spreadsheet Columns for Calculation of Depreiation by SL Method

                                  H                  I               J             K




  Figure 3.5(b) : Partial Spreadsheet Columns for Calculation of Depreciation by SL Method

The above-mentioned computations and spreadsheets (shown in two
parts due to the constraint in the page width) give an idea of the                                         95
process of depreciation calculation using SLM function. The spreadsheet




                                                   Reprint 2026-27
```

---

## page 10

```
                                                                                  Computerised Accounting System

                    calculation includes “Salvage Value”, “Life in Years”, “Allowed
                    Depreciation”, and “Depreciation” Columns with previous spreadsheet
                    “Asset Name” Column for Reference.
                    3.2.2.2 Written Down Value (WDV) Method
                    Written Down Value (WDV) method uses the current book value as the
                    base for computing the depreciation for the next period. It is also called
                    Declining Balance (DB) method and uses the Excel function DB to
                    compute the depreciation. The parameters of the function DB are as
                    follows (Figure 3.6):

                        Column      Parameter                             Explanation

                          G             Cost          Initial cost of the asset
                          H           Salvage         Salvage value
                            I            Life         Life (in years) of the asset
                          J            Period         Period (in years) for which the depreciation
                                                      is calculated
                          K            Month          No. of months in the 1st year
                                Figure 3.6: Column Items and their contents referred in the Spreadsheet

                    In a column, either a value is entered directly or else it is computed
                    using a formula. Such data are given in Figure 3.7.
                    Different data elements are arranged in the spreadsheet as follows:
                    •    Year Beginning Date is entered in cell-C3
                    •    Year End Date is entered in cell-F3
                    •    First-Half Year End Date is entered in cell-I3

     Column       Column                 Abbre. Ref               First line shows Required Formula
                  Heading                                         Second line refers the cell content

       A      Asset Name                Asset Name        Value entered directly
       B      Date of Purchase          Pur. Date         Value entered directly
       C      Date of Instalation       Inst. Date        Value entered directly
       D      Cost of Purchase          Pur. Cost         Value entered directly
       E      Instalation               Inst. Exp.        Value entered directly
              Expenses
       F      Pre-operating             Pre-op Exp        Value entered directly
              Expenses
       G      Cost to Use               Cost to Use       = (Cost of Purchase) + (Instalation
                                                            Expenses) + (Pre-operating Expenses)
                                                          = D5+E5+F5
96     H      Salvage Value             Salvage Val       Value entered directly




                                                Reprint 2026-27
```

---

## page 11

```
Use of Spreadsheet in Business Application


 Column          Column               Abbre. Ref              First line shows Required Formula
                 Heading                                      Second line refers the cell content

     I      Life of Asset in         Life in Yrs        Value entered directly
            Years
    J       Period (in Years)        Period             If (Instalation of asset was done after
            for which Depr.                             March) then take (Current Year) – (Year of
            is to be computed                           Instalation) else take one addl. Year.
                                                        = IF (MONTH(C5) > 3,(YEAR($F$3)-
                                                        YEAR(C5)),(YEAR($F$3)-YEAR(C5))+1)
    K       Months in 1st Year       Months in          No. of months between (Yr-End-Dt in 1st Yr)
            (i.e. the year of        1st Yr             & (Inst.Date)
            installation)                               = ROUND((L5-C5)/30,0)
    L       Year-end Date in         Yr-End-Dt          If (Inst. Date) was Between Jan and Mar,
            1st Year (Reqd.          in 1st Yr          Take it as 31st Mar of (Year of Inst. Date)
            to compute                                  Else Take it as Next Year.
            column-K)                                   = IF(AND(MONTH(C5)>0,MONTH(C5) <4),
                                                        DATE(YEAR(C5),3,31),
                                                        DATE(YEAR(C5)+1,3,31))
    M       Depreciation             Depr.              Parameters of DB function as explained
                                                        above
                                                        = DB(G5,H5,I5,J5,K5)
           Figure 3.7: Column Items and their Contents used in Spreadsheet (in Figure 3.8 a and b)


The spreadsheet is divided in two parts; first part shows columns A to
G in Figure 3.8 a; while second part shows columns H to M are shown
in Figure 3.8 b. The “Asset Name” is repeated in both the figures:




Figure 3.8 a : Partial Spreadsheet Columns for Calculation of Depreciation by WDV Method




                                                                                                      97
Figure 3.8 b : Partial Spreadsheet Columns for Calculation of Depreciation by WDV Method




                                                   Reprint 2026-27
```

---

## page 12

```
                                                                                Computerised Accounting System

                      The above-mentioned computations and spreadsheets (shown in two
                      parts due to the constraint in the page width) give an idea of the
                      process of depreciation calculation using WDV function. The
                      spreadsheet calculation includes “Salvage Value”, “Life in Years”,
                      “Allowed Depreciation”, and “Depreciation” Columns with previous
                      spreadsheet “Asset Name” Column for Reference.
                      3.2.2.3 Schedule Forming Part of the Balance Sheet
                      The details of various columns are given in the following table:

     Column              Column                     Under           First line shows Required Formula
                         Heading                                    Second line refers the cell content

       A       Description                                         Value entered directly
       B       As at Apr 1, 2008                Gross Block        Value entered directly
       C       Additions/Adjustments            Gross Block        Value entered directly
       D       Deductions/Adjustments           Gross Block        Value entered directly
       E       As at Mar 31, 2009               Gross Block        = Op. Bal + Additions/Adjustments
                                                                   = B8+C8-D8
       F       As at Apr 1, 2008                Depreciation       Value entered directly
       G       Additions                        Depreciation       Value Transferred from Depreciation
                                                                   Computation Spreadsheet
       H       Deductions                       Depreciation       Value entered directly
       I       As at Mar 31, 2009               Depreciation       = Op. Bal + Additions – Deductions
                                                                   = F8+G8-H8
       J       As at Apr 1, 2008                Net Block          = Gross Block – Depreciation as on
                                                                     Apr 1, 2008
                                                                   = B7–F7
       K       As at Mar 31, 2009               Net Block          = Gross Block – Depreciation as on
                                                                     Mar 31, 2009
                                                                   = E7-I7
              Figure 3.9: Column Items and their Contents used in Spreadsheet (in Figure 3.10 a and b)

                      The spreadsheet is divided in two parts; first part shows columns A to
                      E in Figure 3.10 a; while second part shows columns F to K are shown
                      in Figure 3.10 b. The “Asset Name” is repeated in both the figures:




98
                           Figure 3.10 a: Spreadsheet Containing Fixed Asset Schedule Showing Gross Block




                                                 Reprint 2026-27
```

---

## page 13

```
Use of Spreadsheet in Business Application




               Figure 3.10 b: Spreadsheet Containing Fixed Asset Schedule
                             Showing Depreciation and Net Block

The above-mentioned computations and spreadsheets (shown in two
parts due to the constraint in the page width) give an idea of the
process of Schedule Forming Part of the balance sheet.

3.3 LOAN REPAYMENT SCHEDULE
3.3.1 LOAN
Loan is a sum of borrowed money (termed as principal amount) for a
specified period at a pre-specified rate of interest. The loan is repaid
through a number of periodic (usually monthly) repayment instalments
over the loan repayment period.
3.3.1.1 Calculating Interest and Repayments of Loan
Computation of repayment installments is an iterative process. The
Excel’s built-in function, PMT can be used to compute monthly
instalments of repayment of loan. The parameters of the function PMT
are as follows:

 Parameter      Explanation

 Rate           Interest rate per period for the loan
 Nper           Total number of payments for the loan. Its unit (e.g. year)
                should match with the unit of the interest rate.
 Pv             Present value, i.e. the loan amount
 Fv             Future value, which is taken as 0, is the balance at the
                end of the loan period
 Type           Whether payment is made at the beginning (value=1) or
                at the end (value=0) of the period
              Figure 3.11 Explanation of Parameters of Excel’s PMT Function

The layout of the spreadsheet for loan repayment calculation is given
in Figure 3.13. In each column of the spreadsheet, either a value is
entered directly or else it is computed using a formula. Such data are        99
given in Figure 3.12.




                                                 Reprint 2026-27
```

---

## page 14

```
                                                           Computerised Accounting System

       Column      Column Heading               First line shows Required Formula
                                                Second line refers the cell content

          A     Loan Amt.                      Value entered directly
         B      Loan Disbursement Date.        Value entered directly
         C      Period of Loan (in Yrs).       Value entered directly
         D      Rate of Interest.              Value entered directly
          E     Future Value.                  Value entered directly
          F     Yearly Installment Amt.        = PMT(D6,C6,-A6,0,1)
         G      Monthly Installment Amt.       =F6/12
                  Figure 3.12: Column Items and their Contents in Spreadsheet



       Why is FV taken as zero (0) in the above calculations?
       At the end of the loan period, the (balance) amount payable will be
       zero assuming that the repayments are made on regular basis.
       Therefore, the future value (FV) is taken as zero.

      The following two examples are considered for computation of repayment
      schedule in the spreadsheet shown in Figure 3.13.
      Example 1
      A bank has given loan of Rs. 1, 00,000 to a customer for the purchase
      of a Plasma TV on April 1, 2007 @ 10% interest rate for a period of two
      years. The loan is to be repaid in 24 monthly instalments.
      Example 2
      Ajay has been sanctioned the bank loan of Rs. 2, 50,000 for the purchase
      of a car on May 15, 2008. The loan carries the rate of interest @ 11%
      and it is to be repaid in 36 monthly instalments.




                 Figure 3.13: Spreadsheet Containing Loan Repayment Schedule




100




                             Reprint 2026-27
```

---

## page 15

```
Use of Spreadsheet in Business Application


                                             Summary
 • MS-Excel is an easy and useful tool for various calculations carried out on spreadsheets.
   In this chapter, three examples have been taken to illustrate the ease and utility of
   spreadsheets. These examples are Payroll Calculation, Fixed Asset Accounting, and Loan
   Repayment Schedule.
 • The first step in using spreadsheet is to list out the elements of the application. For each
   element, it is determined whether a direct value is to be entered or else it is to be computed
   using a formula.
 • Excel has a rich library of various built-in functions including financial functions, which
   can be directly used to carry out various (otherwise complex) calculations. A formula may
   use one or more such functions.
 • In these applications, some of the formulae use absolute address. The absolute address is
   used for those cells whose content should not change while the formula containing such
   cells is copied to other cells.
 • If-function is also used in these applications. If-function is used to implement different
   action corresponding to different conditions.
 • The Excel functions SLN and DB are used for computation of depreciation using Straight
   Line Method (SLM) and Written Down Value Method (WDVM), respectively. WDV Method is
   also termed as declining balance (DB) method.
 • The function PMT is used to compute the loan repayment schedule.




EXERCISE

Q1. MULTIPLE CHOICE QUESTIONS
 1. Which of the following options in a financial function indicates the interest for
    a period?
    a. FV.
    b. PV.
     c. Nper.
    d. Rate.

 2. Which of the following arguments in a financial function represents the total
    number of payments?
    a. FV.
    b. PV.
     c. Nper.
    d. Rate.                                                                                        101




                                               Reprint 2026-27
```

---

## page 16

```
                                                        Computerised Accounting System

      3. What category of functions is used in this formula:
         =PMT(C10/12,C8,C9,1)
         a. Logical.
         b. Financial.
         c. Payment.
         d. Statistical.

      4. When Extend Selection is active, what is the keyboard shortcut for selecting
         all data up to and including the last row?
         a. [Ctrl]+[Down Arrow].
         b. [Ctrl]+[Home].
         c. [Ctrl]+[Shift].
         d. [Ctrl]+[Up Arrow].

      5. Which formula would result in TRUE if C4 is less than 10 and D4 is less than
         100?
         a. =AND(C4>10, D4>10).
         b. =AND(C4>10, C4<100).
         c. =AND(C4>10, D4<10).
         d. =AND(C4<10, D4<100).

      6. Which of these is not an argument of the IF function?
         a. Logical_test.
         b. Value_if_false.
         c. Value_when_false.
         d. Value_if_true.

      7. In what cell is the Rate for PMT function where = PMT (C8, C9, C10, C11,
         C12)?
         a. C8.
         b. C9.
         c. C10.
         d. C12.

      Q2. ANSWER THE FOLLOWING QUESTIONS
      1. What is the meaning of PV?

      2. State the usage of FV?

102   3. What is the purpose of DB function?




                              Reprint 2026-27
```

---

## page 17

```
Use of Spreadsheet in Business Application

 4. If an investment of Rs. 1,000 is made today, ascertain its Future Value (FV)
    after 2 years if the rate of interest is taken as 10%?
 5. If a sum of Rs. 1000 is likely to be earned after 3 years, calculate its present
    value (PV).

 6. What is the difference between WDV method and SLM method of depreciation?
 7. Describe the two basic methods of depreciation. What functions of Excel are
    used for computation of depreciation?
 8. Explain the importance of absolute and relative addresses. What is the basis
    of using relative address and absolute address?

SKILL REVIEW
 1. In columns F, G, H, I, J, and N of the Payroll spreadsheet shown in Figure
    3.3 (a) and Figure 3.3 (b) the absolute addresses are used. What will happen
    if relative addresses are used instead of absolute addresses?

 2. In columns g of the spreadsheet shown in Figure 3.8 b for the depreciation
    calculation using WDV method (i.e. using DB function), the absolute addresses
    of cell F3 is used. Taking relative address of F3 instead of its absolute address
    will lead to wrong result when the formula is copied. Explain the reason and
    write down the values copied along with the correct values, which should
    have been copied.

 3. Prepare attendance record in a spreadsheet for a class of 25 student’s month
    wise for 10 months. Calculate the percentage of presence for each student
    every month. Prepare a month wise summary of every student and calculate
    the overall percentage of presence.

 4. Use spreadsheet to prepare class timetable. It should compute and check the
    total number of lectures, tutorials and lab practical sessions allocated for
    each subject. It should also compute and check the total number of hours of
    engagement for each teacher.

 5. Prepare the worksheets yourself for examples used in sections 3.1, 3.2, 3.3
    and 3.4 respectively. Add two new more records in each worksheet (with your
    own assumed values) and verify whether the computations are correct.

 6. Create a worksheet to keep a record of employees of M/s Opportunities
    Company. Employee details should include Name of Employee, Designation
    and Basic Salary. Enter 50 records. Calculate Dearness Allowance (DA) as
    37.5% of Basic Salary, House Rent Allowance (HRA) 22.5% of Basic Salary,
    Provident Fund (PF) as 12% of Basic Salary, Gross Salary as Basic Salary +
    DA+HRA. The Income Tax (IT) as 20% of Gross Salary and Net Salary is Gross
    Salary – (PF+IT) for each employee. Calculate also Total Salary, Average Salary,
    Maximum Salary and Minimum Salary paid by the company.

 7. In Section-3.3, the loan instalment is computed for a given amount of loan
    repayable over a specified period at a specified rate of interest. Modify this
    exercise by fixing the loan instalment amount and compute the loan period
    using the PMT function.                                                             103




                                               Reprint 2026-27
```

---

## page 18

```
                                                  Computerised Accounting System

      ANSWERS
      1. b      2. c     3. b            4. c   5. d      6. c       7. a




104




                       Reprint 2026-27
```