import pickle
import bike_image_classifier_tensorflow
import whisk
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
import argparse
import os
from urllib.request import urlretrieve
import validators

class Model:
    """
    This class should be used to load and invoke the serialized model and any other required
    model artifacts for pre/post-processing.
    """

    def __init__(self):
        """
        Load the model + required pre-processing artifacts from disk. Loading from disk is slow,
        so this is done in `__init__` rather than loading from disk on every call to `predict`.

        Tensorflow example:

            self.model = load_model(bike_image_classifier_tensorflow.project.artifacts_dir / "model.h5")

        Pickle example:

            with open(bike_image_classifier_tensorflow.project.artifacts_dir / 'tokenizer.pickle', 'rb') as file:
                self.tokenizer = pickle.load(file)
        """

        self.model = load_model(whisk.artifacts_dir / 'bike_classification_model.model')

    def predict(self,data):
        """
        Returns model predictions.
        """
        # The model input should include a list of image paths
        # This model currently supports only one input, so select first item in list
        # TODO: Add support for multiple images
        data = data[0]

        # check if input is a URL, if so download the file and save that path
        # else, try to import the file as a path
        if validators.url(str(data)):
            image_path = 'image'
            urlretrieve(data, image_path)
        else:
            image_path = data

        # Process image file for modeling
        image = load_img(image_path, target_size=(224, 224))
        image = img_to_array(image)
        image = preprocess_input(image)
        image = np.array(image, dtype="float32")
        image = np.expand_dims(image, axis=0)
        
        # use image to create prediction
        [response] = self.model.predict(image)
        return 'Mountain: ' + str(response[0]) + ', Road: ' + str(response[1])
