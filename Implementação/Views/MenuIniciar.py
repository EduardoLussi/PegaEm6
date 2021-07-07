from tkinter import *
from PIL import ImageTk, Image
from IniciarJogada import IniciarJogada


class MenuIniciar(Frame):
    def __init__(self, master, parent_root):
        self.parent_root = parent_root

        Frame.__init__(self,
                       master=master,
                       width=self.parent_root.winfo_screenwidth(),
                       height=self.parent_root.winfo_screenheight(),
                       background="white")

        self.master.configure(background="white")

        self.master.title("Menu Inicial")
        self.master.geometry(f"{self.parent_root.winfo_screenwidth()}x{self.parent_root.winfo_screenheight()}")

        imagemTitulo = Image.open('Titulo.png')
        resizeImagemTitulo = imagemTitulo.resize((900, 250))
        img = ImageTk.PhotoImage(resizeImagemTitulo)

        self.titulo = Label(self, image=img)
        self.titulo.image = img
        self.titulo.configure(background="white")
        self.titulo.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.qtJogadoresTexto = Label(self, text="Escolha a quantidade de jogadores")
        self.qtJogadoresTexto.configure(font=("Arial", 16),
                                        bg="white")
        self.qtJogadoresTexto.place(relx=0.5, rely=0.45, anchor=CENTER)

        self.qtJogadoresEscala = Scale(self, from_=2, to=10, orient=HORIZONTAL)
        self.qtJogadoresEscala.configure(width=25,
                                         length=300,
                                         cursor="hand2",
                                         bg="#444444",
                                         fg="white",
                                         troughcolor="#E1DEDD",
                                         font=("Arial", 12))
        self.qtJogadoresEscala.place(relx=0.5, rely=0.52, anchor=CENTER)

        self.jogar = Button(self, text='Jogar', command=lambda: self.handle_event())
        self.jogar.configure(width=6,
                             height=1,
                             cursor="hand2",
                             fg="#0e70b6",
                             bg="#ead116",
                             font=("Arial", 28),
                             bd=5,
                             relief="groove",
                             activebackground="#efe387",
                             activeforeground="#4c8ebd")
        self.jogar.place(relx=0.4, rely=0.8, anchor=CENTER)

        self.sair = Button(self, text='Sair', command=lambda: self.handle_event())
        self.sair.configure(width=6,
                            height=1,
                            cursor="hand2",
                            fg="#0e70b6",
                            bg="#ead116",
                            font=("Arial", 28),
                            bd=5,
                            relief="groove",
                            activebackground="#efe387",
                            activeforeground="#4c8ebd")
        self.sair.place(relx=0.6, rely=0.8, anchor=CENTER)

        self.pack()

    def handle_event(self):
        IniciarJogada(self.master, self.master)
        self.destroy()
        # self.parent_root.deiconify()


if __name__ == '__main__':
    root = Tk()
    tela = MenuIniciar(root, root)
    root.mainloop()
