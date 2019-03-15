class Gun(object):
    def __init__(self, clips_left):
        self.aim = True
        self.in_clip = 30
        self.clips_left = clips_left
        self.trigger = True
        self.carrier = True

    def reload(self):
        if self.clips_left > 0:
            self.in_clip = 30
            self.clips_left -= 1

    def shoot(self, ammo):
        if ammo <= 0:
            print("You don't have any ammo in the clip")
            print("your trigger is jammed")
            return
        bullet_loss_per_shot = 3
        self.in_clip -= (ammo * bullet_loss_per_shot)
        if self.in_clip <= 0:
            self.in_clip = 0
            print("There's no ammo in the clip")
        elif self.clips_left == 0:
            print("You ain't got anymore bullets after you killed him")
        else:
            print("You killed him")
            print("You have this much ammo, %d" % ammo)

    def throw_gun(self):
        print("AHHHHHH!!!")
        print("it had less ammo then I had last time")
        self.carrier = False


our_gun = Gun("AN47",)
other_gun = Gun("TAC-2", )
regular_gun = Gun("Mac_10")

our_gun.shoot(3)
our_gun.shoot(30)
# our_gun.clip_left(30)
our_gun.shoot(5)
other_gun.throw_gun()
other_gun.shoot(3)
