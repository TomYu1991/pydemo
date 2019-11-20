import requests
import json,csv
import random,time
def parseData(vehicleNo,weightState,consignId):
    url1 = 'http://localhost:8080/a/gateconsign/consign/checkConsignByWeight?vehicleNo={}'.format(vehicleNo)
    res1 = requests.get(url1)
    d=dict(json.loads(res1.text))
    print(d.get('success'),d.get('msg'))
    if d.get("success"):
        if weightState == '0':
            #一次过磅
            zl = random.randint(80000,120000)
            print('开始一次过磅重量：',zl)
            url2 = 'http://localhost:8080/a/weight/weight/saveweightConsign?id={}&zl={}'.format(consignId,zl)
            ret=requests.get(url2)
            print(ret.text)
        else:
            #二次过磅
            zl = random.randint(25000,30000)
            print('开始二次过磅重量：',zl)
            url2 = 'http://localhost:8080/a/weight/weight/updateweightConsign?id={}&zl={}'.format(consignId,zl)
            ret = requests.get(url2)
            print(ret.text)

def parseCsv(filePath):
    file = open(filePath,encoding='utf8')
    lines = csv.reader(file)
    for line in lines:
        vehicleNo = line[22]
        weightState = line[36]
        consignId = line[2]
        print(vehicleNo,'---',weightState,'---',consignId)
        parseData(vehicleNo,weightState,consignId)
        time.sleep(1)
if __name__=='__main__':
    filepath = r"C:\Users\user\Desktop\csv\123.csv"
    parseCsv(filepath)
