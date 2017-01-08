#coding:utf8



def deal_txt(fileName):
    f = open(fileName, 'r')
    f_ = open('out.txt', 'w')
    for line in f.readlines():
        if len(line) > 60:
            line = line[:-1]
        f_.write(line)
    f.close()
    f_.close()



def main():
    fileName = 'aaa.txt'
    deal_txt(fileName)


if __name__ == '__main__':
    main()