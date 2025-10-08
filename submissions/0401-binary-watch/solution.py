class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for i in range(min(turnedOn + 1, 5)):
            hours  = self.hour_strs(i)
            minutes = self.minute_strs(turnedOn - i)

            for h in hours:
                for m in minutes:
                    result.append(f"{h}:{m}")

        return result

    
    # turnedOne is 0 to 4
    def hour_strs(self, turnedOn: int) -> List[str]:
        match turnedOn:
            case 0:
                return ["0"]
            case 1:
                return ["1", "2", "4", "8"]
            case 2:
                return ["3", "5", "6", "9", "10"]
            case 3:
                return ["7", "11"]
            case _:
                return []


    # turnedOne is 0 to 6
    def minute_strs(self, turnedOn: int) -> List[str]:
        match turnedOn:
            case 0:
                return ["00"]
            case 1:
                return ["01", "02", "04", "08", "16", "32"]
            case 2:
                return ["03", "05", "06", "09", "10", "12", 
                        "17", "18", "20", "24", "33", "34", 
                        "36", "40", "48"]
            case 3:
                return ["07", "11", "13", "14", "19", "21",
                        "22", "25", "26", "28", "35", "37",
                        "38", "41", "42", "44", "49", "50",
                        "52", "56"]
            case 4:
                return ["15", "23", "27", "29", "30", "39", 
                        "43", "45", "46", "51", "53", "54", 
                        "57", "58"]
            case 5:
                return ["31", "47", "55", "59"]
            case _:
                return []
        
