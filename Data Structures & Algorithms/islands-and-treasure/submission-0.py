class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:

        rows,cols=len(rooms),len(rooms[0])
        vis=set()
        q=deque()

        def addrom(r,c):
            if (r<0 or r==rows or c<0 or c==cols or (r,c) in vis or rooms[r][c]==-1):
                return
            vis.add((r,c))
            q.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c]==0:
                    q.append([r,c])
                    vis.add((r,c))
        dis=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                rooms[r][c]=dis
                addrom(r+1,c)
                addrom(r-1,c)
                addrom(r,c+1)
                addrom(r,c-1)

            dis+=1

        
