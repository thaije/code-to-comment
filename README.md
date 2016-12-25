# comment-generation
Set of (Tensorflow) implementations which generate comments from code. Thesis for the B.sc. AI. 

# How to execute:
## Seq2seq:
- Create/activate virtualenv
```bash
source ~/tensorflow/bin/activate
```
- Install requirements
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
- Run training. Note, the trainig process has infinite loop in it:
```bash
python translate.py --num_layers=3
```
- Run evaluation (only works when the model has been trained): 
```bash
python translate.py --num_layers=3 --evaluate
```

- Run interactive translation mode (only works when the model has been trained): 
```bash
python translate.py --num_layers=3 --step_per_checkpoint=50 --decode
```

### Options
- add --evaluate to see the score with a trained model on the development file (default False)
- add --size=XX to change size of LSTM layer to XX (default 256)
- add --num_layers=XX to change number of LSTM layers to XX (default 2)
- add --steps_per_checkpoint=XX to change amount of steps per evaluation output to XX(default 200)
- add --code_vocab_size=XX to change the code vocabulary size to XX (default 3000)
- add --en_vocab_size=XX to change the English vocabulary size to XX (default 3000)
- add --lstm=XX to change the LSTM type to normal or attention (default attention)
- uncomment the 'embedding_rnn_seq2seq' part in seq2seq_model.py to enable the embedded_seq2seq lstm without attention


# Results:

## Data info
### Distribution among buckets:
English buckets:
- Bucket 10 has 6251 items
- Bucket 15 has 3049 items
- Bucket 25 has 3791 items
- Bucket 50 has 1790 items
- Bucket 100 has 146 items (not implemented)
- Bucket 2000 has 17 items (not implemented) 


Code buckets:
- Bucket 5 has 3582 items  
- Bucket 10 has 6211 items
- Bucket 20 has 4109 items
- Bucket 40 has 946 items
- Bucket 100 has 178 items (not implemented)
- Bucket 2000 has 18 items (not implemented)



## Seq2seq 

### Python / Django dataset

#### Default: vocab=3000, layers=2 and size=256, lstm=attention
- global step 10400 learning rate 0.5000 step-time 0.23 perplexity 1.09
-  eval: bucket 0 perplexity 2.31
-  eval: bucket 1 perplexity 2.22
-  eval: bucket 2 perplexity 8.32
-  eval: bucket 3 perplexity 24.29
- BLEU = 14.19(BP=1.000, ratio=1.071, hyp_len=41721, ref_len=38963)
-  1-gram: 39.1
-  2-gram: 20.1
-  3-gram:11.3
-  4-gram: 4.6

#### Different layers / size

##### layers=2,  size = 512
- global step 6600 learning rate 0.4950 step-time 0.21 perplexity 1.28
-  eval: bucket 0 perplexity 1.30
-  eval: bucket 1 perplexity 3.13
-  eval: bucket 2 perplexity 5.72
-  eval: bucket 3 perplexity 15.49
- BLEU = 13.94 (Bravity Penalty=1.000, Length ratio=1.042, Translated length=40586, Reference length=38963)
-  1-gram: 39.0
-  2-gram: 20.1
-  3-gram:11.1
-  4-gram: 4.3

  
##### layers=2, size=1000
- global step 4400 learning rate 0.5000 step-time 0.34 perplexity 1.33
-  eval: bucket 0 perplexity 1.34
-  eval: bucket 1 perplexity 2.65
-  eval: bucket 2 perplexity 5.15
-  eval: bucket 3 perplexity 14.88
- BLEU = 13.39 (Bravity Penalty=1.000, Length ratio=1.029, Translated length=40074, Reference length=38963)
-  1-gram: 39.4
-  2-gram: 19.6
-  3-gram:10.6
-  4-gram: 3.9
- Accuracy is: 0.1393246477

With more steps:
- global step 7400 learning rate 0.5000 step-time 0.35 perplexity 1.11
-  eval: bucket 0 perplexity 1.78
-  eval: bucket 1 perplexity 2.65
-  eval: bucket 2 perplexity 6.00
-  eval: bucket 3 perplexity 34.64
- BLEU = 14.18 (Bravity Penalty=1.000, Length ratio=1.065, Translated length=41500, Reference length=38963)
-  1-gram: 39.9
-  2-gram: 20.3
-  3-gram:11.2
-  4-gram: 4.5
- Accuracy is: 0.149162456793

  
##### layers=3, size=256
- global step 9000 learning rate 0.4901 step-time 0.21 perplexity 1.23
-  eval: bucket 0 perplexity 3.04
-  eval: bucket 1 perplexity 3.20
-  eval: bucket 2 perplexity 7.34
-  eval: bucket 3 perplexity 18.86
- BLEU = 12.20 (Bravity Penalty=1.000, Length ratio=1.044, Translated length=40659, Reference length=38963)
-  1-gram: 36.8
-  2-gram: 17.7
-  3-gram:9.5
-  4-gram: 3.6
- Accuracy is: 0.137995214039


##### layers=3, size=1000
- global step 6400 learning rate 0.4950 step-time 0.45 perplexity 1.18
-  eval: bucket 0 perplexity 1.52
-  eval: bucket 1 perplexity 3.62
-  eval: bucket 2 perplexity 6.13
-  eval: bucket 3 perplexity 26.06
- BLEU = 13.99 (Bravity Penalty=1.000, Length ratio=1.065, Translated length=41487, Reference length=38963)
-  1-gram: 39.4
-  2-gram: 20.2
-  3-gram:11.1
-  4-gram: 4.3
  
  
##### layers=4, size=1000




#### Batch size
##### Different train batch size:  vocab=3000, 2 layers, size=256, train batch_size = 1, lstm=attention
- global step 11200 learning rate 0.4568 step-time 0.19 perplexity 6.50
-  eval: bucket 0 perplexity 1.59
-  eval: bucket 1 perplexity 5.09
-  eval: bucket 2 perplexity 2.32
-  eval: bucket 3 perplexity 21.60
- BLEU = 7.54 (Bravity Penalty=0.931, Length ratio=0.933, Translated length=36362, Reference length=38963)
-  1-gram: 33.4
-  2-gram: 13.6
-  3-gram:6.4
-  4-gram: 1.5
  
##### Different test batch size
Doesn't work, translated sentences are looked up one by one. Can't look up multiple sentences at once. 
 
 
#### Different vocab size
##### Vocab size = 40.000
- global step 8400 learning rate 0.4950 step-time 0.19 perplexity 1.26
-  eval: bucket 0 perplexity 5.05
-  eval: bucket 1 perplexity 16.93
-  eval: bucket 2 perplexity 17.70
-  eval: bucket 3 perplexity 38.03
- BLEU = 12.65 (Bravity Penalty=1.000, Length ratio=1.035, Translated length=40310, Reference length=38963)
-  1-gram: 36.9
-  2-gram: 18.1
-  3-gram:9.9
-  4-gram: 3.9
- Accuracy is: 0.142249401755


##### Vocab size = 40.000, size=1000
- global step 7400 learning rate 0.4950 step-time 0.53 perplexity 1.11
-  eval: bucket 0 perplexity 3.67
-  eval: bucket 1 perplexity 8.05
-  eval: bucket 2 perplexity 24.71
-  eval: bucket 3 perplexity 29.66
- BLEU = 15.30 (Bravity Penalty=1.000, Length ratio=1.033, Translated length=40249, Reference length=38963)
-  1-gram: 41.5
-  2-gram: 21.6
-  3-gram:12.2
-  4-gram: 5.0
- Accuracy is: 0.149428343526 


##### Vocab size = 40.000, size=1000, layers=3
after 9800 steps BLEU ~13.30. Accuracy 14.xx



#### More data: 17000 train 1805 test
##### Default
- global step 5600 learning rate 0.4950 step-time 0.23 perplexity 1.58
-  eval: bucket 0 perplexity 1.55
-  eval: bucket 1 perplexity 3.02
-  eval: bucket 2 perplexity 6.59
-  eval: bucket 3 perplexity 13.44
- BLEU = 12.56 (Bravity Penalty=1.000, Length ratio=1.149, Translated length=20306, Reference length=17680)
-  1-gram: 38.6
-  2-gram: 18.1
-  3-gram:9.3
-  4-gram: 3.8
- Accuracy is: 0.17783933518


##### vocab: 4000, size=512
- global step 4800 learning rate 0.4950 step-time 0.22 perplexity 1.39
-  eval: bucket 0 perplexity 1.92
-  eval: bucket 1 perplexity 4.41
-  eval: bucket 2 perplexity 8.97
-  eval: bucket 3 perplexity 18.79
- BLEU = 12.32 (Bravity Penalty=1.000, Length ratio=1.167, Translated length=20635, Reference length=17680)
-  1-gram: 38.8
-  2-gram: 17.7
-  3-gram:9.0
-  4-gram: 3.7
- Accuracy is: 0.192243767313

##### vocab: 4000, size=512 More steps
- global step 13000 learning rate 0.4901 step-time 0.26 perplexity 1.05
-  eval: bucket 0 perplexity 2.01
-  eval: bucket 1 perplexity 6.82
-  eval: bucket 2 perplexity 13.18
-  eval: bucket 3 perplexity 88.26
- BLEU = 12.31 (Bravity Penalty=1.000, Length ratio=1.169, Translated length=20669, Reference length=17680)
-  1-gram: 37.9
-  2-gram: 17.3
-  3-gram:8.9
-  4-gram: 3.9
- Accuracy is: 0.198337950139


#### Use spaced file for BLEU calc, 2x512, vocab=4000, testfile = 1805 lines
##### 2x512, vocab 4000, 
- global step 6400 learning rate 0.4950 step-time 0.22 perplexity 1.24
-  eval: bucket 0 perplexity 1.59
-  eval: bucket 1 perplexity 5.98
-  eval: bucket 2 perplexity 8.13
-  eval: bucket 3 perplexity 22.40
- BLEU = 26.93 (Bravity Penalty=0.862, Length ratio=0.871, Translated length=20435, Reference length=23462)
-  1-gram: 68.2
-  2-gram: 38.0
-  3-gram:24.2
-  4-gram: 15.2
- Accuracy is: 0.186149584488

##### Same with more steps
- global step 9200 learning rate 0.4950 step-time 0.23 perplexity 1.13
-  eval: bucket 0 perplexity 2.18
-  eval: bucket 1 perplexity 4.04
-  eval: bucket 2 perplexity 18.51
-  eval: bucket 3 perplexity 45.24
- BLEU = 26.89 (Bravity Penalty=0.871, Length ratio=0.879, Translated length=20625, Reference length=23462)
-  1-gram: 67.6
-  2-gram: 37.5
-  3-gram:23.9
-  4-gram: 15.0
- Accuracy is: 0.183379501385


#### Use spaced file for BLEU calc, 2x512, vocab=5000, testfile = 1805 lines
- global step 5000 learning rate 0.5000 step-time 0.22 perplexity 1.31
-  eval: bucket 0 perplexity 1.83
-  eval: bucket 1 perplexity 3.46
-  eval: bucket 2 perplexity 9.56
-  eval: bucket 3 perplexity 35.55
- BLEU = 27.45 (Bravity Penalty=0.883, Length ratio=0.889, Translated length=20868, Reference length=23462)
-  1-gram: 66.6
-  2-gram: 37.7
-  3-gram:24.4
-  4-gram: 15.2
- Accuracy is: 0.198337950139


#### Spaced file for BLEU, 2x512, vocab=5000, testfile=1805, enters fixed in python code
- global step 6000 learning rate 0.5000 step-time 0.22 perplexity 1.24
-  eval: bucket 0 perplexity 1.86
-  eval: bucket 1 perplexity 4.10
-  eval: bucket 2 perplexity 11.12
-  eval: bucket 3 perplexity 19.37
- BLEU = 27.50 (Bravity Penalty=0.896, Length ratio=0.901, Translated length=21134, Reference length=23459)
-  1-gram: 67.2
-  2-gram: 37.5
-  3-gram:23.9
-  4-gram: 14.7
- Accuracy is: 0.195013850416



#### Spaced file for BLEU, 2x512, vocab=5000, testfile=1805, enters fixed in python code, random train/test set
- global step 6200 learning rate 0.5000 step-time 0.23 perplexity 1.25
-  eval: bucket 0 perplexity 1.49
-  eval: bucket 1 perplexity 2.22
-  eval: bucket 2 perplexity 2.53
-  eval: bucket 3 perplexity 5.61
- BLEU = 39.16 (Bravity Penalty=0.862, Length ratio=0.871, Translated length=20978, Reference length=24092)
-  1-gram: 74.7
-  2-gram: 51.7
-  3-gram:38.6
-  4-gram: 28.5
- Accuracy is: 0.248199445983

##### even more steps
- global step 8000 learning rate 0.5000 step-time 0.23 perplexity 1.15
-  eval: bucket 0 perplexity 1.49
-  eval: bucket 1 perplexity 1.84
-  eval: bucket 2 perplexity 3.29
-  eval: bucket 3 perplexity 7.08
- BLEU = 40.66 (Bravity Penalty=0.885, Length ratio=0.892, Translated length=21479, Reference length=24092)
-  1-gram: 74.5
-  2-gram: 52.1
-  3-gram:39.3
-  4-gram: 29.2
- Accuracy is: 0.256509695291

##### even more steps
- global step 9000 learning rate 0.5000 step-time 0.22 perplexity 1.10
-  eval: bucket 0 perplexity 1.57
-  eval: bucket 1 perplexity 2.37
-  eval: bucket 2 perplexity 2.84
-  eval: bucket 3 perplexity 7.02
- BLEU = 41.64 (Bravity Penalty=0.899, Length ratio=0.903, Translated length=21766, Reference length=24092)
-  1-gram: 74.4
-  2-gram: 52.3
-  3-gram:39.6
-  4-gram: 30.0
- Accuracy is: 0.268144044321


#### Spaced file for BLEU, 2x512, vocab=6000, testfile=1805, enters fixed in python code, random train/test set
- global step 7400 learning rate 0.4901 step-time 0.22 perplexity 1.16
-  eval: bucket 0 perplexity 1.78
-  eval: bucket 1 perplexity 1.97
-  eval: bucket 2 perplexity 4.59
-  eval: bucket 3 perplexity 5.34
- BLEU = 38.81 (Bravity Penalty=0.883, Length ratio=0.889, Translated length=21419, Reference length=24092)
-  1-gram: 73.0
-  2-gram: 50.1
-  3-gram:37.3
-  4-gram: 27.4
- Accuracy is: 0.263711911357


#### Spaced file for BLEU, 2x512, vocab=5500, testfile=1805, enters fixed in python code, random train/test set
- global step 7800 learning rate 0.4901 step-time 0.29 perplexity 1.16
-  eval: bucket 0 perplexity 1.45
-  eval: bucket 1 perplexity 2.18
-  eval: bucket 2 perplexity 2.93
-  eval: bucket 3 perplexity 8.34
- BLEU = 41.40 (Bravity Penalty=0.902, Length ratio=0.906, Translated length=21830, Reference length=24092)
-  1-gram: 74.1
-  2-gram: 51.8
-  3-gram:39.1
-  4-gram: 29.6
- Accuracy is: 0.272576177285


#### Spaced file for BLEU, 2x512, vocab=5000, testfile=1805, enters fixed in python code, random train/test set, seq2seq cell without attention
- global step 8200 learning rate 0.4950 step-time 0.22 perplexity 1.30
-  eval: bucket 0 perplexity 1.44
-  eval: bucket 1 perplexity 1.93
-  eval: bucket 2 perplexity 3.50
-  eval: bucket 3 perplexity 5.99
- BLEU = 39.32 (Bravity Penalty=0.891, Length ratio=0.897, Translated length=21600, Reference length=24092)
-  1-gram: 73.7
-  2-gram: 50.4
-  3-gram:37.3
-  4-gram: 27.4
- Accuracy is: 0.261495844875

##### more steps
- global step 10600 learning rate 0.4950 step-time 0.21 perplexity 1.18
-  eval: bucket 0 perplexity 1.64
-  eval: bucket 1 perplexity 2.05
-  eval: bucket 2 perplexity 3.15
-  eval: bucket 3 perplexity 6.05
- BLEU = 40.15 (Bravity Penalty=0.881, Length ratio=0.888, Translated length=21386, Reference length=24092)
-  1-gram: 74.7
-  2-gram: 51.7
-  3-gram:38.7
-  4-gram: 28.9
- Accuracy is: 0.267590027701

##### even more steps
- global step 12200 learning rate 0.4901 step-time 0.23 perplexity 1.14
-  eval: bucket 0 perplexity 1.66
-  eval: bucket 1 perplexity 2.59
-  eval: bucket 2 perplexity 3.29
-  eval: bucket 3 perplexity 8.40
- BLEU = 40.94 (Bravity Penalty=0.890, Length ratio=0.896, Translated length=21581, Reference length=24092)
-  1-gram: 74.8
-  2-gram: 52.0
-  3-gram:39.2
-  4-gram: 29.4
- Accuracy is: 0.273684210526


#### Spaced file for BLEU, 3x512, vocab=5000, testfile=1805, enters fixed in python code, random train/test set, seq2seq cell without attention
global steps: 9600

BLEU = 40.43 (Bravity Penalty=0.901, Length ratio=0.905, Translated length=21812, Reference          length=24092)
  1-gram: 73.3
  2-gram: 50.8
  3-gram:38.2
  4-gram: 28.6
Accuracy is: 0.270914127424



#### Spaced file for BLEU, 2x512, vocab=5000, testfile=1805, enters fixed in python code, vocab=5000, beam search=7 (torch implementation)
35 epochs, 296 steps each = 10360 steps
BLEU = 51.80, 79.1/63.1/53.1/44.4 (BP=0.884, ratio=0.890, hyp_len=21452, ref_len=24092)
Precision: 38.891966759
Unique annotations: 32.7635327635% 

#### Spaced file for BLEU, 2x512, vocab=5000, testfile=1805, enters fixed in python code, vocab=5000, beam search=7, repl unk with source attention words (torch implementation)
32 epochs, 296 steps each = 9400 steps
BLEU = 52.58, 79.7/63.9/54.0/45.5 (BP=0.884, ratio=0.890, hyp_len=21452, ref_len=24092)
Accuracy is: 0.413850415512




#### structure alternate 2x512 vocab=5000, testfile 1805, random shit
global step 8200 learning rate 0.4950 step-time 0.45 perplexity 1.13
  eval: bucket 0 perplexity 1.27
  eval: bucket 1 perplexity 2.07
  eval: bucket 2 perplexity 2.35
  eval: bucket 3 perplexity 3.32
BLEU = 7.31 (Bravity Penalty=0.559, Length ratio=0.632, Translated length=15232, Reference length=24092)
  1-gram: 49.3
  2-gram: 17.9
  3-gram:8.2
  4-gram: 4.1
Accuracy is: 0.0016620498615

#### structure concatenated 2x512 vocab=5000, testfile 1805, random shit
global step 6000 learning rate 0.4950 step-time 0.47 perplexity 1.29
  eval: bucket 0 perplexity 2.56
  eval: bucket 1 perplexity 1.48
  eval: bucket 2 perplexity 2.26
  eval: bucket 3 perplexity 4.37
BLEU = 10.91 (Bravity Penalty=0.680, Length ratio=0.722, Translated length=17393, Reference length=24092)
  1-gram: 49.0
  2-gram: 21.3
  3-gram:10.9
  4-gram: 5.8
Accuracy is: 0.0315789473684


#### Code dataset ,2x512 vocab=5000, random 90/10 ratio, vocab=5000
global step 8400 learning rate 0.4950 step-time 0.64 perplexity 1.11
  eval: bucket 0 perplexity 11.55
  eval: bucket 1 perplexity 9603.03
  eval: bucket 2 perplexity 3177.78
  eval: bucket 3 perplexity 6908.59
BLEU = 2.25 (Bravity Penalty=0.197, Length ratio=0.381, Translated length=8817, Reference length=23120)
  1-gram: 25.4
  2-gram: 11.3
  3-gram:8.4
  4-gram: 6.9
Accuracy is: 0.0199233716475


#### Code dataset ,2x512 vocab=5000, random 90/10 ratio, vocab=5000, extra buckets




#### all code dataset 90/10
global step 42600 learning rate 0.4660 step-time 0.53 perplexity 1.08
  eval: bucket 0 perplexity 23.55
  eval: bucket 1 perplexity 455.93
  eval: bucket 2 perplexity 1924.06
  eval: bucket 3 perplexity 1851.07
BLEU = 1.98 (Bravity Penalty=0.173, Length ratio=0.363, Translated length=43903, Reference length=120936)
  1-gram: 23.7
  2-gram: 11.9
  3-gram:8.8
  4-gram: 6.8
Accuracy is: 0.0726461038961

global step 8000 learning rate 0.5000 step-time 0.44 perplexity 7.25
  eval: bucket 0 perplexity 4.43
  eval: bucket 1 perplexity 18.25
  eval: bucket 2 perplexity 29.22
  eval: bucket 3 perplexity 41.84
BLEU = 0.40 (Bravity Penalty=0.048, Length ratio=0.248, Translated length=29997, Reference length=120936)
  1-gram: 23.6
  2-gram: 9.4
  3-gram:5.7
  4-gram: 3.7
Accuracy is: 0.0511363636364




#### all code dataset 90/10, code_vocab=100.000, en_vocab= 25.000
global step 13800 learning rate 0.5000 step-time 0.48 perplexity 2.14
  eval: bucket 0 perplexity 18.97
  eval: bucket 1 perplexity 35.72
  eval: bucket 2 perplexity 107.30
  eval: bucket 3 perplexity 223.57
BLEU = 1.39 (Bravity Penalty=0.183, Length ratio=0.370, Translated length=44795, Reference length=120936)
  1-gram: 22.6
  2-gram: 8.6
  3-gram:5.2
  4-gram: 3.3
Accuracy is: 0.0603354978355


global step 20600 learning rate 0.5000 step-time 0.48 perplexity 1.43
  eval: bucket 0 perplexity 15.71
  eval: bucket 1 perplexity 68.38
  eval: bucket 2 perplexity 297.67
  eval: bucket 3 perplexity 254.55
BLEU = 1.76 (Bravity Penalty=0.212, Length ratio=0.392, Translated length=47401, Reference length=120936)
  1-gram: 22.1
  2-gram: 9.2
  3-gram:5.9
  4-gram: 4.0
Accuracy is: 0.0620941558442

#### all code dataset 90/10, code_vocab=100.000, en_vocab= 25.000, structure concatenate
global step 17400 learning rate 0.4950 step-time 0.41 perplexity 1.23
  eval: bucket 0 perplexity 96.88
  eval: bucket 1 perplexity 86.64
  eval: bucket 2 perplexity 101.23
  eval: bucket 3 perplexity 957.30
BLEU = 0.72 (Bravity Penalty=0.343, Length ratio=0.483, Translated length=58424, Reference length=120936)
  1-gram: 13.4
  2-gram: 2.6
  3-gram:1.1
  4-gram: 0.5
Accuracy is: 0.0206980519481

#### all code dataset 90/10, code_vocab=100.000, en_vocab= 25.000, 3x512
BLEU = 0.43 (Bravity Penalty=0.077, Length ratio=0.281, Translated length=33950, Reference length=120936)
  1-gram: 21.2
  2-gram: 7.2
  3-gram:3.5
  4-gram: 1.8
Accuracy is: 0.0466720779221



#### all code dataset cleaned 90/10, code_vocab = 40.000, en_vocab=20.000, 
global step 6200 learning rate 0.5000 step-time 0.59 perplexity 9.55
  eval: bucket 0 perplexity 6.57
  eval: bucket 1 perplexity 32.38
  eval: bucket 2 perplexity 31.92
  eval: bucket 3 perplexity 35.08
BLEU = 3.10 (Bravity Penalty=0.396, Length ratio=0.519, Translated length=25341, Reference length=48784)
  1-gram: 25.0
  2-gram: 9.2
  3-gram:5.4
  4-gram: 3.0
Accuracy is: 0.0789067665858

step:9.400
BLEU = 5.06 (Bravity Penalty=0.770, Length ratio=0.792, Translated length=38656, Reference length=48784)
  1-gram: 22.1
  2-gram: 7.8
  3-gram:4.3
  4-gram: 2.5
Accuracy is: 0.083535375799


#### all code dataset cleaned 90/10, code_vocab = 40.000, en_vocab=20.000, 3x512

10.000 steps +
BLEU = 6.69 (Bravity Penalty=0.701, Length ratio=0.738, Translated length=35996, Reference length=48784)
  1-gram: 24.9
  2-gram: 10.5
  3-gram:6.8
  4-gram: 4.6
Accuracy is: 0.10359268238950

global step 18600 learning rate 0.5000 step-time 0.76 perplexity 1.61
  eval: bucket 0 perplexity 11.52
  eval: bucket 1 perplexity 66.76
  eval: bucket 2 perplexity 580.03
  eval: bucket 3 perplexity 245.23
BLEU = 7.54 (Bravity Penalty=0.795, Length ratio=0.813, Translated length=39685, Reference length=48784)
  1-gram: 24.2
  2-gram: 10.4
  3-gram:6.9
  4-gram: 4.7
Accuracy is: 0.106678421865
Unique annotations: 0%


#### edx_pylearn_scikit dataset cleaned 90/10, code_vocab = 25.000, en_vocab=12.000, 2x512
global step 10000 learning rate 0.4950 step-time 0.62 perplexity 1.54
  eval: bucket 0 perplexity 110.03
  eval: bucket 1 perplexity 91.02
  eval: bucket 2 perplexity 163.57
  eval: bucket 3 perplexity 719.93
BLEU = 6.78 (Bravity Penalty=0.694, Length ratio=0.733, Translated length=18739, Reference length=25571)
  1-gram: 26.4
  2-gram: 10.7
  3-gram:6.7
  4-gram: 4.8
Accuracy is: 0.0442391832766

global step 14000 learning rate 0.4950 step-time 0.64 perplexity 1.19
  eval: bucket 0 perplexity 158.36
  eval: bucket 1 perplexity 1105.41
  eval: bucket 2 perplexity 766.66
  eval: bucket 3 perplexity 958.09
BLEU = 8.19 (Bravity Penalty=0.758, Length ratio=0.783, Translated length=20013, Reference length=25571)
  1-gram: 25.9
  2-gram: 11.2
  3-gram:7.8
  4-gram: 6.0
Accuracy is: 0.0612542537676

global step 16400 learning rate 0.4950 step-time 0.69 perplexity 1.12
  eval: bucket 0 perplexity 250.31
  eval: bucket 1 perplexity 1125.74
  eval: bucket 2 perplexity 7054.63
  eval: bucket 3 perplexity 1717.69
BLEU = 8.77 (Bravity Penalty=0.795, Length ratio=0.813, Translated length=20798, Reference length=25571)
  1-gram: 25.8
  2-gram: 11.4
  3-gram:8.0
  4-gram: 6.3
Accuracy is: 0.0670879922217

#### edx_pylearn_scikit_salt dataset cleaned 90/10, code_vocab = 35.000, en_vocab=18.000, 2x512

global step 16800 learning rate 0.5000 step-time 0.63 perplexity 1.27
  eval: bucket 0 perplexity 12.71
  eval: bucket 1 perplexity 167.17
  eval: bucket 2 perplexity 274.48
  eval: bucket 3 perplexity 858.49
 Line 500 translated
 Line 1000 translated
 Line 1500 translated
 Line 2000 translated
 Line 2500 translated
 Line 3000 translated
 File translated
BLEU = 10.45 (Bravity Penalty=0.834, Length ratio=0.847, Translated length=28594, Reference length=33777)
  1-gram: 27.5
  2-gram: 13.6
  3-gram:9.6
  4-gram: 6.9
Accuracy is: 0.157978893508

#### edx_pylearn_scikit_salt dataset cleaned 90/10, code_vocab = 32.000, en_vocab=16.000, 3x512
global step 11600 learning rate 0.5000 step-time 0.74 perplexity 1.88
  eval: bucket 0 perplexity 9.31
  eval: bucket 1 perplexity 75.00
  eval: bucket 2 perplexity 158.42
  eval: bucket 3 perplexity 170.58
BLEU = 7.49 (Bravity Penalty=0.636, Length ratio=0.688, Translated length=23250, Reference length=33777)
  1-gram: 29.7
  2-gram: 13.7
  3-gram:8.6
  4-gram: 5.5
Accuracy is: 0.129197313719




  
  ## Possible things to tweak:
  - steps
  - Add buckets
  - size
  - layers
  - batch size
  - tweak bleu method to ignore unnecessary spaces (e.g. " variable " becomes "variable")
  - reverse/ normal sentence
  - different tokenizer
  - vocab size
  - different dataset
  - Meteor measure
  - Train/test ratio
