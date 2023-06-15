function fun(el){
    var element=el;
    element.remove();
}
function prn(){
    let sec0=document.getElementById("sec0");
    let cl=sec0.cloneNode(true);
    for(let i=1;i<=100;i++){
        document.body.appendChild(cl);
    }
}
function prn1(){
    let wrapper=document.getElementsByClassName("wrapper");
    let cl1=wrapper.cloneNode(true);
    for(let j=1;j<=100;j++){
        document.body.appendChild(cl1);   
    }
}