#!/usr/bin/env python3

# This Wonderlands Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Wonderlands Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Wonderlands Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../python_mod_helpers')
from wlhotfixmod.wlhotfixmod import Mod

# The 'weights' array specifies the desired weighting for the boss to appear.
bosses = {
    'Chums':
        {'room':    'ED_Shark_0{}',
         'name':    'ED_SharkBoss_0{}',
         'weights': [0.0, 0.0, 0.0, 0.0],
         'dlc':     'Indigo1'},
    'Imelda':
        {'room':    'ED_Witch_0{}',
         'name':    'ED_Witch_Boss_V{}',
         'weights': [0.0, 0.0, 0.0, 0.0],
         'dlc':     'Indigo2'},
    'Fyodor':
        {'room':    'ED_Smith_0{}',
         'name':    'ED_Smith_Boss_V{}',
         'weights': [0.0, 0.0, 0.0, 0.0],
         'dlc':     'Indigo3'},
    'Redmourne':
        {'room':    'Wyvern_0{}',
         'name':    'Wyvern_Boss_0{}',
         'weights': [0.0, 0.0, 0.0, 0.0],
         'dlc':     'Indigo4'}}

for boss, values in bosses.items():
    mod = Mod('no_{}.wlhotfix'.format(boss.lower()),
              'No Chaos Chamber {}'.format(boss),
              'SentientVibratingApple',
              ['Sets the Chaos Chamber spawn weight for {} (all forms) to 0'.format(boss)],
              lic=Mod.CC_BY_SA_40,
              cats='spawns, qol',
              v='1.0',
              contact_discord='SentientVibratingApple#2453')

    mod.comment('If setting a boss weight other than zero (lines with \'Boss\' in them),')
    mod.comment('then the weight for the corresponding non-boss line should be set to \'1.0\'.')

    weights = values['weights']
    dlc = values['dlc']
    for i in range(len(weights)):
        boss_name = values['name']
        room_name = values['room']
        weight = weights[i]

        set_row = lambda row_name, weight: \
            mod.table_hotfix(
                Mod.LEVEL,
                'EndlessDungeon_P',
                '/Game/PatchDLC/{0}/GameData/Rooms/{0}_DetailedRoomInfos'.format(dlc),
                row_name.format(i+1),
                'Weight',
                str(weight))

        set_row(room_name, 1.0 if weight != 0.0 else 0.0)
        set_row(boss_name, weight)

        mod.newline()
    mod.close()