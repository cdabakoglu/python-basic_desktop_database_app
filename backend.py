import sqlite3

# Connection to database if database doesn't exist it will create one.
def connection():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS movies (id INTEGER PRIMARY KEY, title TEXT, genre TEXT, imdb DECIMAL, user DECIMAL)")
    conn.commit()
    conn.close()

# Adding a Movie to Database
def add_item(title, genre, imdb, user):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movies VALUES(NULL,?,?,?,?)", (title, genre, imdb, user))
    conn.commit()
    conn.close()

# Show all items in the list
def view_all():
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    items = cursor.fetchall()
    conn.close()
    return items

# Search a Movie
def search_item(title=""):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE title LIKE ?", ('%'+title+'%',))
    items = cursor.fetchall()
    conn.close()
    return items

# Delete a Movie
def delete_item(id):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (id,))
    conn.commit()
    conn.close()

# Update a Movie's Info
def update_item(id, title, genre, imdb, user):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE movies SET title=?, genre=?, imdb=?, user=? WHERE id=?", (title,genre,imdb,user,id))
    conn.commit()
    conn.close()

connection()


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu