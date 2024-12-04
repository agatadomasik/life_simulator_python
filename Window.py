import tkinter as tk
from tkinter import filedialog

from Board import Board
from Swiat import Swiat


class Window:
    def __init__(self):
        self.cell_size = 20
        self.window = tk.Tk()
        self.window.title('Game')
        self.window.geometry('1200x600')

        self.label_width = tk.Label(self.window, text='Szerokość:')
        self.label_width.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.width_entry = tk.Entry(self.window)
        self.width_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        self.label_height = tk.Label(self.window, text='Wysokość:')
        self.label_height.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.height_entry = tk.Entry(self.window)
        self.height_entry.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        self.play_button = tk.Button(self.window, text='Graj', command=self.rysuj)
        self.play_button.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)

        self.load_button = tk.Button(self.window, text='Wczytaj', command=self.wczytaj)
        self.load_button.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)

        self.next_turn_button = tk.Button(self.window, text='Nowa tura', command=self.nowa_tura)
        self.next_turn_button.grid(row=0, column=55, rowspan=2, sticky=tk.NW, padx=(0, 5), pady=5)

        self.save_button = tk.Button(self.window, text='Zapisz', command=self.zapisz)
        self.save_button.grid(row=1, column=55, rowspan=2, sticky=tk.NW, padx=(0, 5), pady=5)

        self.save_button = tk.Button(self.window, text='Wydarzenia', command=self.print_events)
        self.save_button.grid(row=2, column=55, rowspan=2, sticky=tk.NW, padx=(0, 5), pady=5)

        self.canvas = tk.Canvas(self.window)
        self.canvas.grid(row=2, column=0, columnspan=20, sticky=tk.NSEW, padx=5, pady=5)

        self.legend_frame = tk.Frame(self.window)
        self.legend_frame.grid(row=2, column=55, sticky=tk.NW, padx=5, pady=40)

        pom = Swiat(0, 0)

        self.legend_labels = []
        self.legend_names = ['Antylopa', 'Barszcz', 'Czlowiek', 'Guarana', 'Lis', 'Mlecz',
                             'Owca', 'Trawa', 'WilczeJagody', 'Wilk', 'Zolw']
        self.legend_colors = ['#ffc990', '#8f2065', '#00BBFF', '#d03232', '#ff8d3c', '#ffdd3d',
                              '#ded8c9', '#259d00', '#5737b7', '#8A8787', '#aac79b']

        for i, name in enumerate(self.legend_names):
            label = tk.Label(self.legend_frame, text=name, bg=self.legend_colors[i])
            label.grid(row=i, column=0, sticky=tk.W, pady=5)
            self.legend_labels.append(label)

        self.window.grid_rowconfigure(2, weight=1)
        self.window.grid_columnconfigure(list(range(60)), weight=1)

        self.window.bind("<Up>", self.handle_arrow_key)
        self.window.bind("<Down>", self.handle_arrow_key)
        self.window.bind("<Left>", self.handle_arrow_key)
        self.window.bind("<Right>", self.handle_arrow_key)
        self.window.bind("<space>", self.handle_arrow_key)

        self.window.mainloop()

    def handle_arrow_key(self, event):
        if event.keysym == "Up":
            direction = "Up"
        elif event.keysym == "Down":
            direction = "Down"
        elif event.keysym == "Left":
            direction = "Left"
        elif event.keysym == "Right":
            direction = "Right"
        elif event.keysym == "space":
            direction = "space"
        else:
            return

        self.swiat.wykonajTure(self.swiat.getVector(), direction)
        self.board.draw()

    def rysuj(self, event=None):
        width_text = self.width_entry.get()
        height_text = self.height_entry.get()

        if width_text and height_text:
            width = int(width_text)
            height = int(height_text)

            self.label_width.grid_forget()
            self.width_entry.grid_forget()
            self.label_height.grid_forget()
            self.height_entry.grid_forget()
            self.play_button.grid_forget()
            self.load_button.grid_forget()

            self.swiat = Swiat(width, height)
            self.swiat.generuj()

            self.board = Board(self.canvas, self.cell_size, width, height, self.swiat)
            self.board.draw()

    def nowa_tura(self):
        self.swiat.wykonajTure(self.swiat.getVector(), 0)
        self.board.draw()

    def zapisz(self):
        import tkinter as tk
        from tkinter import filedialog

        try:
            filename = filedialog.asksaveasfilename(title="Podaj wartość")

            with open(filename, 'w') as f:
                f.write(str(self.swiat.getN()) + " " + str(self.swiat.getM()) + "\n")
                f.write(str(len(self.swiat.getVector())) + " " + str(len(self.swiat.events)) + " " + str(self.swiat.getTura()) + " " + str(
                    self.swiat.getPower()) + "\n")
                for o in self.swiat.getVector():
                    f.write(o.getNazwa() + " " + str(o.getX()) + " " + str(o.getY()) + " " + str(o.getWiek()) + "\n")
                for event in self.swiat.events:
                    f.write(event + "\n")

            tk.messagebox.showinfo("Informacja", "Zapisano")
        except IOError:
            tk.messagebox.showerror("Błąd", "Nie udało się otworzyć pliku")

    def wczytaj(self):
        from Antylopa import Antylopa
        from BarszczSosnowskiego import BarszczSosnowskiego
        from Czlowiek import Czlowiek
        from Guarana import Guarana
        from Lis import Lis
        from Mlecz import Mlecz
        from Owca import Owca
        from Swiat import Swiat
        from Trawa import Trawa
        from WilczeJagody import WilczeJagody
        from Wilk import Wilk
        from Zolw import Zolw
        try:
            filename = filedialog.askopenfilename(title="Podaj nazwę pliku")

            with open(filename, 'r') as f:
                br = f.readlines()

                firstLine = br[0].split(" ")
                n = int(firstLine[0])
                m = int(firstLine[1])

                newS = Swiat(n, m)

                secondLine = br[1].split(" ")
                size1 = int(secondLine[0])
                size2 = int(secondLine[1])
                tura = int(secondLine[2])
                power = bool(secondLine[3])

                for i in range(size1):
                    line = br[i + 2].split(" ")
                    nazwa = line[0]
                    print(nazwa)
                    x = int(line[1])
                    print(x)
                    y = int(line[2])
                    print(y)
                    wiek = int(line[3])
                    print(wiek)
                    o = None

                    if nazwa == "Antylopa":
                        o = Antylopa(x, y, newS)
                    elif nazwa == "BarszczSosnowskiego":
                        o = BarszczSosnowskiego(x, y, newS)
                    elif nazwa == "Czlowiek":
                        o = Czlowiek(x, y, newS)
                        o.setTura(tura)
                        o.setPower(power)
                    elif nazwa == "Guarana":
                        o = Guarana(x, y, newS)
                    elif nazwa == "Lis":
                        o = Lis(x, y, newS)
                    elif nazwa == "Mlecz":
                        o = Mlecz(x, y, newS)
                    elif nazwa == "Owca":
                        o = Owca(x, y, newS)
                    elif nazwa == "Trawa":
                        o = Trawa(x, y, newS)
                    elif nazwa == "WilczeJagody":
                        o = WilczeJagody(x, y, newS)
                    elif nazwa == "Wilk":
                        o = Wilk(x, y, newS)
                    elif nazwa == "Zolw":
                        o = Zolw(x, y, newS)

                    o.setWiek(wiek)
                    newS.dodajOrganizm(o)

                events = []
                for i in range(size2):
                    events.append(br[i + size1 + 2].rstrip())

            tk.messagebox.showinfo("Info", "Wczytano")

            self.swiat = newS
            self.board = Board(self.canvas, self.cell_size, newS.getN(), newS.getM(), newS)

            self.label_width.grid_forget()
            self.width_entry.grid_forget()
            self.label_height.grid_forget()
            self.height_entry.grid_forget()
            self.play_button.grid_forget()
            self.load_button.grid_forget()

            self.board.draw()
            #self.destroy()

        except IOError:
            tk.messagebox.showerror("Info", "Nie udało się otworzyć pliku")

    def print_events(self):
        num_events = len(self.swiat.events)
        num_to_display = min(15, num_events)
        last_events = self.swiat.events[-num_to_display:]
        events_str = '\n'.join(last_events)
        tk.messagebox.showinfo("Wydarzenia", events_str)
