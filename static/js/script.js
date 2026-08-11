document.addEventListener("DOMContentLoaded", function () {
    // Quantity buttons.
    let quantity = document.getElementById("qty");
    let arrow_up = document.getElementById("arrow-up");
    arrow_up.addEventListener("click", function (){
        let number = Number(quantity.innerText);
        quantity.innerText = number + 1;
    });
    let arrow_down = document.getElementById("arrow-down");
    arrow_down.addEventListener("click", function (){
        let number = Number(quantity.innerText);
        if (number > 0) {
        quantity.innerText = number - 1;
        };
    });
    // Product detail main image display. 
    let big_img = document.getElementById("img-big");
    let small_imgs = document.querySelectorAll(".img-small");
    
    small_imgs.forEach(img => {
        img.addEventListener("click",function(event) {
            let imgsrc = event.currentTarget.src;
            big_img.src=imgsrc;
        });

    });
    // Enalarge product detail main image.
    let enlarge = document.getElementById("enlarge");
    enlarge.addEventListener("click", function(){
        enlarge.href = big_img.src

    })




})