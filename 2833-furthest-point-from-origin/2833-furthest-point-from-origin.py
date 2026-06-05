class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        lef=0
        rig=0
        mid=0
        for i in moves:
            if i=="L":
                lef+=1
            elif i=="R":
                rig+=1
            else:
                mid+=1
        return abs(lef-rig)+mid

       
        