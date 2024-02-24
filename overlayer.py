from flask import Flask, render_template, request, redirect, url_for
from downloader import download_video

app = Flask(__name__)

# Route to render the form


@app.route('/vm')
def index():
    return render_template('index.html')

# Route to handle form submission


@app.route('/vm/vplayer', methods=['GET', 'POST'])
def submit():
    # Accessing data from the form
    if request.method == 'POST':
        text_input = request.form['text_input']
        try:
            out_file, file_name = download_video(text_input)
            file_name = '/static/' + file_name
            return render_template('vplayer.html', file_name=file_name)
        except:
            return "video not found"

    elif request.method == 'GET':
        return redirect('/vm')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
