from tkinter import *
import backend

# This function get clicked item as a tuple
def get_selected_item(e):
    try:
        global selectedTuple
        index = movieList.curselection()[0]
        selectedTuple = movieList.get(index)
        entryTitle.delete(0, END)
        entryTitle.insert(END, selectedTuple[1])
        entryGenre.delete(0, END)
        entryGenre.insert(END, selectedTuple[2])
        entryImdb.delete(0, END)
        entryImdb.insert(END, selectedTuple[3])
        entryUser.delete(0, END)
        entryUser.insert(END, selectedTuple[4])
    except IndexError:
        pass

# This commands is used for calling functions from backend.py. Commands are used by buttons.
def view_command():
    movieList.delete(0, END)
    for i in backend.view_all():
        movieList.insert(END, i)

def search_command():
    movieList.delete(0, END)
    for i in backend.search_item(titleText.get()):
        movieList.insert(END, i)

def add_command():
    backend.add_item(titleText.get(), genreText.get(), imdbText.get(), userText.get())
    movieList.delete(0, END)
    movieList.insert(END, (titleText.get(), genreText.get(), imdbText.get(), userText.get()))

def delete_command():
    backend.delete_item(selectedTuple[0])
    movieList.delete(0, END)
    for i in backend.view_all():
        movieList.insert(END, i)

def update_command():
    backend.update_item(selectedTuple[0], titleText.get(), genreText.get(), imdbText.get(), userText.get())
    movieList.delete(0, END)
    for i in backend.view_all():
        movieList.insert(END, i)

# Clean all entry areas
def clean_command():
    entryTitle.delete(0, END)
    entryGenre.delete(0, END)
    entryImdb.delete(0, END)
    entryUser.delete(0, END)
    entryImdb.insert(END, 0.0)
    entryUser.insert(END, 0.0)
    movieList.delete(0, END)

window = Tk() # Creating window for the program

window.wm_title("My Movie Database")

# Creating Labels
labelTitle = Label(window, text="Title", font="Times 12 bold")
labelTitle.grid(row=0, column=0)
labelGenre = Label(window, text="Genre", font="Times 12 bold")
labelGenre.grid(row=0, column=3)
labelImdb = Label(window, text="Imdb Rating", font="Times 12 bold")
labelImdb.grid(row=1, column=0)
labelUser = Label(window, text="User Rating", font="Times 12 bold")
labelUser.grid(row=1, column=3)

# Adding some empty labels just for adding space between the labels above
labelSpace1 = Label(window, text="       ")
labelSpace1.grid(row=0, column=2)
labelSpace2 = Label(window, text="       ")
labelSpace2.grid(row=1, column=2)

# Creating Text Boxes
titleText = StringVar()
entryTitle = Entry(window, textvariable=titleText, bg="#77CEF6")
entryTitle.grid(row=0, column=1)
genreText = StringVar()
entryGenre = Entry(window, textvariable=genreText, bg="#77CEF6")
entryGenre.grid(row=0, column=4)
imdbText = DoubleVar()
entryImdb = Entry(window, textvariable=imdbText, bg="#F2F24A")
entryImdb.grid(row = 1, column = 1)
userText = DoubleVar()
entryUser = Entry(window, textvariable=userText, bg="#F2F24A")
entryUser.grid(row=1, column=4)

# Create ListBox for Movie List
movieList = Listbox(height=15, width=50, bd=4, relief='groove', selectmode='extended')
movieList.grid(row=2, column=0, rowspan=6, columnspan=2)

# Create a Scroll Bar to scroll the listbox
scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)
movieList.configure(yscrollcommand=scroll.set)
scroll.configure(command=movieList.yview)

movieList.bind('<<ListboxSelect>>',get_selected_item)

# Create Buttons
buttonAll = Button(window, text="View All Movies", width=20, command=view_command)
buttonAll.grid(row=2, column=3, columnspan=5)
buttonSearch = Button(window, text="Search", width=20, command=search_command)
buttonSearch.grid(row=3, column=3, columnspan=5)
buttonAdd = Button(window, text="Add Movie", width=20, command=add_command)
buttonAdd.grid(row=4, column=3, columnspan=5)
buttonUpdate = Button(window, text="Update Movie", width=20, command=update_command)
buttonUpdate.grid(row=5, column=3, columnspan=5)
buttonDelete = Button(window, text="Delete Movie", width=20, command=delete_command)
buttonDelete.grid(row=6, column=3, columnspan=5)
buttonClose = Button(window, text="Clean", width=20, command=clean_command)
buttonClose.grid(row=7, column=3, columnspan=5)

window.mainloop() # It is necessary because without this program is run and close immediately.


# Caner Dabakoglu
# GitHub: https://github.com/cdabakoglu