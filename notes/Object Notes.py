import Special_Random


class Phone(object):
    def __init__(self, carrier, change_left = 50):
        # There are attributes that a phone has
        # There should all be relevant to our program
        self.screen = True
        self.camera = 2
        self.mircophone = True
        self.carrier = carrier
        self.battery_left = change_left

    def charge(self, time):
        self.battery_left += time
        if self.battery_left > 100:
            self.battery_left = 100

    def makecall(self,duration):
        if not self.screen:
            print("You can't make a phone call.")
            print("Your screen is broken.")
            return
        battery_loss_per_minute = 1
        self.battery_left -= duration * battery_loss_per_minute
        if self.battery_left < 0:
            self.battery_left = 0
            print("Your phone dies during the conversation")
        elif self.battery_left == 0:
            print("Your phone dies at the end of the conversation")
        else:
            print("You successfully make the phone call")
            print("Your phone is now at %s" % self.battery_left)

    def smash_phone(self):
        print("SMASH!!!!!!!!!!!!!!")
        print("It broke.")
        self.screen = False


my_phone = Phone ("ATT", 100)
your_phone = Phone("Bell")
default_phone = Phone ("Verizon")

my_phone.makw_call(60)
my_phone.makw_call(10)
my_phone.charge(100)
my_phone.makw_call(10)
your_phone.smash_phone()
your_phone.makw_call(1)


print(Special_Random.RandomCaleb.myrandom())