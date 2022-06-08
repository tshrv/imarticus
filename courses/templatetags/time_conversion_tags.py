from django.template.defaulttags import register

@register.filter
def seconds_to_mmss(seconds: int) -> str:
    """
    231 seconds -> 3:51
    """
    mmss_representation = '--:--'
    try:
        mmss_representation = f'{int(seconds/60)}:{seconds%60}'
    except Exception as e:
        pass
    return mmss_representation