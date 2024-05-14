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

fetchUserdataForm = document.querySelector('#fetchuserdataform');

if (fetchUserdataForm){
    fetchUserdataForm.addEventListener('submit', function onSearchFormSubmitted(event) {
        event.preventDefault();
        user_query = document.querySelector('#username_id').value;
        console.log(user_query);
        //response = fetchUserData(user_query);
        //console.log(response);
        fetch('./api/member?' + new URLSearchParams({username: user_query}))
        .then(function(response){
            console.log(response);
            //console.log(response.json());
            return response.json();
        })
        .then(function(data){
            console.log(data);
            console.log(data["data"] === null);
            if (data["data"] === null){
                document.querySelector('.user-search-result').innerHTML = "未找到使用者";
            }
            else {
                console.log(`${data["data"]["username"]}(${data["data"]["name"]})`);
                document.querySelector('.user-search-result').innerHTML = `${data["data"]["username"]}(${data["data"]["name"]})`;
            }//except part needs adding
        })
        .catch(function(error){
            console.log("An error occured");
            console.log(error);
        });
    });
}

patchUsernameForm = document.querySelector('#patchusernameform');
patchUsernameForm.addEventListener('submit', onPatchFormSubmitted);

function onPatchFormSubmitted(event) {
    event.preventDefault();
    if (!confirm('This changes your profile naMMMme. Do you wish to continue?')){
        return false;
    };

    const new_username = document.querySelector("#new_username_id").value;
    console.log(new_username);
    fetch('./api/member',{
        method: 'PATCH',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"name":new_username})
        }
    )
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if ('ok' in data && data['ok'] === true){
            console.log("Successful change!");
            resultText = document.querySelector("#displaynameeditresult");
            resultText.innerHTML = "修改成功！"
        }
        else if ('error' in data && data['error'] === true){
            console.log("Unsuccessful change...");
            resultText = document.querySelector("#displaynameeditresult");
            resultText.innerHTML = "修改失敗..."
        }
        else{
            console.log("Weird thigs happened, check backend code")
            resultText = document.querySelector("#displaynameeditresult");
            resultText.innerHTML = "修改過程中遇到其他錯誤"
        }
        return data;
    })
    .catch(function(error){
        console.log(error);
    });
};

/*
if (patchEvent){
    patchEvent.addEventListener('submit', function onPatchFormSubmitted(event) {
        event.preventDefault();
        const new_username = document.querySelector("#new_username_id").value;
        console.log(new_username);
        fetch('./api/member',{
            method: 'PATCH',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({"name":new_username})
            }
        )
        .then(function(response){
            return response.json();
        })
        .then(function(data){
            if ('ok' in data && data['ok'] === true){
                console.log("Successful change!");
                resultText = document.querySelector("#displaynameeditresult");
                resultText.innerHTML = "修改成功！"
            }
            else if ('error' in data && data['error'] === true){
                console.log("Unsuccessful change...");
                resultText = document.querySelector("#displaynameeditresult");
                resultText.innerHTML = "修改失敗..."
            }
            else{
                console.log("Weird thigs happened, check backend code")
                resultText = document.querySelector("#displaynameeditresult");
                resultText.innerHTML = "修改過程中遇到其他錯誤"
            }
            return data;
        })
        .catch(function(error){
            console.log(error);
        });
    });
}
*/