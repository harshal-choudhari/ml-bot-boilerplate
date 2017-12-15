import os
import sys
try:
    variables = {
        'RASA_NLU_MODEL_PATH': 'models/',
        'RASA_NLU_TRAINING_DATA_PATH': 'training_data/nlu_stories.json',
        'RASA_NLU_CONFIG_PATH': 'training_data/config_spacy.json',
        'RASA_NLU_MODEL_NAME': 'nlu_model',
        'RASA_CORE_TRAINING_DATA_PATH': 'training_data/core_stories.md',
        'RASA_CORE_MODEL_PATH': 'core_model',
        'RASA_CORE_DOMAIN_PATH': 'training_data/domain.yml',
        'RASA_CORE_MAX_HISTORY': 5,
        'RASA_CORE_EPOCHS': 500,
        'RASA_CORE_BATCH_SIZE': 50,
        'RASA_CORE_VALIDATION': 0.2,
        'MINIMUM_INTENT_FOR_DEFAULT_MESSAGE': 0.6,
    }
    for k, v in variables.items():
        i = 'export {}="{}"'.format(k, v)
        os.system('echo {} >> {}'.format(i, sys.argv[1]))
except Exception as e:
    print('Usage: {} <env file>\n Ex- .bashrc or .zshrc'.format(sys.argv[0]))
