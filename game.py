

class BaseWeapon(ABC):

    @abstractmethod
    def fire(self):
        raise NotImplementedError

    @abstractmethod
    def reload(self):
        raise NotImplementedError


# Use Base - Initialize
class Weapon(BaseWeapon):
    count = 0

    def __init__(self, view, damage, rate, reload_time, recoil, mag,
                 accuracy,
                 skin):
        self.view = view
        self.damage = damage
        self.rate = rate
        self.reload_time = reload_time
        self.recoil = recoil
        self.max_mag = mag
        self.mag = mag
        self.accuracy = accuracy
        self.skin = skin
        self.__class__.count += 1

    @property
    def dps(self):
        return self.damage * self.rate

    @property
    def can_fire(self):
        if self.mag == 0:
            return False
        else:
            return True

    def fire(self):
        if self.can_fire:
            self.mag -= 1
            print("in mag :  ", self.mag)
            return None
        print("Weapon is not firing,empty mag,reload!!!!!")

    def reload(self):
        print("reloading weapon...")
        time.sleep(self.reload_time)
        self.mag = self.max_mag
        print(f"reloaded to max cap {self.max_mag}")


class Gun(Weapon):  # inheritance
    def __init__(self, view, damage, rate, reload_time, recoil, mag,
                 accuracy,
                 skin, extensions):
        super(Gun, self).__init__(view, damage, rate, reload_time, recoil, mag, accuracy, skin)
        self.extensions = extensions
        self.trigger = None
        self.scope = None
        self.laser = None
        self.grip = None
        if extensions is not None:
            for ext in extensions:
                if ext.type == "trigger":
                    self.trigger = ext.option
                    self.rate *= ext.option
                elif ext.type == "scope":
                    self.scope = ext.option
                    self.view *= ext.option
                elif ext.type == "grip":
                    self.grip = ext.option
                    self.accuracy *= ext.option
                elif ext.type == "mag_new":
                    self.mag_new = ext.option
                    self.max_mag *= ext.option
                elif ext.type == "laser":
                    self.laser = ext.option
                    self.accuracy *= ext.option


class Sniper(Gun):
    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions):
        super(Sniper, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class M21(Sniper):
    view = 2
    damage = 200
    rate = 0.2
    reload_time = 4
    recoil = 10
    mag = 10
    accuracy = 80
    skin = "Black"
    mag_count = 2

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(M21, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Awm(Sniper):
    view = 4
    damage = 250
    rate = 0.1
    reload_time = 6
    recoil = 20
    mag = 5
    accuracy = 99
    skin = "Black"
    mag_count = 2

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Awm, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Smg(Gun):
    pass


class P90(Smg):
    view = 1
    damage = 40
    rate = 3
    reload_time = 3
    recoil = 5
    mag = 25
    accuracy = 40
    skin = "Black"
    mag_count = 4

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(P90, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Mp5(Smg):
    view = 1
    damage = 35
    rate = 2
    reload_time = 3.5
    recoil = 15
    mag = 20
    accuracy = 50
    skin = "Black"
    mag_count = 3

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Mp5, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Rifle(Gun):
    pass


class M4(Rifle):
    view = 1.2
    damage = 60
    rate = 2
    reload_time = 5
    recoil = 20
    mag = 30
    accuracy = 60
    skin = "Black"
    mag_count = 4

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(M4, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class AK47(Rifle):
    view = 1.2
    damage = 69
    rate = 1.8
    reload_time = 5.5
    recoil = 25
    mag = 30
    accuracy = 75
    skin = "Black"
    mag_count = 3

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(AK47, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Shotgun(Gun):
    pass


class Spass(Shotgun):
    view = 0.8
    damage = 80
    rate = 0.5
    reload_time = 12
    recoil = 80
    mag = 7
    accuracy = 20
    skin = "Black"
    mag_count = 3

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Shotgun, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Remington(Shotgun):
    view = 0.9
    damage = 70
    rate = 0.7
    reload_time = 8
    recoil = 65
    mag = 10
    accuracy = 35
    skin = "Black"
    mag_count = 3

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Shotgun, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Pistol(Gun):
    pass


class Glock(Pistol):
    view = 1
    damage = 20
    rate = 2
    reload_time = 2
    recoil = 15
    mag = 12
    accuracy = 25
    skin = "Black"
    mag_count = 3

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Pistol, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Dessert(Pistol):
    view = 1
    damage = 50
    rate = 1
    reload_time = 4
    recoil = 45
    mag = 5
    accuracy = 80
    skin = "Black"
    mag_count = 2

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Pistol, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class P11(Pistol):
    view = 0.5
    damage = 30
    rate = 1.5
    reload_time = 2
    recoil = 15
    mag = 16
    accuracy = 15
    skin = "Black"
    mag_count = 3

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Pistol, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Blade(Weapon):  # inheritance

    @property
    def can_fire(self):
        return True

    def fire(self):  # polymorphism
        print("slash!!!!!!!!")

    def reload(self):
        return True


class Karambit(Blade):
    view = 1
    damage = 200
    rate = 1
    reload_time = 1
    recoil = 100
    mag = 1
    accuracy = 100
    skin = "Black"
    mag_count = 1

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Karambit, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


class Military(Blade):
    view = 1
    damage = 150
    rate = 1
    reload_time = 1
    recoil = 90
    mag = 1
    accuracy = 90
    skin = "Black"
    mag_count = 1

    def __init__(self, view, damage, rate, recoil, mag, accuracy, skin, extensions=None):
        super(Military, self).__init__(view, damage, rate, recoil, mag, accuracy, skin, extensions)


# class Item(ABC):
#     @abstractmethod
#     def use(self):
#         raise NotImplementedError
#
#
# class Lethal(Item):
#     pass
#
#
# class Grenade(Lethal):
#     pass
#
#
# class NonLethal(Item):
#     pass
#
#
# class Smoke(NonLethal):
#     pass
#
#
# class Flash(NonLethal):
#     pass
#
#
# class Gear(Item):
#     pass
#
#
# class Shield(Gear):
#     pass
#
#
# class Helmet(Gear):
#     pass
#
#
# class Extension(Item):
#     pass
#
#
# class Trigger(Extension):
#     pass
#
#
# class TriggerGood(Trigger):
#     type = "trigger"
#     option = 1.1
#
#
# class TriggerBest(Trigger):
#     type = "trigger"
#     option = 1.3
#
#
# class Scope(Extension):
#     pass
#
#
# class Scope2x(Scope):
#     type = "scope"
#     option = 2
#
#
# class Scope4x(Scope):
#     type = "scope"
#     option = 4
#
#
# class Laser(Extension):
#     pass
#
#
# class LaserGood(Laser):
#     type = "laser"
#     option = 1.1
#
#
# class LaserBest(Laser):
#     type = "laser"
#     option = 1.3
#
#
# class Grip(Extension):
#     pass
#
#
# class GripGood(Grip):
#     type = "grip"
#     option = 1.1
#
#
# class GripBest(Grip):
#     type = "grip"
#     option = 1.3
#
#
# class MagNew(Extension):
#     pass
#
#
# class MagHalf(MagNew):
#     type = "mag"
#     option = 1.5
#
#
# class MagDouble(MagNew):
#     type = "mag"
#     option = 2

# Sniper -> Awp, M24
# Pistol -> P11, Dissert
# Extension -> Laser, Scope, Silencer
# Assault Rifle -> M416 - Ak47
# Extension -> Laser, Scope, Silencer
# Blade -> Knife
# Extension -> KnifeColor
# Item -> Smoke, Flash, Grenade, Shield, Helmet
