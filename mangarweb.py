#1 line :)
#We're using TKK bootstrap here cuz it makes it look Professional. Not like any of my COMMENTS are professional. anyways.
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from bs4 import BeautifulSoup

# Create the main application window
root = ttk.Window(themename="cosmo")
root.title("Base")
root.geometry("400x300")

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
        # Read the existing content of the file
        try:
            with open("output1.html", "r", encoding="utf-8") as file:
                soup = BeautifulSoup(file, "html.parser")
        except FileNotFoundError:
            soup = BeautifulSoup("<html><head></head><body></body></html>", "html.parser")
        
        # Create the "div" tag
        div_tag = soup.new_tag("div")
        DivClass = textboxClassDiv.get()
        DivID = textboxDivID.get()
        div_tag["class"] = DivClass
        div_tag["id"] = DivID
        soup.body.append(div_tag)
        

        # Save the updated HTML to the file
        with open("output1.html", "w", encoding="utf-8") as file:
            file.write(soup.prettify())
        
        # Print the HTML to the console
        print(soup.prettify())

    button = ttk.Button(divsetup, text="Submit", bootstyle=SUCCESS, command=makediv)
    button.pack(pady=20)
#fifty lines! :)
DIVBUTTON = ttk.Button(root, text="Create Div", bootstyle=SUCCESS, command=creatediv)
DIVBUTTON.pack(pady=20)

from bs4 import BeautifulSoup
import tkinter as tk

def seedivs():
    divinvestigation = tk.Tk()
    divinvestigation.title("See Divs")
    divinvestigation.geometry("400x300")
    
    with open("output1.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        div_list = [{"class": div.get("class", []), "id": div.get("id")} for div in soup.find_all("div")]
        # Create a dropdown with div IDs
        div_ids = [div["id"] for div in div_list if div["id"]]
        divclass = [div["class"] for div in div_list if div["id"]]
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
         
        overalltext = ["Headings","Paragraphs"]
        Headngs = ["h1","h2","h3","h4","h5","h6"]
        Paragraph = ["p","a","ul","b","i","u"]

        dropdowncontent = ttk.Combobox(addcontent, values=overalltext, width=25)
        dropdowncontent.set("text.")  # Default text
        dropdowncontent.pack(pady=20)

        def nextbutton():
            OPTION = dropdowncontent.get()
            #100 lines :D
            addcontent1 = tk.Tk()
            addcontent1.title("Add Content")
            addcontent1.geometry("400x300")
            if OPTION == "Headings":
                dropdownheading = ttk.Combobox(addcontent1, values=Headngs, width=25)
                dropdownheading.set("Select a heading :)")  # Default text
                dropdownheading.pack(pady=20)
                textboxContentheading = ttk.Entry(addcontent1)
                textboxContentheading.pack(pady=20)
            if OPTION == "Paragraphs":
                dropdownparagraphs = ttk.Combobox(addcontent1, values=Paragraph, width=25)
                dropdownparagraphs.set("Select a paragraph")  # Default text
                dropdownparagraphs.pack(pady=20)
                textboxContentparagraph = ttk.Entry(addcontent1)
                textboxContentparagraph.pack(pady=20)
            def submitbutton(soup=soup):
                nonlocal div_ids
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
                    divtag = soup.find("div", id=selectedid)
                    p_tag = soup.new_tag(dropdownparagraphs.get())
                    p_tag.string = (textboxContentparagraph.get())
                    divtag.append(p_tag)
                    with open("output1.html", "w", encoding="utf-8") as file:
                        file.write(soup.prettify())

            button = ttk.Button(addcontent1, text="submit", bootstyle=SUCCESS, command=submitbutton)
            button.pack(pady=20)

        button = ttk.Button(addcontent, text="continue", bootstyle=SUCCESS, command=nextbutton)
        button.pack(pady=20)

    button = ttk.Button(divinvestigation, text="add content", bootstyle=SUCCESS, command=addcontent)
    button.pack(pady=20)

        


        

 #this is jerry --> :((: his mother was a :) face, and his dad was a :( face.(yes i got a little bored. lets get back to work. )

seedivbutton = ttk.Button(root, text="See Div", bootstyle=SUCCESS, command=seedivs)

seedivbutton.pack(pady=20)


root.mainloop()
#:((:|    <--- Dont talk to Jerry. He's GROUNDED FOR EATING PAVEMENT >:( 

#150 lines.
#  and make sure to add thse tags: <h1>, <h2>, <h3>, | <h4>, <h5>, <h6>,
# The next day, add these ones: <p>, <a>,<img>,<ul>

#:( jerrys dad is happy. sadly, he can not show it since he is permenantly a :( face.
#Jerry still cant eat pavement. 
