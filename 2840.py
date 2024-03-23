class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        a0 = []
        a1 = []
        b0 = []
        b1 = []
        for i in range(len(s1)):
            if i % 2 == 0:
                a0.append(s1[i])  #кладем тех кто на четной
            else:
                a1.append(s1[i]) #сюда закинула тех, кто на нечет позиции
        for i in range(len(s2)):
            if i % 2 == 0:
                b0.append(s2[i])
            else:
                b1.append(s2[i])
        

        a0.sort()
        a1.sort()
        b0.sort()
        b1.sort()
        return a0 == b0 and a1 == b1
