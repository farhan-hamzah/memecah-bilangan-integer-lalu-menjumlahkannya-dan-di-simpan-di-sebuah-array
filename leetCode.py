nums = int(input())
hasil = []
place = 1
if nums > 0:
    while nums > 0:
        digit = nums % 10
        if digit > 0:
            hasil.append(str(digit * place))
        nums = nums // 10
        place *= 10
    print(" + ".join(hasil[::-1])) 