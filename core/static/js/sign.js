
window.onload = function() {
    for (let i = 1; i <= 31; i++) {
        document.querySelector(".field-day").innerHTML += `<option value="`+i+`">`+i+`</option>`;        
    }
    for (let i = 1; i <= 12; i++) {
        document.querySelector(".field-month").innerHTML += `<option value="`+i+`">`+i+`</option>`;        
    }
    for (let i = 1950; i <= 2006; i++) {
        document.querySelector(".field-year").innerHTML += `<option value="`+i+`">`+i+`</option>`;        
    }
  };

function showAlert(element){
    var alert = document.querySelector(".alert");  
    alert.style.display = "flex";        
}

function closeAlert(element){
    var alert = document.querySelector(".alert");  
    alert.style.display = "none";        
}

