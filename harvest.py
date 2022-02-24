############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = [] # not part of the _init_ arguments

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code

    # def __repr__(self):
    #     return f"MeloneType code = {self.code}"  # finish f string later


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType("musk", 1998,"green",True, True, "Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)
    
    casaba = MelonType("cas", 2003 , "orange",False, False, "Casaba")
    casaba.add_pairing("strawberries")
    casaba.add_pairing("mint")
    all_melon_types.append(casaba)
    
    crenshaw = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    crenshaw.add_pairing("prosciutto")
    all_melon_types.append(crenshaw)

    yellow_watermelon = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yellow_watermelon.add_pairing("ice_cream")
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

# test1 = MelonType(1,2,3,4,5,6)
# test1.add_pairing("milk")
# print(test1.pairings)
# test1.update_code(0)
# print(test1.code)

# print(make_melon_types())

melon_types = make_melon_types()
# print(melon_types)

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    #melone_types: a list of melone types
    for melon in melon_types:
        melon_pairings = "\n-".join(melon.pairings)
        print(f"{melon.name} pairs with \n-{melon_pairings}")
        # print approach #2
        # print(#melon name pairs with)
        # for pairing in melon_pairings:
        #     print(pairing)

        # print(f"{melon.name} pairs with \n-{"\n-".join(melon.pairings)}") #doesn't work
    # Fill in the rest

# print_pairing_info(melon_types)

# print("\n -".join(["a","b","c"]))
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # all_melon_types = make_melon_types()
    # dict_melon_types = {"musk":muskmelon,"yw":yellow_watermelon}
    dict_code_melontype = {}

    for melon_type in melon_types:
        dict_code_melontype[melon_type.code] = melon_type
    return dict_code_melontype
        
# print(make_melon_type_lookup(melon_types))

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""
    def __init__(self,melon_type,shape_rating,color_rating,field_num,harvester):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating=color_rating
        self.field_num=field_num
        self.harvester = harvester
        # self.is_sellable = self.is_sellable()
        
    def is_sellable(self):
        """sellable: if both its shape and color ratings are greater than 5,and it did not come from field 3."""
        return self.shape_rating > 5 and self.color_rating > 5 and self.field_num !=3

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons = []

    # XXX = Melon(melon_type,shape_rating,color_rating,field_num,harvester)
    # all_melon_types.append(xxx)

    melon_1 = Melon("yw", 8, 7, 2, "Sheila")
    melon_2 = Melon("yw", 3, 4, 2, "Sheila")
    melon_3 = Melon("yw", 9, 8, 3, "Sheila")
    melon_4 = Melon("cas", 10, 6, 35, "Sheila")
    melon_5 = Melon("cren", 8, 9, 35, "Michael")
    melon_6 = Melon("cren",8,2,35,"Michael")
    melon_7 = Melon("cren",2,3,4,"Michael")
    melon_8 = Melon("musk",6,7,4,"Michael")
    melon_9 = Melon("yw",7,10,3,"Sheila")

    melons.append(melon_1)
    melons.append(melon_2)
    melons.append(melon_3)
    melons.append(melon_4)
    melons.append(melon_5)
    melons.append(melon_6)
    melons.append(melon_7)
    melons.append(melon_8)
    melons.append(melon_9)

    return melons

melons = make_melons(melon_types)

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
# Harvested by Sheila from Field 2 (CAN BE SOLD)
# Harvested by Sheila from Field 2 (NOT SELLABLE)
    for melon in melons:
        if melon.is_sellable():
            print(f"Harvested by {melon.harvester} from Field {melon.field_num} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvester} from Field {melon.field_num} (NOT SELLABLE)")
        
get_sellability_report(melons)