import json

with open('taipei-attractions-assignment-1', 'r', encoding='UTF-8') as attraction1File:
    data1 = attraction1File.read()

with open('taipei-attractions-assignment-2', 'r', encoding='UTF-8') as attraction2File:
    data2 = attraction2File.read()

import re

import csv

with open('spot.csv', 'a', newline="", encoding='utf-8') as spot_file:

    spot_writer_object = csv.writer(spot_file,delimiter=',')

    parsed_data1 = json.loads(data1)
    #print(parsed_data['data'])

    parsed_data2 = json.loads(data2)
    #print(parsed_data['data'])

    for station in parsed_data2['data']:
        location = station['address'].find('區')
        station['district']=station['address'][location-2:location+1]
    #print(parsed_data2['data'])

    for attraction in parsed_data1['data']['results']:
        #print(attraction['stitle'])
        mrt_dict={}
        for station in parsed_data2['data']:
        #print((station['MRT']+'站'), station['address'], station['SERIAL_NO'])
        
            #print(attraction['info'].find((station['MRT']+'站')))
            mrt_dict[station['MRT']] = attraction['info'].find((station['MRT']+'站'))
            #print(station['MRT']+'站', parsed_data1['data']['results'][0]['info'].find((station['MRT']+'站')))

        #find minimal distance person by value, then get its key - from week2 task1
        keys = [k for k,v in mrt_dict.items() if (v>-1 and v==min(i for i in mrt_dict.values() if i > -1))]
        #print (keys, attraction['info'])
        if len(keys) == 0:
            attraction['district'] = "NA"
            attraction['MRT'] = "NA"
        else:
            attraction['district'] = [d['district'] for d in parsed_data2['data'] if d['MRT'] == keys[0]][0]
            attraction['MRT'] = [d['MRT'] for d in parsed_data2['data'] if d['MRT'] == keys[0]][0]
        
        csv_line = attraction['stitle']+","+attraction['district']+","+attraction['longitude']+","+attraction['latitude']+","+re.findall(r"http.*?(?=http|$)",attraction['filelist'])[0]
        print(csv_line)
        spot_writer_object.writerow([csv_line])
        #print (attraction['stitle'], keys, mrt_dict)

    spot_file.close()

with open('mrt.csv', 'a', newline="", encoding='utf-8') as mrt_file:

    mrt_writer_object = csv.writer(mrt_file,delimiter=',')

    for station in parsed_data2['data']:
        attraction_list = []
        attraction_list.append(station['MRT'])
        for attraction in parsed_data1['data']['results']:
            if station['MRT'] == attraction['MRT']:
                #print(station['MRT'], attraction['stitle'])
                attraction_list.append(attraction['stitle'])
        print(attraction_list)
        mrt_writer_object.writerow(attraction_list)
    
    mrt_file.close()

    #print(parsed_data2['data'])

#for attraction in parsed_data1['data']['results']:
    #print(attraction['stitle'],attraction['longitude'],attraction['latitude'],re.findall(r"http.*?(?=http|$)",attraction['filelist'])[0])
    #這行做完要打開

#test1 = parsed_data1['data']['results'][0]['filelist']



#print(re.findall(r"http.*?(?=http|$)",test1)[0])
#wanted to use re.split first, then found re.findall
#https://stackoverflow.com/questions/48672653/split-a-string-but-keep-the-delimiter-in-the-same-resulting-substring-in-python

#https://darkk6.blogspot.com/2017/03/regexp-lookahead-lookbehind.html
#Positive lookahead ： X(?=Y)
#Negative lookahead ： X(?!Y)
#解釋為： 我要找 X 而其後方必須/不可為 Y ；而其中 X 和 Y 都可以是一個合法的表達式。

#The $ symbol is one of the most commonly used symbols in RegEx. It is used to match the end of a string.
#In other words, you can call it "end of line anchor", since it anchors a pattern to the end of the line.
