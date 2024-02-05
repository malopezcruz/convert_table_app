from flask import Flask, render_template, request, send_file
from flask.helpers import send_file
from html_processor import process_html
from bs4 import BeautifulSoup
import pypandoc
import tempfile

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["html_file"]
        caption_text = request.form["caption_text"]

        # Convert the input docx file to an HTML string
        html_string = pypandoc.convert_text(file.read(), 'html', format='docx')

        # Process the HTML string with BeautifulSoup
        soup = BeautifulSoup(html_string, "html.parser")
        process_html(soup, caption_text)

        # Save the modified HTML to a temporary file
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(str(soup).encode("utf-8"))
        temp_file.close()

        # Send the modified HTML file to the user
        return send_file(temp_file.name, as_attachment=True, download_name="output.html", mimetype="text/html")


    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
