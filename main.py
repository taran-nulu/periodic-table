from Orbitals import *
from PeriodicTable import *
from Element import *

hydrogen = Orbitals(1)
print(hydrogen)
print(hydrogen.getShells())

rutherfordium = Orbitals(104)
print(rutherfordium)
print(rutherfordium.getShells())



periodicTable = PeriodicTable()
periodicTable.printDetailed()
periodicTable.printCompact()
periodicTable.draw()


    # def printMax(self):
    #     maxRow = self.elements[0].row
    #     maxColumn = self.elements[0].column
    #     for element in self.elements:
    #         if element.row > maxRow:
    #             maxRow = element.row
    #         if element.column > maxColumn:
    #             maxColumn = element.column
    #     print(maxRow)
    #     print(maxColumn)