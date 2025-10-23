from lib.music_tracker import *

"""
If an instance of music tracker is made, make sure that it is instantiated properly
"""
def test_music_tracker_instance():
    music_tracker = MusicTracker()
    result = isinstance(music_tracker, MusicTracker)
    assert result == True

"""
Given a track name, it should add a track to the 
track list
"""
def test_add_track():
    m_t = MusicTracker()
    m_t.add_track("Fergalicious")
    assert m_t.track_list[0] == "Fergalicious"

"""
When called, it should return the track list
"""
def test_list_tracks():
    m_t = MusicTracker()
    track = m_t.add_track("Fergalicious")
    track = m_t.add_track("Fergalicious2")
    result = m_t.list_tracks()
    assert result == ['Fergalicious', 'Fergalicious2']
"""
If given an invalid type for the track, it should give an error message
"""
def test_check_valid_type():
    m_t = MusicTracker()
    result = m_t.add_track(["Catalyst", "Ewart"])
    assert result == "Invalid track name!"
