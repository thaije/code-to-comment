# comment-generation
Set of (Tensorflow) implementations which generate comments from code. Thesis for the B.sc. AI. 

# How to execute:
## Seq2seq: 
- Enter tf: source ~/tensorflow/bin/activate
- Execute code: python translate.py --size=350 --num_layers=3 --steps_per_checkpoint=50
- Or interactive mode (only works when the model has been trained): python translate.py --size=350 --num_layers=3 --step_per_checkpoint=50 --decode


