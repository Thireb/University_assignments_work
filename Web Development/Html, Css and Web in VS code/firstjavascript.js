function required(){
    var empt = document.forms["form"]["fname"].value;
    if (empt == ""){
    alert("Enter something");
    return false;}
    else{
    alert("you entered something.");
    return true;

    }
}