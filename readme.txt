To begin this poject, follow information, which derscribe below :

1. Into the desktop open command prompt. 
2. Your will see the way (only in my computer): C:\Users\HP> 
3. Write 'cd desktop'  
4. Create the virual invirinment: python -m venv environment  
5. Activate the virual invirinment: environment\scripts\activate
6. Your will see: (environment) PS C:\Users\HP\
7. Write: pip install django
8. Wite: django-admin startproject United_of_token    (United_of_token - for example the name of poject)
7. On the desktop, your should to remove the folder 'environment' into the folder 'United_of_token' 
8. Open VS code by command in command prompt 'code .'
8. In VS code open the folder 'United_of_token'
9. Open the terminal by 'ctrl + shigt + `(tilda)'
10. Then activated 'environment'
11. In powershell into the way (environment) PS C:\Users\HP\United_of_token> write     python manage.py startapp base 
12. Go into the folder 'United_of_token' -> settings.py  (open it -> # Application definition -> INSTALLED_APPS = [ -> (through an empty line) 
    -> 'base.apps.BaseConfig',)
13. in powershell use the next command: python -m pip install autopep8  

14. inside the folder 'base', create the new folder 'api'

15. inside the folder 'api', create the new file '__init__.py'
16. inside the folder 'api', create the new file 'views.py'
17. inside the folder 'api', create the new file 'urls.py'
18. inside the folder 'api', create the new file 'serializers.py'

19. inside the folder 'api', into the file 'views.py' create the code: 

    from django.http import JsonResponse


    def getRoutes(request):
        routes = [
            '/api/token',
            '/api/token/refresh',
        ]
        
        return JsonResponse(routes, safe=False) 

20. inside the folder 'api', into the file 'urls.py' create the code:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.getRoutes)
    ]

21. inside the folder 'United_of_token', into the file 'urls.py' make the changes: 

    21.1 clean the comments:

    """United_of_token URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
    21.2 create the code (inside the folder 'United_of_token', into the file 'urls.py'):

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.api.urls'))
]

22. go to the next path: United_of_token -> base -> api -> urls.py

    20.1 Your can see the code:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.getRoutes)
    ]

23. in powershell (after the path (environment) PS C:\Users\HP\United_of_token>) use the next command:   python manage.py runserver  
24. paste http://127.0.0.1:8000/ and insert into the browser
25. your will see 'error 404'
26. addinng into the path of browser (/api) as a result, your will have    http://127.0.0.1:8000/api


27. go to the site     https://www.django-rest-framework.org/
28. your should go to the section 'Installation'
29. copy    pip install djangorestframework
30. after the path (environment) PS C:\Users\HP\United_of_token>  your should to write   python -m pip install djangorestframework

31. Ok
32. go to the next path: United_of_token -> settings.py


33. (open it -> # Application definition -> INSTALLED_APPS = [ -> (through an empty line) 
    -> 'base.apps.BaseConfig',) after the 'base.apps.BaseConfig', yout should write     
    'rest_framework',    through an empty line (which is copid from https://www.django-rest-framework.org/)
34. go to the path United_of_token -> base -> api -> views.py
35. in this path your shoul write the code :
    
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    
    return Response(routes)

36. inside the path (environment) PS C:\Users\HP\United_of_token>   your should to write   python manage.py migrate
37. your can see the messages :

    Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK



38. Ok
39. In powershell (after the path (environment) PS C:\Users\HP\United_of_token> ) use the next command:   python manage.py runserver 
40. Starting development server at http://127.0.0.1:8000/api/ 
41. Use the link      https://github.com/jazzband/djangorestframework-simplejwt
42. Go into down of page  ->   Abstract  ->   django-rest-framework-simplejwt.readthedocs.io.
43. As a result  ->  https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
44. Then -> Contents -> installation -> Installation  Simple JWT can be installed with pip:
45. Copy          pip install djangorestframework-simplejwt    
46. In powershell (after the path (environment) PS C:\Users\HP\United_of_token> python -m pip install djangorestframework-simplejwt 
47. In   https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation   copy :
     
    REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
    ...
}

48. Paste in       United_of_token -> settings.py     after  'rest_framework', ]
49. Edit this code:  clear in each line (three times)   '...'    :

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )    
}     

50. Copy from     https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation   after 
'Also, in your root urls.py file (or any other url config), include routes for Simple JWT’s TokenObtainPairView and TokenRefreshView views:'


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



51. Go into base -> api -> urls.py
52. Paste code after  'from . import views'


53. Then go to https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html#installation
54. Copy after 'urlpatterns = [
    ...'

path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


55. Go to base -> api -> urls.py           Paste  after      

urlpatterns = [
    path('', views.getRoutes),

56. Deleting 'api' from pasted code
57. As a result:

urlpatterns = [
                path('', views.getRoutes),
                path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ]


58. Running the command       python manage.py runserver 
59. In the browser go to the     http://127.0.0.1:8000/api/token/
60. Go into (environment) PS C:\Users\HP\United_of_token> and write       python manage.py migrate


61. Go into (environment) PS C:\Users\HP\United_of_token> and write       python manage.py createsuperuser    (later, your should to enter username and password from 'superuser')
62. Probably there will be a problem. To solve it, you need to install   python -m pip install djangorestframework-simplejwt==4.7.2


62. Go into https://jwt.io/    to checking the token.
63. Copy refresh token from http://127.0.0.1:8000/api/token/

64. Go into http://127.0.0.1:8000/api/token/refresh/ 
65. Paste refresh token into the field
66. Go back into the http://127.0.0.1:8000/api/token/refresh/
67. Your won't to see the resfresh token
68. Go into https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
69. Copy the code:

	from datetime import timedelta
...

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

70. Go to the United_of_token -> settings
71. Paste the code after the 

	REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )    
}     

72. Deleted '...'
73. Cutting the           from datetime import timedelta
74. Paste after
    
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


75. Go to the 'SIMPLE_JWT = {'
76. Delete 'SIGNING_KEY': SECRET_KEY,'
77. Rewrite 'REFRESH_TOKEN_LIFETIME': timedelta(days=90),'
78. (environment) PS C:\Users\HP\United_of_token> python manage.py runserver 


79. In the browser go into http://127.0.0.1:8000/api/token/
80. enter 'POST'
81. Copy the refresh token
82. In the browser go into http://127.0.0.1:8000/api/token/refresh


83. Paste refresh token into 'Refresh'
84. Enter 'POST' and give your new "access" token


85. Rewrite 'ROTATE_REFRESH_TOKENS': True,'

86. In the browser go into http://127.0.0.1:8000/api/token/refresh

87. Paste refresh token into 'Refresh'
88. Enter 'POST' and give your new "access" and "refresh" tokens


89. Paste refresh token into 'Refresh'. Enter 'POST' and give your new "access" and "refresh" tokens again.
90. It is vey dangerous (ROTATE_REFRESH_TOKENS)


91. For that reason Go into United_of_token -> settings.py   and rewrite  'BLACKLIST_AFTER_ROTATION': True,


92. Into the browser go into the https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html        'BLACKLIST_AFTER_ROTATION'
93. Copy the code 'rest_framework_simplejwt.token_blacklist',
94. Go to the United_of_token -> settings
95. Paste the code after   

	INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'base.apps.BaseConfig',

     'rest_framework',

95. Write (environment) PS C:\Users\HP\United_of_token> python manage.py migrate
96. Write (environment) PS C:\Users\HP\United_of_token> python manage.py runserver 


97. Go into http://127.0.0.1:8000/api/token/
98. Copy refresh token


99. Paste into 'Refresh'
100. Your again will see "access": and "refresh": tokens and when your again copy 'refresh' and paste into 'Refresh', your will see 
	
{
    "detail": "Token is blacklisted",
    "code": "token_not_valid"
}




101.Go into https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
102. Copy     

	from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
	from rest_framework_simplejwt.views import TokenObtainPairView


103. Go into     United_of_token -> base -> api -> views.py
104. Paste the code after 

	from rest_framework.decorators import api_view


105. Go into https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html
106. Copy
 	
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

107. Go into the way United_of_token -> base -> api -> views.py
108. Paste the code after 
	
	from rest_framework_simplejwt.views import TokenObtainPairView

109. Into the way  United_of_token -> base -> api -> views.py      rewrite    

	# Add custom claims
        token['username'] = user.username

110. Go into the way United_of_token -> base -> api -> urls.py
111. Clear      TokenObtainPairView,         after the    from rest_framework_simplejwt.views import (

112. Rewrite     path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
113. Add   from .views import MyTokenObtainPairView


114. Go into http://127.0.0.1:8000/api/token/
115. Submit username and password. Click 'POST'


116. And your will see refresh and new token
117. Copy "access" token and go into the https://jwt.io/


118. Paste the token into EncodedPASTE A TOKEN HERE
119. Now your will see "username": (it's cool)


120. Go into https://github.com/adamchainz/django-cors-headers
121. Copy from Setup   Install from pip:
	 
	python -m pip install django-cors-headers

122. Go into (environment) PS C:\Users\HP\United_of_token> 
123. Write   python -m pip install django-cors-headers


124. Go into https://github.com/adamchainz/django-cors-headers

125. Copy from Setup   Install from pip:

	'corsheaders',

126. Go into United_of_token -> settings
127. After the     'rest_framework_simplejwt.token_blacklist',      paste

	'corsheaders',

128. Go into https://github.com/adamchainz/django-cors-headers
129. After the  

	You will also need to add a middleware class to listen in on responses:

MIDDLEWARE = [
    ...,
    
130. Copy
	
	"corsheaders.middleware.CorsMiddleware",

131. Go into United_of_token -> settings

132. After the 

	MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

133. Paste 

	'corsheaders.middleware.CorsMiddleware',

134. Go into https://github.com/adamchainz/django-cors-headers 
135. After the Configuration     copy    CORS_ALLOW_ALL_ORIGINS


136. Go into United_of_token -> settings.py

134. After the     DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'    (at the end)
135. Paste     CORS_ALLOW_ALL_ORIGINS and add  'True', as a result:

	DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

	CORS_ALLOW_ALL_ORIGINS = True

136. Write (environment) PS C:\Users\HP\United_of_token> python manage.py runserver 

137. Go into http://127.0.0.1:8000/api/token/ to check the working of refresh token



   






    








