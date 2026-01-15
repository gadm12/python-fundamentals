weather = input("How's the weather today? (sunny, rainy, cloudy): ").lower()

if weather == "sunny":
    print("Great! how about going for a ride")
elif weather == "cloudy":
    print("Great! How about going for a walk or playing a sport outdoors?")
elif weather == "rainy":
    print("lets chill home and watch tv!")
else:
    print("I never heard of such a thing")
