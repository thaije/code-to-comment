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
- add --lstm=XX to change the LSTM type to normal or attention (default attention)


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
______________________________________
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



#### vocab=40000, 2 layers, size=1000, lstm=attention (different vocab size + size)


#### vocab=40000, 2 layers, size=256, lstm=normal (different lstm type) 


#### vocab=3000, 2 layers, size=256, lstm=normal (different test/training ratio) 


#### vocab=3000, 2 layers, size=256, lstm=normal (extra bucket) 





  
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
