import tkinter as tk
import tkinter.messagebox
import xlsxwriter

root = tk.Tk()
root.geometry("600x400")
root.title("Naming Conv")

its_code_var = tk.StringVar()
ws_amt_var = tk.StringVar()
text_widget = tk.Text(root, wrap='word', height=10, width=40)

def key_pressed(event):
    submit()
def submit():
    workbook = xlsxwriter.Workbook('server2022.xlsx')
    worksheet = workbook.add_worksheet()
    text_widget.config(state=tk.NORMAL)
    its_code = its_code_var.get()
    ws_amt = ws_amt_var.get()
    row = 0
    column = 0

    for amt in range(1, int(ws_amt) + 1):
        sys_name = its_code.upper() + "WS" + str(amt).zfill(3) + "@retail.spar.co.za"
        text_widget.insert(tk.END, sys_name + '\n')
        worksheet.write(row, column, sys_name)
        row += 1


    its_code_var.set("")
    ws_amt_var.set("")
    text_widget.config(state=tk.DISABLED)
    workbook.close()
    its_code_entry.focus()
def quit_prg():

    root.destroy()
def clear_txt():
    text_widget.config(state=tk.NORMAL)
    text_widget.delete("1.0", "end")

def copy_text():
    root.clipboard_clear()
    text_widget.focus()
    root.clipboard_append(text_widget.get('1.0', 'end'))

its_code_label = tk.Label(root, text = 'ITSCODE:', font=('calibre', 10, 'bold'))
its_code_entry = tk.Entry(root, textvariable= its_code_var, font=('calibre', 10, 'normal'))

ws_amt_label = tk.Label(root, text = 'WS Amount:', font=('calibre', 10, 'bold'))
ws_amt_entry = tk.Entry(root, textvariable= ws_amt_var, font=('calibre', 10, 'normal'))

notice_label = tk.Label(root, text = 'Hit Enter or click Submit', font=('calibre', 10, 'bold'))

sub_btn = tk.Button(root,text = 'Submit', command = submit)
quit_btn = tk.Button(root,text = 'Quit', command = quit_prg)
clear_btn = tk.Button(root,text = 'Clear', command = clear_txt)

copy_btn = tk.Button(root,text = 'Copy', command = copy_text)

its_code_label.grid(row = 0, column = 0, padx = 40)
its_code_entry.grid(row = 0, column = 1)

ws_amt_label.grid(row = 1, column = 0)
ws_amt_entry.grid(row = 1, column = 1)

notice_label.grid(row = 3, column = 0, padx = 20)

sub_btn.grid(row = 2, column = 1, pady = 20)
quit_btn.grid(row = 2, column = 0, pady = 20)
clear_btn.grid(row = 2, column = 2, pady = 20)
copy_btn.grid(row = 3, column = 2, pady = 20)

text_widget.grid(row = 3, column = 1, pady = 40)
root.bind("<Return>", key_pressed)
its_code_entry.focus()
root.mainloop()

