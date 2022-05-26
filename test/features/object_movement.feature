Feature: Object movement based on commands

    To position the object based on the commands

    Scenario: Object movement forward
        Given a table of <width> and <height> 
        And an object at position <x> and <y> facing towards <direction>
        When user enters <cmd> in the command
        Then the object must move forward step and stand at position <new_x> and <new_y>    

        Examples:            
            | width | height | x | y | direction  |  cmd   | new_x | new_y | 
            | 4     |   4    | 2 | 2 |     N      |   1    |   2   |   1   |
   
    Scenario: Object movement backward
        Given a table of <width> and <height> 
        And an object at position <x> and <y> facing towards <direction>
        When user enters <cmd> in the command
        Then the object must move forward step and stand at position <new_x> and <new_y>

        Examples:            
            | width | height | x | y | direction  |  cmd   | new_x | new_y | 
            | 4     |   4    | 2 | 2 |     N      |   2    |   2   |   3   |

    Scenario: Object rotation clockwise
        Given a table of <width> and <height> 
        And an object at position <x> and <y> facing towards <direction>
        When user enters <cmd> in the command
        Then the object face now towards <new_direction>
        
        Examples:            
            | width | height | x | y | direction  |  cmd   | new_direction | 
            | 4     |   4    | 2 | 2 |     N      |   3    |        E      |

    Scenario: Object rotation anti clockwise
        Given a table of <width> and <height> 
        And an object at position <x> and <y> facing towards <direction>
        When user enters <cmd> in the command
        Then the object face now towards <new_direction>

        Examples:            
            | width | height | x | y | direction  |  cmd   | new_direction | 
            | 4     |   4    | 2 | 2 |     N      |   4    |        W      |