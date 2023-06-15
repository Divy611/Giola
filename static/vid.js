let videolist=document.querySelector();
videolist.forEach(vid=>{
    vid.onclick=()=>{
        videoList.forEach(remove=>{remove.classList.remove('active')});
        vid.classList.add('active');
        let src=vid.querySelector('.list-video').src;
        let title=vid.querySelector('.list-video').innerHTML;
        document.querySelector('main-video-container .main-video').src=src;
        document.querySelector('main-video-container .main-vid-title').innerHTML=title;
    }
}
);
