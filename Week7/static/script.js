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

//Week7: Search for user data.
/*
//listen to #fetchuserdataform submit
fetchUserdataForm = document.querySelector('#fetchuserdataform');

if (fetchUserdataForm){
    fetchUserdataForm.addEventListener('submit', function onSearchFormSubmitted(event) {
        event.preventDefault();
        user_query = document.querySelector('#username_id').value;
        
        //New to week 7: fetch api. 對應main.py @app.get("/api/member")這段
        fetch('./api/member?' + new URLSearchParams({username: user_query}))
        .then(function(response){
            return response.json();
        })
        .then(function(data){
            //沒有找到或是已登出，都會return"未找到使用者"
            if (data["data"] === null){
                document.querySelector('#user_search_result').textContent = "未找到使用者";
            }
            else {
                //console.log(`${data["data"]["username"]}(${data["data"]["name"]})`);
                document.querySelector('#user_search_result').textContent = `${data["data"]["username"]} (${data["data"]["name"]})`;
            }
        })
        .catch(function(error){
            console.log("An error occured");
            console.log(error);
        });
    });
}
*/

//搜尋其他使用者會觸發的function
function onSearchFormSubmitted(event) {
    event.preventDefault();
    user_query = document.querySelector('#username_id').value;
    
    //New to week 7: fetch api. 對應main.py @app.get("/api/member")這段
    fetch('./api/member?' + new URLSearchParams({username: user_query}))
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        if (data["data"] === null){
            document.querySelector('#user_search_result').textContent = "未找到使用者";
        }
        else {
            //console.log(`${data["data"]["username"]}(${data["data"]["name"]})`);
            document.querySelector('#user_search_result').textContent = `${data["data"]["name"]} (${data["data"]["username"]})`;
        }
    })
    //如果有其他(目前尚未發現)的錯誤
    .catch(function(error){
        console.log("An error occured");
        console.log(error);
    });
};

//patchUsernameForm = document.querySelector('#patchusernameform');
//patchUsernameForm.addEventListener('submit', onPatchFormSubmitted);

//修改使用者名稱會觸發的function
function onPatchFormSubmitted(event) {
    event.preventDefault();
    if (!confirm('This will change your profile name. Are you sure?')){
        return false;
    };

    const new_username = document.querySelector("#new_username_id").value;
    //https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
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
        if ('ok' in data && data['ok']){
            console.log("Successful change!");
            resultText = document.querySelector("#name_edit_result");
            resultText.textContent = "更新成功！"
        }
        else if ('error' in data && data['error']){
            console.log("Unsuccessful change...");
            resultText = document.querySelector("#name_edit_result");
            resultText.textContent = "更新失敗"
        }
        else{
            console.log("Other error(s) occured, check backend code")
            resultText = document.querySelector("#name_edit_result");
            resultText.textContent = "更新過程中遇到其他錯誤" //還沒有實際碰到
        }
        return data;
    })
    .catch(function(error){
        console.log(error);
        resultText = document.querySelector("#name_edit_result");
        resultText.textContent = "更新過程中遇到其他錯誤" //還沒有實際碰到
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
                resultText = document.querySelector("#name_edit_result");
                resultText.innerHTML = "修改成功！"
            }
            else if ('error' in data && data['error'] === true){
                console.log("Unsuccessful change...");
                resultText = document.querySelector("#name_edit_result");
                resultText.innerHTML = "修改失敗..."
            }
            else{
                console.log("Weird thigs happened, check backend code")
                resultText = document.querySelector("#name_edit_result");
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