from tkinter import *
import os

def skin():
    skinColours = []
    skin = open("skins\\currentskin.txt", "r").read()
    skinDir = (r"skins\\" + skin + r"\\skin.txt")
    for line in open(skinDir):
        skinColours.append(int(line[:3]))
    backgroundColour = "#%02x%02x%02x" % (skinColours[0],
                                          skinColours[1],
                                          skinColours[2])
    foregroundColour = "#%02x%02x%02x" % (skinColours[3],
                                          skinColours[4],
                                          skinColours[5])
    #formats the user's RGB choice of colour to something
    #that tkinter understands
    skinFont = open(r"skins\\" + skin + r"\\skinfont.txt").read().split("\n")

    if len(skinFont) == 2:
        skinFont.append("")
    elif len(skinFont) < 1:
        skinFont.append("", "", "")
    
    return {"bgColour":backgroundColour,
            "fgColour":foregroundColour,
            "skinFont":skinFont}

def saveFile():
    savingFile = open(str(saveBoxName.get("1.0", 'end-1c')), "w")
    text = textBox.get("1.0", 'end-1c')
    savingFile.write(str(text)) #overwrites old file
    savingFile.close

def openFile():
    file = open(str(saveBoxName.get("1.0", 'end-1c')), "r")
    myText = file.read()
    textBox.delete(1.0, END) #clears text box
    textBox.insert(0.0, myText)

def numberExist():
    numberExist = "0"
    newFile(numberExist)

def newFile(newNumber):
    if os.path.isfile("Untitled" + str(newNumber) + ".txt"):
        newNumber = (int(newNumber) + 1)
        str(newNumber)
        newFile(newNumber)
    else:
        saveBoxName.delete(1.0, END) #clears file name
        textBox.delete(1.0, END) #clears text box
        saveBoxName.insert(INSERT, "Untitled" + str(newNumber) + ".txt")
        #inserts unique name in save box

def close():
    quit()

def help():
    saveBoxName.delete(0.0, END)
    saveBoxName.insert(0.0, "README.txt")
    openFile()
    
def countWords(event):
    text = str(textBox.get("1.0", "end-1c").split())
    if text == "":
        wordCount = 0
        charCount = 0
    else:
        wordCount = 0
        for char in text:
            if char.isspace():
                wordCount+=1
        charCount = len(textBox.get("1.0", "end-1c".split("\n"))) + 1
        wordCount+=1
    wordCount = ("Words: " + str(wordCount) + ", Characters: " + str(charCount))
    wordCountText.set(str(wordCount))

skinInfo = skin()

if __name__ == "__main__":

    master = Tk()
    master.wm_title("Text Editor")

    menuBar = Menu(master) #makes menu bar

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="New", command=numberExist)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Quit", command=close)
    menuBar.add_cascade(label="File", menu=fileMenu)

    menuBar.add_command(label="Help", command=help)

    master.config(menu=menuBar)

    topFrame = Frame(master)
    topFrame.pack(side="top", fill="both")
    textFrame = Frame(master)
    textFrame.pack(side="top", expand=True, fill="both")

    saveBoxName = Text(topFrame, width=20, height=1,
                       background=skinInfo["bgColour"],
                       foreground=skinInfo["fgColour"])
    saveBoxName.insert(END, "enterfilename.txt")
    saveBoxName.grid(row=0, column=0)

    wordCountText = StringVar()
    wordCountText.set("Words: 0, Characters: 0")

    wordCountLabel = Label(topFrame, textvariable=wordCountText)
    wordCountLabel.grid(row=0, column=1)
    
    scrollTextBox = Scrollbar(textFrame)
    scrollTextBox.pack(side=RIGHT, fill=Y)

    textBox = Text(textFrame, background=skinInfo["bgColour"],
                   foreground=skinInfo["fgColour"],
                   yscrollcommand=scrollTextBox.set,
                   font=skinInfo["skinFont"])
    master.grid_columnconfigure(0, weight=1)
    textBox.pack(expand=True, fill=BOTH)
    scrollTextBox.config(command=textBox.yview)
    
    textBox.bind("<Key>", countWords)

    master.mainloop()

