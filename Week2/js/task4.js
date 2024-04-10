function getNumber(index){
// your code here
// this one is a little bit easier so less comments. the logic of the 數列 is:
    let y = 0;
    
    for (let x=0;x<index+1;x++){
        // the 0th item is 0
        if (x === 0){
            y = 0;
        }
        // every 3 items, the 1st and 2nd items add 4.

        else if (x%3 === 0){
            y -= 1;
        }
        //the 3rd item minuses 1.
        else{
            y += 4;
        }
    }   
    // then print out the output.
    console.log(y);
}

console.log("==Task 4==")

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70