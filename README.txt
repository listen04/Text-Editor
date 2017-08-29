This is a text editor that I wrote in Python 3 with tkinter! It has
a few features:

- You can save files
- You can open and edit files
- You can create new files
- It's possible to create custom skins, which can change the colour of the program and the font, font size and font style
- It has a word counter
- It has a character counter

A quick guide on opening files:

- type in the file path and name (e.g. C:\hi\text.txt) into the box below the File menu
- File -> Open
- done

A quick guide to making skins and changing them:

- to make a skin:
- go to the folder where the Text Editor program is
- go into the skin folder
- make a folder, name the folder what you want your skin name to be
- go back to the skin folder
- open the folder named "template"
- copy the "skin" and "skinfont" files
- paste them into the folder you made earlier
- do NOT rename the files, otherwise they won't work
- open the "skin" file in the folder you made
- the first three numbers, each with their own lines, corrospond to the red, green and blue of an RGB colour code thing for the background of the program. Replace these numbers with anything between (and including) 000 and 255.
- the second set of numbers, are for the red, green and blue of the foreground (the text colour). Replace these the same why you did the last ones.
- save the file and close it
- open the "skinfont" file
- put the font name you want on the first line
- put the size you want on the second
- put the style you want (bold, italic, underline or overstrike [all lowercase]) on the third line. You CAN leave this blank if you want the regular style.
- save and close the file
- go back to the skins folder
- open the "currentskin" file
- replace what's there with the name of the folder you names earlier, e.g. the one with the skin files in it.
- save and close.
- open Text Editor.
- done!

