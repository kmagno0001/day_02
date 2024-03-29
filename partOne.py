#Day 2: Cube Conundrum

with open("input.txt", 'r') as puzzel_file:
    sum_ofIDs: int = 0
    counter: int = 0
    for line in puzzel_file:
        lst_ofColor: list[str] = line.replace(';', ' ').replace(",", " ").strip().split()[2::][::-1]
        counter += 1
        
        checking_eachSet: bool = True
        for k, v in zip(lst_ofColor[::2], lst_ofColor[1::2]):
            match k:
                case "green":
                    checking_eachSet = True if int(v) <= 13 else False 
                    if not checking_eachSet: break
                case "red":
                    checking_eachSet = True if int(v) <= 12 else False
                    if not checking_eachSet: break
                case "blue":
                    checking_eachSet = True if int(v) <= 14 else False
                    if not checking_eachSet: break
  
        if checking_eachSet:
            sum_ofIDs += counter
            
    print(sum_ofIDs)

