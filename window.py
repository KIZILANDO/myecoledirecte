from tkinter import *
import ecoledirecteapi
from tkextrafont import Font

window = Tk()
semibolde = Font(file="Akshar-SemiBold.ttf", family="Akshar",size='32')

def login():
    window.iconbitmap("icone.ico")
    window.title("Connection")
    def btn_clicked():
        main_page(entry1.get(), entry0.get())

    window.geometry("1366x768")
    window.configure(bg = "#ffffff")
    window.attributes('-fullscreen', True)
    canvas = Canvas(
        window,
        bg = "#151515",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background0.png")
    background = canvas.create_image(
        683.0, 384.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        982.5, 453.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        font = semibolde,
        highlightthickness = 0)

    entry0.place(
        x = 805, y = 414,
        width = 355,
        height = 77)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas.create_image(
        255.5, 453.5,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#ffffff",
        font= semibolde,
        highlightthickness = 0)

    entry1.place(
        x = 78, y = 414,
        width = 355,
        height = 77)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 433, y = 567,
        width = 377,
        height = 96)

    window.resizable(False, False)
    window.mainloop()

def main_page(user, mdp):

    window.iconbitmap("icone.ico")
    window.title("Page d'accueil")
    semibolde.configure(size=64)
    bolde = Font(file="Akshar-Bold.ttf", family="Akshar", size='64')
    window.geometry("1366x768")
    window.configure(bg = "#179485")
    window.attributes('-fullscreen', True)
    client = ecoledirecteapi.Bot()
    client.login(user, mdp)
    nom = client.nom.title()
    bienvenue = f"Bienvenue {client.prenom} {nom}"
    canvas = Canvas(
        window,
        bg = "#179485",
        height = 768,
        width = 1366,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img1 = PhotoImage(file = f"background.png")
    background1 = canvas.create_image(
        622.5, 579.5,
        image=background_img1)

    canvas.create_text(
        258.5, 324.5,
        text = "Moyenne:",
        font = semibolde,
        fill = "#ffffff")

    canvas.create_text(
        1019.5, 390.5,
        text = "Moyenne classe:\n",
        font = semibolde,
        fill = "#ffffff")

    canvas.create_text(
        682.5, 107.5,
        text = bienvenue,
        font = bolde,
        fill = "#000000")

    canvas.create_text(
        212.0, 457.0,
        text = client.printAverage(),
        font = semibolde,
        fill = "#ffffff")

    canvas.create_text(
        1050.0, 455.0,
        text = client.moyenneClasse(),
        font = semibolde,
        fill = "#ffffff")
    window.resizable(False, False)
    window.mainloop()
login()
