const tabbtncom = document.querySelectorAll(".btncom");
const tabcom = document.querySelectorAll(".comment");


tabbtncom.forEach(onTabCklick);

function onTabCklick(item) {

    
    item.addEventListener('click', function() {
        let currentBtn = item;
        let comid = currentBtn.getAttribute('data-tab');
            
        let currenttab = document.querySelector(comid);
        
        if( ! currentBtn.classList.contains('active')) {
            tabbtncom.forEach(function(item) {
                item.classList.remove('active');
            });
            tabcom.forEach(function(item) {
                item.classList.remove('active');
            });
        
        
            currentBtn.classList.add('active');
            currenttab.classList.add('active');
        }


    });
};

document.querySelector(".btnnav").click();