

/* Slideshow */
function slideShow() {

    let x = 0;
    let time = 5000;
    
    const slides = document.getElementsByClassName('slide');
    
    function slide(){
        if( x > slides.length-1) {
            x = 0;
        }
    
        for(i=0;i < slides.length; i++){
            slides[i].style.display="none";
        }
    
        slides[x].style.display="flex";
        x++;
    }
    
    setTimeout(slide,0);
    setInterval(slide,time);
    
    }
    /* end of slideshow */

