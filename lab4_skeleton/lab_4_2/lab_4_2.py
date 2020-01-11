import numpy as np


def make_cards(array):
    ######################################
    # TODO :  1~25 1차원 array를 (5,5)의 숫자가 random하게 들어있는 2D array로 만든다.
    #         [Input]
    #         - array : (N,) 1-d array  
    #  
    #         [output]
    #         - cards :  (number of people=5, 5) reshaped of array 
    # ========== EDIT HERE ==========
    np.random.shuffle(array)
    cards = array.reshape((5,5))
    print(cards)
    # ===============================
    return cards

def get_winner(cards): 
    ######################################
    # TODO :  여러가지 numpy 연산을 통해서 승자의 인덱스를 구해준다.
    #         (예시를 보면 이해할 수 있음)
    #         주의사항 : loop을 쓰지 않고 구현.
    #         [Input]
    #         - cards : (number of people=5, 5)  
    #  
    #         [output]
    #         - winner :  합이 가장 큰 사람 (index가 0인 사람이 첫번째 사람)
    # ========== EDIT HERE ==========

    iden = np.identity(5)
    one = np.ones((5,5))
    # print(cards * iden)
    print((cards * iden).sum(axis=1))
    # print(cards * (one - iden))
    print((cards * (one - iden)).sum(axis=1))
    sumOfRow = (cards * iden).sum(axis=1) - (cards * (one - iden)).sum(axis=1)
    print(sumOfRow)
    winner = (np.argmax(sumOfRow)+1)


    # ===============================
    return winner

if __name__ == '__main__':
    # ========== EDIT HERE ==========
    # TODO : 1~25의 numpy array를 만든다.
    array = np.arange(1,26)
    # ===============================
    cards = make_cards(array)
    winner = get_winner(cards)

    print(winner)


