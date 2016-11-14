#converts direction to NE, E, SE, S, SW, W, NW, or, N 

def convert2cardinal(windDirection):
    if windDirection > 22.6 and windDirection < 67.5:
        cardinalDirection = 'NE'
    elif windDirection > 67.6 and windDirection < 112.5:
        cardinalDirection = 'E'
    elif windDirection > 112.6 and windDirection < 157.5:
        cardinalDirection = 'SE'
    elif windDirection > 157.6 and windDirection < 202.5:
        cardinalDirection = 'S'
    elif windDirection > 202.6 and windDirection < 247.5:
        cardinalDirection = 'SW'
    elif windDirection > 247.6 and windDirection < 292.5:
        cardinalDirection = 'W'
    elif windDirection > 292.6 and windDirection < 337.5:
        cardinalDirection = 'NW'
    else:
        cardinalDirection = 'N'
    return cardinalDirection;
