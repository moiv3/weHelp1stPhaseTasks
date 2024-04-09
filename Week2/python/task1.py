def find_and_print(messages, current_station):

# your code here
    #dict of stations. Xiaobitan is assigned to value 99.
    stations = {
        "Xindian":1,
        "Xindian City Hall":2,
        "Qizhang":3,
        "Dapinglin":4,
        "Jingmei":5,
        "Wanlong":6,
        "Gongguan":7,
        "Taipower Building":8,
        "Guting":9,
        "Chiang Kai-shek Memorial Hall":10,
        "Xiaonanmen":11,
        "Ximen":12,
        "Beimen":13,
        "Zhongshan":14,
        "Songjiang Nanjing":15,
        "Nanjing Fuxing":16,
        "Taipei Arena":17,
        "Nanjing Sanmin":18,
        "Songshan":19,
        "Xiaobitan":99,
    }

    #main program below
    person_station_dict=messages.copy()

    # translate person-message dict into person-station dict
    for person in messages:
        for station in stations:
            #note: the "find" method in python: it returns -1 if not found, returns 第幾個字元找到 when found
            if messages[person].find(station) != -1:

                #不是Xindian的話，就直接採用
                if station != "Xindian":
                    #print("Updating:", person, station, stations[station])
                    person_station_dict[person]=stations[station]

                #Xindian的話=>還要檢查新店市公所。如果是，就不採用新店，採用新店市公所。
                else:
                    if messages[person].find("Xindian District Office") == -1:
                        #print("Updating:", person, station, stations[station])
                        person_station_dict[person]=stations[station]
            else:
                pass

    # from person-station dict, build person-station_difference dict
    person_station_diff_dict=person_station_dict.copy()

    #calculate how far each person is from current_station, then save it to a dict
    #邏輯可以再通順一些
    for person in person_station_diff_dict:
        #print(person, person_station_dict[person])

        if stations[current_station] != 99:
            #exception: if friend(person) is at Xiaobitan, self(current_station) not at Xiaobitan
            if person_station_dict[person] == 99:
                person_station_diff_dict[person] = abs(stations["Qizhang"]-stations[current_station])+1
            else:            
                person_station_diff_dict[person] = abs(person_station_dict[person]-stations[current_station])
        
        #if current_station is Xiaobitan:
        else:
            #exception: if friend(person) is at Xiaobitan, self(current_station) also at Xiaobitan: diff = 0
            if person_station_dict[person] == 99:
                person_station_diff_dict[person] = 0
            #exception: if friend(person) not at Xiaobitan, self(current_station)  at Xiaobitan
            #go to Qizhang first, then add 1
            else:
                person_station_diff_dict[person] = abs(person_station_dict[person]-stations["Qizhang"])+1
    
        #print(person_station_diff_dict)

    #find minimal distance person by value, then get its key
    keys = [k for k,v in person_station_diff_dict.items() if v==min(person_station_diff_dict.values())]

    for key in keys:
        print(key)


messages={
"Leslie":"I'm at home near Xiaobitan station.",
"Bob":"I'm at Ximen MRT station.",
"Mary":"I have a drink near Jingmei MRT station.",
"Copper":"I just saw a concert at Taipei Arena.",
"Vivian":"I'm at Xindian station waiting for you."
}
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

#messages={
#"Leslie":"I'm at home near Xiaobitan station.",
#"Bob":"I'm at Ximen MRT station.",
#"Mary":"I have a drink near Jingmei MRT station.",
#"Copper":"I just saw a concert at Taipei Arena.",
#"Vivian":"I'm at Xindian station waiting for you.",
#"WiWian":"I'm at Xindian City Hall station waiting for you.",
#"Xixian":"I'm at Qizhang station waiting for you.",
#"Yiyian":"I'm at Dapinglin station waiting for you.",
#"Zizian":"I'm at Jingmei station waiting for you.",
#"Aiaian":"I'm at Wanlong station waiting for you.",
#"Bibian":"I'm at Gongguan station waiting for you.",
#"Cician":"I'm at Taipower Building station waiting for you.",
#}
#
#find_and_print(messages, "Xindian")
#find_and_print(messages, "Xindian City Hall")
#find_and_print(messages, "Qizhang")
#find_and_print(messages, "Dapinglin")
#find_and_print(messages, "Jingmei")
#find_and_print(messages, "Wanlong")
#find_and_print(messages, "Gongguan")
#find_and_print(messages, "Taipower Building")
#find_and_print(messages, "Guting")
#find_and_print(messages, "Chiang Kai-shek Memorial Hall")
#find_and_print(messages, "Xiaonanmen")
#find_and_print(messages, "Ximen")
#find_and_print(messages, "Beimen")
#find_and_print(messages, "Zhongshan")
#find_and_print(messages, "Songjiang Nanjing")
#find_and_print(messages, "Nanjing Fuxing")
#find_and_print(messages, "Taipei Arena")
#find_and_print(messages, "Nanjing Sanmin")
#find_and_print(messages, "Songshan")
#find_and_print(messages, "Xiaobitan")
#detect which station name is found
#calculate stations between
#compare stations between

#exception: Xiaobitan
#exception: Xindian and Xindian District Office


#backup here because i cant make up my mind.
#最後沒有被採用
#stations = [
#    {"staName":"Xindian", "staNumber":1},
#    {"staName":"Xindian District Office", "staNumber":2},
#    {"staName":"Qizhang", "staNumber":3},
#    {"staName":"Dapinglin", "staNumber":4},
#    {"staName":"Jingmei", "staNumber":5},
#    {"staName":"Wanlong", "staNumber":6},
#    {"staName":"Gongguan", "staNumber":7},
#    {"staName":"Taipower Building", "staNumber":8},
#    {"staName":"Guting", "staNumber":9},
#    {"staName":"Chiang Kai-shek Memorial Hall", "staNumber":10},
#    {"staName":"Xiaonanmen", "staNumber":11},
#    {"staName":"Ximen", "staNumber":12},
#    {"staName":"Beimen", "staNumber":13},
#    {"staName":"Zhongshan", "staNumber":14},
#    {"staName":"Songjiang Nanjing", "staNumber":15},
#    {"staName":"Nanjing Fuxing", "staNumber":16},
#    {"staName":"Taipei Arena", "staNumber":17},
#    {"staName":"Nanjing Sanmin", "staNumber":18},
#    {"staName":"Songshan", "staNumber":19},
#    {"staName":"Xiaobitan", "staNumber":99},
#]
#

#testing a function
#似乎是尋找key-value pair的比較標準的用法?但是我要尋找key,所以修改一下
#target = "Xindian"
#keys = [k for k,v in stations.items() if k==target]
#print(keys)