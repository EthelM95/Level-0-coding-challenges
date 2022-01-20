def converting(a):
    hours = a // 60
    minutes =  a % 60
    output = ""
    if hours > 1 and minutes > 1:
        output += str(hours) + " hours, " + str(minutes) + " minutes"

    elif hours <= 1 and minutes <= 1:
        output += str(hours) + " hour, " + str(minutes) + " minute"

    elif hours > 1 and minutes <= 1:
        output += str(hours) + " hours, " + str(minutes) + " minute"

    else:
        output += str(hours) + " hour, " + str(minutes) + " minutes"

    print(output)

converting(65)