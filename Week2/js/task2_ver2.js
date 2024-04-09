// your code here, maybe
function book(consultants, hour, duration, criteria){
    //console.log("===NEW ENTRY===");
    if (criteria === "rate" || criteria === "price"){
        sorted_consultants = sortPeople (consultants,criteria);
        let booking_success = false;
        //console.log(sorted_consultants)
        for (item of sorted_consultants){
            //console.log(item.name);
            let trybooking = bookConsultant(item.name,hour,duration);
            if (trybooking === 0){
                console.log(item.name);
                booking_success = true;
                break;
            }
            
        }
        if (!booking_success){
        console.log("No service");
        }
    }

    else{
        console.log("criteria not supported!");
    }
    // your code here

}

function sortPeople(unsortedPeople,criteria){
    //console.log(unsortedPeople);
    let unsortedArray = JSON.parse(JSON.stringify(unsortedPeople));
    let sortedArray = [];
    //console.log(sortedArray);
    //console.log(unsortedArray);
    //sort according to criteria
    for (let i = 0; i < unsortedPeople.length; i++){

        let bestperson = unsortedArray[0];
        //console.log(unsortedArray.length);
        //console.log(bestperson);
        //console.log(sortedArray);
        for (person of unsortedArray){
            if (criteria === "rate"){
                if (person[criteria]>bestperson[criteria]){
                    bestperson = person;
                }
            }
            else if (criteria === "price"){
                if (person[criteria]<bestperson[criteria]){
                    bestperson = person;
                }
            }
            else{
                print("criteria not supported yet")
                return 0;
            }
        }    
        //console.log(bestperson);
        //append bestperson to new array
        sortedArray.push(bestperson);
        unsortedArray.splice(unsortedArray.indexOf(bestperson),1);
        //console.log(sortedArray);
        //console.log(unsortedArray);
    }
//console.log("sorting function in progress");
//console.log(sortedArray);
return (sortedArray);
}

function bookConsultant(consultant,start,duration){
    // a function for booking ONE consultant
    // search the consultant
    let no_book_flag = 0;
    masterSchedule.forEach(item => {
        if ((item.name) === consultant){
            no_book_flag = 0;
            for (let i=start;i<start+duration;i++){
                let j = i >= 24 ? i - 24 : i;
                if (item.schedule[j] === 1){
                    no_book_flag = 1;
                }
            
            }

            if (no_book_flag === 0){
                //console.log(`consultant ${item.name}'s schedule:`);
                //console.log(item.schedule);
                for (let i=start;i<start+duration;i++){
                    let j = i >= 24 ? i - 24 : i;
                    item.schedule[j] = 1;
                    }
                
                //console.log(`booking ${item.name}...`);
                //console.log(`${item.name}'s new schedule:`);
                //console.log(item.schedule);
            }

            else{
                //console.log("Did not book consultant due to schedule conflict!");
            }
        }
    });
    //console.log(no_book_flag);
    return no_book_flag;

}

const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
    ];



let masterSchedule = [];

for (consultant of consultants){
    let consultantProfile = {};
    consultantProfile.name = consultant["name"];
    consultantProfile.schedule = Array(24).fill(0);
    masterSchedule.push(consultantProfile);
    //console.log(masterSchedule);
}
    
//bookConsultant("Jenny",22,5);
//bookConsultant("Jenny",12,5);
//bookConsultant("Jenny",12,5);
//bookConsultant("Bob",12,5);
//bookConsultant("Bob",12,5);
//
//sortPeople(consultants,"price");
//sortPeople(consultants,"rate");

console.log("==Task 2==")

book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John