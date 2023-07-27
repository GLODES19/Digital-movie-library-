class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director

class DigitalMovieLibrary:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, director):
        movie = Movie(title, director)
        self.movies.append(movie)
        print(f"Movie '{title}' by {director} added to the digital movie library.")

    def search_by_title(self, title):
        found_movies = []
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                found_movies.append(movie)
        return found_movies

    def search_by_director(self, director):
        found_movies = []
        for movie in self.movies:
            if movie.director.lower() == director.lower():
                found_movies.append(movie)
        return found_movies

    def display_movies(self):
        if len(self.movies) == 0:
            print("The digital movie library is empty.")
        else:
            print("Movies in the digital movie library:")
            for movie in self.movies:
                print(f"Title: {movie.title}, Director: {movie.director}")

# Create a digital movie library object
movie_library = DigitalMovieLibrary()

# Function to add movies to the digital movie library
def add_movies():
    while True:
        title = input("Enter the movie title (or 'q' to quit): ")
        if title.lower() == 'q':
            break
        director = input("Enter the director of the movie: ")
        movie_library.add_movie(title, director)

# Function to search movies by title
def search_movies_by_title():
    title = input("Enter the movie title to search for: ")
    found_movies = movie_library.search_by_title(title)
    if len(found_movies) == 0:
        print("No movies found with that title.")
    else:
        print(f"Found {len(found_movies)} movie(s) with the title '{title}':")
        for movie in found_movies:
            print(f"Title: {movie.title}, Director: {movie.director}")

# Function to search movies by director
def search_movies_by_director():
    director = input("Enter the movie director to search for: ")
    found_movies = movie_library.search_by_director(director)
    if len(found_movies) == 0:
        print("No movies found by that director.")
    else:
        print(f"Found {len(found_movies)} movie(s) by the director '{director}':")
        for movie in found_movies:
            print(f"Title: {movie.title}, Director: {movie.director}")

# Function to display all movies in the digital movie library
def display_all_movies():
    movie_library.display_movies()

# Main menu
while True:
    print("\nDigital Movie Library")
    print("1. Add movies")
    print("2. Search movies by title")
    print("3. Search movies by director")
    print("4. Display all movies")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_movies()
    elif choice == '2':
        search_movies_by_title()
    elif choice == '3':
        search_movies_by_director()
    elif choice == '4':
        display_all_movies()
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

