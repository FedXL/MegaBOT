

def ShopValid(text: str)-> bool:
    try:
        new_text = int(text)
        return False
    except ValueError:
        pass
    if len (text)> 25:
        return False
    return True

