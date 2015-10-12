Django Colors provide a model field for storing hexadecimal colors which comes with a handy color picker.

I chose [Stefan Petre's color picker](http://www.eyecon.ro/colorpicker/) because it was the most complete and easy to integrate.

**Note**: currently available only in the trunk

# Usage example #

```

from colors.fields import ColorField

class MyModel(ExtendedModel):
    title = models.CharField('Title', max_length=250)
    color = ColorField(default='ffffff')

```

# Screenshot #

![http://min.us/iCh68.png](http://min.us/iCh68.png)