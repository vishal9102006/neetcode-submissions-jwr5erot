class Solution:
    def carFleet(self, target, position, speed):
        # Combine position and speed
        cars = list(zip(position, speed))

        # Sort cars from closest to target to farthest
        cars.sort(reverse=True)

        fleets = 0
        last_time = 0

        for pos, spd in cars:
            # Time needed to reach target
            time = (target - pos) / spd

            # If this car takes longer, it cannot catch the fleet ahead
            if time > last_time:
                fleets += 1
                last_time = time

        return fleets