import time
import matplotlib.pyplot as plt


class PerformanceTestResult(object):
    def __init__(self, validation_outcome, duration):
        self.validation_outcome = validation_outcome
        self.duration = duration


def run_performance_test(p, size):
    random_input = p.get_random_input(size)
    start_time = time.time()
    res = p.run(random_input)
    end_time = time.time()
    return PerformanceTestResult(
        p.validate_result(random_input, res), end_time-start_time
    )


def draw_line_chart(p, sizes):
    values = []
    for s in sizes:
        res = run_performance_test(p, s)
        values.append(res.duration)

    plt.plot(sizes, values)
    plt.axes().set_xscale('log')
    plt.show()
