from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',

    url(r'^$', 'django.views.generic.simple.direct_to_template', {
        'template': 'colors/colors-test.html',
        'extra_context': {
            'colors_tests': [
                '000000', # Black
                'ff0000', # Red
                '00ff00', # Green
                '0000ff', # Blue
                'ffff00', # Yellow
                '00ffff', # Cyan
                'ff00ff', # Magenta
                'c0c0c0', # Grey
                'ffffff', # White
            ],
            'lightness_range':  range(0, 101, 10),
            'saturation_range': range(0, 101, 10),
            'hue_range':        range(0, 361, 30),
            },
    }, name='django-colors-test'),


)

