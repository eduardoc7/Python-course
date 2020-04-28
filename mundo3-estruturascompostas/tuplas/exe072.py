numbers = (
'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
while True:
    num = int(input('Type a number between 0 and 20: '))
    if 0 <= num <= 20:
        break
    print('Try again. ', end='')
print(f'You typed the number {numbers[num]}')
