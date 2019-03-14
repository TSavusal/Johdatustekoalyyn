import itertools
import copy

BOAT = "B"

class State:
    def __init__(self, state, previous):
        [x.sort() for x in state]
        self.state = state
        self.previous = previous

def possibleMovesAndSide(state):
    """
    Tama funktio palauttaa mahdolliset siirrot seka puolen, jolta siirrot toteutetaan
    """
    state = copy.deepcopy(state)
    startingside = state[0]
    if BOAT in startingside:
        boatside = 0
        side = "startingside"
    else:
        boatside = 1
        side = "goalside"
    
    rolesnoboat = state[boatside]
    rolesnoboat.remove(BOAT)
    
    rolesnoboat = [(x, ) for x in rolesnoboat]
    possiblemoves = rolesnoboat + [x for x in itertools.combinations([y[0] for y in rolesnoboat], 2)]
    return possiblemoves, side

def movePersons(state, persons, fromside):
    """
    Tama funktio toteuttaa siirron
    """
    if fromside == "startingside":
        startingside = state[0]
        goalside = state[1]

    else:
        startingside = state[1]
        goalside = state[0]

    def moveObject(object, startingside, goalside):
        startingside.remove(object)
        goalside.append(object)

    [moveObject(object, startingside, goalside) for object in persons + (BOAT,)]
    return state
    
def illegalStates(roles):
    """
    Tama funktio palauttaa kaikki laittomat tilat
    """
    allstates = []
    legalstates = []
    illegalstates = []
    persons = copy.deepcopy(roles)
    persons.remove(BOAT)
    for i in range(1, len(persons)+1):
        els = [list(x) for x in itertools.combinations(persons, i)]
        allstates.extend(els)
    allstates.append([])
    #-------TAHAN SINUN KOODI--------
    
    
    #--------------------------------
    return illegalstates

def legalState(state, roles):
    """
    Tama funktio tarkistaa etta tutkittava tilan kumpikaan puoli ei kuulu laittomiin tiloihin ja on nain ollen sallittu tila
    """
    illegalstates = illegalStates(roles)
    for side in state:
        side.sort()
        if side in illegalstates or side in [sorted(x + [BOAT]) for x in illegalstates]:
            return False
    return True

def reconstructPath(state):
    """
    Tama funktio rakentaa polun ratkaisun loydyttya alkutilasta tavoitetilaan
    """
    openlist = []
    openlist.append(state)
    nummoves = 0
    print("startingside:   {} \ngoalside:       {}\n".format(state.state[1], state.state[0]))
    while len(openlist) > 0:
        previous = openlist[0].previous
        if previous == None:
            print("Used in total {} moves to solve the problem".format(nummoves))
            break
        print("startingside:   {} \ngoalside:       {}\n".format(previous.state[1], previous.state[0]))
        nummoves += 1
        openlist.append(openlist.pop(0).previous)


def main():
    roles = ["H1", "H2", "H3", "W1", "W2", "W3", BOAT] # Nimetaan pariskunnat H1 & W1, H2 & W2 ja H3 & W3 missa H on mies ja W on vaimo. Veneesta kaytetaan kirjainta B
    startingstate = State([roles, []], None) # Alkutilanteessa aloittavalla puolella on kaikki 3 pariskuntaa ja vene. Aiempi tila on None
    goalstate = State([[], roles], None) # Toisella puolella on aloittavan puolen peilikuva eli ei pariskuntia tai venetta

    openlist = []
    closedlist = []
    openlist.append(startingstate)

    while len(openlist) > 0:
        state = openlist.pop(0)  # Leveyshaku : state = openlist.pop(0)    Syvyyshaku : state = openlist.pop()

        if state.state not in closedlist:
            closedlist.append(state.state)
            possiblemoves, side = possibleMovesAndSide(state.state)

            for move in possiblemoves:
                copystate = copy.deepcopy(state)
                copystate = State(movePersons(copystate.state, move, side), state)

                if legalState(copystate.state, roles):
                    if copystate.state == goalstate.state:
                        print("\n")
                        reconstructPath(copystate)
                        return
                    openlist.append(copystate)

if __name__ == "__main__":
    main()