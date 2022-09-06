import calculations

# Фронтенд программы

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def convStN(str_data):
    str_num = ""
    arr_num = []
    i = 0
    length = len(str_data)

    for elem in str_data:
        if elem.isdigit() or elem == "." or elem == ",":
            if elem == ",":
                elem = "."
            str_num += elem
        elif is_number(str_num):
            arr_num.append(float(str_num))
            str_num = ""
        elif len(arr_num) < 1 and i >= length - 1:
            return True
        i += 1

    if len(arr_num) > 0 and is_number(str_num):
        arr_num.append(float(str_num))

    if len(arr_num) <= 1:
        return False

    return arr_num

def clickCalc():
    str_data = str_nums.get()  # Получаю строку с массивом чисел
    arr_data = []

    if (str_data != ""):
        arr_data = convStN(str_data)  # Получаю массив с числами

        if arr_data != False and arr_data != True:
            data2 = arr_data.copy()
            count_dat = len(arr_data)

            aver_str.delete(0, END)
            aver_str.insert(0, str(calculations.average(arr_data, count_dat)))

            disp_str.delete(0, END)
            disp_str.insert(0, str(calculations.dispersion(arr_data, count_dat)))

            median_str.delete(0, END)
            median_str.insert(0, str(calculations.median(arr_data, count_dat)))

            mode_str.delete(0, END)
            mode_str.insert(0, str(calculations.mode(arr_data)))

            global _number
            global _len

            _number = 0
            _len = 0

            asym_str.delete(0, END)
            asym_str.insert(0, str(calculations.asymmetry(data2, count_dat)))

            excess_str.delete(0, END)
            excess_str.insert(0, str(calculations.excess(data2, count_dat)))

            notif_str.delete(0, END)
            notif_str.insert(0, "Готово.")
            notif_str.configure({"background": "White"})
        elif arr_data == True:
            notif_str.delete(0, END)
            notif_str.insert(0, "Введены не числа.")
            notif_str.configure({"background": "Red"})
            return
        else:
            notif_str.delete(0, END)
            notif_str.insert(0, "Нужно ввести не менее 2 чисел.")
            notif_str.configure({"background": "Red"})
            return
    else:
        notif_str.delete(0, END)
        notif_str.insert(0, "Числа не введены.")
        notif_str.configure({"background": "Red"})

from tkinter import *

window = Tk()
window.title("Статистический анализ одномерной случайной величины")
window.iconbitmap('terminator.ico') # иконка на окне

# строка с вводом строки с массивом чисел
lbl = Label(window, text="Введите числа через пробел и нажмите кнопку \"Рассчитать\"", font=("Arial Bold", 14))
lbl.grid(column = 0, row = 0, pady="10", padx="10")
lbl_nums = Label(window, text="Введите массив чисел: ", font=("Arial", 12))
lbl_nums.grid(column = 0, row = 1, pady="10", padx="10")
str_nums = Entry(window, width=100)
str_nums.grid(column = 1, row = 1, pady="10", padx="10")
str_nums.focus()

# строка с выводом оповещений (в том числе об ошибках ввода)
notif = Label(window, text="Оповещение: ", font=("Arial", 12))
notif.grid(column = 0, row = 2, pady="10", padx="10")
notif = Entry(window, width=20)
notif_str = Entry(window, width=100)
notif_str.grid(column = 1, row = 2, pady="10", padx="10")

# строка с выводом среднего арифметического
aver = Label(window, text="Среднее арифметическое: ", font=("Arial", 12))
aver.grid(column = 0, row = 3, pady="10", padx="10")
aver = Entry(window, width=100)
aver_str = Entry(window, width=30)
aver_str.grid(column = 1, row = 3, pady="10", padx="10")

# строка с выводом дисперсии
disp = Label(window, text="Дисперсия: ", font=("Arial", 12))
disp.grid(column = 0, row = 4, pady="10", padx="10")
disp = Entry(window, width=100)
disp_str = Entry(window, width=30)
disp_str.grid(column = 1, row = 4, pady="10", padx="10")


# строка с выводом медианы
medi = Label(window, text="Медиана: ", font=("Arial", 12))
medi.grid(column = 0, row = 5, pady="10", padx="10")
medi = Entry(window, width=100)
median_str = Entry(window, width=30)
median_str.grid(column = 1, row = 5, pady="10", padx="10")


# строка с выводом моды
mod = Label(window, text="Мода: ", font=("Arial", 12))
mod.grid(column = 0, row = 6, pady="10", padx="10")
mod = Entry(window, width=100)
mode_str = Entry(window, width=30)
mode_str.grid(column = 1, row = 6, pady="10", padx="10")


# строка с выводом асимметрии
asym = Label(window, text="Асимметрия: ", font=("Arial", 12))
asym.grid(column = 0, row = 7, pady="10", padx="10")
asym = Entry(window, width=100)
asym_str = Entry(window, width=30)
asym_str.grid(column = 1, row = 7, pady="10", padx="10")


# строка с выводом эксцесса
exc = Label(window, text="Эксцесс: ", font=("Arial", 12))
exc.grid(column = 0, row = 8, pady="10", padx="10")
exc = Entry(window, width=100)
excess_str = Entry(window, width=30)
excess_str.grid(column = 1, row = 8, pady="10", padx="10")


# кнопка для старта расчетов
btn = Button(window, text="Рассчитать", command=clickCalc, font=("Arial", 12), cursor="hand2")  # Клик на кнопку и запуск функции
btn.grid(column = 1, row = 9, pady="10")

# запуск программы
window.mainloop()

#str_data = "16.06 15.92 16.01 16.05 15.80 15.97 16.18 16.26 16.22 16.20 16.03 16.31 15.92 16.17 16.07 15.99 16.06 16.07 15.98 16.08 16.09 16.21 16.05 15.87 16.03 16.21 16.23 16.04 15.94 16.03 15.96 16.09 16.24 16.10 15.97 16.16 16.11 16.12 16.14 16.11 16.03 16.03 16.05 16.22 15.97 16.27 16.16 16.32 16.21 16.14 16.23 16.17 16.00 16.13 16.10 15.98 16.12 16.07 16.06 16.11 16.02 15.89 16.29 16.14 15.93 16.17 16.16 15.99 16.15 16.13 16.14 16.05 16.34 16.13 16.13 15.91 16.18 16.06 16.18 16.07 16.09 16.15 16.02 16.08 16.40 16.03 16.16 15.89 16.04 16.15 16.22 16.08 16.09 16.17 16.10 16.11 16.12 16.08 16.13 16.10"
#str_data = "1 1,1 2 3.5 4 5 100"