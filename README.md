# Functional Treat – Data Analyzer and Transformer

**Author:** Siddhi Gadhiya

## Project Description

Functional Treat is a Python-based Data Analyzer and Transformer program developed as part of a Python Data Science practical project.

The program allows users to enter 1D or 2D list data and perform different data analysis and transformation operations through a simple menu-driven interface.

The project demonstrates important Python concepts such as built-in functions, User-Defined Functions (UDF), `*args`, `**kwargs`, `__doc__`, recursion, lambda functions, global variables, multiple return values, list operations, and sorting techniques.

## Technology Used

**Python 3.14.6**

## Objectives

- Analyze numerical data using Python built-in functions.
- Create and use User-Defined Functions (UDF).
- Demonstrate `*args` and `**kwargs`.
- Use function documentation with `__doc__`.
- Apply recursion for factorial calculation.
- Use lambda functions with `map()` and `filter()`.
- Demonstrate the use of a global variable.
- Return multiple values from a function.
- Work with both 1D and 2D lists.
- Demonstrate `sort()` and `sorted()`.

## Features

### 1. Input Data

The user can enter:

- A 1D list
- A 2D nested list

### 2. Built-in Functions

The program uses Python built-in functions such as:

- `len()`
- `min()`
- `max()`
- `sum()`

### 3. User-Defined Functions

Separate functions are created for different tasks such as:

- Taking input
- Displaying data
- Calculating summary
- Sorting data
- Filtering data
- Calculating statistics

### 4. `*args`

The program uses `*args` to accept a variable number of numerical values.

### 5. `**kwargs`

The program uses `**kwargs` to pass dataset information as keyword arguments.

### 6. `__doc__`

Function documentation strings are used and displayed using the `__doc__` attribute.

### 7. Recursion

A recursive function is used to calculate the factorial of a number.

### 8. Lambda Function

Lambda functions are used with `filter()` and `map()` to filter and transform list data.

### 9. Global Variable

A global variable is used to maintain information that can be accessed across different functions.

### 10. Multiple Return Values

A function returns multiple statistics such as:

- Minimum
- Maximum
- Sum
- Average

### 11. Sorting

The program demonstrates both:

- `sort()` – changes the original list.
- `sorted()` – returns a new sorted list.

## Menu

```text
Main Menu

1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit

```

## Sample Output

==============================================

Welcome to the Data Analyzer and Transformer

==============================================

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 1
You selected: 1

Choose data type:
1. 1D List
2. 2D List
Enter your choice: 1
You selected: 1
Enter values separated by spaces: 34 12 56 78 43 21 90
Data stored successfully!

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 2
You selected: 2

Current Dataset:
[34, 12, 56, 78, 43, 21, 90]

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 3
You selected: 3

Data Summary (Built-in Functions)
Total elements : 7
Minimum value  : 12
Maximum value  : 90
Sum of values  : 334
Average value  : 47.71

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 4
You selected: 4

User-Defined Function Demo
Count  : 7
Sum    : 334
Highest: 90
Lowest : 12

Dataset Information (**kwargs)
Data_Type      : 1D
Elements       : 7
Average        : 47.71

Function Documentation (__doc__):
Analyze any number of values using *args.

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 5
You selected: 5

Enter a number for factorial: 5
You entered: 5
Factorial of 5 is 120

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 6
You selected: 6

Enter threshold: 50
You entered: 50
Values >= 50 : [56, 78, 90]
Doubled values       : [112, 156, 180]

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 7
You selected: 7

Global Variable Demo
Summary function was used 1 time(s).

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 8
You selected: 8

Dataset Statistics (Multiple Return Values)
Minimum : 12
Maximum : 90
Sum     : 334
Average : 47.71

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 9
You selected: 9

Sorting Options
1. Ascending
2. Descending
Enter your choice: 1
You selected: 1

Original copy : [34, 12, 56, 78, 43, 21, 90]
After sort()  : [12, 21, 34, 43, 56, 78, 90]
sorted() copy : [12, 21, 34, 43, 56, 78, 90]

Main Menu
1. Input Data (1D / 2D)
2. Display Data
3. Data Summary (Built-in Functions)
4. UDF + *args + **kwargs + __doc__
5. Factorial (Recursion)
6. Filter Data (Lambda + map + filter)
7. Global Variable Demo
8. Statistics (Return Multiple Values)
9. Sort Data (sort / sorted)
10. Exit
Please enter your choice: 10
You selected: 10

Thank you for using the Data Analyzer and Transformer!
Goodbye!