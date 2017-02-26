import read
import dri_bik_wal_

if __name__ == '__main__':
    in_ = read.read('../in.csv')
    shanghai = read.divide(in_, 'Shanghai')
    wuxi = read.divide(in_, 'Wuxi')
    suzhou = read.divide(in_, 'Suzhou')
    nantong = read.divide(in_, 'Nantong')
    ningbo = read.divide(in_, 'Ningbo')
    jiaxing = read.divide(in_, 'Jiaxing')
    zhoushan = read.divide(in_, 'Zhoushan')
    # dri_bik_wal_.dri_bik_wal_(o, d, 'driving')