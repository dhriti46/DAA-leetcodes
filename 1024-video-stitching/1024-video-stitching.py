
class Solution(object):
    def videoStitching(self, clips, time):
        clips.sort()

        count = 0
        current_end = 0
        farthest = 0
        i = 0

        while current_end < time:
            while i < len(clips) and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1

            if farthest == current_end:
                return -1

            count += 1
            current_end = farthest

        return count