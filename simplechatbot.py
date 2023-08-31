class TouristSpotChatbot:
    def __init__(self):
        self.budget = 0
        self.season = ""
        self.location = ""

    def start(self):
        print("Welcome to the Tourist Spot Recommendation Chatbot!")
        self.location = input("Is your trip national or international? ").lower()
        self.get_budget()
        self.get_season()
        self.recommend_spot()

    def get_budget(self):
        self.budget = float(input("What is your budget for the trip? "))

    def get_season(self):
        self.season = input("What season are you planning to travel? ").lower()

    def recommend_spot(self):
        if self.location == "national":
            if self.budget > 1000:
                if self.season == "summer":
                    print("You might enjoy a trip to the national beach resort.")
                elif self.season == "winter":
                    print("Consider visiting the national mountain retreat.")
                else:
                    print("Sorry, I don't have recommendations for that season.")
            else:
                print("Your budget might be too low for national travel.")
        elif self.location == "international":
            if self.budget > 5000:
                if self.season == "summer":
                    print("You could explore an exotic international beach destination.")
                elif self.season == "winter":
                    print("You might enjoy a trip to an international city with winter festivities.")
                else:
                    print("Sorry, I don't have recommendations for that season.")
            else:
                print("Your budget might be too low for international travel.")
        else:
            print("Sorry, I didn't understand your location choice.")

if __name__ == "__main__":
    chatbot = TouristSpotChatbot()
    chatbot.start()

