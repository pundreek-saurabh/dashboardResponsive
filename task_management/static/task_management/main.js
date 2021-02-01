var today = new Date();
var month=['January','February','March','April','May','June','July','August','September','October','November','December'];
var dd = today.getDate();

var mm = today.getMonth(); 
var yyyy = today.getFullYear();
if(dd<10) 
{
    dd='0'+dd;
} 
today = dd+' '+month[mm]+','+yyyy;
console.log(today);
document.getElementById("date").innerHTML=today;