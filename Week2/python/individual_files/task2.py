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

#additional booking action
#book(consultants, 15, 1, "price") # Bob
#book(consultants, 11, 2, "price") # No Service
#book(consultants, 10, 2, "price") # No Service
#book(consultants, 20, 2, "rate") # Jenny
#book(consultants, 11, 1, "rate") # No Service
#book(consultants, 11, 2, "rate") # No Service
#book(consultants, 14, 3, "price") # No Service