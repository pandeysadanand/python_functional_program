"""
    @Author: SADANAND PANDEY
    @Date: 2022-06-02  15:40:00
    @Last Modified by: SADANAND PANDEY
    @Last Modified time: 2022-06-02 15:45:00
    @Title : Write a Stopwatch Program for measuring the time that elapses between
             the start and end clicks
"""

import time


def stopwatch():
    """
            Description:
                This function calculate elapse time

            Parameter:
                None
            Return:
                Elapsed time
        """

    try:
        print("\nStopwatch has started...")
        start_time = time.time()

        input("\nPres Ctrl+C to stop stopwatch...\n")

        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopwatch has Stopped...")
        stop_time = time.time()

    return round(stop_time - start_time, 2)


# Main method
if __name__ == '__main__':
    print("\nWelcome to Stopwatch")

    # calling Stopwatch function
    elapsed_time = stopwatch()
    print("\nElapsed Time :", elapsed_time, "sec\n")
