import movie
import fresh_tomatoes

toy_story = movie.Movie("Toy Story",
	"A story about boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

thor = movie.Movie("Toy Story",
	"A story about boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movie.Movie("Toy Story",
	"A story about boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

school_of_rock = movie.Movie("Toy Story",
	"A story about boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
	"https://www.youtube.com/watch?v=KYz2wyBy3kc")

movies = [toy_story,thor,avatar,school_of_rock]
fresh_tomatoes.open_movies_page(movies)