#coding:utf-8
import xlrd
import urllib
import urllib2
import json
import time
from selenium import webdriver
from bs4 import BeautifulSoup


hdr = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def url2doc(url):
    # driver = webdriver.PhantomJS()
    # driver.get(url)
    # document = BeautifulSoup(driver.page_source,'html').find_all('pre')[0].contents[0]
    print '正在请求'
    request = urllib2.Request(url, headers=hdr)
    html = urllib2.urlopen(request)
    print '请求完成'
    document = html.read()

    return document


def address_lnglat(address, resident):
    # url = "http://api.map.baidu.com/geocoder/v2/?address="+urllib.pathname2url(address)+"&output=json&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
    print address
    url = "http://api.map.baidu.com/geocoder/v2/?address=" + address + "&output=json&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
    print resident
    url_ = "http://api.map.baidu.com/geocoder/v2/?address=" + '上海市' + resident.encode('utf-8') + "&output=json&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
    time.sleep(0.5)
    print 'wo yao da kai le'
    document = url2doc(url)
    print 'cheng gong da kai le'
    json_data = json.loads(document)
    if json_data["status"] == 0:
        lng = str(json_data["result"]["location"]["lng"])
        lat = str(json_data["result"]["location"]["lat"])
    else:
        print 'address error, change to resident'
        document = url2doc(url_)
        json_data = json.loads(document)
        if json_data["status"] == 0:
            lng = str(json_data["result"]["location"]["lng"])
            lat = str(json_data["result"]["location"]["lat"])
        else:
            [lng, lat] = ['','']
    # except:
    #     print address + ' ' + resident.encode('utf-8')
    #     [lng, lat] = ['', '']
    print [lng, lat]
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
    f_r = open('out.csv', 'r')
    lines = len(f_r.readlines())
    f_r.close()
    f_w = open('out.csv', 'a')
    f_error = open('error_log.txt', 'a')
    i = 1
    if lines <> 0:
        f_w.write('\n')
    for row in range(1+lines, booksheet.nrows):
        print row
        cel = booksheet.cell(row, 2)
        address = cel.value
        cel = booksheet.cell(row, 1)
        resident = cel.value
        address = deal_address(address)
        [lng, lat] = address_lnglat(address, resident)
        f_w.write(str(row)+','+str(lng)+','+str(lat))
        f_w.write('\n')
        if lng == '':
            f_error.write(str(i)+','+address)
            print address
        i += 1
    f_w.close()
    f_error.close()

if __name__ == '__main__':
    main()