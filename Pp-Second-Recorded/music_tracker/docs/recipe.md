# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
class MusicTracker():
    #Tracks: a list of strings
    def __init__(self):
        # Creates an empty list
    def add_track(self, track_name):
        #Parameters
        # Represents name of track
        #Side effects
        #Saves track to the track list
    
    def list_tracks(self)
    #Returns track list

    def check_valid_type(self, track_var)
    #If the track variable is valid, it will return True.
# EXAMPLE

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        pass # No code here yet

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

"""
If an instance of music tracker is made, make sure that it is instantiated properly
"""

music_tracker = MusicTracker()
result = isinstance(music_tracker, MusicTracker)

"""
Given a track name, it should add a track to the 
track list
"""
m_t = MusicTracker()
m_t.add_track("Fergalicious")
result = "Fergalicious"

"""
When called, it should return the track list
"""
m_t = MusicTracker()
result = m_t.list_tracks()
"""
If given an invalid type for the track, it should give an error message
"""
m_t = MusicTracker()
m_t.add_track(05)
result = "Invalid track name!"

# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
