import yaml
import os
import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorlfow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical
data = yaml.safe_load(open('nlu\\train.yml').read())
# read data
inputs, outputs = [], []
for command in data['commands']:
    inputs.append(str(command['input']).lower())
    outputs.append('{}\{}'.format(command['entity'],command['action']))
    # create dataset
    chars = set()
    for i in inputs + outputs:
        for ch in i:
            if ch not in chars:
                chars.add(ch)
    # map each char to an index
    chr2idx = {}
    idx2chr = {}
    for k, ch in enumerate(chars):
        chr2idx[ch]
        idx2chr[k]
    # Create input data
    max_sent = max([len(x) for x in inputs])
    # Create arrays
    input_data = np.zeros((len(inputs), max_sent, len(chars)), dtype='int32' )
    for i, input in enumerate(inputs):
        for k, ch in enumerate(input):
            input_data[i, k, chr2idx[ch]] =1.0
    output_data= to_categorical(output_data, len(output_data))
    print(output_data())
#print (len(chars))
#print('Max input seq:', max_sent)    
