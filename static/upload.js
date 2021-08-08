
function content(evt,linkname) {

    var i,tabcontent, tablinks;
    // tablink = document.getElementsByClassName('buttons');
    tabcontent = document.getElementByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++){
        tabcontent[i].style.display = "none";
    }

    tablinks = document.getElementByClassName("buttons");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
    }

    document.getElementsByClassName(linkname).style.display = "block";
    evt.currentTarget.className += " active";

    
}

document.getElementByClassName(".podcast").click();



