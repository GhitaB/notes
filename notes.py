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
    def do_configuration(self):
        if path.exists(FOLDER_NOTES):
            msg = STATUS_FOLDER_EXISTS
        else:
            try:
                os.makedirs(FOLDER_NOTES)
                msg = STATUS_FOLDER_SUCCESS
            except Exception:
                msg = STATUS_FOLDER_FAIL

        return msg


    def __init__(self, master):

        msg = self.do_configuration()

        self.label_status = ttk.Label(master, text = msg)
        self.label_status.grid(row = 0, column = 0, columnspan = 2)

        # ttk.Button(master, text = "Romania",
        #            command = self.romania_hello).grid(row = 1, column = 0)
        #
        # ttk.Button(master, text = "USA",
        #            command = self.usa_hello).grid(row = 1, column = 1)

    # def romania_hello(self):
    #     self.label.config(text = 'Hello, Romania!')
    #
    # def usa_hello(self):
    #     self.label.config(text = 'Hi, USA!')


def main():

    root = Tk()
    app = NotesApp(root)
    root.title("My notes")
    root.minsize(500, 500)
    root.mainloop()

if __name__ == "__main__": main()
