function closePopup() {
    let popupmenu = document.querySelector('.popupmenu');
    popupmenu.style.display = 'none';
    //console.log('closed!');
}

function openPopup() {
    let popupmenu = document.querySelector('.popupmenu');
    popupmenu.style.display = 'block';
    //console.log('opened!');
}

//Fetch documentation: https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API/Using_Fetch
//Week 3 program starts here

const smallBoxQty = 3;
const bigBoxQty = 10;
const loadMoreButtonImages = 10;
let totalBoxesLoaded = 0;
let tripFile;
let entries;

const dataSource = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1";


fetch(dataSource)
    .then(function (response) {
        return response.json();
    })
    .then(function (myJson) {
        tripFile = myJson;
        //console.log(tripFile)
        entries = tripFile.data.results.length;
        //console.log(`Entries: ${entries}`);

        //first 3 images to small boxes
        for (let i=0;i<smallBoxQty;i++){
            //console.log(i);
            //render text
            let smallBox = document.querySelectorAll(".smallbox > span")[i];
            smallBox.textContent = myJson.data.results[i].stitle;
            //previous version uses appendChild
            //let smallBox = document.querySelectorAll(".smallbox")[i];
            //let contentText = document.createTextNode(`${myJson.data.results[i].stitle}`);
            //smallBox.appendChild(contentText);
            
            //render images
            let smallBoxImg = document.querySelectorAll(".smallboximage")[i];
            const imgURL = myJson.data.results[i].filelist.split(/(http.*?(?=http|$))/).filter(Boolean); //(https:\/\/\S+?)
            //console.log(imgURL);
            smallBoxImg.src = imgURL[0];
            //let contentImg = document.createTextNode(`${imgURL[0]}`);
            //smallBox.appendChild(contentImg);
            totalBoxesLoaded++;
            
        }
        //next 10 images to big boxes, ignore others
        for (let j=smallBoxQty;j<(smallBoxQty+bigBoxQty);j++){
            
            //render text
            let bigBoxText = document.querySelectorAll(".text-block-text")[j-smallBoxQty];
            let contentText = myJson.data.results[j].stitle;
            let contentTextNode = document.createTextNode(`${myJson.data.results[j].stitle}`);
            bigBoxText.textContent = contentText;
            
            //render images
            let bigBoxImg = document.querySelectorAll(".bigboximage")[j-smallBoxQty];
            const imgURL = myJson.data.results[j].filelist.split(/(http.*?(?=http|$))/).filter(Boolean); //(https:\/\/\S+?)
            bigBoxImg.src = imgURL[0];
            //let contentImg = document.createTextNode(`${imgURL[0]}`);
            //bigBoxImg.appendChild(contentImg);
            totalBoxesLoaded++;
            

            //use a function to replace old code
            //createBigBox(totalBoxesLoaded);
        }
        
    });

    //https://webdesign.tutsplus.com/how-to-implement-a-load-more-button-with-vanilla-javascript--cms-42080t
function loadMore() {
    //let bigBoxGroup = document.querySelector(".bigboxgroup");
    //console.log(bigBoxGroup);
    //console.log(tripFile);
    for(k=0;k<loadMoreButtonImages;k++){
        if (totalBoxesLoaded < entries){
            createBigBox(totalBoxesLoaded);
        }
        else {
            console.log(`All ${entries} entries displayed!`);
            document.querySelector(".loadmorebtn").disabled = true;
            document.querySelector(".loadmorebtn").textContent = "All entries displayed!";
        }
    }
}
//#TODO:全部做完時的例外/邊界條件處理方式=>done!

//沿著html div/img的排版方式依序定義出要加的Box的模樣
//一開始使用innerHTML, 後來調整為逐個box去定義後加入
function createBigBox(index){
    //console.log(index);
    const bigBoxGroup = document.querySelector(".bigboxgroup");
    const newBox = document.createElement("div");
    const newBoxText = tripFile.data.results[index].stitle;
    const newBoxImgSource = tripFile.data.results[index].filelist.split(/(http.*?(?=http|$))/).filter(Boolean)[0];
    newBox.className = "bigbox1";

    const newBoxImg = document.createElement("img");
    newBoxImg.src = tripFile.data.results[index].filelist.split(/(http.*?(?=http|$))/).filter(Boolean)[0];
    newBoxImg.className = "bigboximage";
    newBox.appendChild(newBoxImg);

    const outerTextBlock = document.createElement("div");
    outerTextBlock.className = "text-block";
    const innerTextBlock = document.createElement("div");
    innerTextBlock.className = "text-block-text";
    innerTextBlock.textContent = tripFile.data.results[index].stitle;
    outerTextBlock.appendChild(innerTextBlock);
    newBox.appendChild(outerTextBlock);

    const starImg = document.createElement("img");
    starImg.src = "star.svg";
    starImg.className = "starimg";
    newBox.appendChild(starImg);

    /*kind of dangerous? malicious inputs might go through?
    newBox.innerHTML = `<img src="${newBoxImg}" class="bigboximage">\
    <div class="text-block">\
        <div class="text-block-text">${newBoxText}</div>\
    </div><img src="star.svg" class="starimg"></img>`
    */

    bigBoxGroup.appendChild(newBox);
    totalBoxesLoaded++;
}