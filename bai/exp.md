# Experiment

|                              | Django-Test      |
|:----------------------------:|-----------------|
| lr-0.001 + embed128  | 77.34%, 77.45% |
| bert-base-uncased + lr-0.001 + embed128  | 73.80%, 73.50% |
| bert-base-uncased + lr-0.001 + embed128 + dropout-0.3 | 77.06%, 77.14% |
| bert-base-uncased + lr-0.001 + embed256 + dropout-0.3 | 76.07%, 75.51% |
| bert-base-uncased + finetune + lr-0.001 + embed128 + dropout-0.3 | 76.68%, 76.01% |
| bert-base-uncased + finetune + lr-0.001 + bert-lr-0.000008 + embed128 + dropout-0.3 | 79.89%, 79.39%, 80.39%, 79.72%|
| bert-base-uncased + finetune + warmup(3-epoch) + anneal(60-epoch) + lr-0.002 + embed128 + dropout-0.3 | 70.91% |



|                              | Conala-Test      |
|:----------------------------:|-----------------|
| lr-0.001 + embed128  | 26.92 |
| bert-base-uncased + lr-0.001 + embed128 + dropout-0.3 | 29.09,  27.94|
| bert-base-uncased + finetune + lr-0.001 + bert-lr-0.00008 + embed128 + dropout-0.3 | 28.33 29.17|
| bert-base-uncased + finetune + lr-0.001 + bert-lr-0.00003 + embed128 + dropout-0.3 | 30.02 29.16|
| bert-base-uncased + finetune + lr-0.001 + bert-lr-0.000008 + embed128 + dropout-0.3 | 30.19 30.43|
| bert-base-uncased + finetune + lr-0.001 + bert-lr-0.000008 + embed128 + dropout-0.3 | 28.19 30.20|