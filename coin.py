import coind
def main():
    
    mcoin = coind.Coin()
    print("This is the side up: ",mcoin.show_side())
    
    print("I am about to toss the coin ten times")
    
    for c in range(10):
        mcoin.toss()
        print(mcoin.show_side())
    
    print("Thank you")
if __name__ == "__main__":
    main()
    
    