import tkinter
from utils import dimension_mission
# from mafu import *


# 윈도우 객체 생성
window = tkinter.Tk()

window.title('Mafu')
window.geometry('640x480+1000+200')
# 윈도우 창 실행
# window.mainloop()

win_label = tkinter.Label(window, text="퓨린이")
# win_label.pack()
win_label.grid(row=0, columnspan=3)

account01_label = tkinter.Label(window, text='한또르')
account02_label = tkinter.Label(window, text='StrangeHee')
account03_label = tkinter.Label(window, text='Sc0rpi0n2020')
account01_label.grid(row=4, column=0)
account02_label.grid(row=5, column=0)
account03_label.grid(row=6, column=0)
# account01_label.pack()
# account02_label.pack()
# account03_label.pack()


# def dim_button_click():
#     dimension_mission(10)
#
#
# # def acc_button_click(acc):
# #     change_account(acc)
#
#
# dim_button = tkinter.Button(window, text='Dimension Mission', overrelief="solid", width=15,
#                             command=dim_button_click)
# # dim_button.pack(side='top')
# dim_button.grid(row=7, column=0)
# # dim_button.place(relx=10, rely=10, relwidth=0., relheight=0.)
#
# acc01_button = tkinter.Button(window, text='한또르', overrelief="solid", width=15,
#                               command=acc_button_click(1))
# acc01_button.pack(side='top')
#
# acc02_button = tkinter.Button(window, text='StrangeHee', overrelief="solid", width=15,
#                               command=acc_button_click(2))
# acc02_button.pack(side='top')
#
# acc03_button = tkinter.Button(window, text='HandHee2020', overrelief="solid", width=15,
#                               command=acc_button_click(3))
# acc03_button.pack(side='top')

window.mainloop()
