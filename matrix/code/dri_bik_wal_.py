import urllib2
import json

def dri_bik_wal_(o, d, method):
    output = open('../out/' + method + '.csv', 'w')
    result = []
    for opt in o:
        line = []
        for dpt in d:
            # ostr = ','.join(str(opt))
            # dstr = ','.join(str(dpt))
            ostr = str(opt)[1:-1].replace(' ','')
            dstr = str(dpt)[1:-1].replace(' ','')
            if method == "transit":
                url_ = "http://api.map.baidu.com/direction/v2/" + method + "?output=json&origin="\
                       + ostr + "&destination=" + dstr + "&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
            else:
                url_ = "http://api.map.baidu.com/routematrix/v2/" + method + "?output=json&origins="\
                       + ostr + "&destinations=" + dstr + "&ak=d4aC3XR1Xmpbrcz36VGMaIcj"
            print url_
            html = urllib2.urlopen(url_).read()
            try:
                json_ = json.loads(html)
            except:
                print html
                continue
            if method == "transit":
                if json_["status"] == 0:
                    res = json_["result"]["routes"][0]["duration"]
                else:
                    res = "null"
            else:
                res = json_["result"][0]["duration"]["value"]
            line.append(res)
        result.append(str(line).replace(' ', '')[1:-1])
        output.write(str(line).replace(' ', '')[1:-1])
        output.write('\n')
    # output.writelines(result)