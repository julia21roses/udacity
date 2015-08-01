import video
import fresh_tomatoes

"""
This file contains the information - the name, storyline and the movie trailer link
for the movie trailers to be displayed in the webpage.
toy_story, toy_story2, and toy_story3 are instances of the video class.
"""
toy_story = video.Video("The Fifth Element","In the colorful future , a cab driver unwittingly becomes the central figure in the search for a legendary cosmic weapon to keep Evil and Mr Zorg at bay.",
                        "http://ia.media-imdb.com/images/M/MV5BMTkzOTkwNTI4N15BMl5BanBnXkFtZTYwMDIzNzI5._V1_SX640_SY720_.jpg",
                        "https://www.youtube.com/watch?v=VkX7dHjL-aY")

toy_story2 = video.Video("The Matrix","A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/c/c1/The_Matrix_Poster.jpg/220px-The_Matrix_Poster.jpg",
                        "https://www.youtube.com/watch?v=vKQi3bBA1y8")

toy_story3 = video.Video("Sherlock Holms","Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England.",
                        "http://ia.media-imdb.com/images/M/MV5BMTg0NjEwNjUxM15BMl5BanBnXkFtZTcwMzk0MjQ5Mg@@._V1_SX214_AL_.jpg",
                        "https://www.youtube.com/watch?v=8beqXEMoPfc")

""" The movies are passed to fresh_tomatoes.py open_movies_page funciton
as a list"""
movies = [toy_story, toy_story2, toy_story3]

fresh_tomatoes.open_movies_page(movies)
