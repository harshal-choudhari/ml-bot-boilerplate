from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.agent import Agent
from rasa_core.channels.file import FileInputChannel
from rasa_core.domain import TemplateDomain
from rasa_core.featurizers import BinaryFeaturizer
from rasa_core.interpreter import RegexInterpreter, RasaNLUInterpreter
from rasa_core.policies.memoization import MemoizationPolicy

from config import *

logger = logging.getLogger(__name__)


def train_model_online():
    agent = Agent(RASA_CORE_DOMAIN_PATH,
                  policies=[MemoizationPolicy(), StatusPolicy()],
                  interpreter=RegexInterpreter())

    agent.train_online(
        RASA_CORE_TRAINING_DATA_PATH,
        input_channel=FileInputChannel(
            RASA_CORE_TRAINING_DATA_PATH,
            message_line_pattern='^\s*\*\s(.*)$',
            max_messages=10),
        epochs=RASA_CORE_EPOCHS)

    agent.interpreter = RasaNLUInterpreter(RASA_NLU_MODEL_PATH)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    train_model_online()
