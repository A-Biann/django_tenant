# define get_setting() to return site settings data

from django import template
register = template.Library()

from core.models import Settings

@register.simple_tag
def get_setting(language_code=None):
    if not language_code:
        setting = Settings.objects.get(id='zh-hant')
    else:
        setting = Settings.objects.get(id=language_code)
    setting_dict = setting.__dict__
    setting_dict['home_type1'] = setting.home_type1.__dict__ if setting.home_type1 else None
    setting_dict['home_type2'] = setting.home_type2.__dict__ if setting.home_type2 else None
    setting_dict['home_type3'] = setting.home_type3.__dict__ if setting.home_type3 else None
    return setting_dict

@register.simple_tag
def get_setting_list():
    settings = Settings.objects.all()
    return [{"code": setting.id, "name_local": setting.language} for setting in settings]