Manipulate colors with Django !

![http://min.us/idbmty.png](http://min.us/idbmty.png)

## Example ##

The template for the example above is quite self explanatory:

```

<h1><b style="background-color:#{{ color }};"></b>#{{ color }}</h1>
<h2>Lightness</h2>
<ul class="color-test">
    {% for l in lightness_range %}
    <li style="background-color:#{{ color|lightness:l }};"><b>{{ l }}%</b></li>
    {% endfor %}
</ul>
<h2>Saturation</h2>
<ul class="color-test">
    {% for s in saturation_range %}
    <li style="background-color:#{{ color|saturation:s }};"><b>{{ s }}%</b></li>
    {% endfor %}
</ul>
<h2>Hue</h2>
<ul class="color-test">
    {% for h in hue_range %}
    <li style="background-color:#{{ color|hue:h }};"><b>{{ h }}&deg;</b></li>
    {% endfor %}
</ul>

```

## Current features ##

  * [color space conversion and manipulation](TemplateTags.md)
  * [color field with color picker](ColorField.md)

# Credits #

This project was created and is sponsored by:

[![](http://motion-m.ca/media/img/logo.png)](http://motion-m.ca/)