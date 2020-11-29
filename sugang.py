import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


# 성적 딕셔너리 선언.
score = {}


def student_input(inputname,inputmath,inputeng):
    print(inputname)
    print(inputmath)
    print(inputeng)

    if inputname in score:
        print("학생이 등록되어 있습니다.")
    else:
        # score[이름][영어] ={}
        score[inputname] = {}  # 성적 딕셔너리 초기화
        score[inputname]['영어'] = inputeng
        score[inputname]['수학'] = inputmath
        print("학생이 성적을 입력하였습니다.")

#성적입력
def popup_insert():
    print("========================")
    print("학생 성적 입력 팝업 실행..")
    print("========================")

    win = tk.Toplevel()
    win.wm_title("학생 성적 입력")
    win.geometry("350x200+250+250")

    inputname = tk.StringVar()
    inputmath = tk.StringVar()
    inputeng = tk.StringVar()
    label = tk.Label(win, text="Name")
    label1 = tk.Label(win, text="Math")
    label2 = tk.Label(win, text="English")
    entryname = tk.Entry(win, width=30, textvariable=inputname)
    entrymath = tk.Entry(win, width=30, textvariable=inputmath)
    entryeng = tk.Entry(win, width=30, textvariable=inputeng)
    #성적입력 버튼.
    btn1 = tk.Button(win, text="성적입력", width=10,
                     command=student_input(inputname.get(), inputmath.get(), inputeng.get()))
    #win.destory pop up 창 닫게 하는 부분.
    btn2 = tk.Button(win, text="닫기", width=10, command=win.destroy)


    # 배치.
    label.grid(row=0, column=0)
    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)
    entryname.grid(row=0, column=1, padx=10)
    entrymath.grid(column=1, row=1, padx=10)
    entryeng.grid(column=1, row=2, padx=10)
    btn1.grid(row=5, column=0)
    btn2.grid(row=5, column=1)


# 성적출력
def popup_print():
    print("========================")
    print("학생 출력  팝업 실행..")
    print("========================")
    if len(score) == 0:
        print("출력할 학생이 없습니다.")
    else:
        # {홍길동:{영어:90, 수학:30}}
        for name, info in score.items():
            print("이름 :", name)
            for k, v in info.items():
                print(k, " : ", v, end=" | ")
            print("\n")
# # 성적삭제
# def popup_delete():
#
# #성적변경
# def popup_change():
#
# # 성적차트
# def popup_stack():
#
# # 성적평균
# def popup_divied():
#
# # 성적추가메뉴
# def popup_new():

# 프로그램 실행시 메인 프레임 불러오는 코드.
class MainFrame(ttk.Frame):
    def __init__(self, master):
        # argument 변환을 통해서 class 안에서 이렇게 진행을 해주어야 함.
        font1 = tkFont.Font(root=root.master, family="Malgun Gothic", size=35)
        font2 = tkFont.Font(root=root.master, family="Malgun Gothic", size=20)

        ttk.Frame.__init__(self, master)
        self.pack()
        self.lbl = tk.Label(root, text="동국대 성적관리 프로그램"
                    , font=font1, relief="ridge", borderwidth=5
                    , bg="orange")
        self.lbl.pack()
        self.lbl2 = tk.Label(root, text="컴퓨터공학과")
        self.lbl3 = tk.Label(root, text="2015211365 김태윤")
        self.lbl2.pack()
        self.lbl3.pack()

        # txt = Entry(root)
        # txt.pack()

        # 버튼 각각 추가
        self.btn1 = tk.Button(root, text="성적입력", width=10 , font=font2,command=popup_insert)
        self.btn2 = tk.Button(root, text="성적출력", width=10 , font=font2,command=popup_print)
        self.btn3 = tk.Button(root, text="성적삭제", width=10 , font=font2)
        self.btn4 = tk.Button(root, text="성적변경", width=10 , font=font2)
        self.btn5 = tk.Button(root, text="성적차트", width=10 , font=font2)
        self.btn6 = tk.Button(root, text="성적평균", width=10 , font=font2)

        # 버튼 x,y좌표로 place
        self.btn1.place(x=40, y=200)
        self.btn2.place(x=265, y=200)
        self.btn3.place(x=480, y=200)
        self.btn4.place(x=40, y=305)
        self.btn5.place(x=265, y=305)
        self.btn6.place(x=480, y=305)


root = tk.Tk()
root.title("성적관리 프로그램.")
root.geometry("680x400+100+100")
root.resizable(False, False)

app = MainFrame(root)

root.mainloop()
