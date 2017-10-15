from character_viewer.views import CharacterViewerView, ViewerHomeView


urlpatterns = []

urlpatterns += ViewerHomeView.urls()
urlpatterns += CharacterViewerView.urls()
