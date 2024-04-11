// your code here, maybe
//this one gave me trouble in js...
function book(consultants, hour, duration, criteria){
// your code here
    
    //try to book people
    //console.log("===NEW ENTRY===");
    if (criteria === "rate" || criteria === "price"){
        //because we have only one criteria => sort by that criteria.
        //consultants is a "array of objects."
        sorted_consultants = sortPeople (consultants,criteria);
        //console.log(sorted_consultants)

        let booking_success = false;
        for (consultant of sorted_consultants){
            //every item is an object.
            //console.log(item.name);
            //store the return value(book OK = 0, NG = -1) in trybooking
            let trybooking = bookConsultant(consultant.name,hour,duration);
            //console.log(`Booking ${consultant.name}, trybooking value = ${trybooking}`);
            if (trybooking === 0){
                booking_success = true;
                //console.log(`Booked ${consultant.name}, breaking out of the loop`);
                //if booking success, get out of the loop to avoid double booking
                break;
            }
            else{
                //console.log(`Did not book ${consultant.name}, continuing the loop`);
            }
            
        }
        if (!booking_success){
        console.log("No service");
        }
    }

    else{
        console.log("criteria not supported!");
    }

}

function sortPeople(unsortedPeople,criteria){
    //deep copy unsortedPeople
    let unsortedArray = JSON.parse(JSON.stringify(unsortedPeople));
    let sortedArray = [];
    //sort according to criteria
    //有x個人，就要loop x次
    for (let i = 0; i < unsortedPeople.length; i++){
        //initialize bestperson
        let bestperson = unsortedArray[0];
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
                print("criteria not supported yet");
                return 0;
            }
        }    
        //console.log(bestperson);
        //append bestperson to new array
        sortedArray.push(bestperson);
        //remove bestperson from old array
        unsortedArray.splice(unsortedArray.indexOf(bestperson),1);
        //console.log(sortedArray);
        //console.log(unsortedArray);
    }
//console.log("sorting function in progress");
//console.log(sortedArray);
//return, 讓外面的sorted_consultants可以有一個回傳值
return (sortedArray);
}

// a function for booking ONE consultant
function bookConsultant(consultant,start,duration){
    // search for the consultant
    let no_book_flag = 1;
    //這裡用了一個讓人感到驚恐的method: forEach
    //masterSchedule is an array of objects
    //every object: (人名):(時間表)
    //(might be possible to rewrite by a "for" loop?)
    //masterSchedule裡面的每一個item(就是object)都做這個事情:
    masterSchedule.forEach(item => {
        if ((item.name) === consultant){
            no_book_flag = 0;
            //console.log(no_book_flag);  
            //如果寫成let no_book_flag = 0;, 答案就會改變(錯誤),為什麼?
            //是否重新定義了裡面的no_book_flag = 0, 所以外面的no_book_flag = 1,不受理面的作業影響，就都是1?
            //看起來是。而且程式會照booking
            //檢查是否每一個時間段都可以booking
            for (let i=start;i<start+duration;i++){
                let j = i >= 24 ? i - 24 : i;
                if (item.schedule[j] === 1){
                    no_book_flag = 1;
                    //console.log(`Can not book ${item.name}`);
                }
            
            }
            
            //如果no_book_flag沒有打開就可以booking他
            if (no_book_flag === 0){
                //console.log(`consultant ${item.name}'s schedule:`);
                //console.log(item.schedule);
                for (let i=start;i<start+duration;i++){
                    let j = i >= 24 ? i - 24 : i;
                    item.schedule[j] = 1;
                    
                    }
                console.log(item.name);
                //console.log(`booking ${item.name}...`);
                //console.log(`${item.name}'s new schedule:`);
                //console.log(item.schedule);
            }
            else{
                //console.log(`Did not book ${item} due to schedule conflict!`);
            }
        }
    //console.log(no_book_flag);    
    });
    //forEach會return undefined
    //no_book_flag傳回給trybooking的值
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

//additional test data
//book(consultants, 15, 1, "price"); // Jenny
//book(consultants, 11, 2, "price"); // Jenny
//book(consultants, 10, 2, "price"); // John
//book(consultants, 20, 2, "rate"); // John
//book(consultants, 11, 1, "rate"); // Bob
//book(consultants, 11, 2, "rate"); // No Service
//book(consultants, 14, 3, "price"); // John
//
//book(consultants, 15, 1, "price"); // Bob
//book(consultants, 11, 2, "price"); // No Service
//book(consultants, 10, 2, "price"); // No Service
//book(consultants, 20, 2, "rate"); // Jenny
//book(consultants, 11, 1, "rate"); // No Service
//book(consultants, 11, 2, "rate"); // No Service
//book(consultants, 14, 3, "price"); // No Service