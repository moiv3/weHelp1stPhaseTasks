#Task 1
print("===Task 1===")

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


#Task 2
print("===Task 2===")

def sort_people(unsortedpeople,criteria): 
# a function for sorting people according to criteria
# after completing, use sort or sorted by native python to try NOT reinventing the wheel...

    #initial values. use deep copy to not alter the original since we might need multiple sorts.
    unsortedarray = unsortedpeople.copy()
    sortedarray = []

    #sort according to criteria
    for i in range(len(unsortedarray)):
        bestperson = unsortedarray[0]
        for person in unsortedarray:
            if criteria == "rate":
                if person[criteria]>bestperson[criteria]:
                    bestperson = person
            elif criteria == "price":
                if person[criteria]<bestperson[criteria]:
                    bestperson = person
            else:
                print("criteria not supported yet")
                return False
            
        #print("bestperson:",person['name'])
        #append bestperson to new array
        sortedarray.append(bestperson)
        unsortedarray.remove(bestperson)

    return sortedarray


def book_consultant(consultant,start,duration):
# a function for booking ONE consultant
# define a dict, key = each consultant, value = array of 24 zeroes
    no_book_flag = 0

    #check if hour is greater or equal than 24
    for i in range(duration):
        if start+i >= 24:
            start = start - 24

        #check if consultant is available at specified hour
        #does not do the actual booking yet, because consultant might be available at some hours only
        #print("Booking",consultant,"at hour", start+i)
        if main_booking_dict[consultant][start+i] == 0:
            pass
            #print(consultant,"available at hour", start+i) 
        else:
            #print(consultant,"NOT available at hour", start+i)
            no_book_flag = 1

    #if consultant is available at all hours, book him/her
    if no_book_flag:
        #print("No booking")
        #print ("New Schedule:", main_booking_dict)
        return False
    else:
        for i in range(duration):
            main_booking_dict[consultant][start+i] = 1
        #print ("New Schedule:", main_booking_dict)
        return consultant

#main function
def book(consultants, hour, duration, criteria):

    if not consultants:
        print ("No consultants")
    else:
        if criteria == "rate" or criteria == "price":
            sorted_consultants = sort_people (consultants,criteria)
            booking_success = False
            for consultant in sorted_consultants:
                trybooking = book_consultant(consultant['name'],hour,duration)
                if trybooking:
                    print(trybooking)
                    booking_success = True
                    break
                else:
                    pass
            if booking_success == False:
                print("No Service")
        else:
            print ("invalid sorting criteria")


# thoughts:
# if consultants:
# identify the criteria, rate or price
# list consultants' order 1-> 2-> 3
# try their schedule one by one
# if yes, log their schedule and print out name
# if no , try another
# if all consultants tried, output no service.

# your code here
#initialize consultant array
consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

#initialize booking dict
main_booking_dict = {}

for consultant in consultants:
    main_booking_dict[consultant['name']] = [0]*24

#booking action
book(consultants, 15, 1, "price") # Jenny
book(consultants, 11, 2, "price") # Jenny
book(consultants, 10, 2, "price") # John
book(consultants, 20, 2, "rate") # John
book(consultants, 11, 1, "rate") # Bob
book(consultants, 11, 2, "rate") # No Service
book(consultants, 14, 3, "price") # John


#Task 3
print("===Task 3===")

import math

def func(*data):
    middle_char_array = []
    for item in data:

        # add items by their original order(有順序的)
        middle_char_array.append(item[math.ceil((len(item)-1)/2)])

    #print(middle_char_array)

    flag = 0
    for middle_char in middle_char_array:
        if middle_char_array.count(middle_char) == 1:
            #middle_char_array.index(middle_char): 第幾個item = 1
            #data[~]: 印出原array(tuple?)第"那個"item
            print(data[middle_char_array.index(middle_char)])
            flag = 1
    if flag == 0:
        print("沒有")


# your code here
func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安


#Task 4
print("===Task 4===")

def get_number(index):
    y = 0
    
    for x in range(index+1):
        if x == 0:
            y = 0
        elif x%3 == 0:
            y -= 1
        else:
            y += 4
    
    print(y)
        
get_number(1) # print 4
get_number(5) # print 15
get_number(10) # print 25
get_number(30) # print 70

#Task 5
print("===Task 5===")

def find(spaces, stat, n):
# your code here
    all_matches = []
    #loop through 幾個，算spaces or stat 的length
    for i in range(len(spaces)):
        #創一個dict
        match={}
        #stat[i] == 0不處理
        if stat[i] == 1:
            if spaces[i]-n>=0:
                match['car'] = i
                match['seats'] = spaces[i]
        #沒有match到，就不append了
        if match != {}:
            all_matches.append(match)

    #print(all_matches)
    
    if all_matches == []:
        print(-1)
    else:
        #sort & key的非常常用的用法，如果之後忘了就搜尋"key=lambda:"
        all_matches.sort(reverse=False,key=lambda x:x['seats'])
        print(all_matches[0]['car'])

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2) # print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4) # print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4) # print 2