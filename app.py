from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():

    video_url = request.form["video_url"]

    save_path = "downloads"

    if not os.path.exists(save_path):
        os.makedirs(save_path)

    try:
        youtube = YouTube(video_url)

        video = youtube.streams.get_highest_resolution()

        video.download(output_path=save_path)

        return render_template(
            "index.html",
            mensagem="Download concluído com sucesso!"
        )

    except Exception as e:

        return render_template(
            "index.html",
            mensagem=f"Ocorreu um erro: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)