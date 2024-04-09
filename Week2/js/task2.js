// your code here, maybe
function book(consultants, hour, duration, criteria){
// your code here
}
function sortPeople(unsortedPeople,criteria){
    console.log(unsortedPeople);
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
console.log(sortedArray);
return (sortedArray);
}


function bookConsultant(consultant,start,duration){
   
// a function for booking ONE consultant (rewritten from python code)
// define a dict, key = each consultant, value = array of 24 zeroes
    let no_book_flag = 0

    //check if hour is greater or equal than 24
    for (let i=0;i++;i<duration){
        if (start+i >= 24){
            start = start - 24;
        }

        //check if consultant is available at specified hour
        //does not do the actual booking yet, because consultant might be available at some hours only
        console.log(`Booking consultant at hour ${start+i}`);

        const checkSchedule = masterSchedule.map(person => {
            if (person.name === consultant && person.schedule[start+i]===1) {
                no_book_flag = 1;
                return person;
            }
            else {
                return person;
            }
           });

        if (main_booking_dict[consultant][start+i] == 0){
            // pass (change to: eqiuvalent of python pass in javascript?)
            console.log(`${consultant} available at hour ${start+i}`); 
        }
        else {
            console.log(`${consultant} NOT available at hour ${start+i}`); 
            no_book_flag = 1;
        }
    }


    //if consultant is available at all hours, book him/her
    if (no_book_flag){
        console.log("No booking");
        console.log(`New Schedule: ${main_booking_dict}`);
        return -1;
    }
    else{
        for (i=0;i<duration(range);i++){
            
            main_booking_dict[consultant][start+i] = 1;

            //https://stackoverflow.com/questions/12462318/find-a-value-in-an-array-of-objects-in-javascript
            //Finding the array element:
            let something = masterSchedule.find(o => o.name === consultant["name"]);
            console.log(something);
            //Replacing the array element:
            let obj = masterSchedule.find((o, i) => {
                if (o.name === consultant["name"]) {
                    masterSchedule[i] = { name: consultant["name"], schedule: 'this'};
                    return true; // stop searching
                }
            });

        }
        console.log(`New Schedule: ${main_booking_dict}`);
        return consultant;
    }
}


const consultants=[
{"name":"John", "rate":4.5, "price":1000},
{"name":"Bob", "rate":3, "price":1200},
{"name":"Jenny", "rate":3.8, "price":800}
];

//book(consultants, 15, 1, "price"); // Jenny
//book(consultants, 11, 2, "price"); // Jenny
//book(consultants, 10, 2, "price"); // John
//book(consultants, 20, 2, "rate"); // John
//book(consultants, 11, 1, "rate"); // Bob
//book(consultants, 11, 2, "rate"); // No Service
//book(consultants, 14, 3, "price"); // John

sortPeople(consultants,"price");
sortPeople(consultants,"rate");

let masterSchedule = [];

for (consultant of consultants){
    let consultantProfile = {};
    consultantProfile.name = consultant["name"];
    consultantProfile.schedule = Array(24).fill(0);
    masterSchedule.push(consultantProfile);
    console.log(consultantProfile);
}

//https://stackoverflow.com/questions/12462318/find-a-value-in-an-array-of-objects-in-javascript
//Finding the array element:
let something = masterSchedule.find(o => o.name === consultant["name"]);
console.log(something);
//Replacing the array element:
let obj = masterSchedule.find((o, i) => {
    if (o.name === consultant["name"]) {
        masterSchedule[i] = { name: consultant["name"], schedule: 'this'};
        return true; // stop searching
    }
});

console.log(arr);

console.log(masterSchedule);
//bookConsultant(consultant,start,duration);