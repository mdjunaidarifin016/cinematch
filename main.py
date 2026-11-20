import json
import datetime
def save_movies(movies):
    with open('movies.json','w') as f:
        json.dump(movies,f,indent=4)
def load_movies():
    try:
        with open('movies.json','r') as f:
            content=f.read()
            if not content.strip():
                return []
            movies=json.loads(content)
            if not isinstance(movies,list):
                raise ValueError("Invalid data format: Expected a list of movies in movies.json")
            return movies
    except FileNotFoundError as f:
        return []
    except json.JSONDecodeError:
        raise 
    
def search_movie(movies,title):
    matching_movies=[]
    for movie in movies:
        if title.lower() in movie['title'].lower():
            matching_movies.append(movie)
    if not matching_movies:
        return []
    return matching_movies
def filter_movies(movies,genre,min_rating):
    filtered_movies=[]
    for movie in movies:
        if genre.lower() in movie['genre'].lower() and movie['rating']>=min_rating:
            filtered_movies.append(movie)
    if not filtered_movies:
        return []
    return filtered_movies
def sort_movies(movies,sort_by):
    final_sort_by=sort_by.lower()
    if not (final_sort_by=="rating" or final_sort_by=="year"):
        return []
    sorted_movies=sorted(movies,key= lambda x:x[final_sort_by],reverse=True)
    return sorted_movies
def add_movie(movies,title,genre,rating,year):
    current_year=datetime.date.today().year
    if not 0<=rating<=10:
        return "Please enter valid rating"
    elif not 0<year<=current_year:
        return "Please enter a valid year"
    elif title.strip()=='':
        return "Please enter title"
    elif genre.strip()=='':
        return 'please enter genre'
    for movie in movies:
        if movie['title'].lower()==title.lower() and movie['genre'].lower()==genre.lower() and movie['rating']==rating and movie['year']==year:
            return "Movie with this title is already added"
    movies.append({"title":title.capitalize(),"genre":genre,"rating":rating,"year": year})
    save_movies(movies)
    return f"{title} added successfully!"
def delete_movies(movies,title):
    movie_found=False
    new_movies_list=[]
    another_movie_list=[]
    movie_dict={}
    for movie in movies:
        if movie['title'].lower()==title.lower():
            movie_found=True
            another_movie_list.append(movie)
    if movie_found:
        for index, movie in enumerate(another_movie_list,start=1):
            movie_dict[str(index)]=movie
        for i , m in movie_dict.items():
            print(f"{i}:{m}")
        choice1=input("Enter which one you want to delete")
        if not choice1 in movie_dict:
            return f"Invalid choice : {choice1}"
        choice2=input(f"Are you sure you want to delete {title} movie (y/n):").lower()
        if choice2=='y':
            for m in movies:
                if  m is not movie_dict[choice1]:
                    new_movies_list.append(m)
            movies[:]=new_movies_list
            save_movies(movies)
            return "Movie deleted successfully"
        elif choice2=='n':
            return "As you wish"
        else:
            return 'invalid choice'
    elif not movie_found:
        return "Movie not found"
def update_rating(movies,title,new_rating):
    if not 0<=new_rating<=10:
        return "Invalid rating"
    movie_found=False
    for movie in movies:
            if movie['title'].lower()==title.lower():
                movie_found=True
                movie['rating']=new_rating
                break
    if not movie_found:
        return "Movie not found"
    save_movies(movies)
    return "Rating updated successfully"
def display_movies(movies):
    if not movies:
        print ("No movies available")
        return
    for index,movie in enumerate(movies,start=1):
        print(f"{index}-----------\nTitle:{movie['title']}\nGenre:{movie['genre']}\nRating:{movie['rating']}\nYear:{movie['year']}\n")
def recommend_movies(movies,genre):
    r_m=[]
    for movie in movies:
        if movie['rating']>=7 and genre.lower() in movie['genre'].lower():
            r_m.append(movie)
    return sorted(r_m,key=lambda x : x['rating'],reverse=True)
def menu():
    try:
        movies=load_movies()
    except json.JSONDecodeError as j:
        print(f"Something went wrong:=>{j}")
        return
    while True:
        print('------CineMatch---------')
        print('1.Search movies')
        print('2.filter movies')
        print('3.sort movies')
        print('4.add movies')
        print('5.delete movies')
        print('6.Update rating')
        print("7.display all movies")
        print('8.recommend_movies')
        print('9.Exit')

        choice=input('Enter your choice:')
        if choice=='1':
            title=input('Enter movie title:')
            if title.strip()=='':
                print("please enter title")
                continue
            movie_list=search_movie(movies,title)
            if movie_list:
                display_movies(movie_list)
            else:
                print ("No matching movies found!")
        elif choice=='2':
            genre=input("Enter genre:")
            try:
                min_rating=float(input("Enter min rating:"))
                if not 0<=min_rating<=10:
                    print("Enter a valid rating(between 1 to 10)")
                    continue
            except ValueError:
                print ("Please enter valid min-rating")
                continue
            else:
                filtered_movies=filter_movies(movies,genre,min_rating)
                if filtered_movies:
                    display_movies(filtered_movies)
                else:
                    print("Movie not found according to the requirements")
        elif choice=='3':
            sort_by=input('Enter your sorting preference(rating or year)')
            sorted_movies=sort_movies(movies,sort_by)
            if sorted_movies:
                display_movies(sorted_movies)
            else:
                print("Cant sort , sorting can be possible by year or by rating")
        elif choice=='4':
            title=input('Enter movie title:')
            genre=input("Enter genre:")
            try:
                rating=float(input("Enter rating:"))
                year=int(input("Enter year:"))
            except ValueError:
                print("Enter valid rating  or year")
            else:
                print(add_movie(movies,title,genre,rating,year))
        elif choice=='5':
            title=input('Enter movie title:')
            print(delete_movies(movies,title))
        elif choice=='6':
            title=input('Enter movie title:')
            try:
                new_rating=float(input("Enter new rating:"))
            except ValueError:
                print("Enter valid rating")
            else:
                print(update_rating(movies,title,new_rating))
        elif choice=='7':
            display_movies(movies)
        elif choice=='8':
            genre=input("Enter your prefered genre:")
            if genre.strip()=='':
                print("Please enter genre")
                continue
            recommend_list=recommend_movies(movies,genre)
            if recommend_list:
                display_movies(recommend_list)
            else:
                print("No reccomended movies found")
        elif choice=='9':
            print("Thank You...")
            break
        else:
            print("Please Enter a valid choice")
menu()
