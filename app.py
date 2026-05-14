from flask import Flask, render_template, request, send_file
import qrcode as qr
import os

app = Flask(__name__)



@app.route('/',methods=['POST', 'GET'])

def home():
    image_generated=False

    file_path = "static/qrcode.png"

    if request.method == 'POST':

        url= request.form['content']

        qrcode = qr.QRCode()
        qrcode.add_data(url)
        qrcode.make(fit=True)

        img = qrcode.make_image()
        img.save(file_path)
        image_generated=True

    return render_template("index.html", image_generated=image_generated)

@app.route("/download")
def download():
    return send_file("static/qrcode.png", as_attachment=True)


if __name__ == "__main__":
    app.run()