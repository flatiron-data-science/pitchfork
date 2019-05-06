# create list of boxes of pizza
num_pizzas = [1, 3, 4, 5, 6]

# for each box, tell me how many I have
for box in num_pizzas:
    print(f"I have {box} number of pizza boxes")


# create a box multiplier
def multiply_boxes(boxes, multiplier):
    """Takes each box and multiplies it by the same multiplier"""
    output = []

    for box in boxes:
        output.append(box * multiplier)

    return output


print(
    f"""
If I had a magic wand, I'd increase each box of pizza by 4!
Now each box has more pizza
{multiply_boxes(num_pizzas, 4)}
"""
)


# end of script #
