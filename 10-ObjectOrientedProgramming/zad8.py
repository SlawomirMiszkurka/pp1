class Tv:
    is_on=False
    def __init__(self):
        pass
    def show_status(self):
        if self.is_on==True:
            print('TV is on')
        else:
            print('TV if off')
    def turn_on(self):
        self.is_on=True
    def turn_off(self):
        self.is_on=False
TV=Tv()
TV.show_status()
TV.turn_on()
TV.show_status()
TV.turn_off()
TV.show_status()