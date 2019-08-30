'''

Luhn algorithm

The Luhn algorithm is also known as the "modulus 10" algorithm. It is designed to protect against accidental errors and not malicious attacks. The algorithm is widely used to validate credit card number. The example below shows how the algorithm validates the credit card number 79927398713:

    From the rightmost digit, which is the check digit, and moving left, double the value of every second digit. E.g. 7 9 9 2 7 3 9 8 7 1 3 => 7 18 9 4 7 6 9 16 7 2 3
    If the result of this doubling operation is greater than 9, add the digits of the result. E.g. 7 18 9 4 7 6 9 16 7 2 3 => 7 9 9 4 7 6 9 7 7 2 3
    Take the sum of all the digits. E.g. 7 + 9 + 9 + 4 + 7 + 6 + 9 + 7 + 7 + 2 + 3 = 70
    If the total (from step 3) modulo 10 is equal to 0 (if the total ends in zero) then the number is valid according to the Luhn formula, ese it is not valid. E.g. Since 70 mod 10 = 0, then 79927398713 is considered a valid credit card number.

Task 1: Implement the function luhn(credit_num) which takes credit_num as a integer and returns True if the 16 digits credit_num is a valid credit card code, else False.

'''

def luhn(num):
    num = str(num)
    nums = [int(num[i]) for i in range(len(num))]
    nums = list(reversed(nums))

    for i in range(len(nums)):
        if i%2 != 0:
            nums[i] *= 2
            if nums[i] >= 10:
                nums[i] = int(str(nums[i])[0]) + int(str(nums[i])[1])
     
    sum = 0            
    for i in range(len(nums)):
        sum += nums[i]

    if sum%10 == 0:
        return True
    else:
        return False

#print(luhn(4148634548477380))
#print(luhn(4148634548477385))


f = open('1/credit_num.txt', 'r')
lines = f.readlines()
accepted = []
for i in lines:
    if luhn(i.strip()) == True:
        accepted.append(i.strip())

for i in accepted: 
    print("Accepted: ", end='')
    print(i)
print("Total accepted: ", end='')
print(len(accepted))