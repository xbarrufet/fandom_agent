from dotenv import load_dotenv
from flask import Flask, render_template,request,jsonify
from api.fandom_character import sumarize_fandom_character

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=["POST"])
def process():
    print("post received for character names", request.form["name"])
    name = request.form["name"]
    summary, content = sumarize_fandom_character(character_name=name)
    if content.title=="" or summary is None:
        return jsonify({"error": "Character not found or no information available."}), 404

    return jsonify(
        {
            "title": content.title,
            "summary_and_facts": summary.to_dict(),
            "picture_url": content.url_image,
        }
    )

if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True,port=8081)