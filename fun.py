sports_dict = {
    "Soccer": "Kicking a ball around while pretending you didn’t dive.",
    "Basketball": "Dribbling and dunking your way to glory, or at least style points.",
    "Baseball": "Swing, miss, spit, and repeat—America's oddly slow pastime.",
    "Tennis": "Elegant grunting across a net while chasing fuzzy yellow meteors.",
    "Golf": "Whack a tiny ball and walk after it in stylish pants.",
    "Rugby": "Soccer with more violence and less acting.",
    "Hockey": "Ice ballet with sticks and occasional face-punching.",
    "Cricket": "Where you break for tea halfway through a five-day game.",
    "Volleyball": "Don’t let the ball touch the ground or your social standing will.",
    "Swimming": "Competitive splashing, but with gold medals.",
    "Track and Field": "Running, jumping, throwing—basically gym class but intense.",
    "Boxing": "Two people punch each other while avoiding actual murder.",
    "Wrestling": "Choreographed chaos or Olympic struggle—pick your flavor.",
    "MMA": "All the violence of every sport in one ring.",
    "Fencing": "Dueling with car antennas in bee suits.",
    "Skateboarding": "Defying gravity with a board and youthful joints.",
    "Snowboarding": "Surfing on snow with the occasional faceplant.",
    "Surfing": "Trying not to drown while riding liquid mountains.",
    "Lacrosse": "Hockey with grass stains and sticks with baskets.",
    "Badminton": "Tennis’s quirky cousin with a bird and a lot of sass.",
    "Table Tennis": "Tiny paddles, tiny ball, Olympic-level reflexes.",
    "Archery": "Channeling medieval vibes with laser focus.",
    "Darts": "Precision drinking game for pub heroes.",
    "Esports": "Finger athletics for caffeine-fueled champions.",
    "Sumo Wrestling": "Two giants trying to gently push each other out of a circle.",
    "Skiing": "Downhill racing while hoping trees are avoidable.",
    "Gymnastics": "Spinning, flipping, and balancing like a human Swiss Army knife.",
    "Rowing": "Teamwork, rhythm, and maximum quad burn.",
    "Equestrian": "Letting a horse do the work while you wear fancy hats.",
    "Ultimate Frisbee": "Hippie football with a plastic disc of doom.",
    "Ping Pong": "Only Aus Baraam would play this sport"
}

while True:
    matching = []
    sportValues = []
    sports = []

    b = input("What is your favourite sport? ").lower()
    for sport in sports_dict:
        amountOfCorrect = 0
        try:
            for index, letter in enumerate(sport.lower()):
                if letter == b[index]:
                    amountOfCorrect+=1
        except:
            pass
        matching.append(amountOfCorrect / len(sport))
        sportValues.append(sports_dict[sport])
        sports.append(sport)

    currentHighestIndex = 1
    currentHighest = 0
    for index, value in enumerate(matching):
        if value > currentHighest:
            currentHighest = value
            currentHighestIndex = index

    print(f"I am {round(currentHighest*100, 2)}% sure you are talking about {sports[currentHighestIndex]}, {sportValues[currentHighestIndex]}")