def main():
    vacation()

def vacation():
    spots = ["Santorini", "Rome", "Paris", "Tokyo", "Bermuda"]
    print(spots[2])
    user_spot = input("Enter your ideal vacation destination: ")
    spots.append(user_spot)
    print(len(spots))
    spots.remove(spots[0])
    spots[2] = "Lisbon"
    spots.insert(2, "Ibiza")
    for spot in spots:
        print(spot)
    print(spots.sort())

##main loop thingy
if __name__ == "__main__":
    main()