let popupBg = document.querySelector('.popup__bg');
let popup = document.querySelector('.popup');
let oppenPopupButtons = document.querySelectorAll('#call');
let closePopupButton = document.querySelector('.close-popup');
let btnsubmit = document.querySelector('.submit');



document.addEventListener('click', (e) => {
    if(e.target === popupBg) {
        popupBg.classList.remove('active');
        popup.classList.remove('active');        
    }
});

