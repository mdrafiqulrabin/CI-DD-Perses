import _pickle as pk
import subprocess
import os
from pathlib import Path

# full-path
ROOT_PATH = "/scratch/rabin/deployment/root-all/CI-DD-Perses/code"

# model paths
MODEL = ROOT_PATH + "/files/SVM_Handcrafted.model"
EXTRACTOR = ROOT_PATH + "/files/Features_Handcrafted.jar"
CODE = ROOT_PATH + "/files/sample.java"

# perses paths
ORIGINAL_CODE_SHORT = "perses_test_original.java"
REDUCED_CODE_SHORT = "perses_test_reduced.java"
ORIGINAL_CODE_FULL = ROOT_PATH + "/CI_Perses/" + ORIGINAL_CODE_SHORT
REDUCED_CODE_FULL = ROOT_PATH + "/CI_Perses/" + REDUCED_CODE_SHORT
RESULT_ORIGINAL = ROOT_PATH + "/CI_Perses/tmp/perses_result_original.txt"
RESULT_REDUCED = ROOT_PATH + "/CI_Perses/tmp/perses_result_reduced.txt"
PERSES_LOG = ROOT_PATH + "/CI_Perses/tmp/perses_current_log.txt"
FINAL_LOG = ROOT_PATH + "/log_reduced_perses.txt"

# handcrafted targets
LABELS = ["equals", "main", "setUp", "onCreate", "toString", "run", "hashCode", "init", "execute", "get"]
LABEL2INDEX = {m: i for i, m in enumerate(LABELS)}
INDEX2LABEL = {i: m for i, m in enumerate(LABELS)}


# helper functions
def load_code(code_path):
    t_code = Path(code_path).read_text().strip()
    t_code = "class T {\n" + t_code + "\n}"
    return t_code


def load_model(model_path):
    try:
        import sklearn
        with open(model_path, 'rb') as f:
            clf = pk.load(f)
            return clf
    except Exception as ex:
        # print("Error at load_model:\n{}".format(str(ex)))
        return None


def prediction_by_model(t_model, t_code):
    try:
        cmd = ['java', '-jar', EXTRACTOR, t_code]
        y_test = subprocess.check_output(cmd, encoding="utf-8")  # 0,...,1
        y_test = [int(y) for y in y_test.split(',')]  # [0,...,1]
        y_pred = t_model.predict([y_test])
        y_pred = INDEX2LABEL[y_pred[0]]
        return y_pred
    except Exception as ex:
        # print("Error at prediction_by_model:\n{}".format(str(ex)))
        return ""


def save_initial_code(t_code):
    if os.path.exists(ORIGINAL_CODE_FULL):
        os.remove(ORIGINAL_CODE_FULL)
    with open(ORIGINAL_CODE_FULL, "w") as fp:
        fp.write(t_code + "\n")
    if os.path.exists(REDUCED_CODE_FULL):
        os.remove(REDUCED_CODE_FULL)
    with open(REDUCED_CODE_FULL, "w") as fp:
        fp.write("")


def save_reduced_data(t_data, t_file):
    with open(t_file, 'w') as f:
        for t_line in t_data:
            print(t_line)
            f.write(str(t_line) + "\n")
        f.write("\n")
