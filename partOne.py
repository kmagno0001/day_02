#Day 2: Cube Conundrum

list_of_games: list[int] = []

with open("input.txt", 'r') as puzzel_file:
    counter: int = 0
    for line in puzzel_file:
        lst_ofColor: list[str] = line.replace(';', ' ;').replace(",", " ").strip().split()[2::][::-1]
        lst_ofColor.append(";")
        counter += 1
        
        tmp: list[str] = []
        checking_eachSet: int = 0
        for i in lst_ofColor: 
            if i == ';' :
                for k, v in zip(tmp[::2], tmp[1::2]):
                    match k:
                        case "green":
                            checking_eachSet += 0 if int(v) <= 13 else 1
                        case "red":
                            checking_eachSet += 0 if int(v) <= 12 else 1
                        case "blue":
                            checking_eachSet += 0 if int(v) <= 14 else 1

                tmp.clear()     
                continue

            tmp.append(i)
  
        if checking_eachSet == 0:
            list_of_games.append(counter)
            
    print(sum(list_of_games))

