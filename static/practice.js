const buttons = document.querySelector('.item22');
buttons.addEventListener('click',function() {
    const menu = document.querySelector('.dropdown-item');
    const buttons1 = document.querySelector('.arrow-btn');
    if (menu.style.transform == "translateY(-150px)"){
        menu.style.transform = "translateY(1px)";
        buttons1.src = "../static/arrow2.png";
        
    }
    else {
        menu.style.transform = "translateY(-150px)";
        buttons1.src = "../static/arrow1.png";
    }
    
   
})


$(document).ready(function(){
    $("#list").click(function(){
        $(".sidebar").slideToggle();
    });
});



// const getwidth = document.querySelector().innerWidth;
const getelement = document.querySelector('.sidebar');
const hideelement = document.querySelector('#list');
window.addEventListener('resize',function(){
    const getwidth = window.innerWidth;
//    console.log(getwidth);
    if (getwidth < '950'){
        getelement.style.display = "none";
        hideelement.src = "../static/list.png"
    }
    else {
        getelement.style.display = "block";
        hideelement.src = "../static/cross.png"
    }  
});

// menu.style.transform = "translateY(-150px)";
// const menu1 = document.querySelector('.dropdown-item');
// console.log(menu1.transform.translateY);


// $(document).ready(function(){
//     $(".item22").on({
//        fadeIn: function(){
//            return 'dropdown-item';
//        } 
//     })
// });

const body = document.querySelector('a');
body.draggable = "false";



const popup = document.querySelector('.is-popup');
const card = document.querySelector('.blog-section1');
card.addEventListener('click',function(){
    if (popup.style.display == "none"){
        popup.style.display = "block";
    }
    else{
        popup.style.display = "none";
    }
})