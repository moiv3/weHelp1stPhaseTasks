function getNumber(index){
    // your code here
    let y = 0;
    
    for (let x=0;x<index+1;x++){
        if (x === 0){
            y = 0;
        }
        else if (x%3 === 0){
            y -= 1;
        }
        else{
            y += 4;
        }
    }   

    console.log(y);
}

console.log("==Task 4==")

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70