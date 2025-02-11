from flask import Flask, request, send_file, render_template_string
import qrcode
import io

app = Flask(__name__)

# Șablon HTML simplu pentru formular
html_template = """
<!doctype html>
<html lang="ro">
  <head>
    <meta charset="utf-8">
    <title>Generator Cod QR</title>
  </head>
  <body>
    <h1>Generator Cod QR</h1>
    <form action="/generate" method="post">
      <input type="text" name="text" placeholder="Introdu textul pentru codul QR" required>
      <button type="submit">Generează QR</button>
    </form>
  </body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_template)

@app.route('/generate', methods=['POST'])
def generate():
    text = request.form.get("text", "")
    if not text:
        return "Nu a fost furnizat niciun text!", 400

    # Generarea codului QR
    img = qrcode.make(text)
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    
    return send_file(buf, mimetype="image/png", as_attachment=False, download_name="qr.png")

if __name__ == '__main__':
    app.run(debug=True)
