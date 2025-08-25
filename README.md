# 🐍 Python — Complete Theoretical Knowledge

This repository is designed as a **theory handbook** for Python learners.  
Each file in this repo demonstrates concepts practically, while this `README.md` provides the **in-depth theoretical explanation, rules, and tips**.  

---

## 📌 Table of Contents  

1. [Introduction to Python](#introduction-to-python)  
2. [Basics of Python](#basics-of-python)  
3. [Control Flow](#control-flow)  
4. [Functions](#functions)  
5. [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)  
6. [Data Structures](#data-structures)  
7. [Advanced Concepts](#advanced-concepts)  
8. [File Handling](#file-handling)  
9. [Error Handling](#error-handling)  
10. [Tips & Tricks](#tips--tricks)  

---

## 🟢 Introduction to Python  

- **High-level language** → Focuses on readability and ease of use.  
- **Interpreted** → Runs line by line, no compilation required.  
- **Dynamically typed** → No need to declare data type explicitly.  
- **Cross-platform** → Runs on Windows, macOS, Linux.  
- **Object-Oriented** → Everything in Python is an object.  
- **Large Standard Library** → Provides ready-made modules.  

> 🔑 **Tip:** Always use the latest Python version for new features and better performance.

---

## 🔹 Basics of Python  

### Variables  
- Containers to store data (no need to declare type).  
- Variable names must start with a letter or underscore.  
- Case-sensitive.  

### Data Types  
- **Numeric** → `int`, `float`, `complex`.  
- **Sequence** → `list`, `tuple`, `range`, `str`.  
- **Set** → `set`, `frozenset`.  
- **Mapping** → `dict`.  
- **Boolean** → `True`, `False`.  
- **Special** → `NoneType`.  

### Operators  
- **Arithmetic** → `+ - * / % // **`.  
- **Comparison** → `== != > < >= <=`.  
- **Logical** → `and, or, not`.  
- **Assignment** → `=, +=, -=`.  
- **Membership** → `in, not in`.  
- **Identity** → `is, is not`.  

> ⚡ **Trick:** Use `is` for object identity, `==` for equality of values.

---

## 🔹 Control Flow  

### Conditional Statements  
- **if** → Executes block if condition is true.  
- **elif** → Checks multiple conditions.  
- **else** → Executes when no condition matches.  

### Loops  
- **For Loop** → Iterates over sequences.  
- **While Loop** → Runs until condition is false.  
- **Nested Loops** → Loop inside another loop.  

### Loop Control Statements  
- **break** → Exits loop immediately.  
- **continue** → Skips current iteration.  
- **pass** → Placeholder statement (does nothing).  

> 🔑 **Tip:** Avoid deeply nested loops — they reduce readability and performance.

---

## 🔹 Functions  

### Function Types  
- **Built-in Functions** → Provided by Python (`len`, `type`, etc.).  
- **User-defined Functions** → Created using `def`.  

### Function Arguments  
- **Positional Arguments** → Passed in order.  
- **Keyword Arguments** → Passed by name.  
- **Default Arguments** → Have predefined values.  
- **Variable Arguments** → `*args` and `**kwargs`.  

### Functional Concepts  
- **Recursion** → A function calling itself until base case is met.  
- **Higher-Order Functions** → Functions that take other functions as arguments.  
- **Anonymous Functions** → Lambda expressions.  

> ⚡ **Trick:** Use default arguments carefully — mutable types (`list`, `dict`) can cause unexpected results.  

---

## 🔹 Object-Oriented Programming (OOP)  

### Core Principles  
1. **Encapsulation** → Wrapping data & methods into a single unit (class).  
2. **Inheritance** → Child class can reuse parent class properties.  
3. **Polymorphism** → Same method name with different implementations.  
4. **Abstraction** → Hiding implementation details using abstract classes.  

### Special OOP Features  
- **Class vs Instance Variables** → Shared vs unique to each object.  
- **Static Method** → Belongs to the class, doesn’t need instance.  
- **Class Method** → Works with class itself, not instances.  
- **Property Decorator** → Used to manage attribute access.  
- **Magic/Dunder Methods** → Special methods like `__init__`, `__str__`, `__len__`.  

> 🔑 **Tip:** Use inheritance wisely; prefer composition if relationships aren’t naturally hierarchical.  

---

## 🔹 Data Structures  

### List  
- Ordered, mutable, allows duplicates.  
- Supports slicing and comprehension.  

### Tuple  
- Ordered, immutable.  
- Useful for fixed data.  

### Set  
- Unordered, unique elements only.  
- Supports mathematical operations (union, intersection).  

### Dictionary  
- Key-value pairs.  
- Keys must be unique and immutable.  

> ⚡ **Trick:** Use sets for fast membership checking; dictionaries for fast lookups.  

---

## 🔹 Advanced Concepts  

### Decorators  
- Functions that wrap other functions to extend behavior.  
- Commonly used for logging, authentication, performance measurement.  

### Duck Typing  
- “If it walks like a duck and quacks like a duck, it’s a duck.”  
- Focuses on behavior, not type.  

### Multithreading  
- Run multiple threads concurrently.  
- Useful for I/O bound tasks.  
- Not ideal for CPU heavy tasks (because of GIL).  

### Modules & Packages  
- **Modules** → Single `.py` file.  
- **Packages** → Collection of modules.  
- Use `import` to reuse code.  

---

## 🔹 File Handling  

- **Modes** → `r` (read), `w` (write), `a` (append), `b` (binary).  
- **Context Manager** → Use `with open()` to auto-close files.  
- **Reading** → Read all content, line by line, or fixed size.  
- **Writing** → Overwrite or append data to files.  

> 🔑 **Tip:** Always use context managers to avoid memory leaks.  

---

## 🔹 Error Handling  

- **try-except** → Catch errors gracefully.  
- **finally** → Always runs, useful for cleanup.  
- **raise** → Manually trigger exceptions.  
- **Custom Exceptions** → Create user-defined exceptions.  

> ⚡ **Trick:** Handle specific exceptions instead of using a generic `except:`.  

---

## 💡 Tips & Tricks  

1. Use **list comprehensions** instead of loops for cleaner code.  
2. Prefer **enumerate()** over range for loops with index.  
3. Use **f-strings** for formatting instead of `+` concatenation.  
4. Avoid using mutable default arguments in functions.  
5. Follow **PEP 8** style guide for readable, consistent code.  
6. Use **virtual environments** (`venv`) to manage dependencies.  
7. Use **logging** instead of `print()` for debugging in production.  
8. Profile code with `time` or `cProfile` to optimize performance.  
9. Write **docstrings** (`""" """`) to document your functions and classes.  
10. Break large scripts into **modules** for better organization.  

---

## 📌 Final Note  

This repository + README acts as a **complete Python roadmap** with both:  
- **Code files** for practice  
- **Theory** (this README) for reference  

Master the theory, practice the code, and you’ll be fluent in Python. 🚀  

---
