#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''Brief description to fit on single line.

Elaborate description spanning multiple lines, covering functionality in more
detail and explaining module usage.'''
#-----------------------------------------------------------------------------#
#                  MODULE HISTORY                                             #
#-----------------------------------------------------------------------------#
# Version          1
# Date             %(date)s
# Author           %(username)s
# Note             Original version
#
#-----------------------------------------------------------------------------#
#                  SYSTEM IMPORTS                                             #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                  OTHER IMPORTS                                              #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                  OWN IMPORTS                                                #
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                  META DATA                                                  #
#-----------------------------------------------------------------------------#
__author__ = 'AB Cooper, DE Fox, and GH Irvine'
__copyright__ = 'Copyright 2017, The ABC Project'
__credits__ = ['AB Cooper', 'DE Fox', 'GH Irvine', 'JK Lee']
__license__ = 'GNU'
__version__ = '1'
__maintainer__ = 'AB Cooper'
__email__ = 'a.b.cooper@abc.edu'
__status__ = 'Development'

#-----------------------------------------------------------------------------#
#                  CONSTANTS                                                  #
#-----------------------------------------------------------------------------#
# ratio of a circle's circumference to its diameter
PI = 3.141592

#-----------------------------------------------------------------------------#
#                  GLOBAL VARIABLES                                           #
#-----------------------------------------------------------------------------#
result = []

#-----------------------------------------------------------------------------#
#                  EXPORTED FUNCTIONS                                         #
#-----------------------------------------------------------------------------#
def public_function_example():
    '''This is a public function example.
    :return: tmp_bool'''
    global result
    tmp_bool = True
    return tmp_bool

#-----------------------------------------------------------------------------#
#                  LOCAL FUNCTIONS                                            #
#-----------------------------------------------------------------------------#
def __private_function_example():
    '''This is a private function example, which is indicated by the leading 
    under scores.
    :return: tmp_bool'''
    tmp_bool = True
    return tmp_bool

#-----------------------------------------------------------------------------#
#                  END OF FILE                                                #
#-----------------------------------------------------------------------------#