import math

def func(*data):
    # your code here
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

func("彭大牆", "陳王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆") # print 夏曼藍波安

#additional test data
#func("郭宣雅", "夏曼藍波安", "郭宣恆","郭宣A","郭宣B",) # print 夏曼藍波安
#func("夏曼藍波安", "夏曼藍波安", "郭宣恆","郭宣A","郭宣B",) # print 沒有
#func("AAA", "BBB", "CCC", "CCC","DDD","EEE") # print "AAA", "BBB", "DDD","EEE"
#func("파란색", "주황색", "초록색","노란색") # print "주황색", "초록색"  #韓元鈔票的人名，亂找的