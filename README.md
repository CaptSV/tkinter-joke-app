# Joke Generator


A simple Python desktop application that generates random jokes.

---

## Description

This project is a simple joke generator built with the Tkinter library for Python. It provides a minimalistic graphical user interface (GUI) with a single button that, when clicked, fetches and displays a random joke. The project serves as an excellent example of a complete, small-scale application demonstrating fundamental GUI programming concepts and API interaction in Python.

---

## Getting Started

### Dependencies
* **Python 3.x**
* **`tkinter`**: Python's standard GUI library (usually included with Python installation).
* **`pyjokes`**: A Python library for generating programmer-related jokes.

### Installing

1.  **Clone the Repository:**
    Download or clone this repository to your local machine.
    ```bash
    git clone https://github.com/CaptSV/tkinter-joke-app.git
    ```
2.  No specific modifications to files or folders are needed for initial setup.

### Executing program

1.  **Open your terminal or command prompt.**
2.  **Navigate to the project directory** where the main script (`main.py`) is located.
    ```bash
    cd /path/tkinter-joke-app-folder
    ```
3.  **Run the script:**
    ```bash
    python main.py
    ```
---

## Help

* **ModuleNotFoundError**: If you get an error like "ModuleNotFoundError: No module named 'pyjokes'", it means the pyjokes library is not installed. Re-run the installation command: ```pip install pyjokes```.

* **GUI not appearing**: Ensure you are running the script from a standard terminal. Some IDEs might have issues displaying the Tkinter GUI correctly.

---
## Authors

Simon Valenzuela  
[GitHub](https://github.com/CaptSV)  
[LinkedIn](https://www.linkedin.com/in/simonrpvalenzuela/)

---
## Version History

* 0.1
    * Initial Release: A complete, functional GUI application that generates and displays random jokes.
---
## License

This project is licensed under the [MIT License](https://opensource.org/license/mit)  - see the LICENSE.md file for details

---
## Acknowledgments

* This project was developed as part of the [ZTM - Complete Python Developer course](https://www.udemy.com/course/complete-python-developer-zero-to-mastery/).
* [Tkinter](https://docs.python.org/3/library/tkinter.html) for providing the core GUI framework.
* [Pyjokes(https://pypi.org/project/pyjokes/)] library for the joke content.