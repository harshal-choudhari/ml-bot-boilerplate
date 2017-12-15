import sys

from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer

from config import *

metadata = Metadata.load(RASA_NLU_MODEL_PATH + RASA_NLU_MODEL_NAME)
interpreter = Interpreter.load(metadata, RasaNLUConfig(RASA_NLU_CONFIG_PATH))
print(interpreter.parse(sys.argv[1]))
