
"""
Решение квадратного уравнения

Автор: Клинцов Сергей
E-mail: sklis@yandex.ru
2022-2023
"""
from tkinter import Tk, Label, Button, Entry, StringVar, Menu, LabelFrame
from tkinter import messagebox as mb
import math
from pathlib import Path
import re
import tkinter.filedialog as fd
from typing import Union, TextIO
import pyautogui
from datetime import datetime
from idlelib.tooltip import Hovertip


def open_file():
    """Выбор файла для записи результатов расчета."""
    filetypes = (('Текстовый файл', '*.txt'),
                 ('Изображение', '*.jpg *.gif *.png'),
                 ('Любой', '*'))
    clock_t = str(datetime.now().time())
    clock_t = clock_t.replace(':', '').replace('.', '')
    filename = fd.asksaveasfilename(title='Открыть файл',
                                    initialfile='rez' + clock_t + '.txt',
                                    initialdir='/',
                                    filetypes=filetypes)
    if filename:
        save_report(filename)


def open_file_screenshot():
    """Выбор файла для записи результатов расчета."""
    filetypes = (('Изображение', '*.jpg *.gif *.png'),
                 ('Текстовый файл', '*.txt'),
                 ('Любой', '*'))
    clock_t = str(datetime.now().time())
    clock_t = clock_t.replace(':', '').replace('.', '')
    file_name_screenshot: str = fd.asksaveasfilename(title='Открыть файл',
                                                     initialfile='screenshot' + clock_t + '.png',
                                                     initialdir='/',
                                                     filetypes=filetypes)
    if file_name_screenshot:
        screenshot_save_to_disk(file_name_screenshot)


def save_report(filename, file_out=None):
    """Вывод результата расчета корней в файл."""
    try:
        file_out: TextIO = open(filename, 'a', encoding='utf-8')
        clock_w = str(datetime.today())
        file_out.write(clock_w[:19] + '\n')
        file_out.write('Квадратное уравнение вида:\n')
        file_out.write('(' + str(ax1) + ')*x^2 + (' + str(bx1) + ')*x + (' + str(cx1) + ') = 0\n')
        file_out.write(out_rez.pop(0) + '\n')
        file_out.write(out_rez.pop(0) + '\n')
        file_out.write(out_rez.pop(0) + '\n\n')
        file_out.close()
        mb.showinfo('Save', 'Результаты сохранены в файле: \n' + filename)
    except FileNotFoundError:
        mb.showerror('Невозможно открыть файл.')
    finally:
        file_out.close()


def help_prog():
    """Необходимые пояснения."""
    mb.showinfo('Help', '''Необходимые пояснения.''')


def about():
    """Краткая информация о программе и авторе."""
    mb.showinfo('Об этом:', 'Программа расчёта и вывода в файл\n'
                            'корней квадратного уравнения\n'
                            'Автор: Клинцов Сергей.\n'
                            'E-mail: sklis@yandex.ru')


def a_go():
    """Получение ввода первого числа A и проверка его корректности."""
    global ax1
    try:
        re.match(num_format, ent_ax.get())
        ax1 = float(ent_ax.get())
        ent_a['state'] = 'disabled'
        but_a.configure(text='Верно')
        but_a['state'] = 'disabled'
        frame_b.place(x=20, y=85)
        lab_b.place(x=2, y=2)
        ent_b.place(x=65, y=2)
        but_b.place(x=175, y=-2)
        statusbar.configure(text="Введите второй коэффициент B")
    except Exception:
        mb.showerror('Введено A.', 'A=' + ent_ax.get() + '\n Значение НЕ верно.\n Введите правильное значение.')
        ent_ax.set('')


def b_go():
    """Получение ввода второго числа B и проверка его корректности."""
    global bx1
    try:
        re.match(num_format, ent_bx.get())
        bx1 = float(ent_bx.get())
        ent_b['state'] = 'disabled'
        but_b.configure(text='Верно')
        but_b['state'] = 'disabled'
        frame_c.place(x=20, y=135)
        lab_c.place(x=2, y=2)
        ent_c.place(x=65, y=2)
        but_c.place(x=175, y=-2)
        statusbar.configure(text="Введите свободное число C")
    except Exception:
        mb.showerror('Введено B.', 'B=' + ent_bx.get() + '\n Значение НЕ верно.\n Введите правильное значение.')
        ent_bx.set('')


def c_go():
    """Получение ввода третьего числа C и проверка его корректности."""
    global cx1
    try:
        re.match(num_format, ent_cx.get())
        cx1 = float(ent_cx.get())
        ent_c['state'] = 'disabled'
        but_c.configure(text='Верно')
        but_c['state'] = 'disabled'
        lab_4.configure(bg='#2ADDA2')
        lab_4['text'] = '(' + str(ax1) + ')*x^2 + (' + str(bx1) + ')*x + (' + str(cx1) + ') = 0'
        lab_4.place(x=5, y=200)
        but_4.place(x=80, y=230)
        statusbar.configure(text="Получилось такое уравнение.")
    except Exception:
        mb.showerror('Введено C.', 'C=' + ent_cx.get() + '\n Значение НЕ верно.\n Введите правильное значение.')
        ent_cx.set('')


def korni_go():
    """Вычисление корней квадратного уравнения."""
    but_4['state'] = 'disabled'
    frame_k.place(x=10, y=265)
    d_x = (bx1 ** 2) - 4 * ax1 * cx1
    statusbar.configure(text="Расчёт можно сохранить в файл или скриншот.")
    if d_x > 0:
        pkz = math.sqrt((abs(d_x)))
        k1 = (-bx1 + pkz) / (2 * ax1)
        k2 = (-bx1 - pkz) / (2 * ax1)
        Label(frame_k, text='Корни \nразные.').place(x=15, y=20)
        Label(frame_k, text='K1=' + str(k1)).place(x=110, y=10)
        Label(frame_k, text='K2=' + str(k2)).place(x=110, y=40)
        out_rez.insert(0, 'Корни различные:')
        out_rez.insert(1, 'K1=' + str(k1))
        out_rez.insert(2, 'K2=' + str(k2))

    if d_x == 0:
        k1 = k2 = (-bx1) / (2 * ax1)
        Label(frame_k, text='Корни \nодинаковые.').place(x=15, y=20)
        Label(frame_k, text='K1=' + str(k1)).place(x=110, y=10)
        Label(frame_k, text='K2=' + str(k2)).place(x=110, y=40)
        out_rez.insert(0, 'Корни одинаковые:')
        out_rez.insert(1, 'K1=' + str(k1))
        out_rez.insert(2, 'K2=' + str(k2))

    if d_x < 0:
        Label(frame_k, text='Корни \nкомплексные.').place(x=15, y=20)
        Label(frame_k, text='K1=' + str(-bx1 / (2 * ax1)) + '+i' + str(d_x)).place(x=110, y=10)
        Label(frame_k, text='K2=' + str(-bx1 / (2 * ax1)) + '-i' + str(d_x)).place(x=110, y=40)
        out_rez.insert(0, 'Корни комплексные:')
        out_rez.insert(1, 'K1=' + str(-bx1 / (2 * ax1)) + '+i' + str(d_x))
        out_rez.insert(2, 'K2=' + str(-bx1 / (2 * ax1)) + '-i' + str(d_x))


def screenshot_save_to_disk(file_name_screenshot):
    """Сохранение screenshot экрана на диск."""
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    screenshot = pyautogui.screenshot(region=(f"{center_x + 5}",
                                              f"{center_y - 5}",
                                              f"{window_width}",
                                              f"{window_height + 10}"))
    screenshot.save(file_name_screenshot)
    n = str(file_name_screenshot)
    mb.showinfo('Инфо', f"Результаты расчёта сохранены в виде screenshot в файле {n}.")


def end_prog():
    """Выход из программы."""
    statusbar.configure(text="Расчёт закончен. До встречи!.")
    root.quit()


def set_window_geometry():
    """Размещение окна программы посередине экрана. """
    # get the screen dimension
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # find the center point
    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)
    # set the position of the window to the center of the screen
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


def tick():
    """Текущее время в нижнем правом углу."""
    # get the current local time from the PC
    clock_t = str(datetime.now().time())
    clock["text"] = " " + clock_t[:8] + " "
    # if time string has changed, update it
    # calls itself every 200 milliseconds to update the time
    # display as needed could use >200 ms
    clock.after(200, tick)


# ---___---___---___---___---___---___---___---___---___---___---___---___---___---___---___---___

""" Основной блок программы."""
# Формируем главыное окно вывода.
root = Tk()

# Объявляем глобальные переменные.
ax1: float = 1.0
bx1: float = 1.0
cx1: float = -5.0
# Объявляем переменные полей ввода.
ent_ax = StringVar()
ent_bx = StringVar()
ent_cx = StringVar()
# Начальные значения для переменных A, B, C.
ent_ax.set('1.0')
ent_bx.set('1.0')
ent_cx.set('-5.0')
# Переменная списка для вывода корней в файл. Аргументы могут быть либо str, либо int типов.
out_rez: list[Union[str, int]] = []
# Формируем шаблон проверки вводимых значений коэффициентов.
num_format = re.compile("^[\-\+]?[0-9]?[\d]*\.?[\d]*$")
# Задаем размеры и положение окна.
window_width: int = 300
window_height: int = 470
# устанавливаем окно в центре экрана.
set_window_geometry()
# Задаем заголовок окна.
root.title('Квадратное уравнение')
# Запрещаем изменение размеров окна.
root.resizable(False, False)
# Получаем текущий каталог(папку).
current_dir = Path.cwd()
# Размещаем иконку окна
root.wm_iconbitmap(str(current_dir) + "//kvur.ico")
# Размещаем строку статуса внизу окна.
statusbar: object = Label(root, bd=2, relief="sunken", anchor="w")
statusbar.pack(side="bottom", fill="x")

# Создаем пункты меню в окне
main_menu = Menu(root)

file_menu = Menu(root, tearoff=0)  # отключение плавающего меню root.option_add('*tearOff', False)
file_menu.add_command(label='В файл', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='ScreenShot', command=open_file_screenshot)
main_menu.add_cascade(label='Сохранить результат', menu=file_menu)

help_menu = Menu(root, tearoff=0)
help_menu.add_command(label='Помощь', command=help_prog)
help_menu.add_command(label='О программе', command=about)
main_menu.add_cascade(label='Справка', menu=help_menu)

main_menu.add_cascade(label='Выход', command=end_prog)
root.config(menu=main_menu)

# Текст заголовка окна формулы квадратного уравнения.
lab_0 = Label(root)
lab_0.configure(width=40, justify='center', bg='#00FF00', relief="raised", bd=4)
lab_0.place(x=5, y=8)
lab_0['text'] = 'А*x^2 + B*x + C = 0'
# Метка текущего времени в нижней привой части окна.
clock = Label(root)
clock.configure(bg='#00ff00', foreground="red", font=('times', 15, 'bold'), bd=2, relief="groove")
clock.place(x=215, y=400)

# Блок кода обработки ввода переменной A.
statusbar.configure(text="Введите первый коэффициент A")
frame_a = LabelFrame(root)
frame_a.configure(text='A', width=250, height=50)
frame_a.place(x=20, y=35)
# Поле ввода значения коэффициента A.
lab_a = Label(frame_a, text='Число А')
lab_a.place(x=2, y=2)
ent_a = Entry(frame_a)
ent_a.configure(width=15, justify='center', textvariable=ent_ax, state='normal')
ent_a.place(x=65, y=2)
tip_a = Hovertip(ent_a, 'Введите число для коэфициента А')
# Кнопка принятия и подтверждения правильности ввода значения A.
but_a = Button(frame_a)
but_a.configure(text='Ввести A', command=a_go)
but_a.place(x=175, y=-2)

# Блок кода обработки ввода переменной B.
frame_b = LabelFrame(root)
frame_b.configure(text='B', width=250, height=50)
# Поле ввода значения коэффициента B.
lab_b = Label(frame_b, text='Число B')
ent_b = Entry(frame_b)
ent_b.configure(width=15, justify='center', textvariable=ent_bx, state='normal')
tip_b = Hovertip(ent_b, 'Введите число для коэфициента B')
# Кнопка принятия и подтверждения правильности ввода значения B.
but_b = Button(frame_b)
but_b.configure(text='Ввести B', command=b_go)

# Блок кода обработки ввода переменной C.
frame_c = LabelFrame(root)
frame_c.configure(text='C', width=250, height=50)
# Поле ввода значения коэффициента C.
lab_c = Label(frame_c, text='Число C')
ent_c = Entry(frame_c)
ent_c.configure(width=15, justify='center', textvariable=ent_cx, state='normal')
tip_c = Hovertip(ent_c, 'Введите число для коэфициента C')
# Кнопка принятия и подтверждения правильности ввода значения C.
but_c = Button(frame_c)
but_c.configure(text='Ввести C', command=c_go)

# Строка показа вида получившегося квадратного уравнения.
lab_4 = Label(root)
lab_4.configure(width=40, justify='center', bd=4, relief="ridge")
# Кнопка запуска расчета корней квадратного уравнения.
but_4 = Button(root, text='Посчитать корни', command=korni_go)
tip_4 = Hovertip(but_4, 'Рассчитать корни уравнения для введённых коэффициентов A, B, C.')

# Блок вывода рассчитанных корней квадратного уравнения.
frame_k = LabelFrame(root)
frame_k.configure(text='Корни квадратного уравнения', width=280, height=100)

#  Установка текущего времени в поле окна.
tick()
# Команда активации главного окна вывода.
root.mainloop()
