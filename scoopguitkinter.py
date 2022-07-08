# imports below
import tkinter as tk
import subprocess
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as font


def pages_tutorial():
    class Page(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)
        def show(self):
            self.lift()

    class Page1(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = tk.Label(self, text="This is page 1")
           label.pack(side="top", fill="both", expand=True)

    class Page2(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = tk.Label(self, text="This is page 2")
           label.pack(side="top", fill="both", expand=True)

    class Page3(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = tk.Label(self, text="This is page 3")
           label.pack(side="top", fill="both", expand=True)

    class MainView(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)
            p1 = Page1(self)
            p2 = Page2(self)
            p3 = Page3(self)

            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="x", expand=False)
            container.pack(side="top", fill="both", expand=True)

            p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

            b1 = tk.Button(buttonframe, text="Page 1", command=p1.show)
            b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
            b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

            b1.pack(side="left")
            b2.pack(side="left")
            b3.pack(side="left")

            p1.show()

    if __name__ == "__main__":
        root = tk.Tk()
        main = MainView(root)
        main.pack(side="top", fill="both", expand=True)
        root.wm_geometry("400x400")
        root.iconbitmap(default='scoopicon.ico')
        root.mainloop()


########################################################################################################################



class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        f35 = font.Font(size=35)
        tk.Frame.__init__(self, *args, **kwargs)
        pm = MenuPage(self)
        ps = SearchPage(self)
        # p3 = Page3(self)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        pm.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        ps.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        searchbutton = tk.Button(buttonframe, text="Search", command=ps.show())
        searchbutton['font'] = f35
        # b2 = tk.Button(buttonframe, text="Page 2", command=p2.show)
        # b3 = tk.Button(buttonframe, text="Page 3", command=p3.show)

        searchbutton.pack(side="left")
        # b2.pack(side="left")
        # b3.pack(side="left")

        pm.show()


class MenuPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="This is page 1")
        label.pack(side="top", fill="both", expand=True)

class SearchPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = tk.Label(self, text="Welcome to the search page")
        label.pack(side="top", fill="both", expand=True)





if __name__ == "__main__":
    root = ThemedTk(theme='yaru')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1200x600")
    root.iconbitmap(default='scoopicon.ico')
    root.title("Scoop GUI")
    # ttk.Style().theme_use('scidgreen')
    # s = ttk.Style()
    # print(s.theme_use())
    # print(root.get_themes())
    root.tk.call("source", "Azure-ttk-theme-2.1.0/azure.tcl")
    root.tk.call("set_theme", "dark")
    root.mainloop()
