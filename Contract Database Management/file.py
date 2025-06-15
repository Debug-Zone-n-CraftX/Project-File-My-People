def file_write(content):
    sp = " "
    with open("text.txt",'a',encoding='utf8') as f:
        content = content.split()
        for i in content:
            f.write(i)
            f.write(sp)
        f.write("\n")
            

def show_file():
    with open("text.txt",'r',encoding='utf8') as f:
        print(f.read())


def clear_file():
    with open("text.txt",'w',encoding='utf8') as f:
        f.write("")









