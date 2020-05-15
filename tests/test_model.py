#!/usr/bin/env python
import pytest
from bike_image_classifier_tensorflow.models.model import Model

def test_predict():
    model = Model()
    model.predict([[1,2],[3,4]])
