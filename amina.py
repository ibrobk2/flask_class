from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('bgChanger.html')


@app.route('/login')
def login():
    name = "Aminatu"
    return render_template('login.html', my=name, dear="Ibrahim")

myfamily = ['Aminatu', 'Hauwa', 'Maryam', 'Aisha', 'Bilkisu', 'Hadiza', 'Asiya']

@app.route('/family')
def family():
    return render_template('navbar.html', fam = myfamily)




if __name__=='__main__':
    # app.debug = True
    app.run(debug=True)


