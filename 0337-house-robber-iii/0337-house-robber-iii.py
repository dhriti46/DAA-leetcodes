
class Solution(object):
    def rob(self, root):
        def solve(node):
            if not node:
                return (0, 0)

            left = solve(node.left)
            right = solve(node.right)

            rob_current = node.val + left[1] + right[1]

            skip_current = max(left) + max(right)

            return (rob_current, skip_current)

        return max(solve(root))       