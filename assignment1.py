"""
Replace the contents of this module docstring with your own details
Name: Tao Kexin
Date started: 28/11/2019
GitHub URL: https://github.com/JCUS-CP1404/assignment-01-Glaivenus
"""

MENU = """Menu:
L - List movies
A - Add new movie
W - Watch a movie
Q - Quit
"""

def main():   # This function involves the printing Menu and the choice
    print("Movies To Watch 1.0 - by Tao Kexin")
    print(MENU)
    choice = input(">>> ").upper()
    all_movies = load_movies()
    while choice != "Q":   # If user enter Q, print the end message
        if choice == "L":
            list_movies(all_movies)
        elif choice == "A":
            all_movies.append(add_movies())
        elif choice == "C":
            led_movies(all_movies)
        else:   # If user enter other word, it will display the invalid message
            print("Invalid menu choice")
        print(MENU)
        choice = input(">>> ").upper()
    save_to_file(all_movies)   # If user enter Q, it will overwrite the csv file
    print(len(all_movies), "movies saved to", 'movies.csv', "\nHave a nice day :)")   # Save the data and print the ending
                                                                                                            # message

def load_movies():   # This function is used for open the csv file and put the data to the list
    all_movies = []   # Create a list for saving movies data
    movies_file = open('movies.csv', 'r')   # Open the csv file with 'r' read module
    for line in movies_file:
        line = line.strip("\n")   # To strip the line
        song_artist_year_list = line.split(",")
        all_movies.append(song_artist_year_list)
    movies_file.close()   # Close the csv file
    return all_movies



if __name__ == '__main__':
    main()
