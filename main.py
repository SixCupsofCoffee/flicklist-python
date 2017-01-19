import webapp2
import random

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):

        # make a list with at least 5 movie titles
        movieList = ["Star Trek", "Titanic", "Scott Pilgrim vs. The World", "The Lord of the Rings", "Star Wars", "The Big Lebowski", "The Matrix", "The Cabin in the Woods", "Indiana Jones", "Casablanca", "The Picture of Dorian Gray", "WarGames", "Hackers", "Back to the Future", "Ferris Bueller's Day Off", "Flash Gordon", "Ghostbusters", "Halloween", "Jurassic Park", "Paranormal Activity", "Shrek"]

        movieSelection = movieList[random.randrange(0, len(movieList))]

        return movieSelection

    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        tomorrowsMovie = self.getRandomMovie()

        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        self.response.write(content)

        # pick a different random movie, and display it under
        content2 = "<h1>Tomorrow's Movie</h1>"
        content2 += "<p>" + tomorrowsMovie + "</p>"

        self.response.write(content2)



app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
