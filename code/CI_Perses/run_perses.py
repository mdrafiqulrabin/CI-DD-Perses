import ast
import os
import subprocess
from pathlib import Path

import helper as hp

g_model = None
g_original_prediction = None
g_all_data = list()


def run_perses():
    reduced_codes = []

    # cleanup temp files
    for f in [hp.RESULT_ORIGINAL, hp.RESULT_REDUCED, hp.PERSES_LOG]:
        if os.path.exists(f):
            os.remove(f)
        open(f, 'w').close()
    with open(hp.RESULT_ORIGINAL, 'w') as fp:
        fp.write(g_original_prediction)

    # cmd for perses
    try:
        cmd = ['java', '-jar', 'perses_deploy.jar',
               '--test-script', 'perses_test_script.sh',
               '--input-file', hp.ORIGINAL_CODE_SHORT,
               '--output-file', hp.REDUCED_CODE_SHORT,
               '--code-format', 'COMPACT_ORIG_FORMAT']
        subprocess.call(cmd, close_fds=True)
    except Exception as ex2:
        print("Error at run_perses:\n{}".format(str(ex2)))
        return reduced_codes

    # process perses log
    with open(hp.PERSES_LOG, 'r') as fp:
        t_count = 0
        for line in fp:
            line = str(line).strip()
            if line:
                log_dict = ast.literal_eval(line)
                prediction = log_dict['prediction'].strip()
                reduced_code = log_dict['reduced_code'].replace('\n', '').strip()
                if prediction == g_original_prediction and len(reduced_code) > 0:
                    t_count += 1
                    reduced_codes.append("[{}] {}".format(t_count, reduced_code))

    return reduced_codes


if __name__ == '__main__':
    print("\n<Start>\n")

    # get model
    g_model = hp.load_model(hp.MODEL)
    assert g_model is not None

    # get code
    g_code = hp.load_code(hp.CODE)
    assert g_code is not None
    g_all_data.append("\nSample code:\n\n{}".format(g_code))
    hp.save_initial_code(g_code)

    # get prediction
    g_original_prediction = hp.prediction_by_model(g_model, g_code)
    g_all_data.append("\nOriginal prediction = {}".format(g_original_prediction))

    # run fixpoint-perses
    try:
        # print("Reducing input...")
        g_all_data.append("\n\nTrace of reduced code(s): [preserving original prediction by model]\n")
        results = run_perses()
        g_all_data.extend(results)
        r_code = Path(hp.REDUCED_CODE_FULL).read_text()
        # print("The 1-minimal input is", r_code)
        g_all_data.append("\nMinimal reduced code:\n\n{}".format(r_code))
    except Exception as ex1:
        g_all_data.append("\nException:\n{}".format(str(ex1)))

    # save reduced data
    output_file = hp.FINAL_LOG
    hp.save_reduced_data(g_all_data, output_file)

    print("\n<End>\n")
