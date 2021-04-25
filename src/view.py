#!/usr/bin/python3

import pandas as pd
import platform
from tkinter import Tk, StringVar, Label, Button, Entry, Text, END
from tkinter import W
from tkinter.filedialog import askopenfilename
from main import compare

fileUploadDefaultText = "Choose file"
defaultColumnName = "Text"
fullFileName = ""

# Receives a file that has been uploaded. NOTHING is done until the submit
# button has been clicked
def uploadFile(event):
    file = askopenfilename()
    if file:
        global fullFileName
        fullFileName = file
        splitFile = None
        if (platform.system() == 'Windows'):
            splitFile = file.split('\\')
        else:
            splitFile = file.split('/')
        uploadFileButtonText.set(splitFile[len(splitFile)-1])

def tup_to_dict(tup):
    result = {}
    for num in tup:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result

def set_input(text, value):
    text.delete(1.0, END)
    text.insert(END, value)

# Returns true if the string s is a number
# https://stackoverflow.com/q/354038
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def readTextFile(fileName):
    weights = open(fileName, 'r')
    # Reading from the file
    content = weights.readlines()
    list_weights = []
    # Iterating through the content of the file
    for line in content:
        if is_number(line):
            list_weights.append(float(line))
    return list_weights

# Receives a string, analyzes it, and displays the results
def submit(event):
    sumInput = float(sumEntry.get())
    errorInput = float(errorEntry.get())
    df_wp = None
    weights = None
    occurrences = None
    if ".xlsx" in fullFileName:
        df_wp = pd.read_excel(fullFileName)
        df_wp.dropna()
        weights = [float(num) for num in df_wp["Weights"].tolist()]
        occurrences = [float(num) for num in df_wp["Occurrences"].tolist()]
    elif ".txt" in fullFileName:
        raw_weights = readTextFile(fullFileName)
        len_weights = len(raw_weights) / 2
        weights = raw_weights[:int(len_weights)]
        occurrences = raw_weights[int(len_weights):]
    else:
        raise SyntaxError('require either .xlsx or .txt file')

    print(weights)
    print(occurrences)

    results = compare(sumInput, errorInput, weights, occurrences)
    resultsStringBuilder = ''

    for item in results:
        item_to_dict = tup_to_dict(item)
        resultsStringBuilder += (str(sum(list(item))) + '\n')
        resultsStringBuilder += (str(item_to_dict) + '\n\n')
    if resultsStringBuilder == '':
        set_input(resultsLabel, 'No matches found.')
    else:
        set_input(resultsLabel, resultsStringBuilder)

# Initialize all widgets in GUI here
root = Tk()
root.title("Chem Tools")
root.geometry("600x400")

# Row 1 widgets: Sum Label, Sum Input, Sum Submit
sumLabel = Label(root, text="Enter Desired Sum")
sumEntry = Entry(root, width=10)

# Row 2 widgets: Error Label, Error Input, Error Submit
errorLabel = Label(root, text="Enter Margin of Error")
errorEntry = Entry(root, width=10)

# Row 3 widgets: File Label, File Upload, File Submit
uploadFileLabel = Label(root, text="Upload Weights")
uploadFileButtonText = StringVar()
uploadFileButtonText.set(fileUploadDefaultText)
uploadFileButton = Button(root, textvariable=uploadFileButtonText)
uploadFileButton.bind("<Button-1>", uploadFile)
fileSubmitButton = Button(root, text="Submit")
fileSubmitButton.bind("<Button-1>", submit)

# Row 4 widgets: File Analyzer Results Label
resultsLabel = Text(root)
set_input(resultsLabel, 'DO NOT EDIT: Results will appear here.')

# All widgets are organized in a grid here
sumLabel.grid(row=0, column=0, sticky=W)
sumEntry.grid(row=0, column=1)

errorLabel.grid(row=1, column=0, sticky=W)
errorEntry.grid(row=1, column=1)

uploadFileLabel.grid(row=2, column=0, sticky=W)
uploadFileButton.grid(row=2, column=1, sticky=W)

fileSubmitButton.grid(row=2, column=2)

resultsLabel.grid(row=3, column=0, sticky=W)
resultsLabel.place(y=100, width=600, height=400)

if __name__ == "__main__":
    root.mainloop()
