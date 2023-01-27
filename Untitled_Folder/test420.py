try:
    import Tkinter as tk
    import tkFont
    import ttk
except ImportError:  # Python 3
    import tkinter as tk
    import tkinter.font as tkFont
    import tkinter.ttk as ttk
import re

# def selectItem(a):
#     curItem = tree.focus()
#     print tree.item(curItem)


class MultiColumnListbox(object):
    """use a ttk.TreeView as a multicolumn ListBox"""

    def __init__(self):
        self.tree = None
        self._setup_widgets()
        self._build_tree()
    
    def select(self):
        self.number123 = re.compile(r'(\d{9,12})\, \d+?\]')
        self.reslist = list()
        self.seleccion = self.tree.selection()
        print(self.seleccion)
        for item in self.seleccion:
            l = {}
            print(item)
            i = str(self.tree.item(item))
            # print(i)
            matches = self.number123.findall(i)
            # l["i"] = i
            for match in matches:
                print(repr(matches))
                number = match
                self.entrada = str(number)
                if len(number) == 11:
                    self.reslist.append("+" + self.entrada)
            
                elif len(number) == 9:

                    self.reslist.append("+27" + self.entrada)

        for val in self.reslist:
            print(val)

    def _setup_widgets(self):
        msg = ttk.Label(wraplength="4i", justify="left", anchor="n",
                        padding=(10, 2, 10, 10))

        self.Msgs_button = ttk.Button(text = "Messages", width = 12,
                                      command = self.select)
        self.Msgs_button.grid(row = 17, column = 6)

        self.MM_button = ttk.Button(text = "Main Menu", width = 12)
        self.MM_button.grid(row = 18, column = 6)

        self.log_button = ttk.Button(text = "Log In", width = 12)
        self.log_button.grid(row = 19, column = 6)

        self.Close_button = ttk.Button(text = "Close", width = 12)
        self.Close_button.grid(row = 20, column = 6)

        filter_string_1 = tk.StringVar()
        self.filter_1 = ttk.Entry(textvariable=filter_string_1)
        self.filter_1.grid(row = 1, column = 0)

        filter_string_2 = tk.StringVar()
        self.filter_2 = ttk.Entry(textvariable=filter_string_2)
        self.filter_2.grid(row = 1, column = 1)

        filter_string_3 = tk.StringVar()
        self.filter_3 = ttk.Entry(textvariable=filter_string_3)
        self.filter_3.grid(row = 1, column = 2)

        filter_string_4 = tk.StringVar()
        self.filter_4 = ttk.Entry(textvariable=filter_string_4)
        self.filter_4.grid(row = 1, column = 3)

        self.l1=ttk.Label(text="First_name")
        self.l1.grid(row=0,column=0)

        self.l2=ttk.Label(text="Surname")
        self.l2.grid(row=0,column=1)

        self.l3=ttk.Label(text="contacts_number")
        self.l3.grid(row=0,column=2)

        self.l4= ttk.Label(text="Staff_ID")
        self.l4.grid(row=0,column=3)

        msg.grid()
        container = ttk.Frame()
        container.grid()
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(columns=cotacts_header, show="headings", height = 10)
        vsb = ttk.Scrollbar(orient="vertical",
                            command=self.tree.yview
                            )
        hsb = ttk.Scrollbar(orient="horizontal",
                            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
                            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=2, columnspan = 5, rowspan = 20, sticky='nsew')
        vsb.grid(column=5, row=2, rowspan = 20, sticky='ns')
        hsb.grid(column=0, row=22, columnspan = 5, sticky='ew')
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in cotacts_header:
            self.tree.heading(col, text=col.title(),
                              command=lambda c=col: sortby(self.tree, c, 0))

            # adjust the column's width to the header string
            self.tree.column(col,
                             width=tkFont.Font().measure(col.title()))

        for item in cotacts_list:
            self.tree.insert('', 'end', values=item)
            # adjust column's width if necessary to fit each value
            for ix, val in enumerate(item):
                col_w = tkFont.Font().measure(val)
                if self.tree.column(cotacts_header[ix], width=None) < col_w:
                    self.tree.column(cotacts_header[ix], width=col_w)

def sortby(tree, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tree.set(child, col), child)
            for child in tree.get_children('')]
    # if the data to be sorted is numeric change to float
    # data =  change_numeric(data)
    # now sort the data in place
    data.sort(reverse=descending)
    for ix, item in enumerate(data):
        tree.move(item[1], '', ix)
    # switch the heading so it will sort in the opposite direction
    tree.heading(col, command=lambda col=col: sortby(tree, col,
                                                     int(not descending)))

# the test data ...

cotacts_header = ['First Name', 'Surname', 'Number', 'Staff ID']
cotacts_list = [
            ('Chevy', 'air', '1234567890', '06')
]


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Multicolumn Treeview/Listbox")
    listbox = MultiColumnListbox()
    root.mainloop()
