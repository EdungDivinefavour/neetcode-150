class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Your first thought here might be backtracking, and that could work. But I think we can do this without any recursion at all
        # Basically we can build the combinations one digit at a time. For every combination we have so far, we add each letter of the next digit on the end
        # So if we have ["a", "b", "c"] and the next digit is 3(def), each element would turn into 3 new guys and we now have 9
        
        # If we don't have any digits, there's no need to do anything. We can just return nothing. Without this the loop below would give us [""] which is wrong
        if not digits: return []

        charMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        # We can build our 2D array of all the letter formed by the digits we were given eg 23 will be [ [abc], [def] ]
        groups = [charMap[d] for d in digits]

        # Start with one empty combination
        # The first group needs something to attach its letters to. If we started with an empty list there would be nothing to loop over and we would never build anything
        combinations = [""]

        for group in groups:
            # We can't add to combinations while we are looping through it, so we will collect the next round in a new list
            new_combinations = []

            # No we will take every combination we have so far and extend it with every letter of this digit
            for comb in combinations:
                for char in group:
                    new_combinations.append(comb + char)

            # At this point, we are done with this digit, so the new combinations are what we extend with the next digit
            combinations = new_combinations

        return combinations