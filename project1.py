from search import Problem, depth_first_graph_search, breadth_first_graph_search

class MissCannibals(Problem):
    def __init__(self, M=3, C=3, goal=(0, 0, False)):
        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    def actions(self, state):
        m, c, onLeft = state
        possible_actions = ['MM', 'MC', 'CC', 'M', 'C']
        valid_actions = []

        for action in possible_actions:
            m_change = action.count('M')
            c_change = action.count('C')

            if onLeft:
                new_m = m - m_change
                new_c = c - c_change
            else:
                new_m = m + m_change
                new_c = c + c_change

            if new_m < 0 or new_c < 0 or new_m > self.M or new_c > self.C:
                continue

            if new_m > 0 and new_m < new_c:
                continue

            right_m = self.M - new_m
            right_c = self.C - new_c
            if right_m > 0 and right_m < right_c:
                continue

            valid_actions.append(action)

        return valid_actions

    def result(self, state, action):
        m, c, onLeft = state
        m_change = action.count('M')
        c_change = action.count('C')

        if onLeft:
            return (m - m_change, c - c_change, False)
        else:
            return (m + m_change, c + c_change, True)

###########################################################################

if __name__ == '__main__':
    mc = MissCannibals(M=3, C=3)

    result = depth_first_graph_search(mc)
    if result:
        print("Depth First Graph Search Solution:", result.solution())
    else:
        print("Error: No DFS solution found.")

    result = breadth_first_graph_search(mc)
    if result:
        print("Breadth First Graph Solution:", result.solution())
    else:
        print("Error: No BFS solution found.")
