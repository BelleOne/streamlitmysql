# f = open('filedata/mydata.txt', 'r', encoding='utf-8')

def read_all():
    f = open('filedata/mydata.txt', 'r', encoding='utf-8')
    print(f.read())
    f.close()

# read by line


def read_line():
    f = open('filedata/mydata.txt', 'r', encoding='utf-8')
    for i in range(2, 3):
        print(f.readline(), end='')
    # for line in f:
    #     print(line, end='')
    f.close()


read_all()

read_line()
