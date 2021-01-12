#!/usr/bin/python3
# Run with $ python3 notes.py

from tkinter import *
from tkinter import ttk
import os.path
from os import path

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
        self.label_status = ttk.Label(master, text = msg)

    def create_editor(self, master):
        """ Set the editor for notes
        """
        T = Text(master, height=10, width=60)
        T.grid(row = 1, column = 0, columnspan = 3)

        Label(master, text="File name:").grid(row = 2, column = 0)

        Entry(master).grid(row = 2, column = 1)

        B = Button(master, text="Add").grid(row = 2, column = 2)


    def __init__(self, master):
        """ The app
        """

        # Initial configuration
        self.update_status(master, "")
        is_ok, msg = self.check_configuration()
        self.update_status(master, msg)
        self.label_status.grid(row = 0, column = 0, columnspan = 3)

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
