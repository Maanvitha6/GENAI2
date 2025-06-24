# june 09 2025

1. Programming :- 
    
    The process of giving instructions to a computer to make it do specific tasks.
    Each instruction tells the computer to do one small task.

    why do we need programming in real-life :

        To make computers do work for us.
        Like sending emails, calculating bills, or booking tickets automatically.

        To create apps and websites.
        Like Instagram, Google, Zomato -> all are built using programming.

2. why only python programming compared to other languages? 
    
    * python is super-friendly. 
    * python is very easy to read and write.
    * python is like talking to the computer in a simple way. It helps you build powerful things without getting stuck in        complicated code.

3. Instructions:- 
    
    command you give to the computer to do something. 

4. Operators :- 
    
    Operators are symbols that tell Python to perform some action like adding, comparing, or checking conditions. 

    1. Arithmetic Operators :- (Used for Math Operations)
     
    | Operator | Meaning             | Example   | Result | What it Does                                          |
    | -------- | ------------------- | --------- | ------ | ----------------------------------------------------- |
    | `+`      | Addition            | `5 + 3`   | `8`    | Adds two numbers                                      |
    | `-`      | Subtraction         | `5 - 2`   | `3`    | Subtracts second number from the first                |
    | `*`      | Multiplication      | `4 * 3`   | `12`   | Multiplies the numbers                                |
    | `/`      | Division            | `10 / 2`  | `5.0`  | Divides the first number by the second (float result) |
    | `//`     | Floor Division      | `10 // 3` | `3`    | Gives only the whole number (no decimals)             |
    | `%`      | Modulus (Remainder) | `10 % 3`  | `1`    | Returns the remainder after division                  |
    | `**`     | Exponent (Power)    | `2 ** 3`  | `8`    | Means 2 raised to the power 3 (2 × 2 × 2)             |


    2. Comparison Operators :- (Used to Compare Two Values).

    | Operator | Meaning          | Example  | Result  | What it Checks              |
    | -------- | ---------------- | -------- | ------- | --------------------------- |
    | `==`     | Equal to         | `5 == 5` | `True`  | Are both values equal?      |
    | `!=`     | Not equal to     | `5 != 3` | `True`  | Are values different?       |
    | `>`      | Greater than     | `5 > 3`  | `True`  | Is the first value larger?  |
    | `<`      | Less than        | `5 < 2`  | `False` | Is the first value smaller? |
    | `>=`     | Greater or equal | `5 >= 5` | `True`  | Is it greater or the same?  |
    | `<=`     | Less or equal    | `5 <= 4` | `False` | Is it smaller or the same?  |


    3. Logical Operators :- (Used in Conditions).

    | Operator | Meaning                      | Example          | Result  | What it Means                                |
    | -------- | ---------------------------- | ---------------- | ------- | -------------------------------------------- |
    | `and`    | True if both are true        | `True and False` | `False` | Both sides must be true to return `True`     |
    | `or`     | True if at least one is true | `True or False`  | `True`  | If **any** one is true, the result is `True` |
    | `not`    | Reverses the value           | `not True`       | `False` | Flips the result: `not True` becomes `False` |


    4. Assignment Operators:- (Used to Assign and Update Values)

    | Operator | Example  | Same As     | What it Does                         |
    | -------- | -------- | ----------- | ------------------------------------ |
    | `=`      | `x = 5`  | —           | Assigns value 5 to the variable `x`  |
    | `+=`     | `x += 2` | `x = x + 2` | Adds 2 to current value of `x`       |
    | `-=`     | `x -= 2` | `x = x - 2` | Subtracts 2 from `x`                 |
    | `*=`     | `x *= 3` | `x = x * 3` | Multiplies `x` by 3                  |
    | `/=`     | `x /= 2` | `x = x / 2` | Divides `x` by 2                     |
    | `%=`     | `x %= 2` | `x = x % 2` | Stores remainder of `x` divided by 2 |


    5. Conditional operators :- same as comparision operators.

5. Packages:- 

   . package is a collection of useful tools (functions, classes, or modules) that help you do specific tasks easily without   writing everything from scratch.

   . (or)  A package is like a toolbox in Python. Each toolbox has tools (code) made for solving certain problems like math, data, graphs, or AI.

       Why packages are important ?

       . Saves Time - You dont have to write long code.
       . Easy to Use - Just install and use the function.
   
   * what is meant by import package?

    . import means bringing a toolbox (package or module) into your Python program so you can use its tools (functions, methods, etc.). 

    . Python has many built-in and external packages, but to use them, you must import them first.

    * common and useful python packages:- 

    | Package Name | Used For                      | Significance / Example Use            |
    | ------------ | ----------------------------- | ------------------------------------- |
    | `math`       | Basic math functions          | `math.sqrt(16)` → 4.0                 |
    | `random`     | Random number generation      | Simulate dice, pick random item       |
    | `datetime`   | Date and time operations      | Add days, get current time            |
    | `os`         | Interact with system files    | List files, create folders            |
    | `sys`        | Python interpreter operations | Handle system arguments or exit codes |
    | `re`         | Regular expressions           | Pattern matching in strings           |

     
     *  Data Science & Analysis Packages:- 

    | Package       | Used For                   | Example Use                             |
    | ------------- | -------------------------- | --------------------------------------- |
    | `numpy`       | Math with arrays           | Fast math operations, used in AI and ML |
    | `pandas`      | Data analysis & tables     | Load and clean Excel/CSV files          |
    | `matplotlib`  | Plotting charts            | Bar chart, line chart, etc.             |
    | `seaborn`     | Advanced statistical plots | Heatmaps, regression plots              |
    | `scipy`       | Scientific computing       | Signal processing, optimization         |
    | `statsmodels` | Statistical analysis       | Regression, hypothesis testing          |

    
    * AI & Machine Learning Packages :-

    | Package        | Used For                 | Example Use                               |
    | -------------- | ------------------------ | ----------------------------------------- |
    | `scikit-learn` | Machine learning models  | Build a prediction model like spam filter |
    | `tensorflow`   | Deep learning (Google)   | Neural networks, image recognition        |
    | `keras`        | Simplified deep learning | Easier coding for deep learning models    |
    | `xgboost`      | Boosted trees (ML)       | High-performance prediction models        |


6. Flowchart :-

   . A flowchart is a diagram that shows the steps of a process using different shapes and arrows.

   . It helps you plan, analyze, and communicate how a task or program works — step by step.

   * why use flowcharts ? 

    .  Easy to understand  - 	Shows logic visually – no confusion

    .  Saves time	      -      Helps plan before writing code

    .  Debugging help	    -    Easy to find errors in the logic

   * Common flowchart symbols and their significance :-
    
    | Shape | Symbol | Name             | Meaning / When to Use                          | Example                           |
    | ----- | ------ | ---------------- | ---------------------------------------------- | --------------------------------- |
    | 🔶    | ▭      | **Terminator**   | Start or End of the process                    | `Start`, `End`                    |
    | 🔷    | ◼      | **Process**      | Action step or instruction                     | `Enter password`, `Calculate sum` |
    | 🔷    | ◯      | **Input/Output** | Data entry or output step                      | `Enter number`, `Print result`    |
    | 🔷    | 🔷     | **Decision**     | A Yes/No or True/False question or condition   | `Is age > 18?` → Yes or No        |
    | 🔽    | →      | **Arrow**        | Shows the direction of flow                    | From one step to another          |
    | 🔁    | 🔁     | **Connector**    | Jump from one part to another (for big charts) | To continue on next page          |


    * How flowchart helps in programming? 

    . Before writing code, draw a flowchart to plan the logic.

    . Helps beginners understand how decisions, inputs, and loops work.

7. Condition :-
   . A condition is a statement that checks whether something is True or False.

   . It helps the program decide what to do next.

   Simple example :- 

   if age >= 18:

    print("You can vote")

    Here, age >= 18 is a condition.

    .If it's True → it prints "You can vote".

    .If it's False → it skips that step.

* Types of conditions :- 

1. simple condition :-

   * checks one condition.

   example :- 

   if number > 0:

    print("Positive number")
 

2. if-else condition :- 

   * Gives a choice. Do this or that. 

   example :- 

    if number % 2 == 0:

    print("Even")

else:

    print("Odd")


3.  If-Elif-Else (Multiple Conditions) :-

    * checks many possibilities.

    Example :-

    if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
else:
    print("Needs Improvement")


4. Nested conditions :-

   * one condition inside another.

   example :-
   if age >= 18:
    if has_id:
        print("You can vote")


8. Loops :-
  
* A loop is a way to repeat a block of code again and again until a certain condition is met.

 . It’s like telling the computer: Do this task multiple times without writing the same code again. 

* why loops are used ?

. Repeat Tasks - 	Do the same thing multiple times (e.g., print numbers).

. Save Time    - 	Avoid writing the same line of code many times.
 
Example :-

 Example	      -                 Loop Use

 Counting 1 to 10  -	                Loop prints each number
 Checking all messages in inbox	-    Loop checks each email

Types of loops :-

1. for loop : 

  . Used when you know how many times to repeat.

  example :-
  for i in range(5):
    print(i)


    . Prints: 0, 1, 2, 3, 4

2. while loop :-

   . Used when you dont know how many times to repeat - keep going while a condition is true.

   example :- 
   count = 1
while count <= 5:
    print(count)
    count += 1

    . repeats until count becomes 6 . 

3. Nested loop :-

   A loop inside another loop.

   example :-
   for i in range(3):
    for j in range(2):
        print(i, j)


 * If we write the loop without condition, it goes infinite, that means it is infinite loop.

* Keywords Used in Loops :-

| Keyword    | Use                                    |
| ---------- | -------------------------------------- |
| `break`    | Stop the loop completely               |
| `continue` | Skip current step, go to next one      |
| `range()`  | Gives a list of numbers for `for` loop |



9. Function :-

   . A function is a block of code that does a specific task. 

   . You give it a name, and you can reuse it anytime by calling it.

   * Think of it like a machine:

     . You give input, it does some work, and gives output.

 * Why are functions helpful? 

 . Easy to manage  -	Each function does one task .

 . saves time	   -    Call the function wherever needed.

 1. Built-in Functions :- 

 . These are already provided by Python.

   Function	Use Example :

   | Function         | Use Example                 |
   | ---------------- | --------------------------- |
   | `print()`        | Prints output               |
   | `len()`          | Finds length of string/list |
   | `type()`         | Tells data type             |
   | `input()`        | Takes user input            |
   | `int()`, `str()` | Converts data types         |


2. User-defined functions :-

 . Funtcions that we create.
  <img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/function.png">
   
3. Function with parameters :-

 . Take input values (like variables inside the function).

 <img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/function%20with%20parameters.png">

4. Functions with return value :- 

  . Give back an output (result) using return.

  Example :-
  def square(n):
    return n * n


10. Parameters = input names in function definition.

    . Parameters are the placeholders or variables listed in a function’s definition.

    Example : - 

    <img src ="https://github.com/Maanvitha6/GENAI/blob/main/Assets/parameter%20example.png">


11. Arguments = actual input values in function call.

    . Arguments are the actual values you pass to a function when you call it.

    Example :-

    <img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/arguments%20example.png">

* Key difference between parameters and arguments :-

| Aspect         | Parameters                       | Arguments                         |
| -------------- | -------------------------------- | --------------------------------- |
| What are they? | Variables in function definition | Actual values passed to function  |
| When used?     | When defining a function         | When calling or invoking function |
| Role           | Act as placeholders              | Provide the data for placeholders |


| Term         | What it means                 | Example                |
| ------------ | ----------------------------- | ---------------------- |
| **Defining** | Writing the function’s code   | `def say_hello(): ...` |
| **Calling**  | Running or using the function | `say_hello()`          |


 * DATA STRUCTURES :- 

  .  collections of data types, including lists, string, tuples, sets, dictionaries and arrays.

  .  A data structure is a way to store, organize, and manage data. 

      * Why are data structures useful :-

           . They help organize data in programs.

           . Make it easy to search, add, delete, or update data.

 <img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/types%20of%20data%20structures.png">

1. List :- ordered and mutable.

         -> items are in order. 

         -> you can change, add, or remove items.

         -> you can use loops to go through each item .

* Example :- 

top_dishes = ["biryani", "paneer", "gulab jamun"]

2. Tuple :- Ordered and immutable.

      -> ordered like lists.

      -> cannot change after creation.

3. Set :- Unordered and no duplicates.

      -> used when you want only unique values.

      -> duplicates are automatically removed. 

4. Dictionary :- (Key-Value pairs).
      
      -> used when each value has a name/label.

      Example :-

      student = {"name": "Maanvitha", "age": 22, "course": "Python"}
      
      . Access data using keys like student["name"]

# Real-time example for all these concepts:-