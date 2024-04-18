#urllib.request for requesting data
#json for 觀察輸入的格式是json format
#csv for csv inout/output, re for Regex support("findall" function)
import urllib.request, json, csv, re

#python task => need to read from a network location?

#key data in assignment-1 file: stitle(景點名), info(帶"捷運站名"的描述文字), lat/long(經緯度), filelist(jpg圖片與...一些mp3/flv?) & others
url1 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
req1 = urllib.request.Request(url1)
res1 = urllib.request.urlopen(req1)
data1 = res1.read()
print("Successfully read url:" + url1)

#data in assignment-2 file: 'MRT'(station) & 'address'(中文地址)
url2 = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2"
req2 = urllib.request.Request(url2)
res2 = urllib.request.urlopen(req2)
data2 = res2.read()

print("Successfully read url:" + url2)

with open('spot.csv', 'a', newline="", encoding='utf-8') as spot_file:

    #load data and prepare for writing to file
    spot_writer_object = csv.writer(spot_file,delimiter=',')

    parsed_data1 = json.loads(data1)
    parsed_data2 = json.loads(data2)
    #print(parsed_data1['data'],parsed_data2['data'])

    #connect MRT station to attraction by serial number
    for attraction in parsed_data1['data']['results']:
        for item in parsed_data2['data']:
            if attraction["SERIAL_NO"] == item["SERIAL_NO"]:
                attraction["MRT"] = item["MRT"]
                attraction["address"] = item["address"]

                district_char_location = attraction["address"].find("區")        
                attraction['district'] = attraction['address'][district_char_location-2:district_char_location+1]
        #print(attraction["SERIAL_NO"], attraction["MRT"], attraction["address"],attraction['district'])

        #now we have everything we need except first file for each attraction...
        #英文的話用Regex試試看
        #findall(r"http.*?(?=http|$)",attraction['filelist']): 找出所有符合以下條件的字串(r = raw string in python)
        #由"http"開始，不限長度，但碰到下一個http就停下來。或是end of string("$")也要停下來。
        attraction['first_file'] = re.findall(r"http.*?(?=http|$)",attraction['filelist'])[0]
        #print(attraction['first_file'])

        csv_line = []
        csv_line.append(attraction['stitle'])
        csv_line.append(attraction['district'])
        csv_line.append(attraction['longitude'])
        csv_line.append(attraction['latitude'])
        csv_line.append(attraction['first_file'])
        #print(csv_line)
        spot_writer_object.writerow(csv_line)
            
    print("Saved to file spot.csv.")
    spot_file.close()


with open('mrt.csv', 'a', newline="", encoding='utf-8') as mrt_file:

    mrt_writer_object = csv.writer(mrt_file,delimiter=',')

    #建立一個dict，對於每個景點對應的捷運站加到mrt_dict裡邊
    mrt_dict = {}
    for attraction in parsed_data1['data']['results']:
        try:
            mrt_dict[attraction['MRT']].append(attraction['stitle'])
        except:
            mrt_dict[attraction['MRT']] = [attraction['stitle']]
        #print (attraction['stitle'],mrt_dict)
    #print (attraction['stitle'],mrt_dict)

    #依照assignment指定的格式輸出這個dict
    for item in mrt_dict:
        station_attraction_list = []

        station_attraction_list.append(item)
        for attraction in mrt_dict[item]:
            station_attraction_list.append(attraction)

        #print(station_attraction_list)
        mrt_writer_object.writerow(station_attraction_list)

    print("Saved to file mrt.csv.")
    mrt_file.close()


print("Parse complete.")

#print(re.findall(r"http.*?(?=http|$)",test1)[0])
#wanted to use re.split first, then found re.findall
#https://stackoverflow.com/questions/48672653/split-a-string-but-keep-the-delimiter-in-the-same-resulting-substring-in-python

#https://darkk6.blogspot.com/2017/03/regexp-lookahead-lookbehind.html
#Positive lookahead ： X(?=Y)
#Negative lookahead ： X(?!Y)
#解釋為： 我要找 X 而其後方必須/不可為 Y ；而其中 X 和 Y 都可以是一個合法的表達式。

#The $ symbol is one of the most commonly used symbols in RegEx. It is used to match the end of a string.
#In other words, you can call it "end of line anchor", since it anchors a pattern to the end of the line.

"""
    #this is code from an attempt before realizing "SERIAL_NO" can be linked...

    #first find the districts of each station
    for station in parsed_data2['data']:
        #只會找出第一個符合的XX區, then add 'district':"XX區" to dict. 前提是"XX區"都有正確地寫(沒有亂寫)，才會parse對
        #如果某一站出現兩次以上，後者會蓋過前者(#TODO:待檢查!)
        location = station['address'].find('區')        
        station['district']=station['address'][location-2:location+1]
    #print(parsed_data2['data'])

    for attraction in parsed_data1['data']['results']:
        #想要創造一個dict是對應XX站:在YY景點的第幾個字出現，最後取數值最小的那一個(就是最靠字串前面的捷運站)
        mrt_dict={}

        for station in parsed_data2['data']:
            mrt_dict[station['MRT']] = attraction['info'].find((station['MRT']+'站'))
        #print (mrt_dict)

        #find minimal distance person by value, then get its key - from week2 task1 找出最小值(而且不能是-1)
        keys = [k for k,v in mrt_dict.items() if (v>-1 and v==min(i for i in mrt_dict.values() if i > -1))]
        #print (keys, attraction['info'])

        #在attraction這個字典中加入他最接近哪個區(district)&捷運站(MRT)
        if len(keys) == 0:
            attraction['district'] = "NA"
            attraction['MRT'] = "NA"
        else:
            attraction['district'] = [d['district'] for d in parsed_data2['data'] if d['MRT'] == keys[0]][0]
            attraction['MRT'] = [d['MRT'] for d in parsed_data2['data'] if d['MRT'] == keys[0]][0]
"""