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
    "Ping Pong": "Only Aus Baraam would play this sport",
    "Gym": "Rocco Ianni's hideout"
}

def getMatchFromSlice(slice, original, correctionOffset):
    numOfCorrect = 0
    totalOffset = 0
    try:
        for index, letter in enumerate(slice.lower()):
            if letter == original[index + totalOffset]:
                numOfCorrect+=1
            else:
                totalOffset += correctionOffset
    except:
        pass
    if numOfCorrect==1 and (not (slice.lower()[0] == original[0]) or correctionOffset==0): # Single letter match is inaccurate unless it is the first letter | If correctional offset is neutral, ignore, other offsets will calculate this in its place
        return 0
    return numOfCorrect / len(slice) # Percentage correct as decimal

def getHighestItem(array):
    highestIndex = 0 # Current Highest Index
    highestValue = -1 # Current Highest Value
    for index, value in enumerate(array):
        if value > highestValue:
            highestValue = value
            highestIndex = index
    return highestIndex, highestValue

while True:
    vector = []
    keyed_list = list(sports_dict.keys())
    value_list = list(sports_dict.values())

    baraam = input("What is your favourite sport? ").lower()
    for sport in sports_dict:
        zeroed = getMatchFromSlice(sport, baraam, 0)
        _, bestValue = getHighestItem([
            getMatchFromSlice(sport, baraam, -1),                                       # Negative Offset
            getMatchFromSlice(sport, baraam, 1),                                        # Positive Offset
            zeroed*2 if zeroed <= 0.3 or zeroed >= 0.6 and zeroed <=0.95 else zeroed    # Zero Offset # Give bonus to continueous lines
        ])
        vector.append(bestValue)

    hi, hv = getHighestItem(vector)
    if hi==0 and hv==0: # Only single letter matches
        print("I am not sure about that sport.\n")
    else:
        print(f"I am {round(hv*100, 2)}% sure you are talking about {keyed_list[hi]}, {value_list[hi]}\n")