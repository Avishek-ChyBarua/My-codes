f = 1
# this t_movie function is used to select movie name
def t_movie():
    print("which movie do you want to watch?")
    print("1,Damal ")
    print("2,Poran ")
    print("3,Operation Sundarban")
    print("4,Dhaka Attack")
    print("5,back")
    movie = int(input("choose your movie: "))
    if movie == 4:
        # in this it goes to center function and from center it goes to movie function and it comes back here and then go to theater
        center()
        theater()
        return 0
    if f == 1:
        theater()


# this theater function used to select screen
def theater():
    print("which screen do you want to watch movie: ")
    print("1,SCREEN 1")
    print("2,SCREEN 2")
    print("3,SCREEN 3")
    a = int(input("choose your screen: "))
    ticket = int(input("number of ticket do you want?: "))
    print('-------------------------------\n|    1 2 3 4 5 6 7 8 9 10     |\n|11 12 13 14 15 16 17 18 19 20|\n'
          '|21 22 23 24 25 26 27 28 29 30|\n-------------------------------')
    print('Please select your seat: ')
    seat = input()
    print('You selected no:'+seat)
    cost = 250
    print('Do you want some snacks?')
    snacks = input().lower()
    if snacks == 'yes':
        print('1. Popcorn\n2. Coke')
        pop = 100
        coke = 50
        x = input()
        if x == 1:
            cost += pop
        elif x == 2:
            cost += coke
        else:
            cost += pop + coke
    Total_Bill = ticket * cost
    print('\033[2;31;43m "Sir you have to pay BDT:"\033[0;0m', Total_Bill)
    timing(a)


# this timing function used to select timing for movie
def timing(a):
    time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
    }
    time2 = {
        "1": "10.15-1.15",
        "2": "1.25-4.25",
        "3": "4.35-7.35",
        "4": "7.45-10.45"
    }
    time3 = {
        "1": "10.30-1.30",
        "2": "1.40-4.40",
        "3": "4.50-7.50",
        "4": "8.00-10.45"
    }
    if a == 1:
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        print("successful!, enjoy movie and thanks for coming. time is " + x)
    elif a == 2:
        print("choose your time:")
        print(time2)
        t = input("select your time:")
        x = time2[t]
        print("successful!,  enjoy movie and thanks for coming. time is " + x)
    elif a == 3:
        print("choose your time:")
        print(time3)
        t = input("select your time:")
        x = time3[t]
        print("successful!,  enjoy movie and thanks for coming. time is " + x)
    return 0


def movie(theater):
    if theater == 1:
        t_movie()
    elif theater == 2:
        t_movie()
    elif theater == 3:
        t_movie()
    elif theater == 4:
        city()
    else:
        print("wrong choice")


def center():
    print("which theater do you wish to see movie? ")
    print("1,Star cineplex,Basundhara")
    print("2,Sony Squre Star cineplex,")
    print("3,Balaka")
    print("4,Back")
    a = int(input("choose your option: "))
    movie(a)
    return 0


# this function is used to select city
def city():
    print("Hi welcome to movie ticket booking: ")
    print("where you want to watch movie?:")
    print("1,Dhaka")
    place = int(input("choose your option: "))
    if place == 1:
        center()
    else:
        print("wrong choice")


city()
