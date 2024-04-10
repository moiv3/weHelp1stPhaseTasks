function find(spaces, stat, n){
    // your code here
    let all_matches = []
    for (i=0;i<spaces.length;i++){
        //console.log(i)
        let match= new Object();
        if (stat[i] === 1){
            if (spaces[i]-n >= 0){
                match.car = i;
                match.seats = spaces[i];
            }
        }
        //console.log(match)
        //console.log(Object.keys(match))
        if (Object.keys(match).length != 0){
            all_matches.push(match);
        }           
        
    }
    //console.log(all_matches);
    

    if (all_matches.length === 0){
        console.log(-1);
    }
    else{
        minOfAllMatches = Math.min(...all_matches.map(o => o.seats));
        minCar = all_matches.find(o => o.seats === minOfAllMatches);
        //console.log(minOfAllMatches);
        console.log(minCar['car'])
    }
}
    console.log("==Task 5==")

    find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
    find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
    find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2