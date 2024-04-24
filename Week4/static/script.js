function checkboxCheck(){
    const checkboxStatus = document.querySelector("#termsagreed");
    if (checkboxStatus.checked === false){
        alert("Please check the check box first.")
        return false;
    }
    else{
        return true;
    }
}

/*
const element = document.querySelector(".general-form-2");
element.addEventListener("submit", event => {
    event.preventdefault();

    const theInteger = document.querySelector("#the_integer").value
    //console.log(theInteger);console.log(typeof(theInteger));console.log(parseInt(theInteger));console.log(typeof(parseInt(theInteger)));
    if (isNaN(theInteger) === true){
        //is string
        alert("Please enter a positive number.");
        console.log("catch1");
        return false;
    }
    else if (parseInt(theInteger) <= 0){
        //smaller than zero
        alert("Please enter a positive number.");
        console.log("catch2");
        return false;
    }
    else if (parseInt(theInteger) !== parseFloat(theInteger)){
        //not whole number
        alert("Please enter a positive number.");
        console.log("catch3");
        return false;
    }
    else{
        console.log("here!");
        document.location = "/square/" + theInteger
        return false;
    }
    
});
*/

function integerCheck(){
    const theInteger = document.querySelector("#the_integer").value
    //console.log(theInteger);console.log(typeof(theInteger));console.log(parseInt(theInteger));console.log(typeof(parseInt(theInteger)));
    if (isNaN(theInteger) === true){
        //is string
        alert("Please enter a positive number.");
        console.log("catch1");
        return false;
    }
    else if (parseInt(theInteger) <= 0){
        //smaller than zero
        alert("Please enter a positive number.");
        console.log("catch2");
        return false;
    }
    else if (parseInt(theInteger) !== parseFloat(theInteger)){
        //not whole number
        alert("Please enter a positive number.");
        console.log("catch3");
        return false;
    }
    else{
        document.location = "./square/" + theInteger
        return false;
    }
}