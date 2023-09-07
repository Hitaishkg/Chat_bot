import random

class TouristSpotChatbot:
    def __init__(self):
        self.budget = 0
        self.season = ""
        self.location = ""
        self.kind_of_place = ""

    def start(self):
        print("Welcome to the Tourist Spot Recommendation Chatbot!")
        self.location = input("Is your trip national or international? ").lower()
        self.get_budget()
        self.get_season()
        self.get_kid_of_place()
        self.recommend_spot()

    def get_budget(self):
        self.budget = float(input("What is your budget for the trip? "))

    def get_season(self):
        self.season = input("What season are you planning to travel? ").lower()
    def get_kid_of_place(self):
        self.kind_of_place("what kind of palce do you a  want to visit historical places or mountains or beaches or ")
    def recommend_spot(self):
        if self.location == "national":
            if self.budget > 1000:
                if self.season == "summer":
                    national_summer_spots = [
                        "Shimla, Himachal Pradesh",
                        "Manali, Himachal Pradesh",
                        "Darjeeling, West Bengal",
                        "Munnar, Kerala",
                        "Ooty, Tamil Nadu",
                        "Nainital, Uttarakhand",
                        "Ladakh, Jammu and Kashmir",
                        "Coorg, Karnataka",
                        "Kodaikanal, Tamil Nadu",
                        "Rishikesh, Uttarakhand"
                    ]
                    random_spot = random.choice(national_summer_spots)
                    print(f"You might enjoy a trip to {random_spot}.")
                elif self.season == "winter":
                    national_winter_spots = [
                        "Goa",
                        "Agra, Uttar Pradesh",
                        "Jaipur, Rajasthan",
                        "Jaisalmer, Rajasthan",
                        "Varanasi, Uttar Pradesh",
                        "Rann of Kutch, Gujarat",
                        "Kerala",
                        "Udaipur, Rajasthan",
                        "Delhi",
                        "Mumbai, Maharashtra"
                    ]
                    random_spot = random.choice(national_winter_spots)
                    print(f"You might enjoy a winter trip to {random_spot}.")
                else:
                    print("Sorry, I don't have recommendations for that season.")
            else:
                print("Your budget might be too low for national travel.")
        if self.location == "international":
            if(self.budget > 1000000):
                
                
                
        else:
            print("Sorry, I didn't understand your location choice.")

if __name__ == "__main__":
    chatbot = TouristSpotChatbot()
    chatbot.start()
