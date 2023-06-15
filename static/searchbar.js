t=document.getElementsByClassName('myForm');
t.keyDown(function(e){
    if(e.which==13){
        $('#myForm').submit();
    }
});