from tkinter import ttk
import tkinter as tk


def set_texts():

    caption_label.configure(text=languages[0][language_index])
    weight_label.configure(text=languages[1][language_index])
    height_label.configure(text=languages[2][language_index])
    imt_label.configure(text=languages[3][language_index])
    button_calc.configure(text=languages[4][language_index])
    stroka_1.configure(text=languages[5][language_index])
    stroka_2.configure(text=languages[6][language_index])
    stroka_3.configure(text=languages[7][language_index])
    stroka_4.configure(text=languages[8][language_index])
    stroka_5.configure(text=languages[9][language_index])
    stroka_6.configure(text=languages[10][language_index])
    stroka_7.configure(text=languages[11][language_index])
    stroka_8.configure(text=languages[19][language_index])
    stolb_1.configure(text=languages[12][language_index])
    stolb_2.configure(text=languages[13][language_index])
    stolb_3.configure(text=languages[14][language_index])
    stolb_4.configure(text=languages[15][language_index])
    stolb_5.configure(text=languages[16][language_index])
    stolb_6.configure(text=languages[17][language_index])
    stolb_7.configure(text=languages[18][language_index])
    stolb_8.configure(text=languages[20][language_index])
    russian.config(text=languages[21][language_index])
    england.config(text=languages[22][language_index])
    imt_result.configure(text='')
    root.title(languages[25][language_index])

def validate_weight(text):
    return text.isdecimal() or (text == "." and weight_edit.get().find(".") == -1)


def validate_height(text):
    return text.isdecimal() or (text == "." and height_edit.get().find(".") == -1)


def imt_calculate():
    try:
        w = round(float(weight_edit.get()), 4)
    except:
        imt_result.configure(text='')
        return

    if w == 0:
        imt_result.configure(text=languages[23][language_index])
        return

    try:
        h = round(float(height_edit.get()) / 100, 4)
    except:
        imt_result.configure(text=languages[24][language_index])
        return

    if h == 0:
        imt_result.configure(text=languages[24][language_index])
        return

    imt = round(w / (h ** 2), 2)

    imd = 0

    for i in range(len(weights)):
        if imt >= weights[i][0] and imt < weights[i][1]:
            imd = i

    imt_result.config(text=str(imt) + '  -  ' +
                      languages[12 + imd][language_index])


def rus_language():
    global language_index
    language_index = 0
    set_texts()


def eng_language():
    global language_index
    language_index = 1
    set_texts()


languages = []

languages.append(["Калькулятор индекса массы тела (ИМТ)",
                 "Body mass index calculator (BMI)"])
languages.append(["Вес, кг.", "Weight, kg."])
languages.append(["Рост, см.", "height, cm"])
languages.append(["ИМТ", "BMI"])
languages.append(["Рассчитать ИМТ", "Calculate BMI"])

languages.append(["16 и менее", "16 and less"])
languages.append(["16-18,5", "16-18,5"])
languages.append(["18,5 - 25", "18,5 - 25"])
languages.append(["25 - 30", "25 -30"])
languages.append(["30 - 35", "30 -35"])
languages.append(["35 - 40", "35 - 40"])
languages.append(["40 и более", "40 and more"])

languages.append(["Выраженный дефицит массы тела",
                 "Pronounced body weight deficiency"])
languages.append(["Недостаточная (дефицит) масса тела",
                 "Insufficient (deficiency) body weight"])
languages.append(["Норма", "Standard"])
languages.append(["Избыточная масса тела (предожирение)",
                 "Overweight (pre-obesity)"])
languages.append(["Ожирение 1 степени", "Obesity of the 1st degree"])
languages.append(["Ожирение 2 степени", "Obesity of the 2nd degree"])
languages.append(["Ожирение 3 степени", "Obesity of the 3rd degree"])
languages.append(["Индекс массы тела", "Body Mass Index"])
languages.append(["Соответствие между массой человека и его ростом",
                 "The correspondence between the mass of a person and his height"])

languages.append(["рус", "rus"])
languages.append(["англ", "eng"])

languages.append(["введён некорректный вес", "incorrect weight entered"])
languages.append(["введён некорректный рост",
                 "incorrect growth was introduced"])

languages.append(["ИМТ", "BMI"])


weights = []
weights.append([0, 16])
weights.append([16, 18.5])
weights.append([18.5, 25])
weights.append([25, 30])
weights.append([30, 35])
weights.append([40, 999])

language_index = 0


root = tk.Tk()
root.config(width=800, height=300)



caption_label = ttk.Label()
caption_label.place(x=200, y=10, width=780)
caption_label.configure(font=("Helvetica", 18, "bold"))


height_label = ttk.Label()
height_label.place(x=30, y=70, width=80)


height_edit = ttk.Entry(validate="key", validatecommand=(
    root.register(validate_height), "%S"))
height_edit.place(x=100, y=70, width=150)

weight_label = ttk.Label()
weight_label.place(x=30, y=120, width=80)


weight_edit = ttk.Entry(validate="key", validatecommand=(
    root.register(validate_weight), "%S"))
weight_edit.place(x=100, y=120, width=150)

button_calc = ttk.Button()
button_calc.place(x=30, y=230, width=120)
button_calc.config(command=imt_calculate)

imt_label = ttk.Label()
imt_label.place(x=30, y=180, width=50)

imt_result = ttk.Label()
imt_result.place(x=100, y=180, width=200)


stroka_1 = ttk.Label()
stroka_1.place(x=300, y=100, width=200)

stroka_2 = ttk.Label()
stroka_2.place(x=300, y=120, width=200)

stroka_3 = ttk.Label()
stroka_3.place(x=300, y=140, width=200)

stroka_4 = ttk.Label()
stroka_4.place(x=300, y=160, width=200)

stroka_5 = ttk.Label()
stroka_5.place(x=300, y=180, width=200)

stroka_6 = ttk.Label()
stroka_6.place(x=300, y=200, width=200)

stroka_7 = ttk.Label()
stroka_7.place(x=300, y=220, width=200)

stolb_1 = ttk.Label()
stolb_1.place(x=420, y=100, width=250)

stolb_2 = ttk.Label()
stolb_2.place(x=420, y=120, width=250)

stolb_3 = ttk.Label()
stolb_3.place(x=420, y=140, width=200)

stolb_4 = ttk.Label()
stolb_4.place(x=420, y=160, width=250)

stolb_5 = ttk.Label()
stolb_5.place(x=420, y=180, width=250)

stolb_6 = ttk.Label()
stolb_6.place(x=420, y=200, width=250)

stolb_7 = ttk.Label()
stolb_7.place(x=420, y=220, width=250)

stroka_8 = ttk.Label()
stroka_8.place(x=300, y=80, width=250)

stolb_8 = ttk.Label()
stolb_8.place(x=420, y=80, width=250)

england = ttk.Button()
england.place(x=80, y=10, width=50)
england.config(command=eng_language)


russian = ttk.Button()
russian.place(x=30, y=10, width=50)
russian.config(command=rus_language)


set_texts()


root.mainloop()
