text_1 = input()
text_2 = input()
text_3 = input()

if "зайка" in text_1 and "зайка" in text_2 and "зайка" in text_3:
    answer = min(text_1, text_2, text_3)
elif "зайка" in text_1 and "зайка" in text_2:
    answer = min(text_1, text_2)
elif "зайка" in text_1 and "зайка" in text_3:
    answer = min(text_1, text_3)
elif "зайка" in text_2 and "зайка" in text_3:
    answer = min(text_2, text_3)
elif "зайка" in text_1:
    answer = text_1
elif "зайка" in text_2:
    answer = text_2
else:
    answer = text_3

print(answer, len(answer))