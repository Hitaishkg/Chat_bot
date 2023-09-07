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
        self.get_kind_of_place()
        self.recommend_spot()

    def get_budget(self):
        self.budget = float(input("What is your budget for the trip? "))

    def get_season(self):
        self.season = input("What season are you planning to travel? ").lower()

    def get_kind_of_place(self):
        self.kind_of_place = input("What kind of place do you want to visit (Mountain or Beach)? ").lower()

    def recommend_spot(self):
        if self.location == "national":
            if self.budget > 1000:
                if self.season == "summer":
                    if self.kind_of_place == "mountain":
                        national_summer_mountains = [
                            "Shimla, Himachal Pradesh",
                            "Manali, Himachal Pradesh",
                            "Munnar, Kerala",
                            "Ooty, Tamil Nadu",
                            "Nainital, Uttarakhand",
                            "Ladakh, Jammu and Kashmir",
                            "Coorg, Karnataka",
                            "Kodaikanal, Tamil Nadu",
                            "Rishikesh, Uttarakhand"
                        ]
                        random_spot = random.choice(national_summer_mountains)
                        print(f"You might enjoy a summer mountain trip to {random_spot}.")
                    elif self.kind_of_place == "beach":
                        national_summer_beaches = [
                            "Goa",
                            "Puri, Odisha",
                            "Varkala, Kerala",
                            "Gokarna, Karnataka",
                            "Kovalam, Kerala",
                            "Digha, West Bengal",
                            "Andaman and Nicobar Islands",
                            "Ganpatipule, Maharashtra"
                        ]
                        random_spot = random.choice(national_summer_beaches)
                        print(f"You might enjoy a summer beach trip to {random_spot}.")
                    else:
                        print("Sorry, I don't have recommendations for that kind of place.")
                elif self.season == "winter":
                    if self.kind_of_place == "mountain":
                        national_winter_mountains = [
                            "Auli, Uttarakhand",
                            "Gulmarg, Jammu and Kashmir",
                            "Shimla, Himachal Pradesh",
                            "Manali, Himachal Pradesh",
                            "Munsiyari, Uttarakhand",
                            "Kufri, Himachal Pradesh"
                        ]
                        random_spot = random.choice(national_winter_mountains)
                        print(f"You might enjoy a winter mountain trip to {random_spot}.")
                    elif self.kind_of_place == "beach":
                        national_winter_beaches = [
                            "Goa",
                            "Andaman and Nicobar Islands",
                            "Pondicherry",
                            "Kovalam, Kerala",
                            "Mahabalipuram, Tamil Nadu",
                            "Gokarna, Karnataka"
                        ]
                        random_spot = random.choice(national_winter_beaches)
                        print(f"You might enjoy a winter beach trip to {random_spot}.")
                    else:
                        print("Sorry, I don't have recommendations for that kind of place.")
                else:
                    print("Sorry, I don't have recommendations for that season.")
            else:
                print("Your budget might be too low for national travel.")
        elif self.location == "international":
            if self.budget > 100000:
                if self.kind_of_place == "mountain":
                    international_mountains = [
                        "Swiss Alps, Switzerland",
                        "Patagonia, Argentina",
                        "Banff National Park, Canada",
                        "The Andes, South America",
                        "Himalayas, Nepal",
                        "Rocky Mountains, USA"
                    ]
                    random_spot = random.choice(international_mountains)
                    print(f"You might enjoy an international mountain trip to {random_spot}.")
                elif self.kind_of_place == "beach":
                    international_beaches = [
                        "Phuket, Thailand",
                        "Maldives",
                        "Bora Bora, French Polynesia",
                        "Cancun, Mexico",
                        "Fiji",
                        "Seychelles",
                        "Maui, Hawaii",
                        "Bali, Indonesia",
                        "Mykonos, Greece",
                        "Rio de Janeiro, Brazil"
                    ]
                    random_spot = random.choice(international_beaches)
                    print(f"You might enjoy an international beach trip to {random_spot}.")
                else:
                    print("Sorry, I don't have recommendations for that kind of place.")
            else:
                print("Your budget might be too low for international travel.")
        else:
            print("Sorry, I didn't understand your location choice.")

if __name__ == "__main__":
    chatbot = TouristSpotChatbot()
    chatbot.start()
