function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("main").style.marginLeft = "20px";
}
  
function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}
document.addEventListener('click', function handleClickOutsideBox(event) {
  const box = document.getElementById('box');

  if (!box.contains(event.target)) {
    box.style.display = 'none';
  }
});
  