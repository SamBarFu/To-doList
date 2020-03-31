
var s = 0;

//menu desplegable
function expand(element) { 
    var cont_nav = document.querySelector(".cont_nav");
    if (s==0) {        
        cont_nav.style.display = "block";
        s = 1;
    }else{       
        cont_nav.style.display = "none";
        s = 0;
    }
}
