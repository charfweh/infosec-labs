from flask import Flask, request, url_for, render_template, redirect


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/lfidemo1", methods=['GET'])
def lfidemo1():
    # whitelistfilename = ["text/chapter1.txt","text/chapter2.txt","text/default.txt","text/intro.txt"]
    filename = request.args.get('filename')
    print("[+] filename here",filename)
    # if filename not in whitelistfilename:
    #     return render_template("error.html")
    if filename == "":
        filename = "text/default.txt"
    print("attempting to open",filename)
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)

# @app.route("/home", methods=['POST'])
# def home():
#     filename = request.form['filename']
#     if filename == "":
#         filename = "text/default.txt"
#     f = open(filename,'r')
#     read = f.read()
#     return render_template("index.html",read = read)
@app.route("/lfidemo2",methods=['GET'])
def lfidemo2():
    whitelistfilename = ["text/chapter1.txt","text/chapter2.txt","text/default.txt","text/intro.txt"]
    filename = request.args.get('filename')
    print("[+] filename here",filename)
    if filename not in whitelistfilename:
        return render_template("error.html")
    if filename == "":
        filename = "text/default.txt"
    print("attempting to open",filename)
    f = open(filename,'r')
    read = f.read()
    return render_template("index.html",read = read)

@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
