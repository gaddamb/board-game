
def run_command(obj, cmd_num):
    if cmd_num == 1:
        obj.step_forward()

    elif cmd_num == 2:
        obj.step_backwards()

    elif cmd_num == 3:
        obj.rotate_clockwise()

    elif cmd_num == 4:
        obj.rotate_anti_clockwise()
