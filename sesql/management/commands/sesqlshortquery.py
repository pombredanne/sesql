# -*- coding: utf-8 -*-
# Copyright (c) Pilot Systems and Libération, 2010-2011

# This file is part of SeSQL.

# SeSQL is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# SeSQL is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# ashort with SeSQL.  If not, see <http://www.gnu.org/licenses/>.

"""
This will preform a SeSQL short query and displays the results
It's mostly useful to check your SeSQL installation
"""

from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection, transaction
from django.db.models import Q
import settings
from sesql.shortquery import shortquery
import sys

class Command(BaseCommand):
    help = "Perform a SeSQL short query"
    
    def handle(self, *apps, **options):
        """
        Handle the command
        """
        if not 1 <= len(apps) <= 2:
            print "Syntax : sesqlshortquery <query> [<order>]"
            sys.exit(1)

        query = eval(apps[0])
        order = len(apps) == 2 and eval(apps[1]) or None
        
        print shortquery(query, order).objs
        
