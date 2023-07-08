# -*- coding: utf-8 -*-
import customtkinter as ct
from pyperclip import copy
import threading
import time
from os import _exit
from PIL import Image
from keyboard import wait, add_hotkey, remove_hotkey
#for icon in tray
from pystray import MenuItem as item
import pystray

version = "1.0"

ct.set_appearance_mode("Dark")
ct.set_default_color_theme("green")

def ignore_input(event):
    return "break"

def exit_f():
	_exit(0)

def quit_root(icon, item):
    icon.stop()
    _exit(0)

def show_root(icon, item):
    icon.stop()
    root.after(0,root.deiconify)

def withdraw_root():
    try: 
        root.withdraw()
        image = Image.open("fake_icon.ico")
        menu = (item('Выйти', quit_root), item('Показать', show_root))
        icon = pystray.Icon("name", image, "ClipXpert", menu)
        icon.run()
    except:
        pass


def paste_text():
    str_text_to_paste = text_to_paste.get()
    copy(str_text_to_paste)

def main_window():
    global key_for_bind
    global text_to_paste

    def quit_root(icon, item):
        icon.stop()
        _exit(0)

    def show_root(icon, item):
        icon.stop()
        root.after(0,root.deiconify)

    def withdraw_root():
        try:  
            root.withdraw()
            image = Image.open("fake_icon.ico")
            menu = (item('Выйти', quit_root), item('Показать', show_root))
            icon = pystray.Icon("name", image, "ClipXpert", menu)
            icon.run()
        except:
            pass

    root = ct.CTk()
    root.resizable(False, False)
    def hotkey_listener():
        root.focus()
        key = key_for_bind.get()
        if key:
            text = launch_button.cget("text")
            if text == "Запустить":
                root.focus()
                add_hotkey(key, paste_text)
                launch_button.configure(text="Выключить")
            else:
                root.focus()
                remove_hotkey(key)
                launch_button.configure(text="Запустить")
    root = ct.CTkToplevel()
    root.geometry("450x320+150+150")
    try:
        root.iconbitmap("icon.ico")
    except:
        pass

    root.protocol('WM_DELETE_WINDOW', withdraw_root)

    #DONT TOUCH IT!!!
    root.title("ClipXpert! | developer: https://github.com/3verlaster")
    #DONT TOUCH IT!!!

    key_for_bind = ct.CTkEntry(root, width=95, placeholder_text="Bind")
    key_for_bind.pack(pady=15)

    text_to_paste = ct.CTkEntry(root, placeholder_text="Текст который скопировать", width=185)
    text_to_paste.place(x=130, y=110)

    launch_button = ct.CTkButton(root, text="Запустить", command=hotkey_listener)
    launch_button.pack(pady=15)

    info_frame = ct.CTkFrame(root, width=260, height=128)
    info_frame.place(x=20, y=175)

    version_info_label = ct.CTkLabel(info_frame, text=f"Версия ClipXpert: {version}").pack(pady=3)

    #DONT TOUCH IT!!!
    developer_info_label = ct.CTkLabel(info_frame, text="Developer: https://github.com/3verlaster", font=ct.CTkFont(family='Verdana normal roman', size=12)).pack(pady=3, padx=10)
    opensource_info_label = ct.CTkLabel(info_frame, text="ClipXpert is fully open-sourced on github.").pack(pady=3, padx=3)
    #DONT TOUCH IT!!!

    frame = ct.CTkFrame(root, width=128, height=128)
    #frame.pack(pady=15, side=ct.RIGHT)
    frame.place(x=300, y=175)

    #bt = ct.CTkButton(frame, text="test").pack()
    try:
        large_image = ct.CTkImage(Image.open("image.png"), size=(128, 128))
        large_image_label = ct.CTkLabel(frame, text="", image=large_image)
        large_image_label.pack()
        root.mainloop()
    except:
        pass

agr = ct.CTk()
try:
    agr.iconbitmap("icon.ico")
except:
    pass
agr.resizable(False, False)
agr.protocol('WM_DELETE_WINDOW', exit_f)
agr.geometry("575x515+180+180")
agr.title("ClipXpert! | Terms of Agreement")


text = ct.CTkLabel(agr, text="Terms of Agreement", font=ct.CTkFont(size=12, weight="bold")).pack(pady=5)
terms_of_agreement = ct.CTkTextbox(agr, height=400, width=540)
terms_of_agreement.pack(pady=10)

#DONT TOUCH IT!!!
terms_of_agreement.insert("1.0", 'Пользователь должен понимать, что использование программы, заменяющей буфер обмена (далее по тексту - "программа"), происходит на его собственный риск и ответственность. Компания-разработчик программы (далее по тексту - "мы", "наша компания" или "разработчик") не несет ответственности за любые убытки, повреждения или проблемы, возникшие в результате использования программы.\n\nПрограмма предназначена только для личного использования. Пользователь несет ответственность за соблюдение всех применимых законов и правил, связанных с использованием программы. Мы не несем ответственности за любые нарушения, совершенные пользователем при использовании программы.\n\nМы прилагаем все усилия для обеспечения надежности и безопасности программы. Однако мы не гарантируем, что программа будет работать без ошибок или прерываний. Мы также не гарантируем, что программа будет соответствовать всем требованиям и ожиданиям пользователя.\n\nПользователь несет полную ответственность за содержимое, которое он копирует, вставляет или сохраняет с помощью программы. Мы не осуществляем никакой контроль или модерацию такого содержимого. Пользователь обязуется не использовать программу для распространения незаконного, оскорбительного, непристойного или вредоносного материала.\n\nМы не несем ответственности за любые прямые, косвенные, случайные, особые или последовательные убытки или ущерб, возникшие в результате использования или невозможности использования программы. Это включает, но не ограничивается, потерю данных, потерю доходов, прерывание бизнеса или любые другие финансовые потери.\n\nМы оставляем за собой право вносить изменения в программу, включая функциональность, интерфейс и доступность, без предварительного уведомления. Мы также можем приостановить или прекратить предоставление программы в любое время без объяснения причин.\n\nПользователь обязуется не вмешиваться в работу программы или предпринимать действия, направленные на обход или нарушение мер безопасности программы. Любые попытки несанкционированного доступа или вмешательства могут привести к прекращению доступа пользователя к программе и/или правовым последствиям.\n\nЭтот отказ от ответственности является частью общих условий использования программы и должен быть принят пользователем перед началом использования программы. Продолжая использовать программу, пользователь соглашается с этими условиями и подтверждает свое понимание и согласие с ними.')
#DONT TOUCH IT!!!

def ignore_input(event):
    return "break"

def checkbox_event():
    #print("checkbox toggled, current value:", check_var.get())
    check_button_state()

def check_button_state():
    if check_var.get() == "1":
        button.configure(state=ct.ACTIVE)
    else:
        button.configure(state=ct.DISABLED)

def button_event():
    agr.destroy()
    main_window()

check_var = ct.StringVar()

checkbox = ct.CTkCheckBox(agr, text="Я согласен.", variable=check_var, command=checkbox_event)
checkbox.pack(padx=95, pady=10, side=ct.LEFT)

button = ct.CTkButton(agr, text="Продолжить", command=button_event, state=ct.DISABLED)
button.pack(padx=5, pady=10, side=ct.LEFT)

terms_of_agreement.bind("<Key>", ignore_input)
agr.mainloop()