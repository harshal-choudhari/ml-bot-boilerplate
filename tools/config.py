import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
CWD = ('/'.join(i for i in CWD.split('/')[:-1])) + '/'

RASA_NLU_MODEL_PATH = CWD + os.environ.get('RASA_NLU_MODEL_PATH')
RASA_NLU_MODEL_NAME = os.environ.get('RASA_NLU_MODEL_NAME')
RASA_NLU_CONFIG_PATH = CWD + os.environ.get('RASA_NLU_CONFIG_PATH')
RASA_NLU_TRAINING_DATA_PATH = CWD + \
    os.environ.get('RASA_NLU_TRAINING_DATA_PATH')

RASA_CORE_MODEL_PATH = CWD + os.environ.get('RASA_CORE_MODEL_PATH')
RASA_CORE_DOMAIN_PATH = CWD + os.environ.get('RASA_CORE_DOMAIN_PATH')
RASA_CORE_TRAINING_DATA_PATH = CWD + \
    os.environ.get('RASA_CORE_TRAINING_DATA_PATH')
RASA_CORE_MAX_HISTORY = int(os.environ.get('RASA_CORE_MAX_HISTORY'))
RASA_CORE_EPOCHS = int(os.environ.get('RASA_CORE_EPOCHS'))
RASA_CORE_BATCH_SIZE = int(os.environ.get('RASA_CORE_BATCH_SIZE'))
RASA_CORE_VALIDATION = float(os.environ.get('RASA_CORE_VALIDATION'))
MINIMUM_INTENT_DEFAULT_CONFIDENCE = float(os.environ.get('MINIMUM_INTENT_DEFAULT_CONFIDENCE'))
