import re
from django import template


# Written with AI

register = template.Library()

def clean_youtube_url(url):
    """
    Transforms standard watch links, shorts, or shared paths into clean
    embed links for iframes. Returns original URL if it does not match YouTube.
    """
    if not url:
        return ""
        
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/|youtube\.com/shorts/)'
        r'([^&=%\?\#\s]{11})'
    )
    
    match = re.search(youtube_regex, url)
    if match:
        video_id = match.group(4)
        return f"https://youtube.com{video_id}"
        
    return url


@register.simple_tag(takes_context=True)
def get_dynamic_video(context, video_slot_name):
    """
    Context-aware tag targeting dynamic page assets.
    """
    raw_url = None

    # 1. Product Detail Page Context (Using ManyToMany via property helper)
    product = context.get('product')
    if product and hasattr(product, 'primary_video') and product.primary_video:
        raw_url = product.primary_video.link

    # 2. Homepage Context Layout (Using precise ForeignKey fields)
    else:
        homepage = context.get('homepage')
        if homepage:
            if video_slot_name == 'video1' and homepage.video1:
                raw_url = homepage.video1.link
            elif video_slot_name == 'video2' and homepage.video2:
                raw_url = homepage.video2.link

    # 3. Fallback resolution for slots without database records assigned yet
    if not raw_url:
        fallback_videos = {
            'video1': 'https://www.youtube.com/watch?v=WLsdcbYJABQ&t=581s',
            'video2': 'https://www.youtube.com/watch?v=HPHUQNq-M8s&t=1633s'
        }
        return fallback_videos.get(video_slot_name, 'https://www.youtube.com/watch?v=y8fSub78WxQ&list=PLc6CD0SJH6HOk5yHpXmPeCw-RJPmnsNHO&index=16')

    return clean_youtube_url(raw_url)

# End of AI