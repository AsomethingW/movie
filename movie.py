class Movie:
    def __init__(self, title, director, duration, watched, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.watched = watched
        self.rating = rating
    
    def __str__(self):
        return f"Movie: {self.title} directed by {self.director}. Duration: {self.duration}. Status: {self.watched}. Rating: {self.rating}. "
    
    def mark_as_watched(rating):
        watched = True

        rating = 9.5
    mark_as_watched()

    def is_long_movie():
        
        duration = 123

        if duration > 150:
            return f"True"
        else:
            return f"False"
    is_long_movie()

    def update_rating(new_rating):
        watched = True

        if watched == True:
            rating = input("How do you rate the movie?")
    update_rating()

    def reset_watch_status():
        watched = False

        rating = None
    reset_watch_status()
movie1 = Movie(f"Going Away, Gary Gibson, {4},")
