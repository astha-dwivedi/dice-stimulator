import random;
print("Dice Stimluator");
repeat = input("press 'y' if u want to roll dice:");
while (repeat=="y"):
    x= random.randint(1,6);
    print('---------');
    if x==1:
        print('|       |');
        print('|   *   |');
        print('|       |');
    elif x==2:
        print('|   *   |');
        print('|       |');
        print('|   *   |');
    elif x==3:
        print('|   *   |');
        print('|   *   |');
        print('|   *   |');
    elif x==4:
        print('| *   * |');
        print('|       |');
        print('| *   * |');
    elif x==5:
        print('| *   * |');
        print('|   *   |');
        print('| *   * |');
    elif x==6:
        print('| *   * |');
        print('| *   * |');
        print('| *   * |');
    print('---------');
    repeat = input("press 'y' if u want to roll dice:");
    