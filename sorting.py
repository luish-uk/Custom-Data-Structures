

class Sorting:
    def __init__(self, List: list):
        self.List = List

    def BubbleSort(self):
        s = self.List
        l = len(s)
        j = 0
        for i in range(l):
            for j in range(l-1):
                if s[j] > s[j+1]:
                    n = s.pop(j)
                    s.insert(j+1, n)
        return s
    
    def SelectionSort(self):
        s = self.List
        l = len(s)
        j = 0
        for j in range(l-1):
            min = j
            i = j+1
            while i < l:
                if (s[min] > s[i]):
                    min = i
                i+=1
            if min != j:
                n = s.pop(min)
                s.insert(j, n)
        return s
    
    def MergeSort(self, a=None):
        if a == None:
            a = self.List
        if not a:
            return
        l = len(a)
        if (l == 1):
            return a
        if l % 2 == 0:
            fhalf = l//2 #first half
            lhalf = l//2 #last half
        else:
            fhalf = l//2 #first half
            lhalf = l//2+1 #last half
        s1 = a[:(fhalf)]
        s2 = a[(lhalf):]
        
        s1 = self.MergeSort(s1)
        s2 = self.MergeSort(s2)

        return self.Merge(s1, s2)

    def Merge(self, a, b):
        c = []
        while a and b:
            if a[0] > b[0]:
                c.append(b[0])
                b.pop(0)
            else: 
                c.append(a[0])
                a.pop(0)
        while a:
            c.append(a[0])
            a.pop(0)
        while b:
            c.append(b[0])
            b.pop(0)
        return c
