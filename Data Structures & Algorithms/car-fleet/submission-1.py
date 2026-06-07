class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        ans = 0
        max_turns = -1
        for i in range(len(position)):
            cur_position = position[i]
            cur_speed = speed[i]
            cars.append((cur_position,cur_speed))
        cars.sort(reverse = True) # sort by descending order
        for position, speed in cars:
            turns = (target - position) / speed
            if turns > max_turns:
                max_turns = turns
                ans += 1
        return ans
        

