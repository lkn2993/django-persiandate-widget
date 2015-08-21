import datetime, time

from django.contrib.admin.widgets import AdminFileWidget
from django.forms.fields import EMPTY_VALUES
from django.forms.widgets import DateInput
from django.forms.util import flatatt
from django.utils import formats
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from persiandate import jalali
import os

class PersianDateInput(DateInput):
    class Media:
        css = {
            'all': ('/static/css/persian-datepicker-0.4.5.css',)
        }
        js = (
              '/static/js/persian-date.js',
              '/static/js/persian-datepicker-0.4.5.js',
              '/static/js/persianDateLoad.js',
        )
 
    dformat = '%Y-%m-%d'
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            try:
                final_attrs['value'] = value.strftime(self.dformat)
            except:
                final_attrs['value'] = value
        if not 'id' in final_attrs:
            final_attrs['id'] = u'%s_id' % (name)
        jsdformat = self.dformat
        custom_class = final_attrs.get('class', None)
        final_attrs.pop('class', None)
        parsed_atts = flatatt(final_attrs)
        a = u'<input class="%s observer" input_formats="[%s]" %s> %s' % (custom_class, self.dformat, parsed_atts, self.media)
        return mark_safe(a)
 
    def value_from_datadict(self, data, files, name):
 
        value = data.get(name, None)
        if value in EMPTY_VALUES:
            return None
        if isinstance(value, datetime.datetime):
            return value
        if isinstance(value, datetime.date):
            d = jalali.Persian(value.year, value.month, value.day).gregorian_datetime()
            return datetime.combine(d, time())
        else:
            try:
                d = jalali.Persian(value).gregorian_datetime()
                return d
            except ValueError:
                return None
        return None
 
    def _has_changed(self, initial, data):
        """
        Return True if data differs from initial.
        Copy of parent's method, but modify value with strftime function before final comparsion
        """
        if data is None:
            data_value = u''
        else:
            data_value = data
 
        if initial is None:
            initial_value = u''
        else:
            initial_value = initial 
        return False