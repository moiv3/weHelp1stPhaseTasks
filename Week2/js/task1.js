function findAndPrint(messages, currentStation){
    // your code here

    //deep copy the messages object
    //let unsortedArray = JSON.parse(JSON.stringify(unsortedPeople));
    let matchStation = JSON.parse(JSON.stringify(messages));

    //find string in object
    //console.log(messages);
    //review: why use Object.keys?
    for (const message of Object.keys(messages)){
        //console.log(messages[message]);
        for (station of Object.keys(stations)){
            //console.log(station);
            if (messages[message].includes(station)){
            result = stations[station];
            //console.log(result);
            matchStation[message] = result;
            //update the results to matchStation
            //console.log(matchStation);
            }
        }
    }
    //done

    //deep copy the matchStation object
    let matchDiff = JSON.parse(JSON.stringify(matchStation));

    //calculate the difference
    for (const message of Object.keys(messages)){
        //first case: user is at Xiaobitan
        if (stations[currentStation] === 99){
            if (matchStation[message] === 99){
                matchDiff[message] = 0;
            }
            else{
                matchDiff[message] = Math.abs(stations["Qizhang"] - matchStation[message]) + 1;
            }
        }
        //second case: user is not at Xiaobitan
        else{
            if (matchStation[message] === 99){
                matchDiff[message] = Math.abs(stations[currentStation] - stations["Qizhang"]) + 1;
            }
            else{
            matchDiff[message] = Math.abs(stations[currentStation] - matchStation[message]);
            }
        //console.log(matchDiff);
        }
    }
    //find the closest friend and output
    let distanceArray = []
    for (personDistance in matchDiff){
        distanceArray.push(matchDiff[personDistance]);
    }
    const minDistance = Math.min(...distanceArray);

    //console.log(matchDiff);
    for (item in matchDiff){
        if (matchDiff[item] === minDistance){
            console.log(item);
        }
        
    }
    
    //for (personDistance in matchDiff){
    //    if distanceArray.push(matchDiff[personDistance]);
    //}
    //minDistance = Math.min(distanceArray);



}



    const stations = {
        "Xindian":1,
        "Xindian City Hall":2,
        "Qizhang":3,
        "Dapinglin":4,
        "Jingmei":5,
        "Wanlong":6,
        "Gongguan":7,
        "Taipower Building":8,
        "Guting":9,
        "Chiang Kai-shek Memorial Hall":10,
        "Xiaonanmen":11,
        "Ximen":12,
        "Beimen":13,
        "Zhongshan":14,
        "Songjiang Nanjing":15,
        "Nanjing Fuxing":16,
        "Taipei Arena":17,
        "Nanjing Sanmin":18,
        "Songshan":19,
        "Xiaobitan":99,
    }

console.log("==Task 1==");

    const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
    };
    findAndPrint(messages, "Wanlong"); // print Mary
    findAndPrint(messages, "Songshan"); // print Copper
    findAndPrint(messages, "Qizhang"); // print Leslie
    findAndPrint(messages, "Ximen"); // print Bob
    findAndPrint(messages, "Xindian City Hall"); // print Vivian