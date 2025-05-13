from src.heart.heartSistem import *
from src.heart.heartServices  import *
from src.heart.heartFormWtf import *
class ClientControllerComentario:
        
    def onGetClientControllerComentario():
        try:
            comentario = request.form["txtComentario"]
            email = request.form["txtEmail"]
            id = 1
            estado = 1
            userId = 1
            createdat = datetime.now()

            if comentario != '' and email == '':
                email = 'asistenteabogado63@gmail.com'
                respuesta = ClientServiceComentario.onGetClientServiceComentario(id, comentario, email, estado, createdat ,userId)
                if respuesta:
                    flash('Comentario Guardado Exitosamente', category='success')
                    return render('index.html')
                else:
                    flash('Error al guardar', category='error')
                    return render('index.html')
            elif comentario != '' and email != '':
                respuesta = ClientServiceComentario.onGetClientServiceComentario(id, comentario, email, estado, createdat ,userId)
                if respuesta:
                    flash('Comentario Guardado Exitosamente', category='success')
                    return render('index.html')
                else:
                    flash('Error al guardar', category='error')
                    return render('index.html')
            else:
                flash('Campos vacios, llene porfabor', category='info')
                return render('index.html')
            
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            print(error)
            return render('errors/error500.html')
    

