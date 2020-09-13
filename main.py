from tkinter import *
from functools import partial
import os, sys

class fil_profile:
    def __init__(self, root, file, name):
        self.root = root
        self.file = file
        self.name = name
        self.root_and_file = os.path.join(root, file)

alle_filene = []
nummer_now = 1
allowed_files = ['.docx','.pdf','.pptx','.txt','.py','.cpp','.html','.js','.css']
roots = ['/Users/sebastian/Documents','/Users/sebastian/Desktop','/Users/sebastian/Downloads']

for root in roots:
    for subdir, dirs, files in os.walk(root):
        for file in files:
            filename, file_extension = os.path.splitext(file)
            if file_extension in allowed_files:
                nummer_now += 1
                class_name = fil_profile(subdir,file, filename)
                alle_filene.append(class_name)

def _from_rgb(rgb):
    return("#%02x%02x%02x" % rgb)

def main_win():
    global ting_å_soke_etter, alle_labels, root
    root = Tk()
    root.geometry('525x250+250+250')
    root.title('søke etter fil')
    root.config(background=_from_rgb((19,19,19)))
    root.resizable(width = False, height = False)
    root.attributes("-alpha", 0.95)

    #entry
    ting_å_soke_etter = Entry(root,width=12)
    ting_å_soke_etter.place(x=400,y=15)
    ting_å_soke_etter.config(borderwidth=0,cursor='xterm')
    ting_å_soke_etter.bind('<Return>', soke)

    #labels
    Label_1,Label_2,Label_3,Label_4,Label_5,Label_6,Label_7 = Label(),Label(),Label(),Label(),Label(),Label(),Label()
    alle_labels = (Label_1,Label_2,Label_3,Label_4,Label_5,Label_6,Label_7)
    l = [x for x in range(50,200,25)]
    for label in range(len(alle_labels)):
        alle_labels[label].config(background=_from_rgb((19,19,19)), foreground='white')
    for nummer, y_cord in enumerate(l):
        alle_labels[nummer].place(x=10,y=y_cord)
    root.mainloop()

def finne_fil(num, event):
    os.system(f"open '{num}'")

def soke(event):
    global alle_filene

    label_num = 0
    liste_over_apps = ["",".py", ".txt", ".docx", ".pdf", ".html", ".css", ".js", '.cpp','.pptx']

    for labels in alle_labels:
        labels.config(text='')
        labels.config(background=_from_rgb((19,19,19)))

    for file in alle_filene:
        if file.name.lower() == str(ting_å_soke_etter.get()).lower():
            liste_for_filer, liste_2, liste_3 = [str(file.root)], [], []
            for a in liste_for_filer:
                output = ""
                for b in reversed(a):
                    if b != '–':
                        output += output.join(b)
                    else: break
                liste_2.append(output)
            for letter in liste_2:
                output = ""
                for lettor in reversed(letter):
                    output += output.join(lettor)
                liste_3.append(output)
            alle_labels[label_num].config(text=str(file.file)+'      '+str(liste_3[0]))
            alle_labels[label_num].config(background=_from_rgb((37,37,38)))
            alle_labels[label_num].bind('<Button-1>', partial(finne_fil,file.root_and_file))
            label_num += 1
    if str(ting_å_soke_etter.get()) == '/amount of items':
        alle_labels[0].config(text=len(alle_filene))
        alle_labels[0].config(background=_from_rgb((37,37,38)))
    if str(ting_å_soke_etter.get()) == '/exit':
        sys.exit()
    try:
        ting_å_soke_etter.delete(0, END)
    except: pass

if __name__ == "__main__":
    main_win()
