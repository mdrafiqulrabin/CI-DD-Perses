import DD
import helper as hp

g_model = None
g_original_prediction = None
g_all_data = list()
g_count = 0


class MyDD(DD.DD):
    def __init__(self):
        DD.DD.__init__(self)

    def _test(self, _deltas):
        if not _deltas:
            return self.PASS

        _code = hp.deltas_to_code(_deltas)
        if hp.is_parsable(_code):  # reduced code is parsable
            _prediction = hp.prediction_by_model(g_model, _code)
            if _prediction == g_original_prediction:  # preserving original prediction
                global g_count
                g_count += 1
                g_all_data.append("[{}] {}".format(g_count, _code))
                return self.FAIL

        return self.PASS


if __name__ == '__main__':
    print("\n<Start>\n")

    # get model
    g_model = hp.load_model(hp.MODEL)
    assert g_model is not None

    # get code
    g_code = hp.load_code(hp.CODE)
    assert g_code is not None
    g_all_data.append("\nSample code:\n\n{}".format(g_code))

    # get prediction
    g_original_prediction = hp.prediction_by_model(g_model, g_code)
    g_all_data.append("\nOriginal prediction = {}".format(g_original_prediction))

    # run DDMIN
    try:
        # print("Reducing input...")
        g_all_data.append("\n\nTrace of reduced code(s): [preserving original prediction by model]\n")
        t_deltas = hp.code_to_deltas(g_code)
        c = MyDD().ddmin(t_deltas)
        r_code = hp.deltas_to_code(c)
        # print("The 1-minimal input is", r_code)
        g_all_data.append("\nMinimal reduced code:\n\n{}".format(r_code))
    except Exception as ex:
        g_all_data.append("\nException:\n{}".format(str(ex)))

    # save reduced data
    output_file = hp.FINAL_LOG
    hp.save_reduced_data(g_all_data, output_file)

    print("\n<End>\n")
