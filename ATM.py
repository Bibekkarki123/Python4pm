amount = 20000
Pin = 1234
Pin_Number = int(input("Enter a pin Number:\n"))
if Pin_Number == Pin:
    print("1.Check balance\n2.Withdraw balance")
    option = int(input("Enter a option: "))
    if option == 1:
        print(f"Your total balance is {amount}")
    if option == 2:
        withdraw_amount = int(input("Enter Amount: "))
        if withdraw_amount <= 20000:
            Remaining_Amount = amount - withdraw_amount
            print(f"Remaining Amount is {Remaining_Amount}")
        else:
            print("You have insufficient Balance")
else:
    print("Incorrect Pin Number. Try Again")
