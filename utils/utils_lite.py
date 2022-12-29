
def ShopValid(text: str)-> bool:
    try:
        new_text = int(text)
        return False
    except ValueError:
        pass
    if len (text)> 25:
        return False
    return True


def create_counter():
    i = 0
    def func():
        nonlocal i
        i += 1
        return i
    return func

