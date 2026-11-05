class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        
        # i
        # initial power
        # score of 0
        # bag of tokens
        # maximize the total score
        # playing these tokens
        # 1 move -> 2 ways
        # face-up: >= tokens[i] ->
        # losing tokens[i] +1
        # face-down: >= 1 ->
        # gaining tokens[i] power
        # losing 1 score

        # o
        # maximum possible score

        # c
        # len(tokens) >= 0 <= 1000
        # tokens[i], power >= 0 <= 10^4

        # e
        # len(tokens) == 0
        # len(tokens) == 1
        score = 0

        if len(tokens) == 0:
            return score

        left = 0
        right = len(tokens) - 1

        tokens.sort()

        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1

            else:
                if score <= 0:
                    # gisei surukoto dekin
                    break
                
                else:
                    # score > 0
                    # gisei suru
                    if left == right:
                        break
                    score -= 1
                    power += tokens[right]
                    right -= 1

        return score