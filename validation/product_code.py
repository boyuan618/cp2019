
#code = input("What's your product code: ").strip() 
def product_code(code):
    if code[0].isupper() and 1 <= int(code[1:]) <= 9999:
        return True
    return False