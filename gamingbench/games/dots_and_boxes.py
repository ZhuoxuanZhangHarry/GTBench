import copy
from gamingbench.games.openspiel_adapter import OpenSpielGame
import re

class DotsAndBoxes(OpenSpielGame):
    def __init__(self) -> None:
        super().__init__("dots_and_boxes")
        self.game_name = 'dots_and_boxes'

    def openspiel_action_to_agent(self, action):
        # Convert action strings into the coordinate format <A1−B1> or <A1−A2>
        formatted_actions = []
        for a in action:
            # Extract orientation and coordinates using regex
            match = re.match(r'P\d+\((h|v),(\d+),(\d+)\)', a)
            if match:
                orientation = match.group(1)
                row = int(match.group(2))
                col = int(match.group(3))

                if orientation == 'h':
                    # Horizontal line, so increase column by one for the second coordinate
                    start = f'{chr(65 + col)}{row + 1}'
                    end = f'{chr(66 + col)}{row + 1}'
                else:
                    # Vertical line, so increase row by one for the second coordinate
                    start = f'{chr(65 + col)}{row + 1}'
                    end = f'{chr(65 + col)}{row + 2}'

                formatted_actions.append(f'<{start}−{end}>')
            else:
                # If no match found, possibly log or handle error
                formatted_actions.append('Invalid action format')

        return formatted_actions

    def openspiel_observation_to_dict(self, current_player_idx, openspiel_obs):
        opponent_idx = 1 if current_player_idx == 0 else 0
        res = {
            'opponent_moves': copy.deepcopy(self.quick_action_memory_for_llm.get(opponent_idx, [])),
            'self_moves': copy.deepcopy(self.quick_action_memory_for_llm.get(current_player_idx, [])),
        }
        return res

    def agent_action_to_openspiel(self, action):
        action_mapping = {
        '<A1-B1>': 0,
        '<B1-C1>': 1,
        '<A2-B2>': 2,
        '<B2-C2>': 3,
        '<A3-B3>': 4,
        '<B3-C3>': 5,
        '<A1-A2>': 6,
        '<B1-B2>': 7,
        '<C1-C2>': 8,
        '<A2-A3>': 9,
        '<B2-B3>': 10,
        '<C2-C3>': 11,
        '<A1−B1>': 0,
        '<B1−C1>': 1,
        '<A2−B2>': 2,
        '<B2−C2>': 3,
        '<A3−B3>': 4,
        '<B3−C3>': 5,
        '<A1−A2>': 6,
        '<B1−B2>': 7,
        '<C1−C2>': 8,
        '<A2−A3>': 9,
        '<B2−B3>': 10,
        '<C2−C3>': 11,
        '<B1-A1>': 0,
        '<C1-B1>': 1,
        '<B2-A2>': 2,
        '<C2-B2>': 3,
        '<B3-A3>': 4,
        '<C3-B3>': 5,
        '<A1-A2>': 6,
        '<B1-B2>': 7,
        '<C1-C2>': 8,
        '<A2-A3>': 9,
        '<B2-B3>': 10,
        '<C2-C3>': 11,
        '<B1−A1>': 0,
        '<C1−B1>': 1,
        '<B2−A2>': 2,
        '<C2−B2>': 3,
        '<B3−A3>': 4,
        '<C3−B3>': 5,
        '<A1−A2>': 6,
        '<B1−B2>': 7,
        '<C1−C2>': 8,
        '<A2−A3>': 9,
        '<B2−B3>': 10,
        '<C2−C3>': 11
    }
        
        # Retrieve the action index from the mapping using the input action string
        return action_mapping.get(action, None) 
