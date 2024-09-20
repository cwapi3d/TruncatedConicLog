# Copyright 2024 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of TruncatedConicLog,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import cadwork
import element_controller as ec
import utility_controller as uc

user_start_diameter = uc.get_user_double('Enter start diameter (in):')
user_end_diameter = uc.get_user_double('Enter end diameter (in):')

user_start_diameter *= 25.4
user_end_diameter *= 25.4

uc.print_message('Select start point...', 2, 1)
user_p1 = uc.get_user_point()
uc.print_message('Select end point...', 2, 1)
user_p2 = uc.get_user_point()
user_p3 = cadwork.point_3d(user_p1.x, user_p1.y, user_p1.z + 1)

uc.print_message('', 2, 1)

ec.create_truncated_cone_beam_points(user_start_diameter, user_end_diameter, user_p1, user_p2, user_p3)
