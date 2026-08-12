document.addEventListener("DOMContentLoaded", function () {
    // Quantity buttons.
    let quantityDisplay = document.getElementById("qty");
    let quantityInput = document.getElementById("qty-input");
    let arrow_up = document.getElementById("arrow-up");
    arrow_up.addEventListener("click", function (){
        let number = Number(quantityInput.value);
        let newnumber = number + 1;
        quantityDisplay.innerText = newnumber;
        quantityInput.value = newnumber;
    });
    let arrow_down = document.getElementById("arrow-down");
    arrow_down.addEventListener("click", function (){
        let number = Number(quantityInput.value);
        if (number > 1) {
            let newnumber = number - 1;
        quantityDisplay.innerText = newnumber;
        quantityInput.value = newnumber;
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