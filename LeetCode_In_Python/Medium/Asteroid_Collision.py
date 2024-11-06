class Solution:
    def asteroidCollision(self, asteroids) :
        stack = []

        for asteroid in asteroids:
            if stack:
                previous = stack.pop()
                while True:
                    if (previous < 0 and asteroid < 0) or (previous > 0 and asteroid > 0) or (previous < 0 and asteroid > 0):
                        stack.append(previous)
                        stack.append(asteroid)
                        break

                    if previous > 0 and asteroid < 0:
                        if abs(previous) > abs(asteroid):
                            stack.append(previous)
                            break
                        elif abs(previous) < abs(asteroid):

                            if stack:
                                previous = stack.pop()
                            else:
                                stack.append(asteroid)
                                break
                        else:
                            break
                    
                    
            else:
                stack.append(asteroid)

        return stack