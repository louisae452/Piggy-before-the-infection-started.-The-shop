document.addEventListener("DOMContentLoaded", function () {
    // Quantity buttons.
    let quantityDisplay = document.querySelectorAll(".qty-display");
    let quantityInput = document.querySelectorAll(".qty-input");
    let arrow_up = document.querySelectorAll(".arrow-up");
    arrow_up.forEach(function (num, index) {
        num.addEventListener("click", function () {
            let number = Number(quantityInput[index].value);
            let newnumber = number + 1;
            quantityDisplay[index].innerText = newnumber;
            quantityInput[index].value = newnumber;
        });
    });
    let arrow_down = document.querySelectorAll(".arrow-down");
    arrow_down.forEach(function (num, index) {
        num.addEventListener("click", function () {
            let number = Number(quantityInput[index].value);
            if (number > 1) {
                let newnumber = number - 1;
                quantityDisplay[index].innerText = newnumber;
                quantityInput[index].value = newnumber;
            }
        });
    });
    // Product detail main image display.
    let big_img = document.getElementById("img-big");
    let small_imgs = document.querySelectorAll(".img-small");
    small_imgs.forEach(function (img) {
        img.addEventListener("click", function (event) {
            let imgsrc = event.currentTarget.src;
            big_img.src = imgsrc;
        });
    });
    // Enalarge product detail main image.
    let enlarge = document.getElementById("enlarge");
    if (enlarge) {
        enlarge.addEventListener("click", function () {
            enlarge.href = big_img.src;
        });
    }
    // Remove items from the basket.
    let removebtn = document.querySelectorAll(".remove");
    if (removebtn.length > 0) {
        removebtn.forEach(function (button) {
            button.addEventListener("click", function () {
                let form = button.closest(".bag-form");
                if (form) {
                    let newurl = button.getAttribute("data-alt-url");
                    form.action = newurl;
                    form.submit();
                }
            });
        
        });
    }
    // Star ratings.
    let star_input = document.getElementById("star-input");
    let star1 = document.getElementById("star1");
    let star2 = document.getElementById("star2");
    let star3 = document.getElementById("star3");
    let star4 = document.getElementById("star4");
    let star5 = document.getElementById("star5");
    if (star1 && star2 && star3 && star4 && star5 && star_input) {
        star1.addEventListener("click", function () {
            star_input.value = 1;
            star1.classList.remove("fa-regular");
            star2.classList.remove("fa-solid");
            star3.classList.remove("fa-solid");
            star4.classList.remove("fa-solid");
            star5.classList.remove("fa-solid");
            star1.classList.add("fa-solid");
            star2.classList.add("fa-regular");
            star3.classList.add("fa-regular");
            star4.classList.add("fa-regular");
            star5.classList.add("fa-regular");
        });
        star2.addEventListener("click", function () {
            star_input.value = 2;
            star1.classList.remove("fa-regular");
            star2.classList.remove("fa-regular");
            star3.classList.remove("fa-solid");
            star4.classList.remove("fa-solid");
            star5.classList.remove("fa-solid");
            star1.classList.add("fa-solid");
            star2.classList.add("fa-solid");
            star3.classList.add("fa-regular");
            star4.classList.add("fa-regular");
            star5.classList.add("fa-regular");
        });
        star3.addEventListener("click", function () {
            star_input.value = 3;
            star1.classList.remove("fa-regular");
            star2.classList.remove("fa-regular");
            star3.classList.remove("fa-regular");
            star4.classList.remove("fa-solid");
            star5.classList.remove("fa-solid");
            star1.classList.add("fa-solid");
            star2.classList.add("fa-solid");
            star3.classList.add("fa-solid");
            star4.classList.add("fa-regular");
            star5.classList.add("fa-regular");
        });
        star4.addEventListener("click", function () {
            star_input.value = 4;
            star1.classList.remove("fa-regular");
            star2.classList.remove("fa-regular");
            star3.classList.remove("fa-regular");
            star4.classList.remove("fa-regular");
            star5.classList.remove("fa-solid");
            star1.classList.add("fa-solid");
            star2.classList.add("fa-solid");
            star3.classList.add("fa-solid");
            star4.classList.add("fa-solid");
            star5.classList.add("fa-regular");
        });
        star5.addEventListener("click", function () {
            star_input.value = 5;
            star1.classList.remove("fa-regular");
            star2.classList.remove("fa-regular");
            star3.classList.remove("fa-regular");
            star4.classList.remove("fa-regular");
            star5.classList.remove("fa-regular");
            star1.classList.add("fa-solid");
            star2.classList.add("fa-solid");
            star3.classList.add("fa-solid");
            star4.classList.add("fa-solid");
            star5.classList.add("fa-solid");
        });
    }
    // Delete review.
    let deletereview = document.getElementById("deletereview");
    let deletebox = document.getElementById("deletebox");
    let cancelbutton = document.getElementById("cancelbutton");
    let deletebutton = document.getElementById("deletebutton");
    let updatereview = document.getElementById("updatereview");
    if (
        deletebox &&
        deletereview &&
        cancelbutton &&
        deletebutton &&
        updatereview
    ) {
        deletereview.addEventListener("click", function (event) {
            event.preventDefault();
            deletebox.style.visibility = "visible";
        });
        cancelbutton.addEventListener("click", function (event) {
            event.preventDefault();
            deletebox.style.visibility = "hidden";
        });
        deletebutton.addEventListener("click", function (event) {
            event.preventDefault();
            let newinput = document.createElement("input");
            newinput.type = "hidden";
            newinput.name = "action";
            newinput.value = "delete";
            updatereview.appendChild(newinput);
            updatereview.submit();
        });
    }
});