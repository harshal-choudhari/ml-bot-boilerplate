from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

from config import *

def train_nlu_model():
    try:
        training_data = load_data(RASA_NLU_TRAINING_DATA_PATH)
        trainer = Trainer(RasaNLUConfig(RASA_NLU_CONFIG_PATH))
        trainer.train(training_data)
        model_directory = trainer.persist(
                RASA_NLU_MODEL_PATH, fixed_model_name=RASA_NLU_MODEL_NAME)
        return model_directory
    except Exception as e:
        print('Exception in train nlu', e)


if __name__ == '__main__':
    train_nlu_model()
