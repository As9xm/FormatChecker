import filetype
from pathlib import Path
from tkinter import *
from tkinter import filedialog

#Functionality
def functionality():
    global path
    file_chooser = filedialog.askopenfilename()
    if file_chooser:
        path = Path(file_chooser)
        result1.config(text=f"{path.name}")
    else:
        result1.config(text=f"no file has been chosen")    
    


def checker():
        if path is None:
              result1.config(text="There is no file to check")
              return
        
        try:
              with open(path, "rb") as f:
                    kind = filetype.guess(f.read(265))

                    if kind is not None:
                         result1.config(text=f"""the file is checked!
                                        name: {path}
                                        type: {kind.mime}
                                        expected format: {kind.extension}""")
                    else:
                         result1.config(text=f"""Name: {path} Error format not found""")
        except Exception as e:
             result1.config(text=f"Error while checking: {str(e)}")                      
                   
            
            


#Window Things
window = Tk()
window.geometry("800x600")
window.title("Format Checker")


button = Button(window, text="Choose File", command=functionality)
button.place(x=355, y=200)

welcomer = Label(window, text="Welcome to File Checker!")
welcomer.pack()

result1 = Label(window, text="There is no file has been chosen")
result1.pack()


button2 = Button(window, text="Check", command=checker)
button2.place(x=370, y=120)


window.mainloop()