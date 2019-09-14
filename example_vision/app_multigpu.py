# coding=utf-8
# Created by Meteorix at 2019/8/9

from model import get_prediction, batch_prediction

from gevent import monkey; monkey.patch_all()
from flask import Flask, request, jsonify
from gevent.pywsgi import WSGIServer

from service_streamer import ThreadedStreamer
from vision_model import  ManagedImgModel

from service_streamer import Streamer

app = Flask(__name__)
# streamer = ThreadedStreamer(batch_prediction, batch_size=64)
streamer = None

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()

        # class_id, class_name = get_prediction(img_bytes)
        batch = img_bytes
        streamer.predict(batch)
        # return jsonify({'class_id': class_id, 'class_name': class_name})
        return "ok"

@app.route('/stream_predict', methods=['POST'])
def stream_predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = streamer.predict([img_bytes])[0]
        return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == "__main__":

    streamer = Streamer(ManagedImgModel, batch_size=64, max_latency=0.1, worker_num=4, cuda_devices=(0, 1))  # 0, 1, 2, 3
    app.run(host="0.0.0.0", port=5005)
