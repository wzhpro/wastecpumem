# -*- coding: utf-8 -*-

import time
import argparse
from multiprocessing import Process
from multiprocessing import cpu_count


def exec_func(bt):
    while True:
        for i in range(0, 9600000):
            pass
        time.sleep(bt)


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='runing')

    parse.add_argument(
        "-c",
        "--count",
        default=cpu_count(),
        help='cpu count'
        )
    parse.add_argument(
        "-t",
        "--time",
        default=0.01,
        help='cpu time'
        )
    parse.add_argument(
        "-m",
        "--memory",
        default=1,
        help='memory'
        )

    args = parse.parse_args()

    cpu_logical_count = int(args.count)
    cpu_sleep_time = args.time
    memory_used_gb = int(args.memory)

    try:
        cpu_sleep_time = int(args.time)
    except ValueError:
        try:
            cpu_sleep_time = float(args.time)
        except ValueError as ex:
            raise ValueError(ex)

    _doc = """
    python runing.py -c 2 -t 0.01 -m 1
    -c CPU CORE Number
    -t CPU time interval
    -m Memory to Use

     """

    print("\n====================How to use=========================")
    print("{0}".format(_doc))
    print("\n====================================================")
    print('\nCPU Core:{0}'.format(cpu_logical_count))
    print('\nMemory:{0}GB'.format(memory_used_gb))
    print('\nBegin......')

    try:
        for i in range(memory_used_gb):
            locals()['A' + str(i)] = ' ' * (1 * 1024 * 1024 * 1024)
    except MemoryError:
        print("OOM......")

    try:
        ps_list = []

        for i in range(0, cpu_logical_count):
            ps_list.append(Process(target=exec_func, args=(cpu_sleep_time,)))

        for p in ps_list:
            p.start()

        for p in ps_list:
            p.join()
    except KeyboardInterrupt:
        print("Game Over!")
