class noninteger:
    def NSteps (self, num: int) -> int:
        steps = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -=1
            steps += 1
        return steps

answer = noninteger()
print(answer.NSteps(14))
