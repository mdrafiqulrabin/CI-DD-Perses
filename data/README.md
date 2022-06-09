The `summary_results.csv` file contains the summary results of all experiments, it has the following fields:

* `model`: {code2vec, code2seq}
* `task`: METHOD_NAME
* `reduction_type`: {dd_<token/char>, perses_fixpoint}
* `sample_type`: {freq, rare, small, large}
* `exp_type`: {reduction_type}_{sample_type}_methods
* `filename`: ID for the input file in <c2v/c2s>_simplified folder
* `score`: score of actual prediction
* `loss`: loss of actual prediction
* `reduction_pass`: total/valid/correct stepss for reduction
* `reduction_time`: total time spent for reduction
* `initial_program`: actual raw program
* `final_program`: minimal reduced program
* `len_{initial/final/minimal/reduced}_chars`: number of corresponding chars
* `per_removed_chars`: percentage of removed chars
* `initial_tokens`: tokens in actual program
* `final_tokens`: tokens in minimal program
* `len_{initial/final/minimal/reduced}_tokens`: number of corresponding tokens
* `per_removed_tokens`: percentage of removed tokens



# References
* Code2Vec: https://code2vec.org/

> Uri Alon, Meital Zilberstein, Omer Levy, and Eran Yahav. 2019. Code2Vec: Learning Distributed Representations of Code. In Proceedings of the ACM on Programming Languages (PACMPL'19), Vol. 3, POPL, Article 40. DOI: https://doi.org/10.1145/3290353

* Code2Seq: https://code2seq.org/

> Uri Alon, Omer Levy, and Eran Yahav. 2019. Code2Seq: Generating Sequences from Structured Representations of Code. In International Conference on Learning Representations (ICLR'19). OpenReview.net. DOI: https://openreview.net/forum?id=H1gKYo09tX
