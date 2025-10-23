class MusicTracker():
    def __init__(self):
        self.track_list = []
    def add_track(self, track_name):
        if isinstance(track_name, str):
            print("BBBBBBB")
            self.track_list.append(track_name)
        else:
            print("AAAAAAAA")
            return "Invalid track name!"

    def list_tracks(self):
        return self.track_list 
    def check_valid_type(self, track_var):
        return isinstance(track_var, str)
        