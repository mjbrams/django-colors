# http://www.w3.org/TR/AERT#color-contrast
# http://docs.python.org/library/colorsys.html
# http://www.flett.org/2005/04/26/cool-python-tricks/

from __future__ import division
import colorsys as cs

from django.utils.safestring import SafeString
from django import template

register = template.Library()


def dec2hex(d):
    """return a two character hexadecimal string representation of integer d"""
    return "%02X" % d


# -- Filters -----------------------


def opposite(x):
    """Returns the opposite color on the HSV color space"""
    x = expand_hex(x)
    if x == '000000':
        return 'ffffff'
    elif x == 'ffffff':
        return '000000'
    else:
        h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
        if h > 180:
            h = h - 180
        else:
            h = 180 - h
        return hsv_to_hex(h, s, v)


def short_hex(x):
    """Return shorthand hexadecimal code, ex: cc3300 -> c30"""
    t = list(x)
    if t[0] == t[1] and t[2] == t[3] and t[4] == t[5]:
        return '%s%s%s' % (t[0], t[2], t[4])
    else:
        return x


def expand_hex(x):
    """Expands shorthand hexadecimal code, ex: c30 -> cc3300"""
    if len(x) == 3:
        t = list(x)
        return "".join([t[0], t[0], t[1], t[1], t[2], t[2]])
    else:
        return x


def hsv_to_hex(h, s, v):
    """Returns the hexadecimal value of a HSV color"""
    r, g, b = cs.hsv_to_rgb(h/360, s/100, v/100)
    return dec2hex(r*255) + dec2hex(g*255) + dec2hex(b*255)


def hex_to_hsv(x, format_string='%s %s %s'):
    """Returns the HSV value of a hexadecimal color"""
    x = expand_hex(x)
    h, s, v = cs.rgb_to_hsv(int(x[0:2], 16)/255.0, int(x[2:4], 16)/255.0, int(x[4:6], 16)/255.0)
    out = (int(h * 360), int(s * 100), int(v * 100))
    return format_string % out if format_string else out


def hex_to_rgb(x, format_string='%s %s %s'):
    """Returns the RGB value of a hexadecimal color"""
    x = expand_hex(x)
    out = (int(x[0:2], 16), int(x[2:4], 16), int(x[4:6], 16))
    return format_string % out if format_string else out


# -- Filters / HSV manipulations


def lightness(x, value):
    """Set lightness to x, accept hexadecimal or hsv tuple as value"""
    x = expand_hex(x)
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(h, s, int(value))


def saturation(x, value):
    """Set saturation to x, accept hexadecimal or hsv tuple as value"""
    x = expand_hex(x)
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(h, int(value), v)


def hue(x, value):
    """Set hue to x, accept hexadecimal or hsv tuple as value"""
    x = expand_hex(x)
    h, s, v = hex_to_hsv(x, False) if len(x) == 6 else x
    return hsv_to_hex(int(value), s, v)




register.filter('hue', hue)
register.filter('lightness',  lightness)
register.filter('saturation', saturation)
register.filter('opposite',   opposite)
register.filter('expand_hex', expand_hex)
register.filter('short_hex',  short_hex)
register.filter('hsv_to_hex', hsv_to_hex)
register.filter('hex_to_hsv', hex_to_hsv)
register.filter('hex_to_rgb', hex_to_rgb)
