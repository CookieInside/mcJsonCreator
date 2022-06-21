import tkinter as tk

class JsonApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.is_item = True
        self.id = tk.StringVar(self)
        self.name = tk.StringVar(self)
        self.title("Generate modles Json Data")
        self.geometry("400x400")
        self.lable = tk.Label(self,text = "Item or Block").grid(column=0, row=0)
        self.i_b_button = tk.Button(self, text="Item", command=self.switch)
        self.i_b_button.grid(column=1, row=0)
        self.lable = tk.Label(self, text="ID: ").grid(column=0, row=1)
        self.idEntry = tk.Entry(self, textvar=self.id).grid(column=1, row=1)
        self.lable = tk.Label(self, text="Name: ").grid(column=0, row=2)
        self.nameEntry = tk.Entry(self, textvar=self.name).grid(column=1, row=2)
        self.genButton = tk.Button(self, text="Generate", command=self.gen)
        self.genButton.grid(column=0, row=3)

    def switch(self):
        self.is_item

        # Determine is on or off
        if self.is_item:
            self.i_b_button.config(text="Block")
            self.is_item = False
        else:

            self.i_b_button.config(text="Item")
            self.is_item = True

    def gen(self):
        if self.is_item:
            # creates models/item data
            fp = open(f'MODELS_ITEM{self.id.get()}.json', 'w')
            fp.write(
                '{\r\n    "parent": "item/generated",\r\n    "textures": {\r\n        "layer0": "examplemod:item/' + self.id.get() + '"\r\n    }\r\n}')
            fp.close()
            # outputs data for lang file
            print('"item.examplemod.' + self.id.get() + '": "' + self.name.get() + '"')
        else:
            #Create models/block data
            fp = open(f'MODELS_BLOCK{self.id.get()}.json', 'w')
            fp.write(
                '{\r\n    "parent": "block/cube_all",\r\n    "textures": {\r\n        "all": "examplemod:block/' + self.id.get() + '"\r\n    }\r\n}')
            fp.close()
            #creates models/item data
            fp = open(f'MODELS_ITEM{self.id.get()}.json', 'w')
            fp.write(
                '{\r\n    "parent": "examplemod:block/' + self.id.get() + '"\r\n}')
            fp.close()
            # creates blockstates data
            fp = open(f'BLOCKSTATE{self.id.get()}.json', 'w')
            fp.write(
                '{\r\n    "variants": {\r\n		"": {\r\n			"model": "examplemod:block/' + self.id.get() + '"\r\n		}\r\n	}\r\n}')
            fp.close()
            # outputs data for lang file
            print('"block.examplemod.' + self.id.get() + '": "' + self.name.get() + '"')

w = JsonApp()
w.mainloop()