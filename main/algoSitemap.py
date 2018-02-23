from django.contrib.sitemaps import Sitemap
from main.models import Algo, Code

class AlgoSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Algo.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return "/" + obj.slug


class CodeSitemap(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return Code.objects.all()

    def lastmod(self, obj):
        return obj.algo.created_at

    def location(self, obj):
        return "/code/%s/%s" % (obj.id, obj.algo.slug)
