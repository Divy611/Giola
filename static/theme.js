tippy('.link',{placement: 'bottom'})
const toggle=document.querySelector('.js-change-theme');
const body=document.querySelector('body');
const profile=document.getElementById('profile');
toggle.addEventListener('click',()=>{
    if (body.classList.contains('text-black')) {
        toggle.innerHTML="Light Theme";
        body.classList.remove('text-black');
        body.classList.add('text-gray-100');
        profile.classList.remove('bg-white');
        profile.classList.add('bg-black');
    }
    else{
        toggle.innerHTML="Dark Theme";
        body.classList.remove('text-gray-100');
        body.classList.add('text-black');
        profile.classList.remove('bg-black');			
        profile.classList.add('bg-white');
    }
});