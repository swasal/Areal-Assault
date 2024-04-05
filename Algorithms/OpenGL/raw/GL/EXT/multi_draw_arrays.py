'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_multi_draw_arrays'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_multi_draw_arrays',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLenum,arrays.GLintArray,arrays.GLsizeiArray,_cs.GLsizei)
def glMultiDrawArraysEXT(mode,first,count,primcount):pass
@_f
@_p.types(None,_cs.GLenum,arrays.GLsizeiArray,_cs.GLenum,arrays.GLvoidpArray,_cs.GLsizei)
def glMultiDrawElementsEXT(mode,count,type,indices,primcount):pass