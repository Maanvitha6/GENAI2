# June 11 2025
 
1. File handling :- 
      
    File handling is the process of creating, opening, reading, writing, and updating files using a programming language. In
     
    Python, file handling is done using built-in functions like open(), read(), write(), and close(). 

2. Operations in File Handling :- 

    Mode    - 	      Description	                -                         Behavior

      r	    -       Read-only mode	                -     Opens the file for reading. File must exist; otherwise, raises an error.

      rb	-       Read-only in binary mode	    -     Opens the file for reading binary data. File must exist.

      r+	-       Read and write mode	            -     Opens the file for both reading and writing. File must exist.

      rb+	-       Read and write in binary mode	-     Opens the file for both reading and writing binary data.File must exist

      w	    -       Write mode	                     -    Opens the file for writing.Creates new file or truncates the existingone

      wb	-       Write in binary mode	          -   Opens the file for writing binary data. Creates or truncates file.

      w+	-       Write and read mode	             -    Opens the file for writing and reading. Creates or truncates file.

      wb+	-       Write and read in binary mode	-     Opens file for writing and reading binary data.Creates or truncates file

      a	    -       Append mode	                     -    Opens the file for appending. Creates new file if it doesn’t exist.

      ab	-       Append in binary mode	         -    Opens the file for appending binary data. Creates new file if it doesn’t
      
                                                          exist.

      a+	-       Append and read mode	          -   Opens file for appending and reading.Creates new file if itdoesn’texist.

      ab+	-       Append and read in binary mode	  -   Opens the file for appending and reading binary data. Creates new file
       
                                                          if it doesn’t exist.

      x	    -                                          -  Exclusive creation mode	Creates a new file. Raises error if file 
      
                                                          already exists.

      xb	-       Exclusive creation in binary mode -	  Creates new binary file. Raises error if file exists.

      x+	-       Exclusive creation with read/write -  Creates new file for reading and writing. Error if file exists.

      xb+	-       Exclusive creation in binary with r/w -	Creates new binary file for reading and writing. Error if file exists.

    * Benefits of file handling :- 

         Store data permanently (unlike variables which are temporary) Save user input or program output Read data from files 
         
         like CSV, TXT, logs Log errors or events (e.g., system logs, audit trails).

3. Exception Handling :-

      It is a mechanism that allows your program to gracefully respond to errors during runtime, instead of crashing.

    * Benefits of Exception Handling :- 

          To avoid program crashes To handle unexpected input or events To show meaningful error messages to the user .

    * Common errors :-

        1. ZeroDivisionError : When dividing a number by zero.

        2. FileNotFoundError : When trying to open a file that doesn't exist.

        3. typeError : When incompatible types are used (e.g. adding string to int) valueError: When wrong data type is given
        
           (e.g. text instead of number).

4. Exception Handling Keywords :-

   | **Keyword** | **Purpose** 

   | `try`       | Block of code to test for errors
                                               |
   | `except`    | Block that runs if an error occurs 
                                            |
   | `else`      | Runs if there is **no error** 
                                                 |
   | `finally`   | **Always runs** — used for cleanup (like closing files or returning a card) |

   * Example :- 

     | **Keyword** | **ATM Example**
                                                           
     | ----------- | -------------------------------------------------------------------- |

     | `try`       | You swipe your card at the ATM        
                               |
     | `except`    | If the card is declined, it shows an error message 
                  
     | `else`      | If the card is accepted, it shows your balance   
                    
     | `finally`   | Whether the card is accepted or declined, it is returned back to you |


5. OOPS concepts summary :- 

   | **Concept**       | **Definition**                                                | **Real-World Use 
   
                                                                                           Case** 

   | **Encapsulation** | Hides internal data using methods and access control          | Protecting marks, passwords, banking
   
                                                                                         systems.

   | **Abstraction**   | Shows only essential features while hiding background details | ATM interface, APIs, buttons hiding
   
                                                                                         internal logic.         |

   | **Inheritance**   | Child class inherits properties/methods from a parent class   | Developer inherits from Employee, Car
   
                                                                                         from Vehicle.         |

   | **Polymorphism**  | Same method acts differently in different classes             | `area()` method in Circle vs.
   
                                                                                          Square
                                                                                                                 |
   | **Class**         | A blueprint for creating objects                              | `class

                                                                                          Student:`                                           |
   | **Object**        | Instance of a class                                           | `s1 = Student("Asha")`                                     |
   | **Method**        | Function defined inside a class                               | `get_marks()`, `greet()`                                   |
   | **Constructor**   | `__init__()` method runs when object is created               | Automatically sets name, age when a 
   
                                                                                         student object is made |

   | **Destructor**    | `__del__()` method runs when object is deleted                | Cleanup: closing files, releasing 
   
                                                                                         memory                   |

6. Constructor vs Destructor :-

   | **Term**        | **Explanation**                                                   | **Real-Life 
   
                                                                                           Analogy**   

   | **Constructor** | A special method (`__init__`) that runs when an object is created | When you **buy a phone**, it comes 
   
                                                                                           with pre-installed apps/settings |

   | **Destructor**  | A special method (`__del__`) that runs when an object is deleted  | When you **shut down a computer**, it  

                                                                                           **closes all apps and saves work** |
