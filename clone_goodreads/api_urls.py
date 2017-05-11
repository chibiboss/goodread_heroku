from django.conf.urls import url,include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token,VerifyJSONWebToken,refresh_jwt_token
from rest_framework_swagger.views  import get_swagger_view
schema_view = get_swagger_view(title="Goodreads Clone API")

urlpatterns = [
url(r'^authors/', include("modules.Authors.urls")),
url(r'^books/', include("modules.Books.urls")),
url(r'^auth/', obtain_jwt_token),
url(r'^docs/', schema_view),

]