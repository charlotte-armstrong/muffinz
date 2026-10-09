def main():
    def blue():
        ##prints purple, which is red * 12
        red = 3
        purple = red * 12
        print("\nPurples is: " + str(purple))

    def blastoff():
        ##real original stuff here. we're blastin off. boom shakalaka.
        count = int(input("\nEnter a number to count down from: ")) ##the user input will be the highest number in countdown
        for num in range(count, 0, -1):
            print(num)
        print("BLASTOFF! 🚀")

    def candy_shop():
        ##create list of candies, add KitKat, add Snickers @ index 1, sort list, remove KitKat, print list
        candies = []
        candies.append("KitKat")
        candies.insert(1, "Snickers")
        candies.sort()
        candies.remove(candies[candies.index("KitKat")])
        print("\nCANDIES: " + str(candies))

        ##puts user candy input into a list
        user_candies = []
        for i in range(3):
            user_candy = input("Enter a candy: ")
            user_candies.append(user_candy)

        ##print all candies (user candies and original list)
        all_candies = candies + user_candies
        print("\nCANDIES (including user additions): ")
        for candy in range (len(all_candies)):
            print(all_candies[candy])

        ##give cost of all unique candies, 1.25 each
        single_candies = remove_duplicates(all_candies) ##used a function to clean duplicates
        total_cost = len(single_candies)*1.25
        return total_cost  

    def fruit_pricing():
        ##fruit: price
        fruits = {
            "apple": 0.75,
            "banana": 1.25,
            "orange": 0.80,
            "peach": 2.25,
            "coconut": 2.80
        }
        fruits["pear"] = 1.15

        ##prints value of peach
        print("\nA peach costs $" + str(fruits.get("peach")))

        ##prints all fruits that cost more than 1.25
        print("\nFruits that cost more than $1.25:")
        for fruit in fruits:
            if fruits.get(fruit) >= 1.25:
                print(fruit.upper())

        ##cost to buy 3 apples, 2 bananas,  1 coconut
        shopping_trip_cost = fruits.get("apple")*3 + fruits.get("banana")*2 + fruits.get("coconut")
        print("\nYour shopping trip cost: $" + str(shopping_trip_cost))

    ##remove duplicates from list, return new clean list
    def remove_duplicates(list):
            clean_list = []
            for item in list:
                if item not in clean_list:
                    clean_list.append(item)
            return clean_list 

    blue()
    blastoff()
    candy_shop()
    fruit_pricing()

##main method
if __name__ == "__main__":
    main()