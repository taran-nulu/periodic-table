from tkinter import *

from Element import *
from Family import *


class PeriodicTable:
    def __init__(self):
        self.elements = [
            Element("Hydrogen", "H", 1, 1, Family.NONMETAL, 0, 0),
            Element("Helium", "He", 2, 4, Family.NOBLE_GAS, 0, 17),
            Element("Lithium", "Li", 3, 6.94, Family.ALKALI_METAL, 1, 0),
            Element("Beryllium", "Be", 4, 9.01,
                    Family.ALKALINE_EARTH_METAL, 1, 1),
            Element("Boron", "B", 5, 10.81, Family.METALLOID, 1, 12),
            Element("Carbon", "C", 6, 12.01, Family.NONMETAL, 1, 13),
            Element("Nitrogen", "N", 7, 14, Family.NONMETAL, 1, 14),
            Element("Oxygen", "O", 8, 15.99, Family.NONMETAL, 1, 15),
            Element("Fluorine", "F", 9, 18.99, Family.HALOGEN, 1, 16),
            Element("Neon", "Ne", 10, 20.17, Family.NOBLE_GAS, 1, 17),
            Element("Sodium", "Na", 11, 22.98, Family.ALKALI_METAL, 2, 0),
            Element("Magnesium", "Mg", 12, 24.3,
                    Family.ALKALINE_EARTH_METAL, 2, 1),
            Element("Aluminum", "Al", 13, 26.98, Family.METAL, 2, 12),
            Element("Silicon", "Si", 14, 28.08, Family.METALLOID, 2, 13),
            Element("Phosphorus", "P", 15, 30.97, Family.NONMETAL, 2, 14),
            Element("Sulfur", "S", 16, 32.06, Family.NONMETAL, 2, 15),
            Element("Chlorine", "Cl", 17, 35.45, Family.HALOGEN, 2, 16),
            Element("Argon", "Ar", 18, 39.94, Family.NOBLE_GAS, 2, 17),
            Element("Potassium", "K", 19, 39.09, Family.ALKALI_METAL, 3, 0),
            Element("Calcium", "Ca", 20, 40.07,
                    Family.ALKALINE_EARTH_METAL, 3, 1),
            Element("Scandium", "Sc", 21, 44.95,
                    Family.TRANSITION_METAL, 3, 2),
            Element("Titanium", "Ti", 22, 47.86,
                    Family.TRANSITION_METAL, 3, 3),
            Element("Vanadium", "V", 23, 50.94, Family.TRANSITION_METAL, 3, 4),
            Element("Chromium", "Cr", 24, 51.99,
                    Family.TRANSITION_METAL, 3, 5),
            Element("Manganese", "Mn", 25, 54.93,
                    Family.TRANSITION_METAL, 3, 6),
            Element("Iron", "Fe", 26, 55.84, Family.TRANSITION_METAL, 3, 7),
            Element("Cobalt", "Co", 27, 58.93, Family.TRANSITION_METAL, 3, 8),
            Element("Nickel", "Ni", 28, 58.69, Family.TRANSITION_METAL, 3, 9),
            Element("Copper", "Cu", 29, 63.54, Family.TRANSITION_METAL, 3, 10),
            Element("Zinc", "Zn", 30, 65.38, Family.TRANSITION_METAL, 3, 11),
            Element("Gallium", "Ga", 31, 69.72, Family.METAL, 3, 12),
            Element("Germanium", "Ge", 32, 72.64, Family.METALLOID, 3, 13),
            Element("Arsenic", "As", 33, 74.92, Family.METALLOID, 3, 14),
            Element("Selenium", "Se", 34, 78.96, Family.NONMETAL, 3, 15),
            Element("Bromine", "Br", 35, 79.9, Family.HALOGEN, 3, 16),
            Element("Krypton", "Kr", 36, 83.79, Family.NOBLE_GAS, 3, 17),
            Element("Rubidium", "Rb", 37, 85.46, Family.ALKALI_METAL, 4, 0),
            Element("Strontium", "Sr", 38, 87.62,
                    Family.ALKALINE_EARTH_METAL, 4, 1),
            Element("Yttrium", "Y", 39, 88.9, Family.TRANSITION_METAL, 4, 2),
            Element("Zirconium", "Zr", 40, 91.22,
                    Family.TRANSITION_METAL, 4, 3),
            Element("Niobium", "Nb", 41, 92.9, Family.TRANSITION_METAL, 4, 4),
            Element("Molybdenum", "Mo", 42, 95.96,
                    Family.TRANSITION_METAL, 4, 5),
            Element("Technetium", "Tc", 43, 98, Family.TRANSITION_METAL, 4, 6),
            Element("Ruthenium", "Ru", 44, 101.07,
                    Family.TRANSITION_METAL, 4, 7),
            Element("Rhodium", "Rh", 45, 102.9, Family.TRANSITION_METAL, 4, 8),
            Element("Palladium", "Pd", 46, 106.42,
                    Family.TRANSITION_METAL, 4, 9),
            Element("Silver", "Ag", 47, 107.86,
                    Family.TRANSITION_METAL, 4, 10),
            Element("Cadmium", "Cd", 48, 112.41,
                    Family.TRANSITION_METAL, 4, 11),
            Element("Indium", "In", 49, 114.81, Family.METAL, 4, 12),
            Element("Tin", "Sn", 50, 118.71, Family.METAL, 4, 13),
            Element("Antimony", "Sb", 51, 121.76, Family.METALLOID, 4, 14),
            Element("Tellurium", "Te", 52, 127.6, Family.METALLOID, 4, 15),
            Element("Iodine", "I", 53, 126.9, Family.HALOGEN, 4, 16),
            Element("Xenon", "Xe", 54, 131.29, Family.NOBLE_GAS, 4, 17),
            Element("Cesium", "Cs", 55, 132.9, Family.ALKALI_METAL, 5, 0),
            Element("Barium", "Ba", 56, 137.32,
                    Family.ALKALINE_EARTH_METAL, 5, 1),
            Element("Lanthanum", "La", 57, 138.9, Family.LANTHANOID, 8, 2),
            Element("Cerium", "Ce", 58, 140.11, Family.LANTHANOID, 8, 3),
            Element("Praseodymium", "Pr", 59, 140.9, Family.LANTHANOID, 8, 4),
            Element("Neodymium", "Nd", 60, 144.24, Family.LANTHANOID, 8, 5),
            Element("Promethium", "Pm", 61, 145, Family.LANTHANOID, 8, 6),
            Element("Samarium", "Sm", 62, 150.36, Family.LANTHANOID, 8, 7),
            Element("Europium", "Eu", 63, 151.96, Family.LANTHANOID, 8, 8),
            Element("Gadolinium", "Gd", 64, 157.25, Family.LANTHANOID, 8, 9),
            Element("Terbium", "Tb", 65, 158.92, Family.LANTHANOID, 8, 10),
            Element("Dysprosium", "Dy", 66, 162.5, Family.LANTHANOID, 8, 11),
            Element("Holmium", "Ho", 67, 164.93, Family.LANTHANOID, 8, 12),
            Element("Erbium", "Er", 68, 167.25, Family.LANTHANOID, 8, 13),
            Element("Thulium", "Tm", 69, 168.93, Family.LANTHANOID, 8, 14),
            Element("Ytterbium", "Yb", 70, 173.05, Family.LANTHANOID, 8, 15),
            Element("Lutetium", "Lu", 71, 174.96,
                    Family.LANTHANOID, 8, 16),
            Element("Hafnium", "Hf", 72, 178.49,
                    Family.TRANSITION_METAL, 5, 3),
            Element("Tantalum", "Ta", 73, 180.94,
                    Family.TRANSITION_METAL, 5, 4),
            Element("Tungsten", "W", 74, 183.84,
                    Family.TRANSITION_METAL, 5, 5),
            Element("Rhenium", "Re", 75, 186.2, Family.TRANSITION_METAL, 5, 6),
            Element("Osmium", "Os", 76, 190.23, Family.TRANSITION_METAL, 5, 7),
            Element("Iridium", "Ir", 77, 192.21,
                    Family.TRANSITION_METAL, 5, 8),
            Element("Platinum", "Pt", 78, 195.08,
                    Family.TRANSITION_METAL, 5, 9),
            Element("Gold", "Au", 79, 196.96, Family.TRANSITION_METAL, 5, 10),
            Element("Mercury", "Hg", 80, 200.59,
                    Family.TRANSITION_METAL, 5, 11),
            Element("Thallium", "Tl", 81, 204.38, Family.METAL, 5, 12),
            Element("Lead", "Pb", 82, 207.2, Family.METAL, 5, 13),
            Element("Bismuth", "Bi", 83, 208.98, Family.METAL, 5, 14),
            Element("Polonium", "Po", 84, 209, Family.METALLOID, 5, 15),
            Element("Astatine", "At", 85, 210, Family.HALOGEN, 5, 16),
            Element("Radon", "Rn", 86, 222, Family.NOBLE_GAS, 5, 17),
            Element("Francium", "Fr", 87, 223, Family.ALKALI_METAL, 6, 0),
            Element("Radium", "Ra", 88, 226,
                    Family.ALKALINE_EARTH_METAL, 6, 1),
            Element("Actinium", "Ac", 89, 227, Family.ACTINOID, 9, 2),
            Element("Thorium", "Th", 90, 232.03, Family.ACTINOID, 9, 3),
            Element("Protactinium", "Pa", 91, 231.03, Family.ACTINOID, 9, 4),
            Element("Uranium", "U", 92, 238.02, Family.ACTINOID, 9, 5),
            Element("Neptunium", "Np", 93, 237, Family.ACTINOID, 9, 6),
            Element("Plutonium", "Pu", 94, 244, Family.ACTINOID, 9, 7),
            Element("Americium", "Am", 95, 243, Family.ACTINOID, 9, 8),
            Element("Curium", "Cm", 96, 247, Family.ACTINOID, 9, 9),
            Element("Berkelium", "Bk", 97, 247, Family.ACTINOID, 9, 10),
            Element("Californium", "Cf", 98, 251, Family.ACTINOID, 9, 11),
            Element("Einsteinium", "Es", 99, 252, Family.ACTINOID, 9, 12),
            Element("Fermium", "Fm", 100, 257, Family.ACTINOID, 9, 13),
            Element("Mendelevium", "Md", 101, 258, Family.ACTINOID, 9, 14),
            Element("Nobelium", "No", 102, 259, Family.ACTINOID, 9, 15),
            Element("Lawrencium", "Lr", 103, 262,
                    Family.ACTINOID, 9, 16),
            Element("Rutherfordium", "Rf", 104, 267,
                    Family.TRANSITION_METAL, 6, 3),
            Element("Dubnium", "Db", 105, 268, Family.TRANSITION_METAL, 6, 4),
            Element("Seaborgium", "Sg", 106, 271,
                    Family.TRANSITION_METAL, 6, 5),
            Element("Bohrium", "Bh", 107, 272, Family.TRANSITION_METAL, 6, 6),
            Element("Hassium", "Hs", 108, 270, Family.TRANSITION_METAL, 6, 7),
            Element("Meitnerium", "Mt", 109, 276,
                    Family.TRANSITION_METAL, 6, 8),
            Element("Darmstadtium", "Ds", 110, 281,
                    Family.TRANSITION_METAL, 6, 9),
            Element("Roentgenium", "Rg", 111, 280,
                    Family.TRANSITION_METAL, 6, 10),
            Element("Copernicium", "Cn", 112, 285,
                    Family.TRANSITION_METAL, 6, 11),
            Element("Nihonium", "Uut", 113, 284, Family.METAL, 6, 12),
            Element("Flerovium", "Uuq", 114, 289, Family.METAL, 6, 13),
            Element("Moscovium", "Uup", 115, 288,
                    Family.TRANSITION_METAL, 6, 14),
            Element("Livermorium", "Uuh", 116, 293,
                    Family.ALKALINE_EARTH_METAL, 6, 15),
            Element("Tennessine", "Uus", 117, 294, Family.HALOGEN, 6, 16),
            Element("Ognasson", "Uuo", 118, 294, Family.NOBLE_GAS, 6, 17),
        ]

    def printDetailed(self):
        for element in self.elements:
            element.printDetailed()
            print()

    def printCompact(self):
        for element in self.elements:
            element.printCompact()

    def draw(self):
        tk = Tk()
        width = (self.getMaxColumn() + 1) * cellWidth + elementPadding
        height = (self.getMaxRow() + 1) * cellHeight + elementPadding
        canvas = Canvas(tk, width=1000, height=800,
                        background="white", scrollregion=(0, 0, width, height))
        canvas.grid(row=0, column=0)

        # Configure scrollbars.
        scrollX = Scrollbar(tk, orient="horizontal", command=canvas.xview)
        scrollX.grid(row=1, column=0, sticky="ew")
        scrollY = Scrollbar(tk, orient="vertical", command=canvas.yview)
        scrollY.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollY.set,
                         xscrollcommand=scrollX.set)

        for element in self.elements:
            element.draw(canvas)
        tk.mainloop()

    def getMaxRow(self):
        maxRow = self.elements[0].row
        for element in self.elements:
            if element.row > maxRow:
                maxRow = element.row
        return maxRow

    def getMaxColumn(self):
        maxColumn = self.elements[0].column
        for element in self.elements:
            if element.column > maxColumn:
                maxColumn = element.column
        return maxColumn

    def printRows(self):
        for element in self.elements:
            print(element.row)
