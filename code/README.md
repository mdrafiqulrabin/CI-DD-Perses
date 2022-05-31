This folder contains the sample code for running [DD](https://doi.org/10.1109/32.988498) and [Perses](https://doi.org/10.1145/3180155.3180236) with a [CI](https://doi.org/10.1145/3520312.3534869) model. For simplicity, this section uses a pre-trained [SVM model with handcrafted features on Top-10 Java methods](https://doi.org/10.1145/3416506.3423580).

# Prerequisite
* Add [DD.py](https://github.com/mdrafiqulrabin/dd-py3) to `./CI_DD` folder (already given)
* Add [perses_deploy.jar](https://github.com/perses-project/perses/releases/tag/v1.0) to `./CI_Perses` folder (already given)
* Add [SVM_Handcrafted.model](https://github.com/mdrafiqulrabin/handcrafted-embeddings) to `./files` folder (already given with extractor)
* Add a sample code to `./files/sample.java` file (already a sample `OnCreate` method is given)

# TODO
* Update root path in `./CI_Perses/helper.py` and `./CI_Perses/perses_test_script.sh` files.

# Run
* To reduce sample code using DD:
> $ source run_dd.sh 
* To reduce sample code using Perses:
> $ source run_perses.sh

# Results
* log_reduced_dd.txt (trace of reduced codes for DD)
* log_reduced_perses.txt (trace of reduced codes for Perses)

# Remarks
* To apply DD/Perses with other CI models, update `MODEL & EXTRACTOR` paths and `load_model & prediction_by_model` functions in `helper.py` file, according to the model.
* To apply DD on any programming language dataset, update `is_parsable`, `code_to_deltas`, and `deltas_to_code` in the `./CI_DD/helper.py` file.

# References
* Delta Debugging (DD): https://www.st.cs.uni-saarland.de/dd/
* Perses: https://github.com/perses-project/perses
