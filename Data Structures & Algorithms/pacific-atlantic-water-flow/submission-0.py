class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # To know if water can flow into both the pacific and atlantic, we have to first know
        # What does it means to be able to flow to the pacific or to be the atlantic?
        # This is basically if we hit one of the ends.

        # Asfar as an approach to the problem, my first thought is to do a DFS exploration
        # If you think about the water flowing through the islands, it will act like its in a maze
        # So with this in mind, can start from every cell, and check all 4 directions and keep exploring breadth-wise.
        # If we meet a value that is strictly bigger, we have hit a wall so that cell is useless in our current search.\

        output = set()
        visited = set()

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def canFlow(row, col, maxSoFar):
            if (
                row < 0 or row >= len(heights) or # Out of bounds
                col < 0 or col >= len(heights[0]) or  # Out of bounds
                (row, col) in visited or # Already seen in this iteration of bounds
                heights[row][col] > maxSoFar # Is incompatible cell
            ): return (False, False)

            # Mark me as visited as I want to start exploring
            visited.add((row, col))

            # Each cell should report whether it can hit the atlantic (Last row/col) 
            # or if it can hit the pacific(First row/col)
            atlantic = row == len(heights) - 1 or col == len(heights[0]) - 1
            pacific = row == 0 or col == 0

            canNeighborFlowToAtlantic, canNeighborFlowToPacific = False, False
            for nr, nc in neighbors:
                # Once we find a neighbor that hit one of the oceans, update that
                a, p = canFlow(row+nr, col+nc, heights[row][col])

                if a: canNeighborFlowToAtlantic = True
                if p: canNeighborFlowToPacific = True

            # Combine what I can reach directly with what my neighbors can reach
            atlantic = atlantic or canNeighborFlowToAtlantic
            pacific = pacific or canNeighborFlowToPacific

            # If I have any 2 neighbors such that one can flow to pacific and the other to atlantic
            if atlantic and pacific: output.add((row, col))
                
            # Remove me from visited incase another cell has to explore me during its search
            visited.remove((row, col))

            # Return whether I can hit the atlantic or the pacific
            return (atlantic, pacific)

        for r in range(len(heights)):
            for c in range(len(heights[r])):

                # If we hit a cell that we already know can flow to both atlantic and pacific, we can skip that cell
                if (r, c) in output: continue
                canFlow(r, c, float('inf'))

        return list(output)