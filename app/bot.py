import json

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
        self.inter = RasaNLUInterpreter(RASA_NLU_MODEL_PATH + RASA_NLU_MODEL_NAME)
        self.agent = Agent.load(
            RASA_CORE_MODEL_PATH,
            interpreter=self.inter)
        self.data = None
        self.channel = None
        self.output_channel = None
        self.sender = None

    def checkDefaultMessage(self, text_message):
        from db_models.logging import Logging
        parsed_data = self.inter.parse(text_message)
        confidence = parsed_data['intent']['confidence']
        if (confidence <= float(os.environ.get('MINIMUM_INTENT_DEFAULT_CONFIDENCE'))):
            Logging.create(text=parsed_data['text'], intent=parsed_data['intent']['name'], confidence=confidence)
            return False
        return True

    def on_post(self, req, resp):
        """
            This method will return response to user query
        """
        try:
            data = req.bounded_stream.read()
            data = json.loads(data.decode('utf-8'))
            if (self.checkDefaultMessage(data['text'])):
                ans = self.agent.handle_message(data['text'])
                print('type ', type(ans))
                print('ans ', ans)
                print('type ', type(ans[0]))
                print('ans ', ans[0])
                resp.body = ans[0]
            else:
                resp.body = "Default message"
        except Exception as e:
            print("Exception in bot- ", e)
