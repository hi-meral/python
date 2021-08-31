final = ""

def DecimalToBinary(num):
    global final
    if num >= 1:
        DecimalToBinary(num // 2)
        final += str(num % 2)

    return final.zfill(8)

print( DecimalToBinary(60) )
final = ''
print( DecimalToBinary(13) )
