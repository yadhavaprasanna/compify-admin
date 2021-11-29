var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate(){
var username = document.getElementById("username").value;
var password = document.getElementById("password").value;
if ( username == "compify" && password == "vasty6"){
alert ("Login successfully");
window.location = "homepage.html"; // Redirecting to other page.
return false;
}
else if( username == "" && password == "")
{
    alert("punda username password enter panuda")
}
else if( username == "compify" && password == "")
{
    alert("password podra punda")
}
else{
// Decrementing by one.
alert("Thapu thapu");
// Disabling fields after 3 attempts.

return false;
}
}
