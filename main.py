from src import apprun
from flask import render_template as render
from src.heart.heartSistem import *
app = apprun()
@app.route('/')
def index():  
    flash('logiado correctamente', category='success')
    return render('index.html')

if __name__ == '__main__':
    app.run(debug=True)