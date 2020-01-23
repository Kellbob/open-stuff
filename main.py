from tkinter import *
from functools import partial
import os

skole_fritid_bool = True

def _from_rgb(rgb):
    return("#%02x%02x%02x" % rgb)

def skole_fritid(event):
    global skole_fritid_bool
    if skole_fritid_bool == True:
        skole_fritid_bool = False
        skole_eller_fritid.config(text='Fritid')
    else:
        skole_fritid_bool = True
        skole_eller_fritid.config(text='skole')

def main_win():
    global ting_å_søke_etter, alle_labels, skole_eller_fritid
    root = Tk()
    root.geometry('525x250+250+250')
    root.title('søke etter fil')
    root.config(background=_from_rgb((19,19,19)))

    #entrys
    ting_å_søke_etter = Entry(root,width=12)
    ting_å_søke_etter.place(x=400,y=15)
    ting_å_søke_etter.config(borderwidth=0,cursor='xterm')
    ting_å_søke_etter.bind('<Return>',søke)

    #label knapper
    skole_eller_fritid = Label(root, text='skole')
    skole_eller_fritid.place(x=325,y=15)
    skole_eller_fritid.config(background=_from_rgb((19,19,19)),foreground='white')
    skole_eller_fritid.bind('<Button-1>',skole_fritid)

    #labels
    Label_1 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_2 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_3 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_4 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_5 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_6 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_7 = Label(root,text='', background=_from_rgb((19,19,19)), foreground='white')
    Label_1.place(x=10,y=50)
    Label_2.place(x=10,y=75)
    Label_3.place(x=10,y=100)
    Label_4.place(x=10,y=125)
    Label_5.place(x=10,y=150)
    Label_6.place(x=10,y=175)
    Label_7.place(x=10,y=200)
    alle_labels = (Label_1,Label_2,Label_3,Label_4,Label_5,Label_6,Label_7)

    root.mainloop()

def finne_fil(num, event):
    os.system(f"open '{num}'")

def søke(event):
    dir_path = os.path.dirname(os.path.realpath(__file__)) 

    for labels in alle_labels:
        labels.config(text='')
        labels.config(background=_from_rgb((19,19,19)))
    
    if skole_fritid_bool == True:
        for root, dirs, files in os.walk('/Users/Sebastian/'):
            for file, label in zip(files,alle_labels):
                if (file.lower() == ting_å_søke_etter.get().lower()) or (file.lower() == str(ting_å_søke_etter.get())+'.docx') or (file.lower() == str(ting_å_søke_etter.get())+'.pptx') or (file.lower() == str(ting_å_søke_etter.get())+'.pdf'):
                    liste_for_filer, liste_2, liste_3 = [str(root)], [], []
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
                    label.config(text=str(file)+'      '+str(liste_3[0]))
                    label.config(background=_from_rgb((37,37,38)))
                    label.bind('<Button-1>', partial(finne_fil,root+'/'+file))
    elif skole_fritid_bool == False:
        for root, dirs, files in os.walk('/Users/Sebastian/'):
            for file, label in zip(files,alle_labels):
                if (file.lower() == ting_å_søke_etter.get().lower()) or (file.lower() == str(ting_å_søke_etter.get())+'.py'):
                    liste_for_filer, liste_2, liste_3 = [str(root)], [], []
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
                    label.config(text=str(file)+'      '+str(liste_3[0]))
                    label.config(background=_from_rgb((37,37,38)))
                    label.bind('<Button-1>', partial(finne_fil,root+'/'+file))
    else: pass

    ting_å_søke_etter.delete(0, END)

if __name__ == "__main__":
    main_win()
