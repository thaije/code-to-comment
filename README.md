# comment-generation
Set of (Tensorflow) implementations which generate comments from code. Thesis for the B.sc. AI. 

# How to execute:
## Seq2seq: 
- Enter tf: source ~/tensorflow/bin/activate
- Execute code: python translate.py --size=256 --num_layers=3 --steps_per_checkpoint=50 --bleu
- Or interactive mode (only works when the model has been trained): python translate.py --size=350 --num_layers=3 --step_per_checkpoint=50 --decode

### Options
- add --evaluate to see the score with a trained model on the development file (default False)
- add --size=XX to change size of LSTM layer to XX (default 256)
- add --num_layers=XX to change number of LSTM layers to XX (default 2)
- add --steps_per_checkpoint=XX to change amount of steps per evaluation output to XX(default 200)
- add --code_vocab_size=XX to change the code vocabulary size to XX (default 3000)
- add --en_vocab_size=XX to change the English vocabulary size to XX (default 3000)


# Results:
## Seq2seq 

### Python / Django dataset
####With 4 buckets, vocabulary=3000, layers=2 and size=256
global step 10400 learning rate 0.5000 step-time 0.23 perplexity 1.09
  eval: bucket 0 perplexity 2.31
  eval: bucket 1 perplexity 2.22
  eval: bucket 2 perplexity 8.32
  eval: bucket 3 perplexity 24.29
BLEU = 14.19(BP=1.000, ratio=1.071, hyp_len=41721, ref_len=38963)
  1-gram: 39.1
  2-gram: 20.1
  3-gram:11.3
  4-gram: 4.6

global step 20000 learning rate 0.4851 step-time 0.19 perplexity 1.03
  eval: bucket 0 perplexity 1.49
  eval: bucket 1 perplexity 6.77
  eval: bucket 2 perplexity 14.90
  eval: bucket 3 perplexity 26.01
BLEU = 13.75 (Bravity Penalty=1.000, Length ratio=1.081, Translated length=42108, Reference length=38963)
  1-gram: 38.6
  2-gram: 19.4
  3-gram:10.8
  4-gram: 4.4
  
####With 4 buckets, vocabulary=3000, layers=2 and size=1000
global step 3200 learning rate 0.5000 step-time 0.38 perplexity 1.90
  eval: bucket 0 perplexity 1.36
  eval: bucket 1 perplexity 1.92
  eval: bucket 2 perplexity 5.05
  eval: bucket 3 perplexity 8.08
BLEU = 14.07 (Bravity Penalty=1.000, Length ratio=1.027, Translated length=40029, Reference length=38963)
  1-gram: 39.9
  2-gram: 20.7
  3-gram:11.4
  4-gram: 4.2

global step 4200 learning rate 0.5000 step-time 0.37 perplexity 1.36
  eval: bucket 0 perplexity 1.83
  eval: bucket 1 perplexity 2.46
  eval: bucket 2 perplexity 5.51
  eval: bucket 3 perplexity 10.52
BLEU = 14.50 (Bravity Penalty=1.000, Length ratio=1.000, Translated length=38959, Reference length=38963)
  1-gram: 40.0
  2-gram: 20.6
  3-gram:11.5
  4-gram: 4.7

#### With 4 buckets, vocab=3000, 2 layers, size=256, batch_size = 1
global step 11200 learning rate 0.4568 step-time 0.19 perplexity 6.50
  eval: bucket 0 perplexity 1.59
  eval: bucket 1 perplexity 5.09
  eval: bucket 2 perplexity 2.32
  eval: bucket 3 perplexity 21.60
BLEU = 7.54 (Bravity Penalty=0.931, Length ratio=0.933, Translated length=36362, Reference length=38963)
  1-gram: 33.4
  2-gram: 13.6
  3-gram:6.4
  4-gram: 1.5
  
#### With 4 buckets, vocab=3000, 3 layers, size=1000
global step 6400 learning rate 0.4950 step-time 0.45 perplexity 1.18
  eval: bucket 0 perplexity 1.52
  eval: bucket 1 perplexity 3.62
  eval: bucket 2 perplexity 6.13
  eval: bucket 3 perplexity 26.06
BLEU = 13.99 (Bravity Penalty=1.000, Length ratio=1.065, Translated length=41487, Reference length=38963)
  1-gram: 39.4
  2-gram: 20.2
  3-gram:11.1
  4-gram: 4.3
  
global step 7000 learning rate 0.4950 step-time 0.44 perplexity 1.14
  eval: bucket 0 perplexity 1.95
  eval: bucket 1 perplexity 3.57
  eval: bucket 2 perplexity 7.22
  eval: bucket 3 perplexity 15.93


#### With _buckets = [(5, 10), (10, 15), (20, 25), (40, 50), (1000,70), (2000,100), (2000, 600)], vocab=3000, 2 layers, size=256

global step 800 learning rate 0.5000 step-time 0.30 perplexity 15.30
  eval: bucket 0 perplexity 2.66
  eval: bucket 1 perplexity 7.10
  eval: bucket 2 perplexity 16.90
  eval: bucket 3 perplexity 50.88
  eval: bucket 4 perplexity 53.04
  eval: bucket 5 perplexity 99.28
  eval: bucket 6 perplexity 140.78
steBLEU = 7.56 (Bravity Penalty=1.000, Length ratio=1.056, Translated length=41129, Reference length=38963)
  1-gram: 32.7
  2-gram: 14.2
  3-gram:6.5
  4-gram: 1.1




  
  
  
  Possible things to tweak:
  - steps
  - buckets
  - size
  - layers
  - batch size
  - reverse/ normal sentence
  - different tokenizer
  - vocab size
  - different dataset
  - Meteor measure
