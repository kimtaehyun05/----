coffee = 0

def coffee_machine(button):
    print()
    print("#1. (자동으로) 뜨거운 물을 준비한다.");
    print("#2. (자동으로) 종이컵을 준비한다.");

    if button == 1:
        print("#3. (자동으로) 보통 커피를 탄다.")
    elif button == 2:
        print("#3. (자동으로) 설탕 커피를 탄다.")
    elif button == 3:
        print("#3. (자동으로) 블랙 커피를 탄다.")
    else: 
        print("#3. (자동으로) 아무거나 탄다.\n")

    print("#4. (자동으로) 물을 붓는다.");
    print("#5. (자동으로) 수푼으로 젓는다.");
    print()

coffee = int(input("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙): "))
coffee_machine(coffee)
print("A손님~ 커피 여기 있습니다.");

coffee = int(input("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙): "))
coffee_machine(coffee)
print("B손님~ 커피 여기 있습니다.");

coffee = int(input("어떤 커피를 드릴까요? (1: 보통, 2: 설탕, 3: 블랙): "))
coffee_machine(coffee)
print("C손님~ 커피 여기 있습니다.");