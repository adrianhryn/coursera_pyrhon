from abc import ABC, abstractmethod


class AbstractEffect(ABC):

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass

    @abstractmethod
    def remove_effect(self, buff, name):
        pass


class Hero(AbstractEffect):
    def __init__(self):
        self.positive_effects = []
        self.positive_list = ['Berserk', 'Blessing']
        self.negative_effects = []
        self.negative_list = ['Weakness', 'Curse', 'EvilEye']

        self.stats = {
            "HP": 128,
            "MP": 42,
            "SP": 100,

            "Strength": 15,
            "Perception": 4,
            "Endurance": 8,
            "Charisma": 2,
            "Intelligence": 3,
            "Agility": 8,
            "Luck": 1
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()

    def remove_effect(self, buff, name):
        """
        Checks on name, if removing effect name is correct, remove an effect on hero
        """
        if name == "Berserk":
            # remove the Berserk effect(name) from a positive effects list, but only once!
            for i in buff.positive_effects:
                if i == "Berserk":
                    buff.positive_effects.pop(buff.positive_effects.index(i))
                    break
            # remove all Berserk effects from hero stats
            for i in ["Strength", "Luck", "Agility", "Endurance"]:
                self.stats[i] = self.stats[i] - 7

            for i in ["Perception", "Charisma", "Intelligence"]:
                self.stats[i] = self.stats[i] + 3

        # the same as with Berserk effect
        if name == "Curse":
            for i in buff.negative_effects:
                if i == "Berserk":
                    buff.negative_effects.pop(buff.negative_effects.index(i))
                    break

            for i in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
                self.stats[i] = self.stats[i] + 2


class AbstractPositive(AbstractEffect):
    """
    Lists all function that should be in positive effect buffs
    Use all functions from the last objects
    """

    def __init__(self, obj):
        self.obj = obj

    def get_positive_effects(self):
        return self.obj.get_positive_effects()

    def get_negative_effects(self):
        return self.obj.get_negative_effects()

    def get_stats(self):
        return self.obj.get_stats()

    def remove_effect(self, buff, name):
        return self.obj.remove_effect(buff, name)


class AbstractNegative(AbstractEffect):
    """
    Same as with AbstractPositive
    """

    def __init__(self, obj):
        self.obj = obj

    def get_positive_effects(self):
        return self.obj.get_positive_effects()

    def get_negative_effects(self):
        return self.obj.get_negative_effects()

    def get_stats(self):
        return self.obj.get_stats()

    def remove_effect(self, buff, name):
        return self.obj.remove_effect(buff, name)


class Berserk(AbstractPositive):
    """
    Describes Berserk buff. The constructor initialize all changes to hero stats
    """

    def __init__(self, obj):
        AbstractPositive.__init__(self, obj)
        self.stats = self.obj.stats
        self.negative_effects = self.obj.get_negative_effects()
        self.positive_effects = self.obj.get_positive_effects()

        for i in ["Strength", "Luck", "Agility", "Endurance"]:
            self.stats[i] = self.stats[i] + 7

        for i in ["Perception", "Charisma", "Intelligence"]:
            self.stats[i] = self.stats[i] - 3

        self.positive_effects.append("Berserk")

    def get_positive_effects(self):
        return self.positive_effects


class Blessing(AbstractPositive):
    """
    Describes Blessing buff. The constructor initialize all changes to hero stats
    """

    def __init__(self, obj):
        AbstractPositive.__init__(self, obj)
        self.stats = self.obj.stats
        self.negative_effects = self.obj.get_negative_effects()
        self.positive_effects = self.obj.get_positive_effects()

        for i in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
            self.stats[i] = self.stats[i] + 2

        self.positive_effects.append("Blessing")

    def get_positive_effects(self):
        return self.positive_effects


class Weakness(AbstractNegative):
    """
    Describes Weakness buff. The constructor initialize all changes to hero stats
    """

    def __init__(self, obj):
        AbstractNegative.__init__(self, obj)
        self.stats = self.obj.stats
        self.negative_effects = self.obj.get_negative_effects()
        self.positive_effects = self.obj.get_positive_effects()

        for i in ["Strength", "Agility", "Endurance"]:
            self.stats[i] = self.stats[i] - 4

        self.negative_effects.append("Weakness")

    def get_negative_effects(self):
        return self.negative_effects


class Curse(AbstractNegative):
    """
    Describes Curse buff. The constructor initialize all changes to hero stats
    """

    def __init__(self, obj):
        AbstractNegative.__init__(self, obj)
        self.stats = self.obj.stats
        self.negative_effects = self.obj.get_negative_effects()
        self.positive_effects = self.obj.get_positive_effects()

        for i in ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]:
            self.stats[i] = self.stats[i] - 2

        self.negative_effects.append('Curse')

    def get_negative_effects(self):
        return self.negative_effects


class EvilEye(AbstractNegative):
    """
    Describes EvilEye buff. The constructor initialize all changes to hero stats
    """

    def __init__(self, obj):
        AbstractNegative.__init__(self, obj)
        self.stats = self.obj.stats.copy()
        self.negative_effects = self.obj.get_negative_effects()
        self.positive_effects = self.obj.get_positive_effects()

        self.stats["Luck"] = self.stats["Luck"] - 10

        self.negative_effects.append("EvilEye")

    def get_negative_effects(self):
        return self.negative_effects


if __name__ == "__main__":
    # checks on train inputs from Coursera
    hero = Hero()
    assert (hero.get_stats() == {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8,
                         'Charisma': 2, 'Intelligence': 3,'Agility': 8, 'Luck': 1})
    assert(hero.stats == {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 15, 'Perception': 4, 'Endurance': 8,
                         'Charisma': 2, 'Intelligence': 3, 'Agility': 8, 'Luck': 1})

    assert(hero.get_negative_effects() == [])
    assert(hero.get_positive_effects() == [])

    brs1 = Berserk(hero)
    assert(brs1.get_stats() == {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 22, 'Perception': 1, 'Endurance': 15, 'Charisma': -1,'Intelligence': 0, 'Agility': 15, 'Luck': 8})
    assert(brs1.get_negative_effects() == [])
    assert(brs1.get_positive_effects() == ['Berserk'])

    brs2 = Berserk(brs1)
    cur1 = Curse(brs2)
    assert(cur1.get_stats() == {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 27, 'Perception': -4, 'Endurance': 20,
                                'Charisma': -6, 'Intelligence': -5, 'Agility': 20, 'Luck': 13})
    assert(cur1.get_positive_effects() == ['Berserk', 'Berserk'])
    assert(cur1.get_negative_effects() == ['Curse'])

    cur1.remove_effect(cur1, "Berserk")
    assert(cur1.get_stats() == {'HP': 128, 'MP': 42, 'SP': 100, 'Strength': 20, 'Perception': -1, 'Endurance': 13, 'Charisma': -3, 'Intelligence': -2, 'Agility': 13, 'Luck': 6})

    assert (cur1.get_positive_effects() == ['Berserk'])
    assert(cur1.get_negative_effects() == ['Curse'])

