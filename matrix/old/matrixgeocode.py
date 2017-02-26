import read
import dri_bik_wal_

if __name__ == '__main__':
    o = read.read('o.csv')
    d = read.read('d.csv')
    # dri_bik_wal_.dri_bik_wal_(o, d, 'driving')
    dri_bik_wal_.dri_bik_wal_(o, d, 'transit')