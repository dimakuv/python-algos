# quick & dirty implementation of the non-recursive DFS
#   based on: http://dave.dkjones.org/posts/2014/nonrecursive-dfs.html

class Vertex(object):
    __slots__ = ['pre', 'post', 'value']

def DFS(edges, s):
    stack = [s]
    while len(stack):
        v = stack.pop()
        if v.post: # stage 3: after postprocessing, skip
            continue
        if v.pre:  # stage 2: after preprocessing, do postprocessing
            # in this example, we calculate sums of subtrees
            value = 0
            for u in edges[v]:
                if u.post == False: continue # is it parent?
                value += u.value
            v.value += value
            v.post = True
            continue
        # stage 1: before preprocessing, put both me and my children in stack
        stack.append(v)
        v.pre = True
        for u in edges[v]:
            if u.pre == True: continue # already visited?
            stack.append(u)
