document.addEventListener("DOMContentLoaded", function () {
    // Quantity buttons.
    let quantityDisplay = document.querySelectorAll(".qty-display");
    let quantityInput = document.querySelectorAll(".qty-input");
    let arrow_up = document.querySelectorAll(".arrow-up");

    arrow_up.forEach((num, index) =>{
        num.addEventListener("click", function () {
                let number = Number(quantityInput[index].value);
                let newnumber = number + 1;
                quantityDisplay[index].innerText = newnumber;
                quantityInput[index].value = newnumber;
            });
    })


   
    let arrow_down = document.querySelectorAll(".arrow-down");
    arrow_down.forEach((num, index) => {
        num.addEventListener("click", function () {
            let number = Number(quantityInput[index].value);
            if (number > 1) {
                let newnumber = number - 1;
            quantityDisplay[index].innerText = newnumber;
            quantityInput[index].value = newnumber;
            };
        });
    })
    
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
    if (enlarge) {
        enlarge.addEventListener("click", function(){
            enlarge.href = big_img.src

        })
    };
    // Remove from basket
    let form = document.getElementById("bag-form");
    let removebtn = document.getElementById("remove");
    if (removebtn) {
        removebtn.addEventListener("click", function() {
            let newurl = removebtn.getAttribute("data-alt-url")
            form.action = newurl;
            form.submit();
        });
    };



});