import tkinter as tk
import math

class Button(tk.Button):
    def __init__(self, parent, num, max_num):
        super().__init__(parent)
        self.parent = parent
        self.num = num
        self["height"] = 10
        self["width"] = 10
        self["text"] = str(num)
        self["font"] = ("Courier", 20)
        self["bg"] = "green"
        self["command"] = self.toggle_select
        self.selected = False
        grid_len = math.floor(math.sqrt(max_num))
        self.grid(column=(num-1)%grid_len, row=(num-1)//grid_len)

    def toggle_select(self):
        if self["bg"] == "green" and self.num not in self.parent.not_selectable:
            self.parent.button_selected(self.num)
        elif self["bg"] == "red":
            self.parent.button_deselected(self.num)

class App(tk.Frame):
    def __init__(self, master=None, num=7):
        super().__init__(master)
        self.master = master
        self.pack()
        self.buttons = []
        self.currently_selected = []
        self.already_selected = {}
        self.groups = []
        self.not_selectable = []

        for button_number in range(1,num+1):
            button = Button(self, button_number, num)
            self.buttons.append(button)

    def button_selected(self, n):
        if len(self.currently_selected) == 2:
            self.currently_selected.append(n)
            self.groups.append(self.currently_selected)
            print("New group made {}, total groups: {}".format(self.currently_selected, len(self.groups)))
            for i in self.currently_selected:
                if i not in self.already_selected:
                    self.already_selected[i] = []
                others = [x for x in self.currently_selected if i != x]
                for y in others:
                    self.already_selected[i].append(y)
            self.currently_selected = []
        else:
            self.currently_selected.append(n)
        self.update_view()


    def button_deselected(self, n):
        self.currently_selected.remove(n)
        self.update_view()

    def update_view(self):
        self.not_selectable = []
        for n in self.currently_selected:
            if n in self.already_selected:
                self.not_selectable += self.already_selected[n]
        for i, b in enumerate(self.buttons):
            num = i + 1
            if num in self.not_selectable:
                b["bg"] = "blue"
            elif num in self.currently_selected:
                b["bg"] = "red"
            else:
                b["bg"] = "green"

if __name__ == "__main__":
    root = tk.Tk()
    run = App(master=root, num = 9)
    run.mainloop()
