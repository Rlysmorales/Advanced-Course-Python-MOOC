person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}


def smallest_average(person1: dict, person2: dict, person3: dict):

    mary = person1["result1"] + person1["result2"] + person1["result3"]
    gary = person2["result1"] + person2["result2"] + person2["result3"]
    larry = person3["result1"] + person3["result2"] + person3["result3"]
    
    if (mary < gary) and (mary < larry):
        return person1
    elif (gary < mary) and (gary < larry):
        return person2
    else:
        return person3
    

print(smallest_average(person1, person2, person3))

