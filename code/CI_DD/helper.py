import _pickle as pk
import subprocess
import javalang
from pathlib import Path

# helper files
MODEL = "../files/SVM_Handcrafted.model"
EXTRACTOR = "../files/Features_Handcrafted.jar"
CODE = "../files/sample.java"
FINAL_LOG = "../log_reduced_dd.txt"

# handcrafted targets
LABELS = ["equals", "main", "setUp", "onCreate", "toString", "run", "hashCode", "init", "execute", "get"]
LABEL2INDEX = {m: i for i, m in enumerate(LABELS)}
INDEX2LABEL = {i: m for i, m in enumerate(LABELS)}


# helper functions
def load_code(code_path):
    t_code = Path(code_path).read_text().strip()
    t_code = "class T {\n" + t_code + "\n}"
    return t_code


def is_parsable(t_code):
    try:
        tree = javalang.parse.parse(t_code)
        assert tree is not None
    except:
        return False
    return True


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


def code_to_deltas(t_code):
    tokens = str(t_code).strip().split()  # [t1, ..., tn]
    t_deltas = list(zip(range(len(tokens)), tokens))  # [('t1',0), ..., ('tn',n-1)]
    return t_deltas


def deltas_to_code(t_deltas):
    t_code = " ".join([t[1] for t in t_deltas])
    return t_code


def save_reduced_data(t_data, t_file):
    with open(t_file, 'w') as f:
        for t_line in t_data:
            print(t_line)
            f.write(str(t_line) + "\n")
        f.write("\n")
