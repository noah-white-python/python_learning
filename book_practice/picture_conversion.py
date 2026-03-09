import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os


# --- 核心：解决路径问题 ---
def resource_path(relative_path):
    """ 获取文件的绝对路径，确保在 PyCharm 运行和打包成 exe 后都能找到图片 """
    if hasattr(sys, '_MEIPASS'):
        # 打包后的临时解压路径
        return os.path.join(sys._MEIPASS, relative_path)
    # 开发环境下的绝对路径
    # 这里直接定位到你的文件夹路径
    base_path = r'C:\Users\71098\PycharmProjects\PythonProject\book_practice'
    return os.path.join(base_path, relative_path)


def convert():
    try:
        val = entry.get().strip().upper()
        if val.endswith('C'):
            res = float(val[:-1]) * 9 / 5 + 32
            result_label.config(text=f"{val} = {res:.2f}F", fg="blue")
        elif val.endswith('F'):
            res = (float(val[:-1]) - 32) * 5 / 9
            result_label.config(text=f"{val} = {res:.2f}C", fg="green")
        else:
            messagebox.showwarning("格式提示", "请输入数字+单位\n例如: 250C 或 77F")
    except ValueError:
        messagebox.showerror("错误", "请输入有效的数字内容！")


# 1. 创建主窗口
root = tk.Tk()
root.title("Gemini 温度转换器")
root.geometry("400x500")

# 2. 加载背景图片
try:
    # 使用你提供的文件名
    img_name = "gemini_1.png"
    img_full_path = resource_path(img_name)

    img_open = Image.open(img_full_path)
    # 将图片缩放到窗口大小 (400x500)
    img_resized = img_open.resize((400, 500))
    bg_img = ImageTk.PhotoImage(img_resized)

    # 用 Label 承载图片作为背景
    bg_label = tk.Label(root, image=bg_img)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"图片加载失败，请检查路径。错误信息: {e}")
    root.configure(bg='#ECECEC')

# 3. 界面组件（稍微设置一点背景色让文字更清晰）
title_label = tk.Label(root, text="温度转换器", font=("微软雅黑", 20, "bold"), bg="white")
title_label.pack(pady=40)

entry = tk.Entry(root, font=("微软雅黑", 16), justify='center', bd=2)
entry.pack(pady=10, ipady=5)
entry.insert(0, "32C")  # 默认初始值

btn = tk.Button(root, text="开始转换", command=convert, font=("微软雅黑", 12),
                bg="#4A90E2", fg="white", width=12)
btn.pack(pady=20)

result_label = tk.Label(root, text="等待输入...", font=("微软雅黑(italic)", 14), bg="white")
result_label.pack(pady=30)

# 启动程序
root.mainloop()