function findAndPrint(messages, currentStation){
    // your code here

    //deep copy the messages object
    let matchStation = JSON.parse(JSON.stringify(messages));
    //怕如果動到matchStation會同時動到messages.但會嗎?試一下:
    //let matchStation = messages; 
    //結果出現: 
    //task1.js:22 Uncaught TypeError: messages[message].includes is not a function
    //Bob的message被取代成12了, 所以不能includes

    //find string in object
    //console.log(messages);
    //review: why use Object.keys?
    //console.log(Object.keys(messages));
    //objects are not iterable
    //Object.keys returns an Array ['Bob', 'Mary', 'Copper', 'Leslie', 'Vivian']
    //arrays are iterable!
    //https://www.freecodecamp.org/news/how-to-iterate-over-objects-in-javascript/

    for (message of Object.keys(messages)){  
        for (station of Object.keys(stations)){
            if (messages[message].includes(station)){
            let result = stations[station];
            //update the results to matchStation
            matchStation[message] = result;
            //這裡有個考量點，我按照綠線車站的編號去編碼,那新店區公所剛好在編號2
            //所以如果新店&新店區公所都符合，會先對中1再對中2, 2會取代1
            //如果用其他的編碼方式，就需要處理(新店&新店區公所)或其他的例外
            }
        }
    }
    //console.log(matchStation);

    //deep copy the matchStation object(考量跟上面一樣)
    let matchDiff = JSON.parse(JSON.stringify(matchStation));

    //calculate the difference
    //if both user & friend at Xiaobitan or not at Xiaobitan =>直接相減
    //if only one of (user & friend) at Xiaobitan =>小碧潭那位，先算到七張，再加1
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
    //find the closest friend
    let distanceArray = []
    //console.log(Object.keys(matchDiff));
    for (person of Object.keys(matchDiff)){
        //why can't i use matchDiff.person? returns "undefined".
        //console.log(matchDiff[person]);
        distanceArray.push(matchDiff[person]);
    }
    // Math.min returns the minimum of all GIVEN NUMBERS, not an array.
    // Math.max(value1, value2, /* …, */ valueN) by MDN.
    const minDistance = Math.min(...distanceArray);

    //console.log(distanceArray);
    //console.log(...distanceArray);
    //console.log(Math.min(...distanceArray));
    //console.log(Math.min(distanceArray));
    //console.log(minDistance);

    //and finally, output matching people
    for (person of Object.keys(matchDiff)){
        if (matchDiff[person] === minDistance){
            console.log(person);
        }
        
    }
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

    //additional test data
    /*
    const messages={
        "Leslie":"I'm at home near Xiaobitan station.",
        "Bob":"I'm at Ximen MRT station.",
        "Mary":"I have a drink near Jingmei MRT station.",
        "Copper":"I just saw a concert at Taipei Arena.",
        "Vivian":"I'm at Xindian station waiting for you.",
        "WiWian":"I'm at Xindian City Hall station waiting for you.",
        "Xixian":"I'm at Qizhang station waiting for you.",
        "Yiyian":"I'm at Dapinglin station waiting for you.",
        "Zizian":"I'm at Jingmei station waiting for you.",
        "Aiaian":"I'm at Wanlong station waiting for you.",
        "Bibian":"I'm at Gongguan station waiting for you.",
        "Cician":"I'm at Taipower Building station waiting for you.",
        }
        
        findAndPrint(messages, "Xindian"); //Vivian
        findAndPrint(messages, "Xindian City Hall"); //Wiwian
        findAndPrint(messages, "Qizhang"); //Xixian
        findAndPrint(messages, "Dapinglin"); //Yiyian
        findAndPrint(messages, "Jingmei"); //Mary
        findAndPrint(messages, "Wanlong"); //Zizian
        findAndPrint(messages, "Gongguan"); //Aiaian
        findAndPrint(messages, "Taipower Building"); //Bibian
        findAndPrint(messages, "Guting"); //Cician
        findAndPrint(messages, "Chiang Kai-shek Memorial Hall"); //Cician
        findAndPrint(messages, "Xiaonanmen"); //Bob
        findAndPrint(messages, "Ximen"); //Bob
        findAndPrint(messages, "Beimen"); //Bob
        findAndPrint(messages, "Zhongshan"); //Bob
        findAndPrint(messages, "Songjiang Nanjing"); //Copper
        findAndPrint(messages, "Nanjing Fuxing"); //Copper
        findAndPrint(messages, "Taipei Arena"); //Copper
        findAndPrint(messages, "Nanjing Sanmin"); //Copper
        findAndPrint(messages, "Songshan"); //Copper
        findAndPrint(messages, "Xiaobitan"); //Leslie
    */