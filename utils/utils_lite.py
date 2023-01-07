
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


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False