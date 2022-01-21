class Orbitals:
    def __init__(self, atomicNumber):
        self.atomicNumber = atomicNumber
        self.o1s = 0
        self.o2s = 0
        self.o2p = 0
        self.o3s = 0
        self.o3p = 0
        self.o3d = 0
        self.o4s = 0
        self.o4p = 0
        self.o4d = 0
        self.o4f = 0
        self.o5s = 0
        self.o5p = 0
        self.o5d = 0
        self.o5f = 0
        self.o6s = 0
        self.o6p = 0
        self.o6d = 0
        self.o7s = 0
        self.o7p = 0
        self.fill()

    def fill(self):
        remaining = self.atomicNumber
        self.o1s = min(2, remaining) 
        remaining -= self.o1s
        self.o2s = min(2, remaining) 
        remaining -= self.o2s
        self.o2p = min(6, remaining) 
        remaining -= self.o2p
        self.o3s = min(2, remaining)
        remaining -= self.o3s
        self.o3p = min(6, remaining)
        remaining -= self.o3p
        self.o4s = min(2, remaining)
        remaining -= self.o4s
        self.o3d = min(10, remaining)
        remaining -= self.o3d
        self.o4p = min(6, remaining)
        remaining -= self.o4p
        self.o5s = min(2, remaining)
        remaining -= self.o5s
        self.o4d = min(10, remaining)
        remaining -= self.o4d
        self.o5p = min(6, remaining)
        remaining -= self.o5p
        self.o6s = min(2, remaining)
        remaining -= self.o6s
        self.o4f = min(14, remaining)
        remaining -= self.o4f
        self.o5d = min(10, remaining)
        remaining -= self.o5d
        self.o6p = min(6, remaining)
        remaining -= self.o6p
        self.o7s = min(2, remaining)
        remaining -= self.o7s
        self.o5f = min(14, remaining)
        remaining -= self.o5f
        self.o6d = min(10, remaining)
        remaining -= self.o6d
        self.o7p = min(6, remaining)
        remaining -= self.o7p

    def __str__(self):
        configuration = ""
        if self.o1s > 0: configuration += f"1s{self.o1s} "
        if self.o2s > 0: configuration += f"2s{self.o2s} "
        if self.o2p > 0: configuration += f"2p{self.o2p} "
        if self.o3s > 0: configuration += f"3s{self.o3s} "
        if self.o3p > 0: configuration += f"3p{self.o3p} "
        if self.o4s > 0: configuration += f"4s{self.o4s} "
        if self.o3d > 0: configuration += f"3d{self.o3d} "
        if self.o4p > 0: configuration += f"4p{self.o4p} "
        if self.o5s > 0: configuration += f"5s{self.o5s} "
        if self.o4d > 0: configuration += f"4d{self.o4d} "
        if self.o5p > 0: configuration += f"5p{self.o5p} "
        if self.o6s > 0: configuration += f"6s{self.o6s} "
        if self.o4f > 0: configuration += f"4f{self.o4f} "
        if self.o5d > 0: configuration += f"5d{self.o5d} "
        if self.o6p > 0: configuration += f"6p{self.o6p} "
        if self.o7s > 0: configuration += f"7s{self.o7s} "
        if self.o5f > 0: configuration += f"5f{self.o5f} "
        if self.o6d > 0: configuration += f"6d{self.o6d} "
        if self.o7p > 0: configuration += f"7p{self.o7p} "
        return configuration

    def getShells(self):
        shell0 = self.o1s
        shell1 = self.o2s + self.o2p
        shell2 = self.o3s + self.o3p + self.o3d
        shell3 = self.o4s + self.o4p + self.o4d + self.o4f
        shell4 = self.o5s + self.o5p + self.o5d + self.o5f
        shell5 = self.o6s + self.o6p + self.o6d
        shell6 = self.o7s + self.o7p

        shells = []

        if shell0 != 0: shells.append(shell0)
        if shell1 != 0: shells.append(shell1)
        if shell2 != 0: shells.append(shell2)
        if shell3 != 0: shells.append(shell3)
        if shell4 != 0: shells.append(shell4)
        if shell5 != 0: shells.append(shell5)
        if shell6 != 0: shells.append(shell6)

        return shells