#coding:utf-8
import xlrd
import urllib
import urllib2
import json
import time


def address_lnglat(address, resident):
    # url = "http://api.map.baidu.com/geocoder/v2/?address="+urllib.pathname2url(address)+"&output=json&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
    url = "http://api.map.baidu.com/geocoder/v2/?address=" + address + "&output=json&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
    url_ = "http://api.map.baidu.com/geocoder/v2/?address=" + '上海市' + resident.encode('utf-8') + "&output=json&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
    time.sleep(0.01)
    html = urllib2.urlopen(url)
    document = html.read()
    json_data = json.loads(document)
    if json_data["status"] == 0:
        lng = str(json_data["result"]["location"]["lng"])
        lat = str(json_data["result"]["location"]["lat"])
    else:
        html = urllib2.urlopen(url_)
        document = html.read()
        json_data = json.loads(document)
        if json_data["status"] == 0:
            lng = str(json_data["result"]["location"]["lng"])
            lat = str(json_data["result"]["location"]["lat"])
        else:
            [lng, lat] = ['','']
    # except:
    #     print address + ' ' + resident.encode('utf-8')
    #     [lng, lat] = ['', '']
    return [lng, lat]


def deal_address(address):  # 对于address多个地址的去重
    if ',' in address:
        address = address.split(',')[0].replace(' ', '')
    else:
        address = address.replace(' ', '')
    address = "上海市" + address.encode('utf-8')
    return address


def main():
    workbook = xlrd.open_workbook('11.xlsx')
    booksheet = workbook.sheet_by_name('Sheet1')
    f_w = open('out.csv', 'w')
    f_error = open('error_log.txt', 'w')
    i = 2
    for row in range(1, booksheet.nrows):
        print i
        cel = booksheet.cell(row, 3)
        address = cel.value
        cel = booksheet.cell(row, 1)
        resident = cel.value
        address = deal_address(address)
        [lng, lat] = address_lnglat(address, resident)
        f_w.write(str(lng)+','+str(lat))
        f_w.write('\n')
        if lng == '':
            f_error.write(str(i)+','+address)
            print address
        i += 1
    f_w.close()
    f_error.close()

if __name__ == '__main__':
    main()