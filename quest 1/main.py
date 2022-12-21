import sys

from RobotControllerClass import RobotController


if __name__ == '__main__':
    assert (len(sys.argv) - 1 == 6)
    ctrl = RobotController(sys.argv[1:])

    ctrl.connect()

    ctrl.run()