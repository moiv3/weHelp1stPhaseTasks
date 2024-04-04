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