import pandas as pd
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog


class wood:
    w_list = []

    def __init__(self, no: int, name: str, type: str, price: float, length: float, width: float, height: float):
        self.no = no
        self.name = name
        self.type = type
        self.l = float(length)
        self.w = float(width)
        self.h = float(height)
        self.prc = float(price)
        self.w_list.append(self)


class hardware:
    h_list = []

    def __init__(self, no: int, name: str, price: float):
        self.no = no
        self.name = name
        self.prc = float(price)
        self.h_list.append(self)


class view_wood:
    def __init__(self):
        refresh_frame()
        self.title = Label(frame, text="Wood list")
        self.title.grid(row=0, column=3)
        self.button1 = Label(frame, text="FW wood")
        self.button1.grid(row=0, column=0, sticky='nswe')
        self.button2 = Button(frame, text="Other wood", command=lambda: [self.list_frame.destroy(), self.selection_wood()])
        self.button2.grid(row=0, column=1, sticky='nsw')
        self.switch = 0
        self.no_clm = Label(frame, text="No.", padx=23, pady=20, borderwidth=2, relief='groove')
        self.no_clm.grid(row=1, rowspan=2, column=0)
        self.name_clm = Label(frame, text="Parts", padx=94, pady=20, borderwidth=2, relief='groove')
        self.name_clm.grid(row=1, rowspan=2, column=1)
        self.type_clm = Label(frame, text="Materials", padx=82, pady=20, borderwidth=2, relief='groove')
        self.type_clm.grid(row=1, rowspan=2, column=2)
        self.prc_clm = Label(frame, text="Price", padx=22, pady=20, borderwidth=2, relief='groove')
        self.prc_clm.grid(row=1, rowspan=2, column=3)
        self.size = Label(frame, text="Size", padx=121, pady=5, borderwidth=2, relief='groove')
        self.size.grid(row=1, column=4, columnspan=3, sticky='nswe')
        self.length_clm = Label(frame, text="Length", padx=25, pady=5, borderwidth=2, relief='groove')
        self.length_clm.grid(row=2, column=4, sticky='nswe')
        self.width_clm = Label(frame, text="Width", padx=25, pady=5, borderwidth=2, relief='groove')
        self.width_clm.grid(row=2, column=5, sticky='nswe')
        self.height_clm = Label(frame, text="Height", padx=25, pady=5, borderwidth=2, relief='groove')
        self.height_clm.grid(row=2, column=6, sticky='nswe')
        self.selection_wood()
        self.add_btt = Button(frame, text="Add", padx=30, pady=1, borderwidth=3, command=lambda: self.add())
        self.add_btt.grid(row=1, column=7)
        self.back_btt = Button(frame, text="Back", padx=30, pady=5, borderwidth=3, command=lambda: home_page())
        self.back_btt.grid(row=20, column=6)

    def selection_wood(self):
        if self.switch == 1:
            self.button1 = Button(frame, text="FW wood", command=lambda: [self.list_frame.destroy(), self.selection_wood()])
            self.button1.grid(row=0, column=0, sticky='nswe')
            self.button2 = Label(frame, text="Other wood")
            self.button2.grid(row=0, column=1, sticky='nsw')
            self.switch = 2

        elif self.switch == 2:
            self.button1 = Label(frame, text="FW wood")
            self.button1.grid(row=0, column=0, sticky='nswe')
            self.button2 = Button(frame, text="Other wood", command=lambda: [self.list_frame.destroy(), self.selection_wood()])
            self.button2.grid(row=0, column=1, sticky='nsw')
            self.switch = 1

        elif self.switch == 0:
            self.switch = 1

        # Scrollbar
        self.list_frame = Frame(frame)
        self.list_frame.grid(row=3, column=0, columnspan=8, pady=3, sticky='nswe')
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)
        self.list_frame.grid_propagate(False)

        self.canvas = Canvas(self.list_frame)
        self.canvas.grid(row=0, column=0, sticky='nswe')

        self.scrollbar = Scrollbar(self.list_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_info = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_info, anchor='nw')

        for x, w in enumerate(wood.w_list):
            self.view(w, x)

        self.frame_info.update_idletasks()
        self.list_frame.config(height=475)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def view(self, w, x):
        Label(self.frame_info, text=w.no, width=9).grid(row=x, column=0, sticky='nswe')
        Label(self.frame_info, text=w.name, width=30).grid(row=x, column=1, sticky='nswe')
        Label(self.frame_info, text=w.type, width=30).grid(row=x, column=2, sticky='nswe')
        Label(self.frame_info, text=w.prc, width=10).grid(row=x, column=3, sticky='nswe')
        Label(self.frame_info, text=w.l, width=12).grid(row=x, column=4, sticky='nswe')
        Label(self.frame_info, text=w.w, width=12).grid(row=x, column=5, sticky='nswe')
        Label(self.frame_info, text=w.h, width=12).grid(row=x, column=6, sticky='nswe')
        Button(self.frame_info, text='Edit', padx=30, pady=5, command=lambda: self.edit(w, w.no)).grid(row=x, column=7, sticky='nswe')

    def add(self):
        refresh_frame()
        Label(frame, text="Add Wood").grid(row=0, column=0, columnspan=1)
        Label(frame, text="Name", padx=25, pady=20).grid(row=1, column=0)
        Label(frame, text="Materials", padx=25, pady=20).grid(row=2, column=0)
        Label(frame, text="Price", padx=25, pady=20).grid(row=3, column=0)
        Label(frame, text="Length", padx=25, pady=5).grid(row=4, column=0)
        Label(frame, text="Width", padx=25, pady=5).grid(row=5, column=0)
        Label(frame, text="Depth", padx=25, pady=5).grid(row=6, column=0)
        name = Entry(frame, width=20, borderwidth=1)
        name.grid(row=1, column=1)
        material = Entry(frame, width=20, borderwidth=1)
        material.grid(row=2, column=1)
        price = Entry(frame, width=10, borderwidth=1)
        price.grid(row=3, column=1)
        length = Entry(frame, width=10, borderwidth=1)
        length.grid(row=4, column=1)
        width = Entry(frame, width=10, borderwidth=1)
        width.grid(row=5, column=1)
        height = Entry(frame, width=10, borderwidth=1)
        height.grid(row=6, column=1)
        addlist = [name, material, price, length, width, height]

        Label(frame, text="If Width >= 100 & Length >= 630:\nDepth < 20: RM3100\tDepth >= 20: RM3200", justify='left',
              padx=25).grid(row=1, column=2, sticky='w')
        Label(frame, text="If Width >= 100 & Length >= 760:\nRM3000", justify='left', padx=25).grid(row=2, column=2,
                                                                                                    sticky='w')
        Label(frame, text="If Width < 100 & Length <= 760:\nRM2600", justify='left', padx=25).grid(row=3, column=2,
                                                                                                   sticky='w')

        button1 = Button(frame, text="Back", padx=25, pady=5, borderwidth=3, command=view_wood)
        button1.grid(row=7, column=0, sticky="w")
        button2 = Button(frame, text="Confirm", padx=25, pady=5, borderwidth=3,
                         command=lambda: [add(addlist, True, False),
                                          view_wood])
        button2.grid(row=7, column=1, sticky="e")
        button3 = Button(frame, text='Calculate the price', padx=25, pady=5, borderwidth=3,
                         command=lambda: self.calc(addlist))
        button3.grid(row=4, column=2)

    def calc(self, add_list):
        length = add_list[3].get()
        width = add_list[4].get()
        depth = add_list[5].get()
        price = add_list[2]

        if length == '' or width == '' or depth == '':
            messagebox.showerror(title="Error", message="Please fill out the length, width and depth "
                                                        "before clicking the \'calculating price\' button")

        else:
            length = float(length)
            width = float(width)
            depth = float(depth)
            if width >= 100:
                if 630 <= length < 760:
                    if depth < 20:
                        price.delete(0, END)
                        price.insert(0, '3100')

                    elif depth >= 20:
                        price.delete(0, END)
                        price.insert(0, '3200')

                elif length >= 760:
                    price.delete(0, END)
                    price.insert(0, '3000')

            elif width < 100:
                if length <= 760:
                    price.delete(0, END)
                    price.insert(0, '2600')

    # noinspection PyTypeChecker
    def edit(self, w, x):
        self.name = Entry(self.frame_info, width=30, borderwidth=1)
        self.name.grid(row=x, column=1)
        self.name.insert(0, w.name)
        self.type = Entry(self.frame_info, width=30, borderwidth=1)
        self.type.grid(row=x, column=2)
        self.type.insert(0, w.type)
        self.price = Entry(self.frame_info, width=10, borderwidth=1)
        self.price.grid(row=x, column=3)
        self.price.insert(0, w.prc)
        self.length = Entry(self.frame_info, width=10, borderwidth=1)
        self.length.grid(row=x, column=4)
        self.length.insert(0, w.l)
        self.width = Entry(self.frame_info, width=10, borderwidth=1)
        self.width.grid(row=x, column=5)
        self.width.insert(0, w.w)
        self.height = Entry(self.frame_info, width=10, borderwidth=1)
        self.height.grid(row=x, column=6)
        self.height.insert(0, w.h)
        Button(self.frame_info, text='Confirm', padx=15, pady=5, command=lambda: [
            self.delete_btt.grid_forget(),
            self.change(w),
            self.view(wood.w_list[x], x)
        ]).grid(row=x, column=7, sticky='nswe')
        self.delete_btt = Button(frame, text='Delete', padx=25, pady=3, command=lambda: [
            self.delete_btt.grid_forget(),
            self.delete(x),
            view_wood()
        ])
        self.delete_btt.grid(row=2, column=7)

    def change(self, w):
        w.name = self.name.get()
        w.type = self.type.get()
        w.prc = float(self.price.get())
        w.l = float(self.length.get())
        w.w = float(self.width.get())
        w.h = float(self.height.get())
        wood_file.loc[w.no, column1[0]] = w.name
        wood_file.loc[w.no, column1[1]] = w.type
        wood_file.loc[w.no, column1[2]] = float(w.prc)
        wood_file.loc[w.no, column1[3]] = float(w.l)
        wood_file.loc[w.no, column1[4]] = float(w.w)
        wood_file.loc[w.no, column1[5]] = float(w.h)
        save_file(wood_file, 'Sheet1')
        self.name.grid_forget()
        self.type.grid_forget()
        self.price.grid_forget()
        self.length.grid_forget()
        self.width.grid_forget()
        self.height.grid_forget()

    @staticmethod
    def delete(x):
        wood.w_list.pop(x)
        file = pd.read_excel('Wood file.xlsx', 'Sheet1').drop(x)
        save_file(file, 'Sheet1')
        for x, y in enumerate(wood.w_list):
            y.no = x


class view_hardware:
    def __init__(self):
        refresh_frame()
        self.title = Label(frame, text="Wood list")
        self.title.grid(row=0, column=3)
        self.no_clm = Label(frame, text="No.", padx=25, pady=20, borderwidth=2, relief='groove')
        self.no_clm.grid(row=1, rowspan=2, column=0)
        self.name_clm = Label(frame, text="Parts", padx=25, pady=20, borderwidth=2, relief='groove')
        self.name_clm.grid(row=1, rowspan=2, column=1)
        self.price_clm = Label(frame, text="Price", padx=25, pady=20, borderwidth=2, relief='groove')
        self.price_clm.grid(row=1, rowspan=2, column=2)

        self.list_frame = Frame(frame)
        self.list_frame.grid(row=3, column=0, columnspan=4, pady=3, sticky='nswe')
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)
        self.list_frame.grid_propagate(False)

        self.canvas = Canvas(self.list_frame)
        self.canvas.grid(row=0, column=0, sticky='nswe')

        self.scrollbar = Scrollbar(self.list_frame, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_info = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_info, anchor='nw')

        for x, h in enumerate(hardware.h_list):
            self.view(h, x)

        self.frame_info.update_idletasks()
        self.list_frame.config(height=475)
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.add_btt = Button(frame, text="Add", padx=30, pady=3, borderwidth=3, command=lambda: self.add())
        self.add_btt.grid(row=1, column=3, sticky='n')
        self.back_btt = Button(frame, text="Back", padx=30, pady=5, borderwidth=3, command=lambda: home_page())
        self.back_btt.grid(row=4, column=3)

    def view(self, h, x):
        Label(self.frame_info, text=h.no, width=9).grid(row=x, column=0, sticky='nswe')
        Label(self.frame_info, text=h.name, width=11).grid(row=x, column=1, sticky='nswe')
        Label(self.frame_info, text=h.prc, width=11).grid(row=x, column=2, sticky='nswe')
        Button(self.frame_info, text='Edit', padx=25, pady=5,
               command=lambda: self.edit(h, h.no)).grid(row=x, column=3, sticky='nswe')

    @staticmethod
    def add():
        refresh_frame()
        Label(frame, text="Add Hardware").grid(row=0, column=0, columnspan=1)
        Label(frame, text="Name", padx=25, pady=20).grid(row=1, column=0)
        Label(frame, text="Price", padx=25, pady=20).grid(row=2, column=0)
        name = Entry(frame, width=25, borderwidth=1)
        name.grid(row=1, column=1)
        price = Entry(frame, width=10, borderwidth=1)
        price.grid(row=2, column=1, sticky='w')
        addlist = [name, price]
        button1 = Button(frame, text="Back", padx=25, pady=5, borderwidth=3, command=lambda: view_hardware())
        button1.grid(row=4, column=0, sticky="w")
        button2 = Button(frame, text="Confirm", padx=25, pady=5, borderwidth=3,
                         command=lambda: [add(addlist, False, True), view_hardware()])
        button2.grid(row=4, column=1, sticky="e")

    def edit(self, h, x):
        self.name = Entry(self.frame_info, width=10, borderwidth=1)
        self.name.grid(row=x, column=1)
        self.name.insert(0, h.name)
        self.price = Entry(self.frame_info, width=10, borderwidth=1)
        self.price.grid(row=x, column=2)
        # noinspection PyTypeChecker
        self.price.insert(0, h.prc)
        Button(self.frame_info, text='Confirm', padx=15, pady=5, anchor=CENTER, command=lambda: [
            self.delete_btt.grid_forget(),
            self.change(h),
            self.view(hardware.h_list[x], x)
        ]).grid(row=x, column=3, sticky='nswe')
        self.delete_btt = Button(frame, text='Delete', padx=25, pady=3, command=lambda: [
            self.delete_btt.grid_forget(),
            self.delete(x),
            view_hardware()
        ])
        self.delete_btt.grid(row=2, column=3)

    def change(self, h):
        h.name = self.name.get()
        h.prc = float(self.price.get())
        hardware_file.loc[h.no, column2[0]] = h.name
        hardware_file.loc[h.no, column2[1]] = float(h.prc)
        save_file(hardware_file, 'Sheet2')
        self.name.grid_forget()
        self.price.grid_forget()

    @staticmethod
    def delete(x):
        hardware.h_list.pop(x)
        file = pd.read_excel('Wood file.xlsx', 'Sheet2').drop(x)
        save_file(file, 'Sheet2')
        for x, y in enumerate(hardware.h_list):
            y.no = x


class view_prc:
    list = []
    save_data = []
    row = 4
    all_t_price = float(0.00)
    total_w = None
    total = None

    def __init__(self, name, type, prc, l, w, h, qty):
        self.qty = qty
        self.prc = prc
        self.m3 = self.cal_prc(l, w, h)
        self.t_prc = round((self.m3 * prc), 2)
        self.set = [
            Label(frame, text=name, anchor=W, width=30),
            Label(frame, text=type, anchor=W, width=30),
            Label(frame, text=prc, width=10),
            Entry(frame, width=10, borderwidth=1),
            Entry(frame, width=10, borderwidth=1),
            Entry(frame, width=10, borderwidth=1),
            Entry(frame, width=10, borderwidth=1),
            Label(frame, text=self.m3, width=10),
            Label(frame, text=self.t_prc, width=10),
        ]
        self.set[3].insert(END, l)
        self.set[4].insert(END, w)
        self.set[5].insert(END, h)
        self.set[6].insert(END, self.qty)

        self.bool_del = BooleanVar()
        self.check_btt = Checkbutton(frame, variable=self.bool_del)

        if not self.list:
            view_prc.row = 4

        self.row = view_prc.row
        view_prc.row += 1

        self.set[3].bind('<KeyRelease>', lambda event: self.refresh(event))
        self.set[4].bind('<KeyRelease>', lambda event: self.refresh(event))
        self.set[5].bind('<KeyRelease>', lambda event: self.refresh(event))
        self.set[6].bind('<KeyRelease>', lambda event: self.refresh(event))

        self.list.append(self)

        for n, x in enumerate(self.list[-1].set):
            x.grid(row=self.row, column=n)

        view_prc.all_t_price += self.t_prc
        self.total.configure(text=round(view_prc.all_t_price, 2))

        self.total_w.grid_forget()
        self.total.grid_forget()
        self.total_w.grid(row=self.row + 1, column=7)
        self.total.grid(row=self.row + 1, column=8)

    def cal_prc(self, l, w, h):
        return round(((l * w * h) / 1000000000) * self.qty, 4)

    @staticmethod
    def list_price():
        refresh_frame()
        title = Label(frame, text="Wood list price")
        title.grid(row=0, column=4)
        name = Label(frame, text="Parts", padx=94, pady=20, borderwidth=2, relief='groove')
        name.grid(row=2, rowspan=2, column=0)
        type = Label(frame, text="Materials", padx=82, pady=20, borderwidth=2, relief='groove')
        type.grid(row=2, rowspan=2, column=1)
        price = Label(frame, text="Price", padx=22, pady=20, borderwidth=2, relief='groove')
        price.grid(row=2, rowspan=2, column=2)
        size = Label(frame, text="Size", padx=121, pady=5, borderwidth=2, relief='groove')
        size.grid(row=2, column=3, columnspan=3)
        length = Label(frame, text="Length", padx=25, pady=5, borderwidth=2, relief='groove')
        length.grid(row=3, column=3, sticky='nswe')
        width = Label(frame, text="Width", padx=25, pady=5, borderwidth=2, relief='groove')
        width.grid(row=3, column=4, sticky='nswe')
        height = Label(frame, text="Depth", padx=25, pady=5, borderwidth=2, relief='groove')
        height.grid(row=3, column=5, sticky='nswe')
        qty = Label(frame, text='QTY', padx=25, pady=20, borderwidth=2, relief='groove')
        qty.grid(row=2, rowspan=2, column=6)
        m3 = Label(frame, text='m3', padx=25, pady=20, borderwidth=2, relief='groove')
        m3.grid(row=2, rowspan=2, column=7)
        total = Label(frame, text='Total', padx=25, pady=20, borderwidth=2, relief='groove')
        total.grid(row=2, rowspan=2, column=8)
        view_prc.total_w = Label(frame, text='Total', anchor=CENTER, width=10)
        view_prc.total_w.grid(row=view_prc.row, column=7)
        view_prc.total = Label(frame, text=view_prc.all_t_price, anchor=CENTER, width=10)
        view_prc.total.grid(row=view_prc.row, column=8)
        Button(frame, text="Save as", padx=20, pady=5, borderwidth=3, command=view_prc.save_file).grid(row=1, column=0,
                                                                                                       sticky='w')
        Button(frame, text="Add", padx=20, pady=5, borderwidth=3, command=search_list).grid(row=1, column=7)
        Button(frame, text="Back", padx=20, pady=5, borderwidth=3,
               command=lambda: [view_prc.list.clear(), home_page()]).grid(row=1, column=8)

        edit_button = Button(frame, text="Edit", padx=15, pady=5, borderwidth=3,
                             command=lambda: [view_prc.edit(edit_button)])
        edit_button.grid(row=1, column=9)

        view_prc.recover()

    @staticmethod
    def add():
        data = search_list.data
        view_prc.save_data.append([data.name, data.type, data.prc, data.l, data.w, data.h, 1])
        view_prc(data.name, data.type, data.prc, data.l, data.w, data.h, 1)
        rows = view_prc.list[-1].row
        view_prc.save_data[-1].append(rows)
        # for n, x in enumerate(prc_list.list[-1].set):
        #     x.grid(row=rows, column=n)

    @staticmethod
    def recover():
        for index in range(0, len(view_prc.save_data)):
            data = view_prc.save_data[index]
            view_prc(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            # rows = prc_list.list[-1].row
            # for n, x in enumerate(prc_list.list[-1].set):
            #     x.grid(row=rows, column=n)

    def refresh(self, event):
        try:
            l = float(self.set[3].get())
            w = float(self.set[4].get())
            h = float(self.set[5].get())
            qty = int(self.set[6].get())
        except ValueError:
            print('Value is not integer or floating point')
            return

        self.m3 = self.cal_prc(l, w, h)
        self.t_prc = round((self.m3 * self.prc), 2)

        self.set[7].configure(text=self.m3)
        self.set[8].configure(text=self.t_prc)

        view_prc.all_t_price = 0
        for x in self.list:
            view_prc.all_t_price += x.t_prc

        self.total.configure(text=round(view_prc.all_t_price, 2))

        self.qty = qty

        for data in self.save_data:
            if self.row in data:
                data[3] = l
                data[4] = w
                data[5] = h
                data[6] = self.qty
                break

    @staticmethod
    def edit(edit_button):
        for x in view_prc.list:
            view_prc.modify_button(x, False)
            edit_button.configure(text='Delete', command=lambda: [
                view_prc.modify_button(x, True),
                view_prc.delete(x),
                view_prc.list.clear(),
                view_prc.list_price()
            ])

    def modify_button(self, delete):
        if delete is False:
            self.check_btt.grid(row=self.row, column=9, sticky='w')

        else:
            self.check_btt.grid_forget()

    def delete(self):
        index_list = [x.row for x in self.list if x.bool_del.get() is True]
        for x in index_list:
            for y in self.save_data:
                if x == y[-1]:
                    self.save_data.remove(y)
                    break
        row = 4
        for y in self.save_data:
            y[-1] = row
            row += 1

    @staticmethod
    def save_file():
        file_dir = filedialog.asksaveasfilename(defaultextension='.xlsx',
                                                filetypes=[
                                                    ("Excel Workbook", ".xlsx")
                                                ])
        if not file_dir:
            return
        data = {
            'Part': [x[0] for x in view_prc.save_data],
            'Material': [x[1] for x in view_prc.save_data],
            'Price': [x[2] for x in view_prc.save_data],
            'Length': [x[3] for x in view_prc.save_data],
            'Width': [x[4] for x in view_prc.save_data],
            'Depth': [x[5] for x in view_prc.save_data],
            'QTY': [x.qty for x in view_prc.list],
            'm3': [x.m3 for x in view_prc.list],
            'TOTAL': [x.t_prc for x in view_prc.list]
        }
        file = pd.DataFrame(data)
        last_r = len(file)
        file.loc[last_r, 'm3'] = 'Total'
        file.loc[last_r, 'TOTAL'] = view_prc.all_t_price
        file.to_excel(file_dir, index=False)


class search_list:
    data = None
    store = [[], [], [], [], [], [], []]

    def __init__(self):
        self.window = Toplevel(width=1200, height=600)
        Label(self.window, text="No", padx=16, pady=20, borderwidth=2, relief='groove').grid(row=0, column=0)
        Label(self.window, text="Parts", padx=80, pady=20, borderwidth=2, relief='groove').grid(row=0, column=1)
        Label(self.window, text="Materials", padx=69, pady=20, borderwidth=2, relief='groove').grid(row=0, column=2)
        Label(self.window, text="Price", padx=26, pady=20, borderwidth=2, relief='groove').grid(row=0, column=3)
        Label(self.window, text="Length", padx=24, pady=20, borderwidth=2, relief='groove').grid(row=0, column=4)
        Label(self.window, text="Width", padx=26, pady=20, borderwidth=2, relief='groove').grid(row=0, column=5)
        Label(self.window, text="Height", padx=24, pady=20, borderwidth=2, relief='groove').grid(row=0, column=6)

        self.no = Entry(self.window, width=5, borderwidth=2, relief='groove')
        self.no.grid(row=1, column=0)
        self.name = Entry(self.window, width=30, borderwidth=2, relief='groove')
        self.name.grid(row=1, column=1)
        self.type = Entry(self.window, width=30, borderwidth=2, relief='groove')
        self.type.grid(row=1, column=2)
        self.price = Entry(self.window, width=10, borderwidth=2, relief='groove')
        self.price.grid(row=1, column=3)
        self.length = Entry(self.window, width=12, borderwidth=2, relief='groove')
        self.length.grid(row=1, column=4)
        self.width = Entry(self.window, width=12, borderwidth=2, relief='groove')
        self.width.grid(row=1, column=5)
        self.height = Entry(self.window, width=12, borderwidth=2, relief='groove')
        self.height.grid(row=1, column=6)
        self.all_entrybox = [
            self.no,
            self.name,
            self.type,
            self.price,
            self.length,
            self.width,
            self.height
        ]
        self.data_list = ttk.Treeview(self.window)
        self.data_list['columns'] = ('name', 'type', 'price', 'length', 'width', 'depth')
        self.data_list.column('#0', anchor=CENTER, width=-35)
        self.data_list.column('name', anchor=W, width=100)
        self.data_list.column('type', anchor=W, width=100)
        self.data_list.column('price', anchor=W, width=0)
        self.data_list.column('length', anchor=W, width=0)
        self.data_list.column('width', anchor=W, width=0)
        self.data_list.column('depth', anchor=W, width=0)

        self.data_list.heading('#0', text='No', anchor=W)
        self.data_list.heading('name', text='Part', anchor=W)
        self.data_list.heading('type', text='Material', anchor=W)
        self.data_list.heading('price', text='Price', anchor=W)
        self.data_list.heading('length', text='Length', anchor=W)
        self.data_list.heading('width', text='Width', anchor=W)
        self.data_list.heading('depth', text='Depth', anchor=W)
        self.data_list.grid(row=2, column=0, columnspan=7, sticky='NSWE')

        self.scrollbar = Scrollbar(self.window, orient='vertical', command=self.data_list.yview)
        # noinspection PyArgumentList
        self.data_list.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=2, column=7, sticky='nsw')

        self.update()
        self.data_list.bind('<ButtonRelease-1>', self.select)

        self.no.bind('<KeyRelease>', lambda event: self.search(event, self.no, 'no'))
        self.name.bind('<KeyRelease>', lambda event: self.search(event, self.name, 'name'))
        self.type.bind('<KeyRelease>', lambda event: self.search(event, self.type, 'type'))
        self.price.bind('<KeyRelease>', lambda event: self.search(event, self.price, 'price'))
        self.length.bind('<KeyRelease>', lambda event: self.search(event, self.length, 'length'))
        self.width.bind('<KeyRelease>', lambda event: self.search(event, self.width, 'width'))
        self.height.bind('<KeyRelease>', lambda event: self.search(event, self.height, 'height'))

        Button(self.window, text="Add", padx=25, pady=5, borderwidth=3, command=view_prc.add).grid(row=3, column=6)

    def select(self, event):
        for n in self.all_entrybox:
            n.delete(0, END)

        selected = self.data_list.focus()
        value = self.data_list.item(selected, 'values')

        self.all_entrybox[0].insert(0, selected)
        for n, x in enumerate(value):
            n += 1
            self.all_entrybox[n].insert(0, x)

        search_list.data = wood.w_list[int(selected)]

    def search(self, event, entry, data):
        clear = False
        index = None
        word = entry.get()
        l_word = len(word)

        if data == 'no':
            self.store[0].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word in str(value.no)[0:l_word]:
                        index = value.no
                        self.store[0].append(index)

                if index is None:
                    clear = True

        if data == 'name':
            self.store[1].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word.lower() in value.name.lower()[0:l_word]:
                        index = value.no
                        self.store[1].append(index)

                if index is None:
                    clear = True

        elif data == 'type':
            self.store[2].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word.lower() in value.type.lower()[0:l_word]:
                        index = value.no
                        self.store[2].append(index)

                if index is None:
                    clear = True

        elif data == 'price':
            self.store[3].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word in str(value.prc)[0:l_word]:
                        index = value.no
                        self.store[3].append(index)

                if index is None:
                    clear = True

        elif data == 'length':
            self.store[4].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word in str(value.l)[0:l_word]:
                        index = value.no
                        self.store[4].append(index)

                if index is None:
                    clear = True

        elif data == 'width':
            self.store[5].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word in str(value.w)[0:l_word]:
                        index = value.no
                        self.store[5].append(index)

                if index is None:
                    clear = True

        elif data == 'height':
            self.store[6].clear()
            if word == "":
                pass
            else:
                for value in wood.w_list:
                    if word in str(value.h)[0:l_word]:
                        index = value.no
                        self.store[6].append(index)

                if index is None:
                    clear = True

        if clear is True:
            for record in self.data_list.get_children():
                self.data_list.delete(record)
        else:
            sort_list = []
            empty = 0

            for n in range(0, 7):
                if not self.store[n]:
                    empty += 1
                    continue

                elif not sort_list:
                    sort_list = self.store[n].copy()

                temp_list = [x for x in self.store[n] if x in sort_list]

                sort_list = temp_list.copy()
                temp_list.clear()

            for record in self.data_list.get_children():
                self.data_list.delete(record)

            if empty == 7:
                self.update()
                return

            for x in sort_list:
                for y in wood.w_list:
                    if x == y.no:
                        self.data_list.insert(parent='', index='end', iid=y.no, text=y.no,
                                              values=(y.name, y.type, y.prc, y.l, y.w, y.h))

    def update(self):
        for x in wood.w_list:
            self.data_list.insert(parent='', index='end', iid=x.no, text=x.no,
                                  values=(x.name, x.type, x.prc, x.l, x.w, x.h))


def refresh_frame():
    global frame
    frame.destroy()
    frame = Frame(screen, width=1200, height=600)
    frame.grid(row=0, column=0, sticky='news')
    frame.tkraise()


def add(list, wood_bl, hardware_bl):
    if wood_bl is True:
        for x, y in enumerate(list):
            z = y.get()
            list[x] = z
        if list[0] == "":
            list[0] = '-'
        no = len(wood_file.index)

        try:
            wood(no, list[0], list[1], list[2], list[3], list[4], list[5])
        except:
            messagebox.showerror(title="Error", message="Please fill correctly")
            return

        wood_file.loc[no] = [x for x in list]
        save_file(wood_file, 'Sheet1')
        print(wood_file)

    if hardware_bl is True:
        for x, y in enumerate(list):
            z = y.get()
            list[x] = z
        no = len(hardware_file.index)
        hardware(no, list[0], list[1])
        t_rows = len(hardware_file.index)
        hardware_file.loc[t_rows] = [x for x in list]
        save_file(hardware_file, 'Sheet2')
        print(hardware_file)


def home_page():
    refresh_frame()
    txt = Label(frame, text="Menu", font="28")
    txt.place(x=600, y=20, anchor="center")
    view1 = Button(frame, text="View wood", padx=30, pady=5, anchor="center", font="28", command=view_wood)
    view1.place(x=600, y=100, anchor="center")
    view2 = Button(frame, text="View hardware", padx=30, pady=5, anchor="center", font="28", command=view_hardware)
    view2.place(x=600, y=160, anchor="center")
    view3 = Button(frame, text="View price", padx=30, pady=5, anchor="center", font="28", command=view_prc.list_price)
    view3.place(x=600, y=220, anchor="center")


def save_file(file, sheetname):
    with pd.ExcelWriter('Wood file.xlsx', engine='openpyxl', mode='a') as writer:
        workbook = writer.book
        workbook.remove(workbook[sheetname])
    with pd.ExcelWriter('Wood file.xlsx', engine='openpyxl', mode='a') as writer:
        file.to_excel(writer, sheetname, index=False)


wood_file = pd.read_excel("Wood file.xlsx", "Sheet1")
column1 = [x for x in wood_file.columns]
t_row = len(wood_file.index)

for r in range(0, t_row):
    no = r
    name = wood_file.loc[r, column1[0]]
    if str(name) == 'nan':
        name = '-'
    type = wood_file.loc[r, column1[1]]
    price = wood_file.loc[r, column1[2]]
    length = wood_file.loc[r, column1[3]]
    width = wood_file.loc[r, column1[4]]
    height = wood_file.loc[r, column1[5]]
    wood(no, name, type, price, length, width, height)

hardware_file = pd.read_excel("Wood file.xlsx", "Sheet2")
column2 = [x for x in hardware_file.columns]
t_row = len(hardware_file.index)

for r in range(0, t_row):
    no = r
    name = hardware_file.loc[r, column2[0]]
    price = hardware_file.loc[r, column2[1]]
    hardware(no, name, price)

screen = Tk()
screen.geometry("1200x600")
frame = Frame(screen)

home_page()
screen.mainloop()
