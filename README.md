# 🧠 Kax Programming Language

**Kax** is a small, lightweight, and easy-to-understand programming language inspired by early BASIC interpreters.  
It’s written in **Python** and designed to be simple, readable, and beginner-friendly — just like coding in the 1980s!

---

## 🚀 Features

✅ BASIC-style syntax  
✅ Simple interpreter written in pure Python (no dependencies)  
✅ Colored error messages (ANSI-based, no libraries)  
✅ Line-number-based GOTO  
✅ PRINT command for output  
✅ LET command for variables  

---

## 📄 Example Program (`example.kx`)

```basic
LET A = 42
PRINT "HELLO WORLD"
PRINT A
```

### Output
```
HELLO WORLD
42
```

---


## ⚙️ Running a Program

1. Save your program as a `.kx` file (for example, `test.kx`).
2. Run it using the Kax interpreter:

```bash
python kax.py test.kx
```
If no file is provided, or the file doesn’t exist, the interpreter will show a friendly error.


## 🧱 Project Structure

```
kax/
├── kax.py          # The main interpreter
├── example.kx      # Example program
└── README.md       # You are here!
```


## ⚖️ License

This project is open-source under the **MIT License**.  
You’re free to modify, share, and build upon it — just credit the original author.

---

## 🧑‍💻 Author

Created by **Bartosz Szczepkowski**  
Feel free to share ideas or improvements!
