
function expandTaskNotCompleted(element) {
    var task = document.querySelectorAll(".task-not-completed");    
    task.forEach((t, i) => {
        if(i+1 == element.id) {
            if (t.style.display == "none") {     
                t.style.display = "block";
            } else {
                t.style.display = "none";
            }    
        } 
    });  
}

function expandTaskCompleted(element) {
    var task = document.querySelectorAll(".task-completed");
    task.forEach((t, i) => {
        if(i+1 == element.id) {
            if (t.style.display == "none") {     
                t.style.display = "block";
            } else {
                t.style.display = "none";
            }    
        } 
    }); 
}

/* function showPopUp(id) {
    var popUp = document.querySelectorAll(".cont-popup");
    var scroll = document.querySelector(".body-bg");    
    popUp.forEach((t, i) => {
        if(i+1 == id) {           
            t.style.display = "flex"; 
            scroll.style.overflowY = "hidden";   
        } 
    }); 
} */

function showPopUp(element) {
    console.log(element.href)
    var popUp = document.querySelector(".cont-popup");
    var scroll = document.querySelector(".body-bg"); 
    var id = document.getElementById("id-task");              
    popUp.style.display = "flex"; 
    scroll.style.overflowY = "hidden";  
    id.href = "{% url 'home' %}"
}

function closePopUp(id) {
    var popUp = document.querySelectorAll(".cont-popup");   
    console.log(popUp.length)  
    popUp.forEach((t, i) => {
        if(i+1 == id) {           
            t.style.display = "none";   
        } 
    }); 
}
