def sum3(q, w, e):
    return q + w + e


def curry(func, arn):

    if arn < 0:
        raise ValueError("Арность < 0")
    if arn > 3:
        raise ValueError("Арность больше чем количество аргументов")

    def curried(first):

        if arn == 1:
            return func(first)

        def next_curried(second):
            if arn == 2:
                return func(first, second)
            else:
                def final_curried(third):
                    return func(first, second, third)
                return final_curried
        return next_curried
    
    return curried



def uncurry(curried_func, arn):
    def uncurried(arg1, arg2, arg3):
        return curried_func(arg1)(arg2)(arg3)
    return uncurried
