# comment-generation
Set of (Tensorflow) implementations which generate comments from code. Thesis for the B.sc. AI. 

# How to execute:
## Seq2seq: 
- Enter tf: source ~/tensorflow/bin/activate
- Execute code: python translate.py --size=256 --num_layers=3 --steps_per_checkpoint=50 --bleu
- Or interactive mode (only works when the model has been trained): python translate.py --size=350 --num_layers=3 --step_per_checkpoint=50 --decode

### Options
- add --bleu to calculate BLEU-score of translated dev file (default False)
- add --size=XX to change size of LSTM layer to XX (default 256)
- add --num_layers=XX to change number of LSTM layers to XX (default 2)
- add --steps_per_checkpoint=XX to change amount of steps per evaluation output to XX(default 200)
- add --code_vocab_size=XX to change the code vocabulary size to XX (default 3000)
- add --en_vocab_size=XX to change the English vocabulary size to XX (default 3000)
