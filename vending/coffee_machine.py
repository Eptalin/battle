import time

class CoffeeMachine():       
     
    def run(self):
        coffee = input("How do you take your coffee? ")
        for i in range(3):
            print(".")
            time.sleep(1)
        print(f"Here's your coffee: {coffee}")

        