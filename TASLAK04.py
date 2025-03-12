# V 0.4
#1 line :)
#We're using TKK bootstrap here cuz it makes it look Professional. Not like any of my COMMENTS are professional. anyways.
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from bs4 import BeautifulSoup, Comment
from tkinter import filedialog

try:
    print("created")
    with open("output1.html", "r", encoding="utf-8") as file:
        print("created0")
        soup = BeautifulSoup(file, "html.parser")
        print("created1")
except FileNotFoundError:
        print("created2")
        soup = BeautifulSoup("<html><head></head><body></body></html>", "html.parser")
        print("created3")
        
        with open("output1.html", "w", encoding="utf-8") as file:
            file.write(soup.prettify())
# Create the main application window
root = ttk.Window(themename="cosmo")
root.title("Base")
root.geometry("400x300")
selectedid = None
div_ids = []
# The script for creating a div.
def creatediv():
    # Sets up the window
    divsetup = ttk.Window(themename="cosmo")
    divsetup.title("Create Div")
    divsetup.geometry("400x300")

    # Class entry box
    textboxClassDiv = ttk.Entry(divsetup)
    textboxClassDiv.pack(pady=20)
    # ID entry box
    textboxDivID = ttk.Entry(divsetup)
    textboxDivID.pack(pady=20)
    
    # Function to create the div
    def makediv():
        print("starting Makediv")

        # Read the existing content of the file

        # Create the "div" tag
        div_tag = soup.new_tag("div")
        print(div_tag)
        DivClass = textboxClassDiv.get()
        print(DivClass)
        DivID = textboxDivID.get()
        print(DivID)
        div_tag["class"] = DivClass
        print("added class")
        div_tag["id"] = DivID
        print("added id")
        soup.body.append(div_tag)
        
        with open("output1.html", "w", encoding="utf-8") as file:
            print("opening file")
            file.write(soup.prettify())
            print("writing file")
        # Save the updated HTML to the file

        
        # Print the HTML to the console
        print(soup.prettify())

    button = ttk.Button(divsetup, text="Submit", bootstyle=SUCCESS, command=makediv)
    button.pack(pady=20)
#fifty lines! :)
DIVBUTTON = ttk.Button(root, text="Create Div", bootstyle=SUCCESS, command=creatediv)
DIVBUTTON.pack(pady=20)

from bs4 import BeautifulSoup
import tkinter as tk
def extractdivs():
    global div_ids
    with open("output1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        div_list = [{"class": div.get("class", []), "id": div.get("id")} for div in soup.find_all("div")]
        # Create a dropdown with div IDs
        div_ids = [div["id"] for div in div_list if div["id"]]


def seedivs():
    divinvestigation = tk.Tk()
    divinvestigation.title("See Divs")
    divinvestigation.geometry("400x300")
    global div_ids
    with open("output1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        # div_list = [{"class": div.get("class", []), "id": div.get("id")} for div in soup.find_all("div")]
        # # Create a dropdown with div IDs
        # div_ids = [div["id"] for div in div_list if div["id"]]
        # divclass = [div["class"] for div in div_list if div["id"]]
        dropdown = ttk.Combobox(divinvestigation, values=div_ids, width=25)
        print("Extracted Div IDs:", div_ids)
        dropdown.set("Select a div :)")  # Default text
        dropdown.pack(pady=20)

        # Label to display the content of the selected div
        content_label = ttk.Label(divinvestigation, text="", wraplength=300)
        content_label.pack(pady=20)

        def showdivcontent(event):
            with open("output1.html", "r", encoding="utf-8") as file:
                src = file.read()
            soup = BeautifulSoup(src, 'html.parser')
            global selectedid
            selectedid = dropdown.get()
            print(f"Selected Div ID: {selectedid}")
            selecteddiv = soup.find("div", id=selectedid)
            print(f"Selected Div Raw: {selecteddiv}")
            if selecteddiv:   
                divcontent = selecteddiv.decode_contents().strip()  # Extract inner content
                print(f"Extracted Content: {divcontent}")
                
                if divcontent:
                    content_label.config(text=divcontent)
                else:
                    content_label.config(text="No content found in the selected div.")
            else:
                print("No div found with the slected ID.")
                content_label.config(text="No div found with the selected ID.")
        # Bind the dropdown selection change to the show_div_content function
        dropdown.bind("<<ComboboxSelected>>", showdivcontent)

    def addcontent():
        addcontent = tk.Tk()
        addcontent.title("Add Content")
        addcontent.geometry("400x300")
         
        overalltext = ["Headings","Paragraphs","Fonts"]
        overallvisuals =["Backgrounds","Images"]
        Headngs = ["h1","h2","h3","h4","h5","h6"]
        Paragraph = ["p","a","ul","b","i","u"]
        Backgrounds = ["background-color","background-image"]
        Images = ["img"]
        font = ["font-size","font-weight",]

        dropdowncontent = ttk.Combobox(addcontent, values=overalltext, width=25)
        dropdowncontent.set("text.")  # Default text
        dropdowncontent.pack(pady=20)

        dropdowncontent1 = ttk.Combobox(addcontent, values=overallvisuals, width=25)
        dropdowncontent1.set("images.")  # Default text
        dropdowncontent1.pack(pady=20)

        def nextbutton():
            OPTION = dropdowncontent.get()
            if OPTION == "text.":
                OPTION = dropdowncontent1.get()
            #100 lines :D
            addcontent1 = tk.Tk()
            addcontent1.title("Continue")
            addcontent1.geometry("400x300")
            #It seems to not be reading the options from here
            print("OPTION", OPTION)
            if OPTION == "Headings":
                print("hEADINGS")
                dropdownheading = ttk.Combobox(addcontent1, values=Headngs, width=25)
                dropdownheading.set("Select a heading :)")  # Default text
                dropdownheading.pack(pady=20)
                textboxContentheading = ttk.Entry(addcontent1)
                textboxContentheading.pack(pady=20)
            if OPTION == "Paragraphs":
                print("Paragraphs")
                dropdownparagraphs = ttk.Combobox(addcontent1, values=Paragraph, width=25)
                dropdownparagraphs.set("Select a paragraph")  # Default text
                dropdownparagraphs.pack(pady=20)
                textboxContentparagraph = ttk.Entry(addcontent1)
                textboxContentparagraph.pack(pady=20)
            if OPTION == "Fonts":
                print("FONTS")
                print(OPTION)
                textcolours = ["red","blue","green","purple","black","white"] #I speak American English, but i think the the British speaking makes more sense. Its not "Col-or" Its "Colour" 
                fontfamily = ttk.Entry(addcontent1)
                fontfamily.insert(0, "Font Family")
                fontfamily.pack(pady=20)
                colourselect = ttk.Combobox(addcontent1, values=textcolours, width=25)
                colourselect.set("select a colour")  # Default text
                colourselect.pack(pady=20)      
                Fontname = ttk.Entry(addcontent1)
                Fontname.insert(0, "Font Name")
                Fontname.pack(pady=20)
            if OPTION == "Images":
                print("skibdi simga")
                file_path = filedialog.askopenfilename(title="Select a file")  # Prints the selected file path
                print(file_path)
                with1 = ttk.Entry(addcontent1)
                with1.insert(0, "with of image")
                with1.pack(pady=20)
                altxt = ttk.Entry(addcontent1)
                altxt.insert(0, "alt text")
                altxt.pack(pady=20)
                print("done")

                #color: red; font-family: 'Times New Roman', serif;"
            def submitbutton(soup=soup):
                selectedid = dropdown.get()
                print("DIV IDS inside submit button:", div_ids)
                if OPTION == "Headings":
                    divtag = soup.find("div", id=selectedid)
                    h_tag = soup.new_tag(dropdownheading.get())
                    h_tag.string = (textboxContentheading.get())
                    divtag.append(h_tag)
                
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())

                if OPTION == "Paragraphs":
                    print
                    divtag = soup.find("div", id=selectedid)
                    p_tag = soup.new_tag(dropdownparagraphs.get())
                    p_tag.string = (textboxContentparagraph.get())
                    divtag.append(p_tag)
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())
                if OPTION == "Fonts":
                    print("fonts")
                    nonlocal colourselect
                    nonlocal fontfamily
                    nonlocal Fontname

                    textcolour = colourselect.get()
                    fontfam = fontfamily.get()
                    flnoidl = Fontname.get() #flnoidl = font legal name on its driver liscense
                    div = soup.find("div", id=selectedid)
                    div['style']= f"color: {textcolour}; font-family: '{fontfam}','{flnoidl}';"
                    colournotes = Comment(f"color: {textcolour}; font-family: '{fontfam}','{flnoidl}';")
                    div.append(colournotes)
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())     
                
                if OPTION == "Images":
                    nonlocal with1
                    nonlocal altxt
                    altxt = altxt.get()
                    with1 = with1.get()
                    div = soup.find("div", id=selectedid)
                    imgtag = soup.new_tag("img", src=file_path, alt=altxt, width=with1)
                    div.append(imgtag)
                    
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())


            button = ttk.Button(addcontent1, text="submit", bootstyle=SUCCESS, command=submitbutton)
            button.pack(pady=20)

        button = ttk.Button(addcontent, text="continue", bootstyle=SUCCESS, command=nextbutton)
        button.pack(pady=20)

    button = ttk.Button(divinvestigation, text="add content", bootstyle=SUCCESS, command=addcontent)
    button.pack(pady=20)

        


        

 #this is jerry --> :((: his mother was a :) face, and his dad was a :( face.(yes i got a little bored. lets get back to work. )

def delete():
    global div_ids
    print("skibdi")
    Deletewindow = ttk.Window(themename="cosmo")
    Deletewindow.title("Create Div")
    Deletewindow.geometry("400x300")
    dropdown = ttk.Combobox(Deletewindow, values=div_ids, width=25)
    dropdown.set("Select a div to delete")  # Default text
    dropdown.pack(pady=20)

    def deletediv():
        with open("output1.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
        selecteddiv = dropdown.get()
        for div in soup.find_all("div", id=selecteddiv): 
            div.decompose()
        with open("output1.html", "w", encoding="utf-8") as file:
            file.write(str(soup))
        print("Deleted div with ID:", selecteddiv)
        print(soup.prettify())
    
    deletebutton1 = ttk.Button(Deletewindow, text="Delete Div", bootstyle=SUCCESS, command=deletediv)
    deletebutton1.pack(pady=20) 


extractdivs()
# Create a button to delete the selected div
print("EXtracted div ids".upper(), div_ids)#.upper() is a method that makes the string uppercase.
deletebutton = ttk.Button(root, text="Delete Div", bootstyle=SUCCESS, command=delete)
deletebutton.pack(pady=20)

seedivbutton = ttk.Button(root, text="See Div", bootstyle=SUCCESS, command=seedivs)

seedivbutton.pack(pady=20)




#ALWAYS REMEMBER TO READ THE CODE FULLY! DONT SKIM OVER IT. YOU MIGHT MISS SOMETHING IMPORTANT.
#ALSO, DONT EAT PAVEMENT. ITS NOT GOOD FOR YOU.
#200 lines. Jerry is at school. Mr Shocked-Face  is teaching
#                              | (::( |
#                              | _____
#                              
#                            __________
#                           |          |
#                           |  :0      |
#                           ___________
root.mainloop()
#:((:|    <--- Dont talk to Jerry. He's GROUNDED FOR EATING PAVEMENT >:( 

#150 lines.
#250 lines :D
#300 lines :D
#next day, DONT EAT PAVEMENT JERRY. HES UNGROUNDED BUT WE JUST WANNA LET HIM KNOW.
# Also,fix the addcontent1 window,  fix the delete button  as well as finish making the font feature.
#We will make sure it deletes all css realated to the div in the next update.
#:( jerrys dad is happy. sadly, he can not show it since he is permenantly a :( face.
#Jerry still cant eat pavement. 
