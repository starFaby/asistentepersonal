import Index from "./index.js"
import NavbarDesplazamiento from "./navbar.js"

$(document).ready(function () {
    const aux = new Index()
    aux.textVoz()

    /** Navbar de desplazamiento */
    const auxNavbarDesplazamiento = new NavbarDesplazamiento()
    auxNavbarDesplazamiento.nabDesplazamiento()
    auxNavbarDesplazamiento.menuDesplazamiento()

    /** show alert */
    
})