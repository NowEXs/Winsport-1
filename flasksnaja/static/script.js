function toggleHam(x) {
    x.classList.toggle("change");

    let myMenu = document.getElementById('myMenu')
    let winDiv = document.getElementById('winDiv')

    if (myMenu.className === 'menu') {
        myMenu.className += ' menu-active'
        if (myMenu.className === 'menu menu-active') {
            winDiv.className = ' win-active'
        }
    } else {
        myMenu.className = 'menu'
        winDiv.className = 'win'
    }
    

} 


document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll("[data-carousel-button]");

    buttons.forEach(button => {
        button.addEventListener("click", () => {
            const offset = button.dataset.carouselButton === "next" ? 1 : -1;
            const slides = button.closest("[data-carousel]").querySelector("[data-slides]");

            const activeSlide = slides.querySelector("[data-active]");
            let newIndex = [...slides.children].indexOf(activeSlide) + offset;
            if (newIndex < 0) newIndex = slides.children.length - 1;
            if (newIndex >= slides.children.length) newIndex = 0;

            activeSlide.removeAttribute("data-active");
            slides.children[newIndex].setAttribute("data-active", true);
        });
    });

    document.querySelectorAll(".carousel img").forEach(slide => {
        slide.addEventListener("click", () => {
            const popupImg = document.querySelector('.popup-img');
            const popupImgSrc = slide.getAttribute("src");
            popupImg.style.display = 'block';
            popupImg.querySelector('img').src = popupImgSrc;
        });
    });

    document.querySelector('.popup-img span').onclick = () => { //ไว้ลบรูป
        document.querySelector('.popup-img').style.display = 'none';
    };
});
