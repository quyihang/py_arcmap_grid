import read
import dri_bik_wal_
import xlrd



# def create_inner_matrix()


if __name__ == '__main__':
    in_ = read.read('../in.csv')
    shanghai = read.divide(in_, 'Shanghai') # [31.2, 121.3, 'shanghai', 0]
    wuxi = read.divide(in_, 'Wuxi')
    suzhou = read.divide(in_, 'Suzhou')
    nantong = read.divide(in_, 'Nantong')
    ningbo = read.divide(in_, 'Ningbo')
    jiaxing = read.divide(in_, 'Jiaxing')
    zhoushan = read.divide(in_, 'Zhoushan')
    huzhou = read.divide(in_, 'Huzhou')
    others = read.divide_(in_, 283, 315)
    print 'test'
    # dri_bik_wal_.dri_bik_wal_(o, d, 'driving')