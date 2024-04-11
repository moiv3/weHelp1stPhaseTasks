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

#some test data
find([9, 8, 7, 6], [1, 1, 1, 1], 9) # print 0
find([9, 8, 7, 6], [1, 1, 1, 1], 10) # print -1
find([9, 8, 7, 6], [0, 1, 1, 1], 9) # print -1
find([9, 8, 7, 6], [0, 1, 1, 1], 6) # print 3
find([9, 8, 7, 6], [0, 1, 1, 1], 6) # print 3
find([9, 8, 7, 6], [0, 0, 0, 1], 6) # print 3
find([9, 8, 7, 6], [0, 0, 0, 0], 6) # print -1
find([0, 0, 0, 0], [1, 1, 1, 1], 9) # print -1
