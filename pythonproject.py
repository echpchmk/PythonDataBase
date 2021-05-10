import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import  scrolledtext


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        root_frame = tk.Frame(root)
        root_frame['bg'] = '#FFFFFF'
        root_frame.pack(expand=1)
        btn_open_add_data = tk.Button(root_frame,
                                      text='Добавление данных', font="20", command=self.open_add_data, bg='#009900', fg='#FFFFFF',
                                    activebackground='#009933', compound=tk.TOP, width=20, height=3)
        btn_open_add_data.pack(expand=1, pady=20)
        btn_open_change_data = tk.Button(root_frame,
                                         text='Изменение данных', font="20", command=self.open_change_data,
                                      bg='#009900', fg='#FFFFFF',
                                      activebackground='#009933', compound=tk.TOP, width=20, height=3)
        btn_open_change_data.pack(expand=1, pady=20)
        btn_open_statistics = tk.Button(root_frame,
                                        text='Статистика и графики', font="20", command=self.open_statistics,
                                      bg='#009900', fg='#FFFFFF',
                                      activebackground='#009933', compound=tk.TOP, width=20, height=3)
        btn_open_statistics.pack(expand=1, pady=20)
        btn_exitroot = tk.Button(root, text='Выход', bg='#009900', fg='#FFFFFF', width=8,
                                      activebackground='#009933', command=self.exitroot)
        btn_exitroot.pack(pady = 20)

    def open_add_data(self):
        add_data()
    def open_change_data(self):
        change_data()
    def open_statistics(self):
        statistics()
    def exitroot(self):
        root.destroy()

class add_data(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.title('Добавление данных')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        tk.Label(self, bg='#bfffbf').place(relx=0.05, rely=0.05,
                                           relwidth=0.9, relheight=0.83)
        self.lbl_1 = tk.Label(self, text='Бренд:', bg='#bfffbf')
        self.lbl_1.place(x=70, y=50)
        self.entry_lbl1 = tk.Entry(self, width=20, bg='#f4f4f4')
        self.entry_lbl1.place(x=115, y=50)
        self.lbl_2 = tk.Label(self, text='Модель:', bg='#bfffbf')
        self.lbl_2.place(x=265, y=50)
        self.entry_lbl2 = tk.Entry(self, width=40, bg='#f4f4f4')
        self.entry_lbl2.place(x=320, y=50)
        self.lbl_3 = tk.Label(self, text='Год:', bg='#bfffbf')
        self.lbl_3.place(x=70, y=80)
        self.entry_lbl3 = tk.Entry(self, width=7, bg='#f4f4f4')
        self.entry_lbl3.place(x=100, y=80)
        lbl_4 = tk.Label(self, text='Месяц:', bg='#bfffbf')
        lbl_4.place(x=150, y=80)
        combo1 = Combobox(self, width=10)
        combo1.place(x=200, y=80)
        combo1['values'] = ('Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь')
        combo1.current(0)
        lbl_5 = tk.Label(self, text='День:', bg='#bfffbf')
        lbl_5.place(x=290, y=80)
        combo2 = Combobox(self, width=3)
        combo2.place(x=330, y=80)
        combo2['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
        combo2.current(0)
        lbl_7 = tk.Label(self, text='Идентификатор:', bg='#bfffbf')
        lbl_7.place(x=380, y=80)
        entry_lbl7 = tk.Entry(self, width=14, bg='#f4f4f4')
        entry_lbl7.place(x=477, y=80)
        lbl_8 = tk.Label(self, text='Розничная цена, $:', bg='#bfffbf')
        lbl_8.place(x=70, y=110)
        entry_lbl8 = tk.Entry(self, width=5, bg='#f4f4f4')
        entry_lbl8.place(x=180, y=110)
        lbl_9 = tk.Label(self, text='Основной цвет:', bg='#bfffbf')
        lbl_9.place(x=220, y=110)
        entry_lbl9 = tk.Entry(self, width=15, bg='#f4f4f4')
        entry_lbl9.place(x=315, y=110)
        btn1 = tk.Button(self,
                                      text='Добавить', command='', bg='#009900',
                                      fg='#FFFFFF',
                                      activebackground='#009933', compound=tk.TOP, width=20)
        btn1.pack(pady=150)
        lbl_15 = tk.Label(self, text='Идентификатор:', bg='#bfffbf')
        lbl_15.place(x=70, y=210)
        entry_lbl15 = tk.Entry(self, width=28, bg='#f4f4f4')
        entry_lbl15.place(x=172, y=210)
        lbl_10 = tk.Label(self, text='Средняя цена перепродажи в 2016 году, $:', bg='#bfffbf')
        lbl_10.place(x=70, y=240)
        entry_lbl10 = tk.Entry(self, width=5, bg='#f4f4f4')
        entry_lbl10.place(x=310, y=240)
        lbl_11 = tk.Label(self, text='Средняя цена перепродажи в 2017 году, $:', bg='#bfffbf')
        lbl_11.place(x=70, y=270)
        entry_lbl11 = tk.Entry(self, width=5, bg='#f4f4f4')
        entry_lbl11.place(x=310, y=270)
        lbl_12 = tk.Label(self, text='Средняя цена перепродажи в 2018 году, $:', bg='#bfffbf')
        lbl_12.place(x=70, y=300)
        entry_lbl12 = tk.Entry(self, width=5, bg='#f4f4f4')
        entry_lbl12.place(x=310, y=300)
        lbl_13 = tk.Label(self, text='Средняя цена перепродажи в 2019 году, $:', bg='#bfffbf')
        lbl_13.place(x=70, y=330)
        entry_lbl13 = tk.Entry(self, width=5, bg='#f4f4f4')
        entry_lbl13.place(x=310, y=330)
        lbl_14 = tk.Label(self, text='Средняя цена перепродажи в 2020 году, $:', bg='#bfffbf')
        lbl_14.place(x=70, y=360)
        entry_lbl14 = tk.Entry(self, width=5, bg='#f4f4f4')
        entry_lbl14.place(x=310, y=360)
        btn2 = tk.Button(self,
                         text='Добавить', command='', bg='#009900',
                         fg='#FFFFFF',
                         activebackground='#009933', compound=tk.TOP, width=20)
        btn2.pack(pady=75)
        btn_exitroot = tk.Button(self, text='Выход', bg='#009900', fg='#FFFFFF', width=8,
                                 activebackground='#009933', command=self.exitself)
        btn_exitroot.place(x=292,y=452)

    def exitself(self):
        self.destroy()


class change_data(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.title('Изменение данных')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        self['bg'] = '#FFFFFF'
        self.grab_set()
        self.focus_get()
        tk.Label(self, bg='#bfffbf').place(relx=0.05, rely=0.05,
                                           relwidth=0.9, relheight=0.83)
        lbl_2 = tk.Label(self, text='База данных №:', bg='#bfffbf')
        lbl_2.place(x=70, y=50)
        combo2 = Combobox(self, width=3)
        combo2.place(x=165, y=50)
        combo2['values'] = (1,2)
        combo2.current(0)
        lbl_1 = tk.Label(self, text='Фильтр:', bg='#bfffbf')
        lbl_1.place(x=210, y=50)
        combo1 = Combobox(self, width=30)
        combo1.place(x=260, y=50)
        combo1['values'] = ('Фильтр 1','Фильтр 2','Фильтр 3','Фильтр 4')
        combo1.current(0)
        entry_lbl2 = tk.Entry(self, width=65, bg='#f4f4f4')
        entry_lbl2.place(x=73, y=80)
        btn1 = tk.Button(self,
                         text='Вывести', command='', bg='#009900',
                         fg='#FFFFFF',
                         activebackground='#009933', width=12)
        btn1.place(x=480,y=60)
        txt = scrolledtext.ScrolledText(self, width=60, height=17, bg='#f4f4f4')
        txt.place(x=73, y=110)
        btn_exitroot = tk.Button(self, text='Выход', bg='#009900', fg='#FFFFFF', width=8,
                                 activebackground='#009933', command=self.exitself)
        btn_exitroot.place(x=292, y=452)
        btn_save = tk.Button(self, text='Сохранить', bg='#009900', fg='#FFFFFF', width=8,
                                 activebackground='#009933', command='')
        btn_save.place(x=240, y=400)
        btn_del = tk.Button(self, text='Удалить', bg='#009900', fg='#FFFFFF', width=8,
                                 activebackground='#009933', command='')
        btn_del.place(x=340, y=400)



    def exitself(self):
        self.destroy()

class statistics(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.title('Статистика и графики')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        tk.Label(self, bg='#bfffbf').place(relx=0.05, rely=0.05,
                                           relwidth=0.9, relheight=0.83)
        lbl_1 = tk.Label(self, text='Фильтр:', bg='#bfffbf')
        lbl_1.place(x=70, y=50)
        combo1 = Combobox(self, width=30)
        combo1.place(x=125, y=50)
        combo1['values'] = ('Фильтр 1', 'Фильтр 2', 'Фильтр 3', 'Фильтр 4')
        combo1.current(0)
        btn_graf=tk.Button(self, text='Построить график', bg='#009900', fg='#FFFFFF',
                                 activebackground='#009933', command='')
        btn_graf.place(x=340, y=50)
        btn_stat = tk.Button(self, text='Показать статистику', bg='#009900', fg='#FFFFFF',
                             activebackground='#009933', command=self.open_show_stat)
        btn_stat.place(x=460, y=50)
        btn_exitroot = tk.Button(self, text='Выход', bg='#009900', fg='#FFFFFF', width=8,
                                 activebackground='#009933', command=self.exitself)
        btn_exitroot.place(x=292, y=452)


    def exitself(self):
        self.destroy()

    def open_show_stat(self):
        show_stat()


class show_stat(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.title('Статистика')
        self.geometry('650x500+435+100')
        self.resizable(False, False)
        tk.Label(self,bg='#bfffbf').place(relx=0.05, rely=0.05,
                                relwidth=0.9, relheight=0.83)
        self.grab_set()
        self.focus_get()
        self['bg'] = '#FFFFFF'
        btn_exitroot = tk.Button(self, text='Выход', bg='#009900', fg='#FFFFFF', width=8,
                                 activebackground='#009933', command=self.exitself)
        btn_exitroot.place(x=292, y=452)

    def exitself(self):
        self.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title('SneakerAnalysis')
    root.geometry('650x500+435+100')
    root['bg'] = '#FFFFFF'
    root.resizable(False, False)
    root.mainloop()
