# -*- coding: utf-8 -*-
#
# This file is part of EventGhost.
# Copyright © 2005-2019 EventGhost Project <http://www.eventghost.net/>
#
# EventGhost is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# EventGhost is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along
# with EventGhost. If not, see <http://www.gnu.org/licenses/>.

import wx

# Local imports
import eg

class DisplayChoice(eg.Choice):
    """
    A wx.Choice control, that shows all available displays.
    """
    def __init__(self, parent, value, *args, **kwargs):
        numDisplays = wx.Display().GetCount()
        choices = ["Monitor %d" % (i + 1) for i in range(numDisplays)]
        eg.Choice.__init__(self, parent, value, choices, *args, **kwargs)
