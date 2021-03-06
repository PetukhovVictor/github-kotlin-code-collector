import time
import datetime


class TimeLogger:
    def __init__(self, accuracy=3):
        self.start_time = time.time()
        self.accuracy = accuracy

    def finish(self, task_name):
        seconds = round(time.time() - self.start_time, self.accuracy)
        print(task_name + ' finished. Time: ' + str(datetime.timedelta(seconds=seconds)))

    @staticmethod
    def _output(times, prefix, accuracy):
        output_str = ''
        if prefix is not None:
            output_str = prefix

        if isinstance(times, list):
            for time in times:
                output_str += '|' + str(round(time, accuracy))
        else:
            output_str += str(round(times, accuracy))

        return output_str

    @staticmethod
    def console_output(times, prefix=None, accuracy=3):
        print(TimeLogger._output(times, prefix, accuracy))


    @staticmethod
    def file_output(filename, times, prefix=None, accuracy=3):
        with open(filename, 'a') as logfile:
            logfile.write(TimeLogger._output(times, prefix, accuracy) + '\n')
