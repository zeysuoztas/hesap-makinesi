import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("zeynepsudeoztas hesap makinesi odev")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_669=tk.Button(root)
        GButton_669["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_669["font"] = ft
        GButton_669["fg"] = "#000000"
        GButton_669["justify"] = "center"
        GButton_669["text"] = "+"
        GButton_669.place(x=80,y=220,width=50,height=35)
        GButton_669["command"] = self.GButton_669_command

        GButton_132=tk.Button(root)
        GButton_132["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_132["font"] = ft
        GButton_132["fg"] = "#000000"
        GButton_132["justify"] = "center"
        GButton_132["text"] = "-"
        GButton_132.place(x=140,y=220,width=50,height=35)
        GButton_132["command"] = self.GButton_132_command

        GButton_397=tk.Button(root)
        GButton_397["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_397["font"] = ft
        GButton_397["fg"] = "#000000"
        GButton_397["justify"] = "center"
        GButton_397["text"] = "x"
        GButton_397.place(x=200,y=220,width=50,height=35)
        GButton_397["command"] = self.GButton_397_command

        GButton_933=tk.Button(root)
        GButton_933["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_933["font"] = ft
        GButton_933["fg"] = "#000000"
        GButton_933["justify"] = "center"
        GButton_933["text"] = "/"
        GButton_933.place(x=260,y=220,width=50,height=35)
        GButton_933["command"] = self.GButton_933_command

        GLabel_966=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_966["font"] = ft
        GLabel_966["fg"] = "#333333"
        GLabel_966["justify"] = "center"
        GLabel_966["text"] = "RAKAM 1"
        GLabel_966.place(x=80,y=130,width=70,height=25)

        self.GLineEdit_901=tk.Entry(root)
        self.GLineEdit_901["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_901["font"] = ft
        self.GLineEdit_901["fg"] = "#333333"
        self.GLineEdit_901["justify"] = "center"
        self.GLineEdit_901["text"] = ""
        self.GLineEdit_901.place(x=80,y=180,width=70,height=25)

        self.GLineEdit_666=tk.Entry(root)
        self.GLineEdit_666["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_666["font"] = ft
        self.GLineEdit_666["fg"] = "#333333"
        self.GLineEdit_666["justify"] = "center"
        self.GLineEdit_666["text"] = ""
        self.GLineEdit_666.place(x=190,y=180,width=70,height=25)

        GLabel_883=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_883["font"] = ft
        GLabel_883["fg"] = "#333333"
        GLabel_883["justify"] = "center"
        GLabel_883["text"] = "RAKAM 2"
        GLabel_883.place(x=180,y=130,width=70,height=25)

        GLabel_324=tk.Label(root)
        ft = tkFont.Font(family='Times',size=15)
        GLabel_324["font"] = ft
        GLabel_324["fg"] = "#333333"
        GLabel_324["justify"] = "center"
        GLabel_324["text"] = "*SONUC*"
        GLabel_324.place(x=360,y=130,width=70,height=25)

        self.GLineEdit_95=tk.Entry(root)
        self.GLineEdit_95["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_95["font"] = ft
        self.GLineEdit_95["fg"] = "#333333"
        self.GLineEdit_95["justify"] = "center"
        self.GLineEdit_95["text"] = ""
        self.GLineEdit_95.place(x=350,y=160,width=100,height=35)

    def GButton_669_command(self):
        self.calculate_result('+')

    def GButton_132_command(self):
        self.calculate_result('-')

    def GButton_397_command(self):
        self.calculate_result('*')

    def GButton_933_command(self):
        self.calculate_result('/')

    def calculate_result(self, operation):
        try:
            num1 = float(self.GLineEdit_901.get())
            num2 = float(self.GLineEdit_666.get())
            
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Hata: 0'a bölme"
            else:
                result = "Geçersiz İşlem"

            self.GLineEdit_95.delete(0, tk.END)
            self.GLineEdit_95.insert(0, str(result))
        except ValueError:
            self.GLineEdit_95.delete(0, tk.END)
            self.GLineEdit_95.insert(0, "Geçersiz Girdi")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()