import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import tkinter.messagebox


# 성적 딕셔너리 선언.
score = {}

# 알림 함수
def Msg_no_student():
    tk.messagebox.showwarning("경고", "성적변경 할 학생이 없습니다.")
def Msg_no_print_student():
    tk.messagebox.showwarning("경고", "콘솔에 출력 할 학생이 없습니다.")
def Msg_no_name_input():
    tk.messagebox.showwarning("경고", "이름을 입력하여주십쇼.")

# 기능함수
def student_input(text1, text2, text3):
    print("함수 실행 ㄱㄱ")
    print(text1)
    print(text2)
    print(text3)

    if text1 in score:
        print("학생이 등록되어 있습니다.")
    elif len(text1) == 0 or len(text2) == 0 or len(text3) == 0:
        tk.messagebox.showwarning("경고", "이름을 입력하여주십쇼.")
    else:
        # score[이름][영어] ={}
        score[text1] = {}  # 성적 딕셔너리 초기화
        score[text1]['영어'] = text3
        score[text1]['수학'] = text2
        print("학생이 성적을 입력하였습니다.")


# 성적입력
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

    # 성적입력 버튼.
    btn1 = tk.Button(win, text="성적입력", width=10,
                     command=lambda: [student_input(inputname.get(), inputmath.get(), inputeng.get()), win.destroy()])
    # win.destory pop up 창 닫게 하는 부분.
    btn2 = tk.Button(win, text="닫기", width=10, command=win.destroy)


    # 배치 place 사용.
    label.place(x=20, y=20)
    label1.place(x=20, y=60)
    label2.place(x=20, y=100)
    entryname.place(x=80, y=20)
    entrymath.place(x=80, y=60)
    entryeng.place(x=80, y=100)
    btn1.place(x=50, y=150)
    btn2.place(x=200, y=150)


# 성적출력
def popup_print():
    print("========================")
    print("학생 출력  팝업 실행..")
    print("========================")
    if len(score) == 0:
        Msg_no_student()
    else:
        # {홍길동:{영어:90, 수학:30}}
        for name, info in score.items():
            print("이름 :", name)
            for k, v in info.items():
                print(k, " : ", v, end=" | ")
            print("\n")
# 성적삭제
def popup_delete():

    print("========================")
    print("성적 삭제 팝업 실행..")
    print("========================")

    win = tk.Toplevel()
    win.wm_title("학생 이름 입력")
    win.geometry("350x100+250+250")

    inputname = tk.StringVar()
    label = tk.Label(win, text="Name")
    entryname = tk.Entry(win, width=30, textvariable=inputname)

    #성적입력 버튼.
    btn1 = tk.Button(win, text="이름입력", width=10,
                     command=lambda: [student_delete(inputname.get()), win.destroy()])
    #win.destory pop up 창 닫게 하는 부분.
    btn2 = tk.Button(win, text="닫기", width=10, command=win.destroy)

    # 배치.
    label.place(x=20, y=20)
    entryname.place(x=80, y=20)
    btn1.place(x=50, y=50)
    btn2.place(x=200, y=50)

# 성적변경
def popup_alt():

    print("========================")
    print("성적 변경 팝업 실행..")
    print("========================")

    win = tk.Toplevel()
    win.wm_title("학생 이름 입력")
    win.geometry("350x100+250+250")

    inputname = tk.StringVar()
    label = tk.Label(win, text="Name")
    entryname = tk.Entry(win, width=30, textvariable=inputname)

    #성적입력 버튼.
    btn1 = tk.Button(win, text="이름입력", width=10,
                     command=lambda: [popup_alt2(inputname.get()), win.destroy()])
    #win.destory pop up 창 닫게 하는 부분.
    btn2 = tk.Button(win, text="닫기", width=10, command=win.destroy)

    # 배치.
    label.place(x=20, y=20)
    entryname.place(x=80, y=20)
    btn1.place(x=50, y=50)
    btn2.place(x=200, y=50)

def popup_alt2(text):
    if text in score:
        print("========================")
        print("성적 변경 팝업 실행..")
        print("========================")

        win = tk.Toplevel()
        win.wm_title("학생 성적 입력")
        win.geometry("350x200+250+250")

        inputmath = tk.StringVar()
        inputeng = tk.StringVar()
        label1 = tk.Label(win, text="Math")
        label2 = tk.Label(win, text="English")
        entrymath = tk.Entry(win, width=30, textvariable=inputmath)
        entryeng = tk.Entry(win, width=30, textvariable=inputeng)

        # 성적입력 버튼.
        btn1 = tk.Button(win, text="성적입력", width=10,
                         command=lambda: [function_altscore(text, inputmath.get(), inputeng.get()),
                                          win.destroy()])
        # win.destory pop up 창 닫게 하는 부분.
        btn2 = tk.Button(win, text="닫기", width=10, command=win.destroy)

        # 배치 place 사용.
        label1.place(x=20, y=20)
        label2.place(x=20, y=60)
        entrymath.place(x=80, y=20)
        entryeng.place(x=80, y=60)
        btn1.place(x=50, y=150)
        btn2.place(x=200, y=150)
    else:
        Msg_no_student()

def student_delete(text):
    print("\n\n >>성적삭제<<")
    print(len(text))
    # 해당 딕셔너리의 크기가 0일때
    if len(score) == 0:
        Msg_no_student()
    elif len(text) == 0:
        Msg_no_name_input()
    else:
        if text in score:
            del (score[text])
            print("성적삭제완료")
        else:
            Msg_no_student()

#성적변경
def function_change(text):
    print("\n\n >>성적변경<<")
    # 해당 딕셔너리의 크기가 0일때
    if len(score) == 0:
        Msg_no_student()
    elif len(text) == 0:
        Msg_no_name_input()
    else:
        function_altscore(text)

#성적 변경.
def function_altscore(text, text1, text2):
    print("\n\n >>성적변경<<")
    # score에 입력한 학생이름이 있을 경우
    if text in score:
        # 영어성적 교체
        score[text]['영어'] = text2
        # 수학성적 교체
        score[text]['수학'] = text1
        print("학생이  성적을 입력하였습니다.")
    else:
        Msg_no_student()

# 성적차트
def print_stack():
    print("\n\n >>성적차트<<")
    if len(score) == 0:
        Msg_no_print_student()
    else:
        for name, info in score.items():
            print("이름 :", name)
            # 두 변수 sum, half 선언.
            sum = 0
            half = 0
            for k, v in info.items():
                # 점수를 sum에 합계.
                sum = sum + int(v)
                # 10점 단위로 구분할수 있도록 int형으로 계산.
                half = int(sum / 10)
            print("총점 : ", end="")
            for i in range(half):
                print("*", end="")
            print("(", sum, "점)")
            print()
            print("------------------")
# 성적평균
def function_divied():
    print("\n\n >>성적평균<<")
    if len(score) == 0:
        Msg_no_print_student()
    else:
        for name, info in score.items():
            print("이름 :", name)
            sum = 0
            for k, v in info.items():
                # 성적을 sum변수에 집어넣음.
                sum = sum + int(v)
            # sum을 과목 개수별로 출력하여 모든 학생 평균 출력.
            print("평균 : ", sum / 2)
# 성적추가메뉴
def popup_new():
    print("\n\n >>성적 평가<<")
    if len(score) == 0:
        Msg_no_print_student()
    else:
        for name, info in score.items():
            print("이름 :", name)
            count = 0
            for k, v in info.items():
                num = int(v)
                if count == 1:
                    print(" --------수학과목--------- ")
                else:
                    print(" --------영어과목--------- ")
                if num < 60:
                    print(v, "점 F 입니다.")
                elif num < 70 and num <= 60:
                    print(v, "점 D 입니다.")
                elif num < 80 and num <= 70:
                    print(v, "점 C 입니다.")
                elif num < 90 and num <= 80:
                    print(v, "점 B 입니다.")
                else:
                    print(v, "점 A 입니다.")
                count = count + 1

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
        self.btn1 = tk.Button(root, text="성적입력", width=10, font=font2, command=popup_insert)
        self.btn2 = tk.Button(root, text="성적출력", width=10, font=font2, command=popup_print)
        self.btn3 = tk.Button(root, text="성적삭제", width=10, font=font2, command=popup_delete)
        self.btn4 = tk.Button(root, text="성적변경", width=10, font=font2, command=popup_alt)
        self.btn5 = tk.Button(root, text="성적차트", width=10, font=font2, command=print_stack)
        self.btn6 = tk.Button(root, text="성적평균", width=10, font=font2, command=function_divied)
        self.btn7 = tk.Button(root, text="등급확인", width=10, font=font2, command=popup_new)
        self.btn8 = tk.Button(root, text="종   료", width=10, font=font2, command=root.destroy)


        # 버튼 x,y좌표로 place
        self.btn1.place(x=40, y=200)
        self.btn2.place(x=265, y=200)
        self.btn3.place(x=480, y=200)
        self.btn4.place(x=40, y=305)
        self.btn5.place(x=265, y=305)
        self.btn6.place(x=480, y=305)
        self.btn7.place(x=40, y=410)
        self.btn8.place(x=480, y=410)


root = tk.Tk()
root.title("성적관리 프로그램.")
root.geometry("700x600+350+100")
root.resizable(False, False)

app = MainFrame(root)

root.mainloop()
