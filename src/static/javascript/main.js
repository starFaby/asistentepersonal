import Index from "./index.js"
import NavbarDesplazamiento from "./navbar.js"

$(document).ready(function () {
    const aux = new Index()
    aux.textVoz()

    /** Navbar de desplazamiento */
    const auxNavbarDesplazamiento = new NavbarDesplazamiento()
    auxNavbarDesplazamiento.nabDesplazamiento()
    auxNavbarDesplazamiento.menuDesplazamiento()

    /** mensaje de comentario */
    var btnComent = document.getElementById("btnComent");
    var count = 1;
    btnComent.addEventListener("click", function () {
        var comentario = document.getElementById("comentario");
        var aux = count++
        if (aux % 2 != 0) {
            comentario.style.display = 'none'
        } else {
            comentario.style.display = 'block'
        }
    });
})