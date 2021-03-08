function autofill() {
    if (document.getElementById("same").checked){
     document.getElementById("login_username2").value = document.getElementById("login_username").value;
    }
    else {
     document.getElementById("login_username2").value = "";
    }
 }

 setTimeout(function popup() {
     if (document.getElementById("message").value = "You are not Logged in"){
         alert("You're not logged in")
     }
 },100
 )