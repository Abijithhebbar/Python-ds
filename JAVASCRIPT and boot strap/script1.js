var randomNum; 
// Stores a Random number

function create() { // creates the grid
    randomNum = Math.floor(Math.random() * 9) + 1;
    console.log(randomNum);
     var name = document.forms["name"]["fname"]
    if (document.forms["name"]["fname"].value == "" || document.forms["name"]["lname"].value == "") {
        alert("Enter the name fields");
    }else {
        fname = document.getElementById("fname").value;
        lname = document.getElementById("lname").value;
        document.getElementById("fname").disabled = true;
        document.getElementById("lname").disabled = true;
    for (var i = 1; i < 10; i++) {
var d1 = document.getElementById('one');
d1.insertAdjacentHTML('beforeend', '<div class="col-xs-4 well"><button style="width: 100%" id = "'+i+'" onclick="myFunction(this.id)"><b><center>'+i+'</center></b></button></div>');
}
count = 1;
document. getElementById("play").disabled = true;
}
}




var count = 1;
var result;
var fname;
var lname;


function myFunction(num) { // Gives the result
var a;
if (num == randomNum) {
    document.getElementById(num).style.backgroundColor = "green";
    document.getElementById(num).innerHTML = "BOMB found";
    document.getElementById(num).disabled = true; 
    for (var i = 1; i <= 9; i++) {
            document.getElementById(i).disabled = true; 

    }

    document.getElementById("chances").innerHTML = "HIP HIP HURRAY!!! you won the game 🎉";
    document.getElementById("refresh").style.display = "block";
    result = "You won the game"
    document.getElementById("img").src = "happy.gif";

    // alert("HIP HIP HURRAY!!!");
    var d1 = document.getElementById('tc1');
    d1.insertAdjacentHTML('afterbegin', fname + "<br>");
    var d2 = document.getElementById('tc2');
    d2.insertAdjacentHTML('afterbegin', lname + "<br>");
    var d3 = document.getElementById('tc3');
    d3.insertAdjacentHTML('afterbegin', result + "<br>");
    var d4 = document.getElementById('tc4');
    d4.insertAdjacentHTML('afterbegin', count + "<br>");
        
} else {
        count++;

    if (count <= 3) {
    a = 0;
    a = 4 - count;
    document.getElementById(num).style.backgroundColor = "red";
    document.getElementById(num).innerHTML = "BOMB not found";
    document.getElementById(num).disabled = true; 
    document.getElementById("chances").innerHTML = "chances left :" + a;
    } else {
    document.getElementById(num).style.backgroundColor = "red";
    document.getElementById(num).innerHTML = "BOMB not found";
    document.getElementById(num).disabled = true; 
    for (var i = 1; i <= 9; i++) {
            document.getElementById(i).disabled = true; 

    }

    document.getElementById("chances").innerHTML = "chances left :" + 0;
    document.getElementById("chances").innerHTML = "OHH no you lost the game need practice click try again";
    result = "You lost the game";
    count = count-1;
    document.getElementById("img1").src = "sad.gif";
    // alert("you lost the game");
    var d1 = document.getElementById('tc1');
    d1.insertAdjacentHTML('afterbegin', fname + "<br>");
    var d2 = document.getElementById('tc2');
    d2.insertAdjacentHTML('afterbegin', lname + "<br>");
    var d3 = document.getElementById('tc3');
    d3.insertAdjacentHTML('afterbegin', result + "<br>");
    var d4 = document.getElementById('tc4');
    d4.insertAdjacentHTML('afterbegin', count + "<br>");

        document.getElementById("refresh").style.display = "block";


    }
    
}

}
function resetfun() { // resets on the click of Wanna Play Again!!
    
document.getElementById("fname").disabled = false;
document.getElementById("lname").disabled = false;
document. getElementById("play").disabled = false;
document.getElementById("name").reset();
document.getElementById("refresh").style.display = "none";
document.getElementById("one").innerHTML= "";
document.getElementById("chances").innerHTML= "";

document.getElementById("img1").src = "";
document.getElementById("img").src = "";




}
