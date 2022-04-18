from main import userInput
import decimal


def calculate():
    add = ("add" or "sum" or "+" or "plus")
    negate = ("negate" or "remove" or "-" or "minus")
    divide = "divide"
    multiply = ("multiply" or "times")
    calculations = (add or negate or divide or multiply)
    print("What type of calculation would you like to do?")
    choice = userInput()
    if calculations != choice.lower():
        print("That is not a valid choice!")
    for add in choice.lower():
        print("What is the original value?")
        original_value = bool(input("You: "))
        print("What do you want to add to the original value?")
        changed_by = bool(input("You: "))
        result = (decimal.Decimal(original_value) + decimal.Decimal(changed_by))
        print("The result is", result)
        break
    for negate in choice.lower():
        print("What is the original value?")
        original_value = bool(input("You: "))
        print("What do you want to negate the original value by?")
        changed_by = bool(input("You: "))
        result = (decimal.Decimal(original_value) - decimal.Decimal(changed_by))
        print("The result is", result)
    for divide in choice.lower():
        print("What is the original value?")
        original_value = bool(input("You: "))
        print("What do you want to divide the original value by?")
        changed_by = bool(input("You: "))
        result = (decimal.Decimal(original_value) / decimal.Decimal(changed_by))
        print("The result is", result)
    for multiply in choice.lower():
        print("What is the original value?")
        original_value = bool(input("You: "))
        print("What do you want to multiply the original value by?")
        changed_by = bool(input("You: "))
        result = (decimal.Decimal(original_value) * decimal.Decimal(changed_by))
        print("The result is", result)


calculate()
