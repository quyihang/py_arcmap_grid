#coding:utf8

def month(in_, num):
    in_ = in_ * (1 + num / 100 / 12)
    return in_

if __name__ == '__main__':
    in_ = 100
    a = raw_input('yue li:')
    while a <> '':
        num = float(a)
        in_ = month(in_, num)
        print 'your money: ' + str(in_)
        a = raw_input('yue li:')