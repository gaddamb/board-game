
from pytest_bdd import scenario, given, when, then, parsers

from business.move import ObjectMovement
from test.utils import run_command

@scenario("features/object_movement.feature", "Object movement forward")
def test_command_move_forward():
    pass

@scenario("features/object_movement.feature", "Object movement backward")
def test_command_move_backward():
    pass

@scenario("features/object_movement.feature", "Object rotation clockwise")
def test_command_rotate_clockwise():
    pass

@scenario("features/object_movement.feature", "Object rotation anti clockwise")
def test_command_rotate_anti_clockwise():
    pass

@scenario("features/object_pos_based_on_set_commands.feature", "Object movement based on set of commands")
def test_set_of_command():
    pass

@given(parsers.parse("a table of {width} and {height}"), target_fixture="context")
def given_table_dimension(width, height):
    context = dict(width=int(width), height=int(height))
    return context

@given(parsers.parse("an object at position {x} and {y} facing towards {direction}"))
def given_object_position(context, x, y, direction):
    context['original_pos_x'] = int(x)
    context['original_pos_y'] = int(y)
    obj = ObjectMovement(context['width'], context['height'], int(x), int(y))
    obj.standing_direction_of_object = direction

    obj.construct_matrix()

    context['object'] = obj

@when(parsers.parse("user enters {cmd} in the command"))
def when_user_enters_cmd(context, cmd):
    cmd_num = int(cmd)
    run_command(context['object'], cmd_num)

@when(parsers.parse("user enters set of {set_of_cmds} in the command"))
def when_user_enters_cmd(context, set_of_cmds):
    print(set_of_cmds)
    commands_list = set_of_cmds.encode("ascii", "ignore").decode().split(',')
    obj = context['object']

    for cmd in commands_list:
        run_command(obj, int(cmd))

@then(parsers.parse('the object must move forward step and stand at position {new_x} and {new_y}'))
def verify_obj_new_position(context, new_x, new_y):
    obj = context['object']
    assert int(new_x) == obj.pos_x
    assert int(new_y) == obj.pos_y

@then(parsers.parse('the object face now towards {new_direction}'))
def verify_obj_new_position(context, new_direction):
    obj = context['object']

    assert context['original_pos_x'] == obj.pos_x
    assert context['original_pos_y'] == obj.pos_y
    assert new_direction == obj.standing_direction_of_object


@then(parsers.parse('the object must stand at position {new_x} and {new_y}'))
def verify_obj_new_positions(context, new_x, new_y):
    obj = context['object']
    assert int(new_x) == obj.pos_x
    assert int(new_y) == obj.pos_y
