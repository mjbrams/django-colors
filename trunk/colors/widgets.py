# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class ColorPickerWidget(forms.TextInput):
    class Media:
        css = {
            'all': (
                settings.MEDIA_URL + 'colors/css/colorpicker.css',
            )
        }
        js = (
            settings.MEDIA_URL + 'colors/colorpicker.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        super(ColorPickerWidget, self).__init__(attrs=attrs)

    def render(self, name, value, attrs=None):
        rendered = super(ColorPickerWidget, self).render(name, value, attrs)
        #var preview = $('<div id="customWidget"><div id='colorSelector2'><div style='background-color: #00ff00'></div></div>').insertAfter('#id_%s');
        return rendered + mark_safe(u"""<script type="text/javascript">(function($){
$(function(){
    var preview = $('<div class="color-picker-preview"><div style="background-color:#%s"></div></div>').insertAfter('#id_%s');
    $('#id_%s').ColorPicker({
        color: '%s',
        onSubmit: function(hsb, hex, rgb, el) { $(el).val(hex); $(el).ColorPickerHide();$(preview).find('div').css('backgroundColor', '#' + hex); },
        onBeforeShow: function () { $(this).ColorPickerSetColor(this.value); },
        //onChange: function (hsb, hex, rgb) { $(preview).find('div').css('backgroundColor', '#' + hex); }
    }).bind('keyup', function(){ $(this).ColorPickerSetColor(this.value); });
});})(typeof(django) != 'undefined' && django.jQuery || jQuery);</script>""" % (value, name, name, value))
