# Problem: Remove Sub-Folders from the Filesystem - https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        i=folder[0] if folder[0] != '' and folder[0] != '/' else folder[1]
        ans=[i]
        # while folder:
        for j in range(1,len(folder)):
            if i +'/' not in folder[j][:len(i)+1] and folder[j] != '' and folder[j] != '/':
                ans.append(folder[j])
                i=folder[j]
        return ans
