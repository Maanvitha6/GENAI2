  # June 10 2025

  1. Identifier :-
     
     identifiers are the names used to identify variables, functions, classes, modules, and objects.

      * Rules for writing Identifiers :-
         
         . Start with a letter (A - Z or a - z) or an underscore _ 
           
            Example :
              
               Valid: name, _value, myVar
            
         . Followed by any number of letters, digits (0 - 9), or underscores
           
           Example :

              student1, total_score, data123

         . Cannot use special characters such as @, $, %, !, etc.

         . Case-sensitive.

              value, Value, and VALUE are all different identifiers.

         . Cannot be a Python keyword. 

  2.  Instruction :-

       Instructions are individual lines of code that perform actions like:

             Assigning values

             Taking input

             Doing calculations

    . Each line in Python is usually one instruction.

  3. Comments :-

       A comment is a note written to explain the code.

       Comments can be written by using # or ''' triple quotes '''

       Two types of comments :-

         1. Single-line comment :-

              When we want to just write single line we can use #.

         2. Multiple-line comment :-

              When we want to write multiple lines then we can write by placing the text in '''  '''

        * Why comments are helpful ?

             Explain the code.

             Help others understand the code.

   4. Docstring :-
       
        It can be written at any part of the code like right after a defining a function we will use this.

        It appears at the beginning of function, class, module.

   5. Indentation :-

       Indentation means adding spaces or tabs at the beginning of a line of code to show structure.
    
    Example :-

    <img src = "https://github.com/Maanvitha6/GENAI/blob/main/Assets/intendation.png">

    6. Variable :-

         A variable is a name that stores data .

         Example :-

         x = 10

         name = "Alice"

           Here x is a variable that stores data value 10. and name is a variable that stores alice.

    Types of variables :- 

     1. By Data types :-

            1. Integer (int) - Stores whole numbers.

               Example: x = 10

            2. Float (float) - Stores decimal numbers.

               Example: pi = 3.14

            3. String (str) - Stores text.

               Example: name = "Python"

            4. Boolean (bool) - Stores True or False.

               Example: is_active = True

            5. List - Stores an ordered collection.

               Example: fruits = ["apple", "banana"]

            6. Tuple - Stores an ordered, immutable collection.

               Example: point = (4, 5)

            7. Set - Stores unordered unique items.

               Example: items = {1, 2, 3}

            8. Dictionary - Stores key-value pairs.

               Example: student = {"name": "Alice", "age": 20}

     2. By scope :- 

            1. Local Variable - Defined inside a function, used only there.

            Example :-

            def greet():

                message = "Hello"

                print(message)

            2. Global Variable - Defined outside all functions, accessible everywhere.

            Example :-

            greeting = "Hi"

            def say_hi():

                print(greeting)

   7. Operations on datatypes :-

               1. List :-
                
                 A list is an ordered, mutable collection.

                 Example:-

                 my_list = [10, 20, 30, 40]

                 * Indexing:-

                 Access elements by position.

                 Syntax: list[index]

                 Example :- print(my_list[0])  # 10

                 * slicing :- 

                 Extract a sublist.

                 Syntax: list[start:stop]

                 Example :- print(my_list[1:3])  # [20, 30]

                 * Adding :-

                 Append to end: list.append(value)

                 Insert at index: list.insert(index, value)

                 Add multiple items: list.extend([v1, v2])

                 Example :-

                 my_list.append(50)

                 my_list.insert(1, 15)

                 my_list.extend([60, 70])

                 *  Removing

                 By value: list.remove(value)

                 By index: list.pop(index)

                 Example :- 

                 my_list.remove(30)

                 my_list.pop(0)

                 * Deleting ;-
                
                  Delete by index: del list[index]

                  Delete all items: list.clear()

                  Delete list: del list

                  Example :-

                  del my_list[1]

                  my_list.clear()

                  del my_list

            2. Tuple :- 
              
               A tuple is an ordered, immutable collection.

               my_tuple = (1, 2, 3, 4).

               * Indexing:-

               Syntax: tuple[index]

               print(my_tuple[2])  # 3

               * slicing :-

                Syntax: tuple[start:stop]

                print(my_tuple[1:3])  # (2, 3)

            3. Dictionary :-

              A dictionary stores data as key-value pairs.

              my_dict = {'a': 1, 'b': 2}

               *  Indexing (by key)

                 Syntax: dict[key]

                 Example :- print(my_dict['a'])  # 1

                * Adding / Updating :- 

                  Add new or update existing key.

                  Syntax: dict[key] = value

                    Example :- my_dict['c'] = 3

                               my_dict['a'] = 10

                * Removing :- 

                 Remove and return value: dict.pop(key)

                 Delete by key: del dict[key]

                 Example :- my_dict.pop('b')

                 del my_dict['c']

                 * Deleting :-

                 Delete all: dict.clear()

                 Delete dict: del dict

                 Example :- my_dict.clear()

                 del my_dict

            4. set :-
             
               A set is an unordered collection of unique items.

               my_set = {1, 2, 3}

               * Adding :- 

                Add single item: set.add(value)

                Add multiple: set.update([v1, v2])

                Example :- my_set.add(4)

                my_set.update([5, 6])

                * Removing :-

                  Remove value: set.remove(value) (error if not found)

                  Safe remove: set.discard(value) (no error if not found)

                  Remove random: set.pop()

                  Example :- my_set.remove(2)

                  my_set.discard(10)

                  my_set.pop()

                  * Deleting :-

                  Clear set: set.clear()

                  Delete set: del set

                  Example :- my_set.clear()

                  del my_set











         

