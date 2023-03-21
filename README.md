Random Password Generator Mini-Project
======================================

This is a simple command-line random password generator program written in Python. The program takes user input for the minimum password length, and whether to include numbers and special characters in the generated password. It then generates a random password that meets the specified criteria.

Requirements
------------

-   Python 3.6+

Files
-----

-   `password_generator.py`: The main Python script that runs the random password generator program.

How to Run
----------

1.  Ensure you have Python 3.6+ installed on your system.
2.  Run the `password_generator.py` script using `python password_generator.py` or `python3 password_generator.py`, depending on your system configuration.
3.  Enter the desired minimum password length when prompted.
4.  Specify whether you want numbers in your password by entering 'y' for yes or 'n' for no when prompted.
5.  Specify whether you want special characters in your password by entering 'y' for yes or 'n' for no when prompted.
6.  The program will generate a random password based on your preferences and display it.

Customizing the Password Generator
----------------------------------

To customize the character sets used in the password generation process, modify the `letters`, `digits`, and `special` variables in the `generate_password()` function within the `password_generator.py` script. For example, you can add more special characters or exclude certain characters from the available options.
