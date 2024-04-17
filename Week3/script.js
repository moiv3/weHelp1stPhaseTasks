function closePopup() {
    let popupmenu = document.querySelector('.popupmenu');
    popupmenu.style.display = 'none';
    console.log('closed!');
}

function openPopup() {
    let popupmenu = document.querySelector('.popupmenu');
    popupmenu.style.display = 'block';
    console.log('opened!');
}

//https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API/Using_Fetch
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
    .then(function (response) {
    return response.json();
    })
    .then(function (myJson) {
        console.log(myJson);

        for (i=0;i<3;i++){
            let smallbox = document.querySelectorAll(".smallbox")[i];
            let contentText = document.createTextNode(`${myJson.data.results[i].stitle}`);
            smallbox.appendChild(contentText);

            let smallboxImg = document.querySelectorAll(".smallboximage")[i];
            const imgURL = myJson.data.results[i].filelist.split(/(http.*?(?=http|$))/).filter(Boolean); //(https:\/\/\S+?)
            smallboxImg.src = imgURL[0];
            console.log(imgURL[0]);
            //let contentImg = document.createTextNode(`${imgURL[0]}`);
            //smallbox.appendChild(contentImg);

        }

        for (j=3;j<13;j++){
            let bigboxtext = document.querySelectorAll(".text-block-text")[j-3];
            let contentText = document.createTextNode(`${myJson.data.results[j].stitle}`);
            bigboxtext.appendChild(contentText);
            
            let bigboxImg = document.querySelectorAll(".bigboximage")[j-3];
            const imgURL = myJson.data.results[j].filelist.split(/(http.*?(?=http|$))/).filter(Boolean); //(https:\/\/\S+?)
            bigboxImg.src = imgURL[0];
            //let contentImg = document.createTextNode(`${imgURL[0]}`);
            //bigboxImg.appendChild(contentImg);
        }
        
    });
