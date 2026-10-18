from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_alert():

    data = request.json

    for alert in data.get("alerts", []):

        if alert["labels"].get("alertname") == "NginxDown":

            print("NGINX DOWN DETECTED")
            print("Running Ansible Playbook...")

            subprocess.run(
                ["ansible-playbook", "ansible/restart-nginx.yml"]
            )

    return "OK", 200

app.run(host="0.0.0.0", port=5001)
