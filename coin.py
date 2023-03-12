import coind
def main():
    
    coins = coind.Coin()
    print("This is the side up: ",coins.show_side())
    
    print("I am about to toss the coin four times")
    
    for c in range(4):
        coins.toss()
        print(coins.show_side())
if __name__ == "__main__":
    main()
    
    