class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Our last solution technically works, but is too inefficient
        # We are repeating a lot of work.. A cell we saw during one traversal and had already computed, will be revisited again if its a neighbor of another cell
        # What if we reverse the question and instead flow from the oceans into the cells?
        # That way, we can flow from atlantic to the other end and store the cells we could flow to, and then from pacific to the other end and store those
        # Any cells that is contained in both of these results is indeed one that can flow to both

        # This then turns our approach into a multisource BFS
        atlantic, pacific = deque(), deque()
        for r in range(len(heights)):
            for c in range(len(heights[r])):
                # If it is the first row or first column, it is bordering the pacific
                if r == 0 or c == 0: 
                    pacific.append((r, c))

                # If it is the last row or last column it is bordering the atlantic
                if r == len(heights) - 1 or c == len(heights[r]) - 1: 
                    atlantic.append((r, c))

        def flowFromOcean(ocean):
            visited, res = set(), set()

            while ocean:
                for _ in range(len(ocean)):
                    r, c  = ocean.popleft()

                    # If I was in this queue, I could flow from the ocean, so add me to the result
                    res.add((r, c))


                    # Spread to all 4 'valid' neighbors
                    neighbors = [(r, c-1), (r, c+1), (r-1, c), (r+1, c)]
                    for nr, nc in neighbors:
                        if (
                            nr < 0 or nr >= len(heights) or # Is an invalid row
                            nc < 0 or nc >= len(heights[0]) or # Is an invalid column
                            (nr, nc) in visited or
                            # If we were flowing from the cells to the ocean, a valid flow path would be from higher to lower
                            # But because we are flowing in reverse, we will be able to traverse from equal or greater heights so anything < me is an invalid path
                            heights[nr][nc] < heights[r][c]
                        ): continue
                        
                        # Add me to the queue
                        ocean.append((nr, nc))
                        
                        # Then mark me as visited
                        visited.add((nr, nc))

            return res

        # Flow from atlantic to the other end, then flow from pacific to the other end
        resA, resP = flowFromOcean(atlantic), flowFromOcean(pacific)

        # Return the cells that we could reach from both atlantic and pacific
        return list((resA & resP))
