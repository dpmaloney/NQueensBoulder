import copy
import math
import random

def succ(state, boulderX, boulderY):
    boardSize = len(state)
    newStates = []
    for i in range(len(state)):
        currQueenX = i
        currQueenY = state[i]

        for j in range(boardSize):
            newY = j

            if not (currQueenX == boulderX and newY == boulderY) and not (newY == currQueenY):
                if not(newY > boardSize -1 or newY < 0):
                    newState = copy.deepcopy(state)
                    newState[i] = newY
                    newStates.append(newState)


    return newStates

def f(state, boulderX, boulderY):
    f = 0
    boardSize = len(state)
    for i in range(boardSize):
        for j in range(boardSize):
            if not i == j:
                queen1X = i
                queen1Y = state[i]
                queen2X = j
                queen2Y = state[j]

                if queen1Y == queen2Y:
                    slope1andBoulder = math.atan2(abs((queen1Y - boulderY)), abs((queen1X - boulderX)))
                    slope2andBoulder = math.atan2(abs((queen2Y - boulderY)), abs((queen2X - boulderX)))
                    if slope1andBoulder == slope2andBoulder:
                        if boulderX > min(queen1X, queen2X) and boulderY >= min(queen1Y, queen2Y):
                            if boulderX < max(queen1X, queen2X) and boulderY <= max(queen1Y, queen2Y):
                                continue



                    f+=1
                    break

                if abs(queen1X-queen2X) == abs(queen1Y-queen2Y):
                    slope1andBoulder = math.atan2(abs((queen1Y - boulderY)), abs((queen1X - boulderX)))
                    slope2andBoulder = math.atan2(abs((queen2Y - boulderY)), abs((queen2X - boulderX)))
                    if slope1andBoulder == slope2andBoulder:
                        if boulderX > min(queen1X, queen2X) and boulderY >= min(queen1Y, queen2Y):
                            if boulderX < max(queen1X, queen2X) and boulderY <= max(queen1Y, queen2Y):
                                continue

                    f+=1
                    break


    return f


def choose_next(curr, boulderX, boulderY):
    succStates = succ(curr, boulderX, boulderY)
    tuples = []
    tuples.append((curr, f(curr, boulderX, boulderY)))
    for state in succStates:
        tuples.append((state, f(state, boulderX, boulderY)))

    tuples.sort(key=lambda k:k[1])

    minscore = tuples[0][1]
    sortedMin = []
    for tuple in tuples:
        if tuple[1] == minscore:
            sortedMin.append(tuple)

    sortedMin.sort(key=lambda k:k[0])

    if sortedMin[0][0] == curr:
        return None
    else:
        return sortedMin[0][0]

def nqueens(initial_state, boulderX, boulderY):
    lastState = None
    currentState = initial_state
    currentF = 10000000000
    while currentState is not None and currentF != 0:
        print(str(currentState) + " - f=" + str(f(currentState, boulderX, boulderY)))
        lastState = currentState
        currentF = f(lastState, boulderX, boulderY)
        currentState = choose_next(currentState, boulderX, boulderY)


    return lastState



def nqueens_restart(n, k, boulderX, boulderY):
    listResults = []
    currentLoop = 0
    result = nqueens(randomState(n, boulderX, boulderY), boulderX, boulderY)
    while f(result, boulderX, boulderY) != 0 and currentLoop < k:
        print("\n")
        listResults.append(result)
        result = nqueens(randomState(n, boulderX, boulderY), boulderX, boulderY)
        currentLoop+=1

    if f(result, boulderX, boulderY) == 0:
        print("\n")
        print(result)
    else:
        tuples = []
        for state in listResults:
            tuples.append((state, f(state, boulderX, boulderY)))

        tuples.sort(key=lambda k: k[1])

        minscore = tuples[0][1]
        sortedMin = []
        for tuple in tuples:
            if tuple[1] == minscore:
                sortedMin.append(tuple)

        sortedMin.sort(key=lambda k: k[0])
        print("\n")
        for state in sortedMin:
            print(state[0])





def randomState(n, boulderX, boulderY):
    state = []
    valid = False

    while not valid:
        for i in range(n):
            queenY = random.randint(0, n-1)
            if i == boulderX and queenY == boulderY:
                state.clear()
                break
            else:
                state.append(queenY)

        if len(state) != 0:
            valid = True

    return state






