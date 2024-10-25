class Clock:

    # Constructor - time is 0 by default
    def __init__(self, time = 0):
        self.time = time
        self.is_stopped = True

    # increases time by one
    def tick(self):
        if self.is_stopped == False:
            self.time += 1

    # Different transitions
    # (with and without reset and for exact transition the time has to exactly match the duraction, in order for it to return true and not just to be greater or equal than)
    def transition(self, duration):
        if self.time >= duration:
            self.time = 0
            return True
        return False
    def transition_without_reset(self, duration):
        if self.time >= duration:
            return True
        return False
    def exact_transition(self, duration):
        if self.time == duration:
            return True
        return False

    # resets the time
    def reset(self):
        self.time = 0

    # Clock cant be stopped and started again
    def stopp(self):
        self.is_stopped = True
    def start(self):
        self.is_stopped = False
