from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulate smart devices state
smart_home_devices = {
    "lights": "off",
    "music": "stopped"
}

# Endpoint to control lights via text or gesture input


@app.route("/control/lights", methods=["POST"])
def control_lights():
    data = request.json
    action = data.get("action")  # Expected: 'on' or 'off'

    if action not in ["on", "off"]:
        return jsonify({"status": "error", "message": "Invalid action for lights"}), 400

    smart_home_devices["lights"] = action
    return jsonify({
        "status": "success",
        "message": f"Lights turned {action}",
        "current_state": smart_home_devices
    })

# Endpoint to control music via voice commands or text


@app.route("/control/music", methods=["POST"])
def control_music():
    data = request.json
    action = data.get("action")  # Expected: 'play' or 'stop'

    if action not in ["play", "stop"]:
        return jsonify({"status": "error", "message": "Invalid action for music"}), 400

    smart_home_devices["music"] = "playing relaxing music" if action == "play" else "stopped"
    return jsonify({
        "status": "success",
        "message": f"Music is now {smart_home_devices['music']}",
        "current_state": smart_home_devices
    })

# Endpoint to provide visual feedback (current status)


@app.route("/status", methods=["GET"])
def get_status():
    return jsonify({
        "status": "success",
        "smart_home_state": smart_home_devices
    })

# Simulated audio confirmation (basic placeholder)


@app.route("/audio/confirmation", methods=["POST"])
def audio_confirmation():
    action = request.json.get("action")
    responses = {
        "lights_on": "The lights are now on.",
        "lights_off": "The lights are now off.",
        "music_play": "Relaxing music is playing now.",
        "music_stop": "Music has been stopped."
    }
    response = responses.get(action, "Action not recognized.")
    return jsonify({"audio_response": response})


if __name__ == "__main__":
    app.run(debug=True)
