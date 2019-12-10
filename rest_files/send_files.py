import os
from flask import Flask, request, redirect, jsonify
import time


DIR = '/home/jules/test/tmp-themes'


if __name__ == "__main__":
    app = Flask(__name__)
    app.run()


@app.route('/file-upload', methods=['POST'])
def upload_file():
    start_time = time.time()
    data = request.files
    stream = data.get("file").stream
    tmp_file = data.get("file").filename
    tmp_path = os.path.join(DIR, tmp_file)
    with open(tmp_path, "wb") as out:
        out.write(stream.read())
    print("--- %s seconds ---" % (time.time() - start_time))
    return '{"status": "done", "path": "%s"}' % DIR





