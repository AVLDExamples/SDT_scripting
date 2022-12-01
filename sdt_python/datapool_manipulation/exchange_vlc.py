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

DEG2PI = np.pi/180.
PI2DEG = 180./np.pi

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

    dp = project.data_pool.project
    
    dp_vlc_in_1 = [ x for x in dp.project.elements if "intake_valve_lift_curve_1" in x.name ][0]
    dp_vlc_in_2 = [ x for x in dp.project.elements if "intake_valve_lift_curve_2" in x.name ][0]
    dp_vlc_ex   = [ x for x in dp.project.elements if "exhaust_valve_lift_curve" in x.name ][0]

    np_vlc_in_1 = np.asarray(  [ 
        [0, 0],
        [349*DEG2PI,0],
        [350*DEG2PI,0.2e-3],
        [395*DEG2PI,8e-3],
        [540*DEG2PI,0.2e-3],
        [541*DEG2PI,0],
        [720*DEG2PI,0],
    ])
    np_vlc_in_2 = np.asarray(  [ 
        [0, 0],
        [339*DEG2PI,0],
        [340*DEG2PI,0.2e-3],
        [485*DEG2PI,8e-3],
        [530*DEG2PI,0.2e-3],
        [531*DEG2PI,0],
        [720*DEG2PI,0],
    ])
    
    np_vlc_ex =  np.asarray(  [ 
        [0, 0],
        [129*DEG2PI,0],
        [130*DEG2PI,0.2e-3],
        [200*DEG2PI,8e-3],
        [370*DEG2PI,0.2e-3],
        [371*DEG2PI,0],
        [720*DEG2PI,0],
    ])
    
    dp_vlc_in_1.data = np_vlc_in_1
    dp_vlc_in_2.data = np_vlc_in_2
    dp_vlc_ex.data = np_vlc_ex
    
    print("Save project...")
    project.save(proj_file)
    print("Save project... finished")
    if sys.platform != "win32":
        fcntl.flock(fd, fcntl.LOCK_UN)
        fd.close()
