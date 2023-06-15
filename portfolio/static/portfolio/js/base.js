window.addEventListener("DOMContentLoaded", (event) => {
    var icon = document.getElementById("toggleDark");
    icon.onclick = function () {
        console.log("AQUI");
        document.body.classList.toggle("darkmode");
        if (document.body.classList.contains("darkmode")) {
            icon.src = "sun.png";
        } else {
            icon.src = "portfolio/images/sun.png";
        }
    }

    menu = document.querySelector(".dropbtn");
    menu.onclick = function() {
        nav = document.querySelector(".nav");
        nav.classList.toggle("active");
        var arrow = document.getElementsByClassName(".ri-arrow-right-s-line");
        arrow.classList.toggle('ri-arrow-down-s-line') ;
    }








});

