"""
agent.py:
Class for agents.
"""

class Agent:

    def __init__(self, s_x, s_y, g_x, g_y, priority): 
        self.s_x = s_x
        self.s_y = s_y
        self.g_x = g_x
        self.g_y = g_y
        self.priority = priority
