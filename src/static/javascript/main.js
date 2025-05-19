import Index from "./index.js"
import NavbarDesplazamiento from "./navbar.js"
import Comentario from "./btnComentario.js"
/** eventos */
import "./caracteresDispon.js"

$(document).ready(function () {
    const aux = new Index()
    aux.textVoz()

    /** Navbar de desplazamiento */
    const auxNavbarDesplazamiento = new NavbarDesplazamiento()
    auxNavbarDesplazamiento.nabDesplazamiento()
    auxNavbarDesplazamiento.menuDesplazamiento()

    /** Comentario */
    const auxComenatrio = new Comentario()
    auxComenatrio.viewComentario()
    
})