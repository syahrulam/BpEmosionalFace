from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import Database
app = Flask(__name__)
app.secret_key = "bebas"
db = Database()


@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/userdata')
def userdata():
    data = db.read(None)

    return render_template('userdata.html', data = data)

@app.route('/log')
def log():
    return render_template('log.html')

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/adddata', methods = ['POST', 'GET'])
def adddata():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("Berhasil tambah data")
        else:
            flash("Error tambah data")

        return redirect(url_for('userdata'))
    else:
        return redirect(url_for('userdata'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('userdata'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatedata', methods = ['POST'])
def updatedata():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('Data diperbarui')

        else:
            flash('Error perbarui data')

        session.pop('update', None)

        return redirect(url_for('userdata'))
    else:
        return redirect(url_for('userdata'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('userdata'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletedata', methods = ['POST'])
def deletedata():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('Data dihapus')

        else:
            flash('Tidak bisa hapus data')

        session.pop('delete', None)

        return redirect(url_for('userdata'))
    else:
        return redirect(url_for('userdata'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
