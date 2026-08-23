from django.urls import resolve
from. models import Homepage, Product


# Written with AI
def vertical_bar_videos(request):
    video_1 = None
    video_2 = None
    # Step 1: Check if we are on a Product Detail page using the URL slug
    try:
        match = resolve(request.path_info)
        if 'slug' in match.kwargs:
            product = Product.objects.filter(slug=match.kwargs['slug']).prefetch_related('videos').first()
            if product:
                product_videos = list(product.videos.all()[:2])  # Slice to get max 2 videos
                if len(product_videos) >= 1:
                    video_1 = product_videos[0]
                if len(product_videos) >= 2:
                    video_2 = product_videos[1]
    except Exception:
        pass

    # Step 2: Fallback to Homepage layout videos if product videos aren't present
    if not video_1 and not video_2:
        active_homepage = Homepage.objects.filter(is_active=True).first()
        if active_homepage:
            video_1 = active_homepage.video1
            video_2 = active_homepage.video2

    return {
        'side_video_1': video_1,
        'side_video_2': video_2,
    }