function checklengthuser(inputtxt, minlength, maxlength){
var field = inputtxt.value;
var mnlength = minlength;
var mxlength = maxlength;
if(field.length< mnlength || field.length>mxlength){
    alert("Enter a User ID between "+mnlength+ " and " + mxlength + " characters.");
    return false;
}
else
return true;
}
function checklengthpass(inputpass, minlength, maxlength){
var field = inputpass.value;
var mnlength = minlength;
var mxlength = maxlength;
if(field.length< mnlength || field.length>mxlength){
    alert("Enter a password between " + mnlength + " and " + mxlength + " characters.");
    return false;
}
else
return true;

}