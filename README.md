# MyString
## Description This project implements a custom class called `MyString`, which enhances the functionality of the built-in `str` class in Python.
## Features
- Override the `lower()` method to convert the string to lowercase and append an exclamation mark (!).
-  - Implement a `count_words()` method that returns the number of words in the string. - Override the `replace()` method to convert the string to uppercase before performing the replacement.
   -  - Override the `__add__()` method to insert a space between two `MyString` objects when concatenating.
      -  - Override the `__mul__()` method to repeat the string with a dash (-) separating each repetition.  ## Usage
         -  To use the `MyString` class, you can import it from your module
         -  : ```python from mystring import MyString my_str = MyString("Hello World") print(my_str.lower()) # Outputs: hello world!
