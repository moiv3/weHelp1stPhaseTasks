//try to combine these FullyEntered functions?

function signupFormFullyEntered(){
    const nameEnterStatus = document.querySelector("#signup_name");
    const usernameEnterStatus = document.querySelector("#signup_username");
    const passwordEnterStatus = document.querySelector("#signup_password");
    if (nameEnterStatus.value && usernameEnterStatus.value && passwordEnterStatus.value){
        return true;
    }
    else{
        alert("One or more fields is/are blank.");
        return false;
    }
}

function signinFormFullyEntered(){
    const usernameEnterStatus = document.querySelector("#signin_username");
    const passwordEnterStatus = document.querySelector("#signin_password");
    if (usernameEnterStatus.value && passwordEnterStatus.value){
        return true;
    }
    else{
        alert("One or more fields is/are blank.");
        return false;
    }
}

function messageFormFullyEntered(){
    const messageEnterStatus = document.querySelector("#new_message");
    if (messageEnterStatus.value){
        return true;
    }
    else{
        alert("Please enter a message.");
        return false;
    }
}

function confirmDelete(){
    if (window.confirm("Do you really want to delete this message?")){
        return true;
    }
    else{        
        return false;
    }
}