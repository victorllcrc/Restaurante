from .models import Link

def ctx_dict(requet):
    ctx ={}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx