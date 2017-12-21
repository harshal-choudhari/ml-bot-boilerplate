from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from tools.policy import StatusPolicy
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy

from config import *


def train_rasa_core():
    agent = Agent(RASA_CORE_DOMAIN_PATH,
                  policies=[MemoizationPolicy(), StatusPolicy()])
    agent.train(
        RASA_CORE_TRAINING_DATA_PATH,
        max_history=RASA_CORE_MAX_HISTORY,
        epochs=RASA_CORE_EPOCHS,
        batch_size=RASA_CORE_BATCH_SIZE,
        validation_split=RASA_CORE_VALIDATION
    )
    agent.persist(RASA_CORE_MODEL_PATH)


if __name__ == '__main__':
    train_rasa_core()
