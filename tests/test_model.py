#!/usr/bin/env python
import pytest
from bike_image_classifier_tensorflow.models.model import Model

def test_predict():
    model = Model()
    model.predict(["https://whisk-examples.s3.amazonaws.com/bike-images/mountain_bike.jpg"])
