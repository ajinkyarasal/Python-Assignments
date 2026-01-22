def ChekPrime(No):
    count = 0
    if No < 2:
        return True
    elif No == 2:
        return True
    else:
        for i in range(2,No):
            if No % i == 0:
                count += 1
        if count > 0:
            return False
        else:
            return True