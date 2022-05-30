import helper as hp
from pathlib import Path

if __name__ == '__main__':
    g_model = hp.load_model(hp.MODEL)
    g_code = Path(hp.ORIGINAL_CODE_SHORT).read_text()

    open(hp.RESULT_REDUCED, 'w').close()
    if g_model is not None:
        prediction = hp.prediction_by_model(g_model, g_code)
        with open(hp.PERSES_LOG, 'a') as fp:
            reduced_code = Path(hp.REDUCED_CODE_FULL).read_text()
            log_dict = {'prediction': str(prediction), 'reduced_code': str(reduced_code)}
            print(log_dict, file=fp)
            fp.write('\n')
        with open(hp.RESULT_REDUCED, 'w') as fp:
            fp.write(str(prediction))
