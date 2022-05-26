Feature: Object movement based on set of commands

    To position the object based on given set of commands
  
    Scenario: Object movement based on set of commands
        Given a table of <width> and <height> 
        And an object at position <x> and <y> facing towards <direction>
        When user enters set of <set_of_cmds> in the command
        Then the object must stand at position <new_x> and <new_y>    

        Examples:            
            | width | height | x | y | direction  |   set_of_cmds     | new_x | new_y | 
            | 4     |   4    | 2 | 2 |     N      |​1,4,1,3,2,3,2,4,1,0​|   0   |   1   |