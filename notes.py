#!/usr/bin/python3
# Run with $ python3 notes.py

from tkinter import *
from tkinter import ttk
import os.path
from os import path
from datetime import datetime


STATUS_FOLDER_EXISTS = u"Status: Configuration is ok."
STATUS_FOLDER_SUCCESS = u"Status: The folder for notes was created."
STATUS_FOLDER_FAIL = u"Status: Cannot create the folder for notes."
FOLDER_NOTES = "./my-notes/"


class NotesApp:
    """ Keep your notes in a folder, easy to access, search and modify
    """
    def check_configuration(self):
        """ Make sure the folder exists
        """
        if path.exists(FOLDER_NOTES):
            msg = STATUS_FOLDER_EXISTS
            ok = True
        else:
            try:
                os.makedirs(FOLDER_NOTES)
                msg = STATUS_FOLDER_SUCCESS
                ok = True
            except Exception:
                msg = STATUS_FOLDER_FAIL
                ok = False

        return (ok, msg)

    def update_status(self, master, msg):
        """ Show a message as status
        """
        self.label_status.configure(text = msg)

    def save_note(self, master):
        """ On save put the text in the file, in notes folder
        """
        filename = self.entry_filename.get()
        text = self.text_note.get('1.0', 'end')

        note = open(FOLDER_NOTES + filename, "w")
        note.write(text)
        note.close()

        self.update_status(master, "Status: saved " + filename)

    def create_editor(self, master):
        """ Set the editor for notes
        """
        self.text_note = Text(master, height=10, width=60)
        self.text_note.grid(row = 1, column = 0, columnspan = 3)

        self.label_filename = ttk.Label(master, text="File name:")
        self.label_filename.grid(row = 2, column = 0)

        self.entry_filename = ttk.Entry(master)

        now = datetime.now()
        default_filename = now.strftime("%Y_%m_%d__%H_%M_%S.txt")
        self.entry_filename.insert(END, default_filename)
        self.entry_filename.grid(row = 2, column = 1)

        self.button_save = ttk.Button(
                master, text="Save", command = lambda: self.save_note(
                master))
        self.button_save.grid(row = 2, column = 2)


    def __init__(self, master):
        """ The app
        """

        # Initial configuration
        is_ok, msg = self.check_configuration()
        self.label_status = Label(master)
        self.label_status.grid(row = 0, column = 0, columnspan = 3)
        self.update_status(master, msg)

        # Manage notes
        if is_ok:
            self.create_editor(master)


def main():
    root = Tk()
    app = NotesApp(root)
    root.title("My notes")
    root.minsize(500, 500)
    root.mainloop()

if __name__ == "__main__": main()
