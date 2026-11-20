# 🎬 CineMatch – Movie Manager

CineMatch is a Python-based command-line application that allows users to manage, search, filter, sort, and discover movies. It uses JSON for data storage, so movie records remain saved even after the program is closed.

## ✨ Features

- **Search Movies:** Find movies by title, including partial matches.
- **Filter Movies:** Filter movies by genre and minimum rating.
- **Sort Movies:** Sort movies by rating or release year.
- **Add Movies:** Add new movies with title, genre, rating, and release year.
- **Delete Movies:** Delete a selected movie, with confirmation before deletion.
- **Update Ratings:** Update the rating of an existing movie.
- **Display Movies:** View all stored movie records.
- **Recommend Movies:** Get movie recommendations based on genre and a minimum rating of 7.

## 🛠️ Technologies Used

- Python
- JSON
- `datetime` module

## 📂 Project Structure

```text
CineMatch/
│
├── main.py
├── movies.json
└── README.md
```

`movies.json` is created when movie data is saved.

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Clone this repository:

   ```bash
   git clone https://github.com/mdjunaidarifin016/cinematch.git
   ```

3. Navigate to the project directory:

   ```bash
   cd CineMatch
   ```

4. Run the application:

   ```bash
   python main.py
   ```

## 💾 Data Storage

CineMatch stores movie records in a JSON file. This allows the application to load previously saved movies whenever it starts.

## 🎯 Learning Objectives

This project helped me practice:

- Python functions and loops
- Lists and dictionaries
- List comprehensions and sorting concepts
- File handling
- JSON serialization and deserialization
- Exception handling
- User input validation
- Working with dates and data validation

## 🔮 Future Improvements

- Add a graphical user interface.
- Improve input validation and error handling.
- Add movie recommendations based on multiple preferences.
- Introduce unique movie IDs.
- Add more advanced search and filtering options.

---

**CineMatch** – Your personal movie collection manager.