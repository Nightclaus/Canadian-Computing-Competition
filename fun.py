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

def getMatchFromSlice(slice, original):
    amountOfCorrect = 0
    negativeOffset = 0
    try:
        for index, letter in enumerate(slice.lower()):
            if letter == original[index - negativeOffset]:
                amountOfCorrect+=1
            else:
                negativeOffset += 1
    except:
        pass
    return amountOfCorrect / len(slice)

def getHighestItem(array):
    highestIndex = 0 # Current Highest Index
    highestValue = 0 # Current Highest Value
    for index, value in enumerate(array):
        if value > highestValue:
            highestValue = value
            highestIndex = index
    return highestIndex, highestValue

while True:
    matching = []
    keyed_list = list(sports_dict.keys())
    value_list = list(sports_dict.values())

    baraam = input("What is your favourite sport? ").lower()
    for sport in sports_dict:
        matching.append(getMatchFromSlice(sport, baraam))
    hi, hv = getHighestItem(matching)

    print(f"I am {round(hv*100, 2)}% sure you are talking about {keyed_list[hi]}, {value_list[hi]}\n")