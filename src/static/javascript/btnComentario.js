class Comentario{

    viewComentario(){
        /** mensaje de comentario */
        var btnComent = document.getElementById("btnComent");
        var count = 1;
        btnComent.addEventListener("click", function () {
            var comentario = document.getElementById("comentario");
            var aux = count++
            if (aux % 2 != 0) {
                comentario.style.display = 'block'
            } else {
                comentario.style.display = 'none'
            }
        });
        }
}

export default Comentario