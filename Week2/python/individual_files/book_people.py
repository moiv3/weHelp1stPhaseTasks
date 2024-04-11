#sandbox for book_consultant

#book(consultants, 15, 1, "price") # Jenny
#book(consultants, 11, 2, "price") # Jenny
#book(consultants, 10, 2, "price") # John
#book(consultants, 20, 2, "rate") # John
#book(consultants, 11, 1, "rate") # Bob
#book(consultants, 11, 2, "rate") # No Service
#book(consultants, 14, 3, "price") # John

consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
]

main_booking_dict = {}

for consultant in consultants:
    main_booking_dict[consultant['name']] = [0]*24

def book_consultant(consultant,start,duration):
    no_book_flag = 0
    for i in range(duration):
        if start+i >= 24:
            start = start - 24
        #print("Booking",consultant,"at hour", start+i)
        if main_booking_dict[consultant][start+i] == 0:
            pass
            #print(consultant,"available at hour", start+i) 
        else:
            #print(consultant,"NOT available at hour", start+i)
            no_book_flag = 1
        
    if no_book_flag:
        #print("No booking")
        #print ("New Schedule:", main_booking_dict)
        return False
    else:
        for i in range(duration):
            main_booking_dict[consultant][start+i] = 1
        #print ("New Schedule:", main_booking_dict)
        return consultant

book_consultant("Jenny", 15, 1)
book_consultant("Jenny", 11, 2)
book_consultant("John", 10, 2)
book_consultant("John", 20, 2)
book_consultant("Bob", 11, 1)
book_consultant("Jenny", 11, 2)
book_consultant("John", 14, 3)