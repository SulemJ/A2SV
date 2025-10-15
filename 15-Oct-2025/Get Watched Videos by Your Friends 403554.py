# Problem: Get Watched Videos by Your Friends - https://leetcode.com/problems/get-watched-videos-by-your-friends/description/

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n=len(friends)
        visited = set([id])
        pq= deque([id])
        curLevel =0

        while pq and curLevel < level:
            for _ in range(len(pq)):
                person = pq.popleft()
                for f in friends[person]:
                    if f not in visited:
                        visited.add(f)
                        pq.append(f)
            curLevel+=1
        
        vid=[]
        for person in pq:
            vid.extend(watchedVideos[person])

        freq = Counter(vid)
        res = sorted(freq.keys(), key=lambda x: (freq[x], x))

        return res