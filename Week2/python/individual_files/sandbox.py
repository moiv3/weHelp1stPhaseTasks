#sandbox for sort_people

def sort_people(unsortedpeople,criteria):

    unsortedarray = unsortedpeople.copy()
    sortedarray = []

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
            
        print("bestperson:",person['name'])
        sortedarray.append(bestperson)
        print("appending:",person['name'])
        unsortedarray.remove(bestperson)
        print("removing:",person['name'])

    return sortedarray

consultants=[
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800},
{"name":"John", "rate":4.5, "price":1000}
]

print("before:",consultants)
sortedpeople = sort_people(consultants,"rate")
print("aftersorting:",sortedpeople)
print("after:",consultants)
print("before:",consultants)
sortedpeople = sort_people(consultants,"price")
print(sortedpeople)
print("after:",consultants)

