const page1 = document.querySelector("#page1"); 
const page2 = document.querySelector("#page2");


function turn(){
    page1.style.WebkitAnimation = "fadeOut 1s";
    page1.style.animation = "fadeOut 1s";
    page2.style.WebkitAnimation = "fadeIn 1s";
    page2.style.animation = "fadeIn 1s";

    page1.style.display = "none";
    page2.style.display = "block";
}