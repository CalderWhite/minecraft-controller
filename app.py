import subprocess

from flask import Flask, Response

app = Flask(__name__, static_url_path='', static_folder='public')

@app.route('/status')
def status():
    res = subprocess.run("gcloud compute instances list | grep minecraft-with-friends".split(" "), stdout=subprocess.PIPE)
    return Response(res.stdout.decode("utf-8"), mimetype="text/plain")

@app.route('/on')
def turn_on():
    res = subprocess.run("gcloud compute instances start minecraft-with-friends".split(" "))
    return 'done'

@app.route('/off')
def turn_off():
    subprocess.Popen("gcloud compute instances stop minecraft-with-friends".split(" "))
    return 'done'

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080")
