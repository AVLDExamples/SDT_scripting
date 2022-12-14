# Needs sdt_python to work!
import datetime

try:
    import fcntl
except ImportError:
    pass
import os

import sdt.project
import sys
import time
import numpy as np

if __name__ == '__main__':
    os.environ["SIMFS_DISABLE_SHORTENING"] = "1"
    # os.environ["SIMFS_DISABLE_METAINFO"] = "1"
    fd = None
    print("Starting Prepare!")
    if len(sys.argv) != 2:
        print("Wrong amount of Parameters! Expected one got: " + str(len(sys.argv) - 1))
        exit()

    proj_path = sys.argv[1]
    print(proj_path)
    if not os.path.exists(proj_path):
        print("Path does not exist!")
        exit()
    if not proj_path.endswith(".proj"):
        print("Not a .proj file can't prepare")
        exit()

    starting_dir = os.getcwd()
    if os.getcwd() != os.path.dirname(os.path.abspath(proj_path)):
        os.chdir(os.path.dirname(proj_path))
    proj_file = os.path.basename(proj_path)

    if sys.platform == "win32":
        print("API_prep started on windows! Cant ensure preping only one time!")
    else:
        fd = open("prep.lock", "w+")
        while True:
            pid = fd.read().rstrip()
            try:
                # checks if it could kill it -> if it could kill it, it is still running
                if pid == "":
                    pass
                else:
                    os.kill(int(pid), 0)
            except OSError:
                # unlocking because process in mutex is no longer running
                print("Deadlock detected\nUnlocking...")
                fcntl.flock(fd, fcntl.LOCK_UN)
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                print("Got Lock: " + str(os.getpid()))
                fd.seek(0)
                fd.write(str(os.getpid()))
                fd.truncate()
                break
            except Exception:
                # print("Waiting for lock: " + str(os.getpid()))
                time.sleep(1)

    if os.path.exists(".preped"):
        print("Was already preped. Exiting.\nIf you want to prep this again remove '.preped' from the proj dir.")
        if sys.platform != "win32":
            fcntl.flock(fd, fcntl.LOCK_UN)
        exit(0)

    # try:
    print("Load Project...")
    project = sdt.project.load_project(proj_file)
    print("Load project... finished")

    for model in project.models:
        if not hasattr(model, "jobs"):
            continue
        for case_set in project.cases.case_sets:
            for case in case_set.cases:
                model.jobs.settings.add_case(case)

        model.jobs.settings.computing_resources.manual.select()
        model.jobs.settings.computing_resources.manual.use_server = False
        my_run = model.jobs.run()

    with open(".preped", "w") as f_p:
        if sys.platform == "win32":
            time_str = str(datetime.datetime.now().strftime("%H%M%S%d%m%Y"))
        else:
            time_str = str(datetime.datetime.now().strftime("%H%M%S%::%d%m%Y"))
        f_p.write(str(os.getpid()) + "  " + time_str)
    # except Exception as e:
    #    print("Crash during prep, with exception:\n" + str(e))
    #    traceback.print_tb(e.__traceback__)
    # os.chdir(starting_dir)
    print("API Prep Script done.")
    if sys.platform != "win32":
        fcntl.flock(fd, fcntl.LOCK_UN)
        fd.close()
