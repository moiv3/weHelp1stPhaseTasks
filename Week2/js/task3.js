function func(...data){
    // your code here
    //"...data" means: there might be more than 1 data. all "data"s.

    //create an array of middle characters.
    let middle_char_array = []
    //when do we use for-of? when do we use for-in?
    for (item of data){
        //console.log(item[Math.ceil((item.length-1)/2)]);
        middle_char_array.push(item[Math.ceil((item.length-1)/2)]);     
    }
    //for example, middle_char_array=["大,"明","明"]
    console.log(middle_char_array);

    //count how many middle_char's are in this array. for those with one middle_char, they are to be printed.
    let flag = 0;
    for (middle_char of middle_char_array){
        //no count method in js, manually do so
        let middle_char_counter = 0;
        for (let i = 0; i < middle_char_array.length; i++) {
            //console.log(middle_char_array[i]);
            if (middle_char_array[i] === middle_char){
                middle_char_counter ++;
            }
        }
        if (middle_char_counter === 1){;
        //middle_char_array.index(middle_char): 第幾個item = 1
        //data[~]: 印出原array(tuple?)第"那個"item
        //javascript使用indexOf = python的index method
        //因為第幾個item順序沒有變
        console.log(data[middle_char_array.indexOf(middle_char)]);
        flag = 1;
        }

    }
    //if no match
    if (flag === 0){
        console.log("沒有");
    }
}

    console.log("==Task 3==")

    func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
    func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
    func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
    func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安    
    func("郭宣雅", "夏曼藍波安", "郭宣恆", "林靜花"); // print 夏曼藍波安, 林靜花
    