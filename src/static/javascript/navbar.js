const abg = document.querySelector('.abg');
const navs = document.querySelector('.navs');
const abgm = document.querySelector('.abgm');
const btnsm = document.querySelector('.btnsm');


class NavbarDesplazamiento {
    nabDesplazamiento() {
        var count = 1;
        var numpi = 0;
        if (abg) {
            abg.addEventListener('click', () => {
                numpi = count++;
                if (numpi % 2 != 0) {
                    navs.style.display = 'none'
                } else {
                    navs.style.display = 'block'
                }
            });
        }
    }

    menuDesplazamiento() {
        var count = 1;
        var numpi = 0;
        if (btnsm) {
            btnsm.addEventListener('click', () => {
                numpi = count++;
                if (numpi % 2 != 0) {
                    abgm.style.display = 'block'
                } else {
                    abgm.style.display = 'none'
                }
            });
        }
    }
}




export default NavbarDesplazamiento
