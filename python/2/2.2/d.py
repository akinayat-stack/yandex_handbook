petya = int(input())
vasya = int(input())
tolya = int(input())
if petya > vasya and petya > tolya:
    first = "Петя"
    if vasya > tolya:
        second = "Вася"
        third = "Толя"
    elif tolya > vasya:
        second = "Толя"
        third = "Вася"
elif vasya > petya and vasya > tolya:
    first = "Вася"
    if petya > tolya:
        second = "Петя"
        third = "Толя"
    elif tolya > petya:
        second = "Толя"
        third = "Петя"   
elif tolya > petya and tolya > vasya:
    first = "Толя"
    if petya > vasya:
        second = "Петя"
        third = "Вася"
    elif vasya > petya:
        second = "Вася"
        third = "Петя" 
print(f"1. {first}")
print(f"2. {second}")
print(f"3. {third}")