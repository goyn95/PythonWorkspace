from tkinter import *
from tkmacosx import Button

root = Tk()
root.title("goyn GUI")
root.geometry("640x480")

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# # btn1.pack()
# # btn2.pack()
# # btn1.pack(side="left")
# # btn2.pack(side="left")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

#  맨 윗줄
btn_f16 = Button(root, text="F16", width=70, height=70)
btn_f17 = Button(root, text="F17", width=70, height=70)
btn_f18 = Button(root, text="F18", width=70, height=70)
btn_f19 = Button(root, text="F19", width=70, height=70)

btn_f16.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", width=70, height=70)
btn_equal = Button(root, text="=", width=70, height=70)
btn_div = Button(root, text="/", width=70, height=70)
btn_mul = Button(root, text="*", width=70, height=70)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 시작 줄
btn_7 = Button(root, text="7", width=70, height=70)
btn_8 = Button(root, text="8", width=70, height=70)
btn_9 = Button(root, text="9", width=70, height=70)
btn_sub = Button(root, text="-", width=70, height=70)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 시작 줄
btn_4 = Button(root, text="4", width=70, height=70)
btn_5 = Button(root, text="5", width=70, height=70)
btn_6 = Button(root, text="6", width=70, height=70)
btn_plus = Button(root, text="+", width=70, height=70)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_plus.grid(row=3, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1시작 줄
btn_1 = Button(root, text="1", width=70, height=70)
btn_2 = Button(root, text="2", width=70, height=70)
btn_3 = Button(root, text="3", width=70, height=70)
btn_enter = Button(root, text="enter", width=70, height=70) # 세로로 합쳐짐

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S) # 현재 위치로부터 아래쪽으로 몇줄을 더함

btn_0 = Button(root, text="0", width=70, height=70)
btn_dot = Button(root, text=".", width=70, height=70)


btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3) # 현재 위치로부터 오른쪽으로 몇칸 더함
btn_dot.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop()