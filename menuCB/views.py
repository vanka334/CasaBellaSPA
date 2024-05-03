from django.views.generic import TemplateView



# Create your views here.
class IndexView(TemplateView):
    context_object_name = 'sections'
    template_name = 'sections.html'

    # def get_season(self):
    #     season = 0
    #     menus = Menu.objects.all()
    #     for x in menus:
    #         if x.isActive == True:
    #             season = x.id
    #
    #     sections = Type.objects.filter(season=season)
    #     sorted(sections, key=lambda queue: queue.queue_view)
    #     return sections
    # def get_context_data(self, **kwargs):
    #
    #     context = super(IndexView, self).get_context_data(**kwargs)
    #     sections = self.get_season()
    #     context['sections'] = sections
    #     return super().get_context_data(sections=sections, **kwargs)


