let popupBg1 = document.querySelector('.popup__bg1');
let popup1 = document.querySelector('.popup1');
let oppenPopupButtons1 = document.querySelectorAll('#consumables');
let closePopupButton1 = document.querySelector('.close-popup1');


oppenPopupButtons1.forEach((buttom) => {
    buttom.addEventListener('click', (e) => {
        e.preventDefault();
        popupBg1.classList.add('active');
        popup1.classList.add('active');
    });
}); 


closePopupButton1.addEventListener('click', (e) => {
    
    popupBg1.classList.remove('active');
    popup1.classList.remove('active');
    

});




document.addEventListener('click', (e) => {
    if(e.target === popupBg1) {
        popupBg1.classList.remove('active');
        popup1.classList.remove('active');        
    }
});