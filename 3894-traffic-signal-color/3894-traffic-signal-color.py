class Solution(object):
    def trafficSignal(self, timer):
        if timer <= 90 and timer>30:
            return "Red"
        elif timer == 30:
            return "Orange"
        elif timer==0:
            return "Green"
        else:
            return "Invalid"