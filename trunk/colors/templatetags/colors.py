from __future__ import division
import colorsys as cs

from django import template
from django.utils.safestring import SafeString

register = template.Library()

def dec2hex(d):
    """return a two character hexadecimal string representation of integer d"""
    r = "%X" % d
    return r if len(r) > 1 else r+r


def hsv_to_hex(hsv):
    """Returns the hexadecimal value of a HSV color"""
    h, s, v = hsv
    r, g, b = cs.hsv_to_rgb(h/360, s/100, v/100)
    return dec2hex(r*255) + dec2hex(g*255) + dec2hex(b*255)


# -- Filters -----------------------


@register.filter()
def opposite(x):
    """Returns the opposite color on the HSV color space"""
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(360-h, 100-s, 100-v)


# -- Filters / HSV manipulations


@register.filter()
def lightness(x, value):
    """Set lightness to x, accept hexadecimal or hsv tuple as value"""
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(h, s, int(value))


@register.filter()
def saturation(x, value):
    """Set saturation to x, accept hexadecimal or hsv tuple as value"""
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(h, int(value), v)


@register.filter()
def hue(x, value):
    """Set hue to x, accept hexadecimal or hsv tuple as value"""
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(int(value), s, v)


# -- Filters / color conversions


@register.filter()
def hex_to_rgb(x, format_string='%s %s %s'):
    """Returns the RGB value of a hexadecimal color"""
    out = (int(x[0:2], 16), int(x[2:4], 16), int(x[4:6], 16))
    return format_string % out if format_string else out


@register.filter()
def hex_to_hsv(x, format_string='%s %s %s'):
    """Returns the HSV value of a hexadecimal color"""
    h, s, v = cs.rgb_to_hsv(int(x[0:2], 16)/255.0, int(x[2:4], 16)/255.0, int(x[4:6], 16)/255.0)
    out = (int(h * 360), int(s * 100), int(v * 100))
    return format_string % out if format_string else out
