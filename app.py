from flask import Flask, render_template, request, jsonify
from calendlink import CalendLink

app = Flask(__name__)
calendar_assistant = CalendLink()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add_event", methods=["POST"])
def add_event():
    data = request.get_json()
    event_text = data.get("event_text", "")
    
    if not event_text:
        return jsonify({"status": "error", "message": "No event text provided"}), 400

    try:
        calendar_assistant.create_calendar_event(event_text)
        return jsonify({"status": "success", "message": "Event created!"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/profile_photo")
def profile_photo():
    try:
        url = calendar_assistant.get_profile_photo_url()
        return jsonify({"photo_url": url})
    except Exception as e:
        return jsonify({"photo_url": None, "error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

