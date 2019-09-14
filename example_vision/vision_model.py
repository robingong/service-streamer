# coding=utf-8
# Created by Meteorix at 2019/7/30
import logging
import torch
from typing import List
from pytorch_transformers import *
from service_streamer import ManagedModel

logging.basicConfig(level=logging.ERROR)

class ImgInfillingModel(object):
    def __init__(self, max_sent_len=16):
        self.model_path = "bert-base-uncased"


class ManagedImgModel(ManagedModel):

    def init_model(self):
        self.model = ImgInfillingModel()

    def predict(self, batch):
        print("-->> ManagedImgModel.predict")
        return self.model.predict(batch)