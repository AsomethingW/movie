class Movie:
    def __init__(self, title, director, duration, watched, rating):
        self.title = title
        self.director = director
        self.duration = duration
        self.watched = False
        self.rating = None
    
    def __str__(self):
        status = "Watched" if self.watched else "Not watched yet"
        rating = self.rating if self.rating is not None else "N/A"
        return f"Movie: {self.title} directed by {self.director}. Duration: {self.duration}. Status: {self.watched}. Rating: {self.rating}. "
    
    def mark_as_watched(self, rating):
        if 0<= rating <=10:
            self.watched = True
            self.rating = rating
        else:
            print("Invalid rating. Must be between 0 and 10.")

    def is_long_movie(self):
        
        return self.duration > 150


    def update_rating(self, new_rating):

        if self.watched:
            self.rating = new_rating
        else:
            print("Cannot update rating. Movie has not been watched yet.")

    def reset_watch_status(self):
        self.watched = False

        self.rating = None


movie1 = Movie(f"Going Away, Gary Gibson, {4},")

print(movie1)

movie1.mark_as_watched(8)

movie1.update_rating(10)

print(movie1.is_long_movie())

movie1.reset_watch_status()

print(movie1)
