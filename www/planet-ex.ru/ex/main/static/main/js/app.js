const tabbtnnav = document.querySelectorAll(".btnnav");
const tabroom = document.querySelectorAll(".room");


tabbtnnav.forEach(onTabCklick);

function onTabCklick(item) {

    
    item.addEventListener('click', function() {
        let currentBtn = item;
        let roomid = currentBtn.getAttribute('data-tab');
            
        let currenttab = document.querySelector(roomid);
        
        if( ! currentBtn.classList.contains('active')) {
            tabbtnnav.forEach(function(item) {
                item.classList.remove('active');
            });
            tabroom.forEach(function(item) {
                item.classList.remove('active');
            });
        
        
            currentBtn.classList.add('active');
            currenttab.classList.add('active');
        }


    });
};

document.querySelector(".btnnav").click();



