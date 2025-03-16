while True:
    import random
    words = {
        "Brave": "Showing courage",
        "Angry": "Feeling strong dislike",
        "Kind": "Being nice and helpful",
        "Lazy": "Not wanting to work",
        "Fast": "Moving quickly",
        "Slow": "Moving at a low speed",
        "Happy": "Feeling joyful",
        "Sad": "Feeling unhappy",
        "Strong": "Having great power",
        "Weak": "Lacking strength",
        "Smart": "Having intelligence or being clever",
        "Dumb": "Not smart; lacking intelligence",
        "Big": "Large in size",
        "Small": "Little in size",
        "Hot": "Having a high temperature",
        "Cold": "Having a low temperature",
        "Near": "Close by",
        "Far": "A long distance away",
        "Light": "Not heavy; also can mean brightness",
        "Dark": "Without light; can also mean sad or scary",
        "Easy": "Simple to do",
        "Difficult": "Hard to do",
        "Young": "Not old",
        "Old": "Having lived for a long time",
        "Tired": "Feeling like you need rest",
        "Rich": "Having a lot of money or valuable things",
        "Poor": "Having little money or resources",
        "Funny": "Making people laugh",
        "Quiet": "Making little or no noise",
        "Loud": "Producing a lot of noise"
    }


    word, meaning = random.choice(list(words.items()))


    a = input(f"What is this word: {meaning}")
    if a.lower() == word.lower():
        print("Yess")
    else:
        print("wrong")
         
