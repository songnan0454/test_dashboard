import tkinter as tk
from tkinter import filedialog, messagebox
from core.GetOrderList import GetOrderList

def on_button_click():
    if not entry_username.get() or not entry_password.get() or not entry_start_time.get() or not entry_end_time.get() or not entry_storage_path.get():
        result_label.config(text="请填写所有必要信息")
    else:
        messagebox.showinfo("注意！", "代码即将运行，请点击OK后千万不要动鼠标，不要操作浏览器，将持续几分钟，谢谢！")
        result_label.config(
            GetOrderList.get_order_lists("http://sf.myps188.com", entry_username.get(), entry_password.get(),
                                         entry_start_time.get(), entry_end_time.get(), entry_storage_path.get()))
        # Show a message box after processing
        messagebox.showinfo("操作完成", "您获取的信息已经写在以下路径下:\n" + entry_storage_path.get())

def browse_folder():
    folder_path = filedialog.askdirectory()
    entry_storage_path.delete(0, tk.END)  # Clear previous content
    entry_storage_path.insert(tk.END, folder_path)

# 创建主窗口
root = tk.Tk()
root.title("自动获取订单信息程序")
root.geometry("400x300")  # 设置默认窗口大小

# 添加用户名标签和文本框
label_username = tk.Label(root, text="用户名")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=10)
entry_username.insert(tk.END, "18367823720")

# 添加密码标签和文本框
label_password = tk.Label(root, text="密码")
label_password.grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")  # show="*"将密码内容显示为"*"
entry_password.grid(row=1, column=1, padx=10, pady=10)
entry_password.insert(tk.END, "asd1993")

# 添加开始时间标签和文本框
label_start_time = tk.Label(root, text="开始时间")
label_start_time.grid(row=2, column=0, padx=10, pady=10)
entry_start_time = tk.Entry(root)
entry_start_time.grid(row=2, column=1, padx=10, pady=10)
entry_start_time.insert(tk.END, "2023-11-01")

# 添加结束时间标签和文本框
label_end_time = tk.Label(root, text="结束时间")
label_end_time.grid(row=3, column=0, padx=10, pady=10)
entry_end_time = tk.Entry(root)
entry_end_time.grid(row=3, column=1, padx=10, pady=10)
entry_end_time.insert(tk.END, "2023-11-02")

# 添加存放路径标签、文本框和浏览按钮
label_storage_path = tk.Label(root, text="存放路径")
label_storage_path.grid(row=4, column=0, padx=10, pady=10)
entry_storage_path = tk.Entry(root)
entry_storage_path.grid(row=4, column=1, padx=10, pady=10)
button_browse = tk.Button(root, text="浏览", command=browse_folder)
button_browse.grid(row=4, column=2, padx=10, pady=10)

# 添加其他标签和文本框（存放路径等）
# ...

# 添加按钮，并绑定点击事件
button = tk.Button(root, text="生成", command=on_button_click)
button.grid(row=5, column=0, columnspan=2, pady=10)  # columnspan用于横跨两列

# 添加用于显示结果的标签
result_label = tk.Label(root, text="")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# 启动主循环
root.mainloop()
