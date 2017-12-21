from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_nlu.model import Metadata, Interpreter
from rasa_nlu.config import RasaNLUConfig

from tools.config import *

class Bot():
    """
    Bot class to Process Data
    """

    def __init__(self):
        self.agent = Agent.load(
            RASA_CORE_MODEL_PATH,
            interpreter=RasaNLUInterpreter(RASA_NLU_MODEL_PATH + RASA_NLU_MODEL_NAME))
        self.data = None
        self.channel = None
        self.output_channel = None
        self.sender = None

    def checkDefaultMessage(self, text_message):
        interpreter = Interpreter.load(RASA_NLU_MODEL_PATH + \
                RASA_NLU_MODEL_NAME, RasaNLUConfig(RASA_NLU_CONFIG_PATH))
        return interpreter.parse(text_message)
    def on_post(self, req, resp):
        """
            This method will return response to user query
        """
        try:
            resp.body = str(self.checkDefaultMessage("hello"))
        except Exception as e:
            print("Exception in bot- ", e)
