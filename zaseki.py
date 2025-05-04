import tkinter as tk
from tkinter import messagebox

# 定数
ROWS, COLS = 6, 5
TOTAL = ROWS * COLS

# メインアプリクラス
class SeatAssignmentApp:
    def __init__(self, master):
        self.master = master
        master.title("成績順の席替えアプリ（6x6）")

        self.entries = []
        self.create_input_fields()

        self.assign_button = tk.Button(master, text="席替え開始", command=self.assign_seats)
        self.assign_button.grid(row=TOTAL+1, column=0, columnspan=COLS, pady=10)

        self.output_frame = tk.Frame(master)
        self.output_frame.grid(row=TOTAL+2, column=0, columnspan=COLS)

    def create_input_fields(self):
        for i in range(TOTAL):
            frame = tk.Frame(self.master)
            frame.grid(row=i, column=0, columnspan=COLS, sticky="w")

            name_var = tk.StringVar()
            score_var = tk.StringVar()

            tk.Label(frame, text=f"{i+1:02d}人目").pack(side="left")
            tk.Entry(frame, textvariable=name_var, width=15).pack(side="left")
            tk.Label(frame, text="点数").pack(side="left")
            tk.Entry(frame, textvariable=score_var, width=5).pack(side="left")

            self.entries.append((name_var, score_var))

    def assign_seats(self):
        # 入力チェックとデータ取得
        students = []
        try:
            for name_var, score_var in self.entries:
                name = name_var.get().strip()
                score = int(score_var.get())
                students.append({"name": name, "score": score})
        except ValueError:
            messagebox.showerror("エラー", "点数には必ず数字を入力してください。")
            return

        # 成績順に並び替え
        sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)

        # 出力フレームをリセット
        for widget in self.output_frame.winfo_children():
            widget.destroy()

        # 成績順で座席表示（左上→右下）
        for i in range(ROWS):
            for j in range(COLS):
                index = i * COLS + j
                student = sorted_students[index]
                label_text = f"{student['name']}\n{student['score']}点"
                label = tk.Label(self.output_frame, text=label_text, borderwidth=1, relief="solid", width=15, height=4)
                label.grid(row=i, column=j, padx=2, pady=2)

# 起動
if __name__ == "__main__":
    root = tk.Tk()
    app = SeatAssignmentApp(root)
    root.mainloop()