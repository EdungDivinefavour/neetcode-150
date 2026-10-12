class PrefixTree:

    # The idea behind a trie is that we will store one character per level, and any words that start the same way will then end up sharing the same path.. 
    # So "apple" and "app" will walk through the exact same nodes until they part ways
    # The great thing about this is that looking up anything will only ever cost us the length of the word, no matter how many words we have stored

    def __init__(self):
        # Every node is really just a map of character which then points to whatever node is below it
        # We are starting with one empty node at the top that doesn't belong to any character, so every word will continue off of it
        self.trie = {"": {}}
        

    def insert(self, word: str) -> None:
        curr = self.trie[""]

        for c in word:
            # If nothing has ever gone down this character before, then we will have to create the node for it
            # Notice we are only creating it when it is missing, because if we created it every time we would end up
            # wiping out every other word that was already sharing this path
            if curr.get(c) == None:
                curr[c] = {"isEnd": False}
            
            curr = curr[c] # We need to step down into that character's node so we can carry on from there
            
        # At this point, we have run out of characters, so whatever node we are standing on is where this word ends
        # We have to mark it as an end, because without this flag there would be no way to tell a real word from a path we just happened to pass through
        # ie inserting "apple" will walk us through "app" but "app" itself is not a word yet
        curr["isEnd"] = True


    def search(self, word: str) -> bool:
        curr = self.trie[""]

        for c in word:
            # If the word was previously stored, then we will never run into this scenario where the key does not exist.
            # Meaning if this ever happened, the word was never inserted in the first place
            if not curr.get(c): return False
            
            curr = curr[c]
            
        # We managed to walk the whole word, but that on its own doesn't really make it a word.. 
        # We might have just landed somewhere in the middle of a longer one. So the flag is what actually answers the question for us
        return curr["isEnd"]
        
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.trie[""]

        for c in prefix:
            if not curr.get(c): return False
        
            curr = curr[c]
        
        # This is the same walk as search, except that here we don't really care about the flag at all
        # Getting to the end of the path is our proof that this is a prefix! If it wasn't we would have returned much earlier
        return True