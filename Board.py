
class Board:
    def __init__(self, canvas, cell_size, width, height, swiat):
        self.canvas = canvas
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.swiat = swiat

    def draw(self):
        #self.swiat.generuj()
        self.canvas.delete('all')

        for i in range(self.width):
            for j in range(self.height):
                x1 = i * self.cell_size
                y1 = j * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                #if self.swiat.getOrganizmy()[i][j] is not None:
                self.canvas.create_rectangle(x1, y1, x2, y2, outline='#cdd3d4')
                if self.swiat.getOrganizmy()[i][j] is not None:
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline='#cdd3d4',
                    fill=self.swiat.getOrganizmy()[i][j].rysowanie())
                else: self.canvas.create_rectangle(x1, y1, x2, y2, outline='#cdd3d4')
                #else:
                    #self.canvas.create_rectangle(x1, y1, x2, y2, outline='#cdd3d4', fill=self.swiat.getOrganizmy()[i][j].rysowanie())
                    #pass
                #self.swiat.getOrganizmy()[0][0].rysowanie()