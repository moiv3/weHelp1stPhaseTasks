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

//Fetch documentation: https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API/Using_Fetch
//Week 3 program starts here

const smallBoxQty = 3;
const bigBoxQty = 10;

fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
    .then(function (response) {
    return response.json();
    })
    .then(function (myJson) {
        //console.log(myJson);

        //first 3 images to small boxes
        for (let i=0;i<smallBoxQty;i++){
            //render text
            let smallBox = document.querySelectorAll(".smallbox")[i];
            let contentText = document.createTextNode(`${myJson.data.results[i].stitle}`);
            smallBox.appendChild(contentText);

            //render images
            let smallBoxImg = document.querySelectorAll(".smallboximage")[i];
            const imgURL = myJson.data.results[i].filelist.split(/(http.*?(?=http|$))/).filter(Boolean); //(https:\/\/\S+?)
            smallBoxImg.src = imgURL[0];
            //let contentImg = document.createTextNode(`${imgURL[0]}`);
            //smallBox.appendChild(contentImg);

        }
        //next 10 images to big boxes, ignore others
        for (let j=smallBoxQty;j<(smallBoxQty+bigBoxQty);j++){
            //render text
            let bigBoxText = document.querySelectorAll(".text-block-text")[j-smallBoxQty];
            let contentText = document.createTextNode(`${myJson.data.results[j].stitle}`);
            bigBoxText.appendChild(contentText);
            
            //render images
            let bigBoxImg = document.querySelectorAll(".bigboximage")[j-smallBoxQty];
            const imgURL = myJson.data.results[j].filelist.split(/(http.*?(?=http|$))/).filter(Boolean); //(https:\/\/\S+?)
            bigBoxImg.src = imgURL[0];
            //let contentImg = document.createTextNode(`${imgURL[0]}`);
            //bigBoxImg.appendChild(contentImg);
        }
        
    });
