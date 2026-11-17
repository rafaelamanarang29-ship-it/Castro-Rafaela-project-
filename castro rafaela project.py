while True:

    print("===============================")
    print("  WELCOME TO PYTHON TUTORIAL   ")
    print("===============================")
    print("")
    print("Hello welcome to python tutorial system.")
    print("How can I help you today?")

    print("")
    print("What chapter do you want to study?")
    print("[1] Chapter 1 - Introduction to programming")
    print("[2] Chapter 2 - Python basic syntax")
    print("[3] Chapter 3 - Arithmetic operators and expressions")
    print("")

    chapter = input("Enter chapter number: ")
    print("")

    if chapter == "1":

        print("Chapter 1: Introduction to programming")
        print("[1] What is Python programming?")
        print("[2] Why learn Python?")
        print("[3] What do you need to start Python?")
        print("")

        lesson = input("Enter lesson number: ")

        if lesson == "1":
            print("Lesson: What is Python programming?")
            print("Python is a high-level, interpreted, and general-purpose programming language. It was created by Guido van Rossum in 1991.")
            print("")
            print("Example code:")
            print('print("Hello, world")')
            print("")
            print("Output:")
            print("Hello, world!")

        elif lesson == "2":
            print("Lesson: Why learn Python?")
            print("Python is simple and easy to learn. It has readable syntax and is versatile. It also has a huge community.")
            print("")
            print("Example code:")
            print('print("Python is easy to learn!")')
            print("")
            print("Output:")
            print("Python is easy to learn!")

        elif lesson == "3":
            print("Lesson: What do you need to start Python?")
            print("You need Python and a code editor or IDE. Examples are PyCharm, VS Code, and Jupyter Notebook.")
            print("")
            print("Example code:")
            print('print("I am ready to learn Python!")')
            print("")
            print("Output:")
            print("I am ready to learn Python!")

        else:
            print("Invalid lesson number!")

    elif chapter == "2":

        print("Chapter 2: Python basic syntax")
        print("What lesson do you want to learn?")
        print("[1] What is Python syntax?")
        print("[2] Python is case-sensitive")
        print("[3] Indentation")
        print("")

        lesson = input("Enter lesson number: ")

        if lesson == "1":
            print("Lesson: What is Python syntax?")
            print("Syntax refers to the rules used to correctly write Python code.")
            print("")
            print("Example code:")
            print('name = "John"')
            print("print(name)")
            print("")
            print("Output:")
            print("John")

        elif lesson == "2":
            print("Lesson: Python is case-sensitive")
            print("Python treats uppercase and lowercase letters differently. Name and name are not the same.")
            print("")
            print("Example code:")
            print('name = "John"')
            print("print(name)")
            print("")
            print("Output:")
            print("John")

        elif lesson == "3":
            print("Lesson: Indentation")
            print("Indentation refers to the spaces at the beginning of a line of code. It defines blocks of code in Python.")
            print("")
            print("Example code:")
            print("age = 18")
            print("if age >= 18:")
            print('    print("Adult")')
            print("")
            print("Output:")
            print("Adult")

        else:
            print("Invalid lesson number!")

    elif chapter == "3":

        print("Chapter 3: Arithmetic operators")
        print("What lesson do you want to learn?")
        print("[1] What are arithmetic operators?")
        print("[2] Arithmetic operators in Python")
        print("[3] Expression in Python")
        print("[4] PEMDAS")
        print("")

        lesson = input("Enter lesson number: ")

        if lesson == "1":
            print("Lesson: What are arithmetic operators?")
            print("Arithmetic operators are symbols used to perform mathematical calculations.")
            print("")
            print("Example code:")
            print("print(5 + 3)")
            print("")
            print("Output:")
            print("8")

        elif lesson == "2":
            print("Lesson: Arithmetic operators")
            print("+ Addition")
            print("- Subtraction")
            print("* Multiplication")
            print("/ Division")
            print("// Floor Division")
            print("% Modulus")
            print("** Exponentiation")
            print("")
            print("Example code:")
            print("a = 10")
            print("b = 5")
            print("print(a + b)")
            print("")
            print("Output:")
            print("15")

        elif lesson == "3":
            print("Lesson: Expression in Python")
            print("An expression is a combination of values, variables, and operators that evaluates to a result.")
            print("")
            print("Example code:")
            print("a = 10")
            print("b = 5")
            print("result = a + b")
            print("print(result)")
            print("")
            print("Output:")
            print("15")

        elif lesson == "4":
            print("Lesson: PEMDAS")
            print("Python follows the order of operations:")
            print("P - Parentheses")
            print("E - Exponents")
            print("M - Multiplication")
            print("D - Division")
            print("A - Addition")
            print("S - Subtraction")
            print("")
            print("Example code:")
            print("result = 1 + 3 * 4")
            print("print(result)")
            print("")
            print("Output:")
            print("13")

        else:
            print("Invalid lesson number!")

    else:
        print("Invalid chapter number!")

    print("")
    repeat = input("Do you want to study another lesson? (yes/no): ")

    if repeat.lower() == "yes":
        print("")
        continue
    else:
        print("")
        print("Thank you for using Python Tutorial System!")
        break