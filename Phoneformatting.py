numbers=[1,2,3,4,5,6,7,8,9,0]

def FormatPhoneNumber(numbers):
    area = "".join(map(str, numbers[0:3]))
    first3 = "".join(map(str, numbers[3:6]))
    last4 = "".join(map(str, numbers[6:10]))  
    return f"({area}) {first3}-{last4}"

FormatPhoneNumber(numbers)
