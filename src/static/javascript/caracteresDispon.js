/** cantidad de caracteres disponibles */

    export default document.getElementById("txtComentario").addEventListener("keyup", function(){
        let cant = document.getElementById("txtComentario").value.length;
        let disponibles = 110 - parseInt(cant);
        document.getElementById("cantidad").innerHTML = disponibles;
    })