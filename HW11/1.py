class Indenter:

    def __init__(self):  
        self.indent = -1 #باید با منفی یک شروع کنیم تا تو ورود صفر بشه

    def __enter__(self):
        self.indent += 1 # با هر بار ورود یک واحد به فاصله ها اضافه میکنیم
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.indent -= 1    #در خروج یک واحد کاهش میدهیم 

    def print(self, text):
        indents = '\t' * self.indent  
        print(f'{indents}{text}\n' )


with Indenter() as indent:
    indent.print("Hi")
    with indent:
        indent.print("Talk is Cheap!")
        with indent:
            indent.print("Show me the Code...")
    indent.print("Torvalds")


