class SweetPotatoPie(object):
    def __init__(self,cooked, pie_left,cut_pie):
        self.food = True
        self.sweet = True
        self.cooked = cooked
        self.pie_left = pie_left
        self.cut_pie = cut_pie
        self.pan = 1

    def cut_pie (self, eat):
        self.pie_left += eat
        if self.pie_left > 100:
            self.pie_left = 100

    def get_pie(self,):
        if not self.pan

