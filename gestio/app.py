from django.conf.urls import patterns, url, include
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse_lazy

GESTIO_INSTALLED_APPS = (
    'gestio.apps.customer',
    'gestio.apps.dashboard',
)

from gestio.core.application import Application

from gestio.apps.customer import forms
from gestio.views.decorators import login_forbidden


class Gestio(Application):
    name = None

    def get_urls(self):
        urlpatterns = patterns('',
            (r'^i18n/', include('django.conf.urls.i18n')),
#           (r'^accounts/', include(self.customer_app.urls)),
#           (r'^search/', include(self.search_app.urls)),
            (r'^dashboard/', include(self.dashboard_app.urls)),

            # Password reset - as we're using Django's default view funtions,
            # we can't namespace these urls as that prevents
            # the reverse function from working.
            url(r'^password-reset/$',
                login_forbidden(auth_views.password_reset),
                {'password_reset_form': forms.PasswordResetForm,
                 'post_reset_redirect': reverse_lazy('password-reset-done')},
                name='password-reset'),
            url(r'^password-reset/done/$',
                login_forbidden(auth_views.password_reset_done),
                name='password-reset-done'),
            url(r'^password-reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                login_forbidden(auth_views.password_reset_confirm),
                {'post_reset_redirect': reverse_lazy('password-reset-complete')},
                name='password-reset-confirm'),
            url(r'^password-reset/complete/$',
                login_forbidden(auth_views.password_reset_complete),
                name='password-reset-complete'),
            (r'', include(self.promotions_app.urls)),
        )
        return urlpatterns


for app in GESTIO_INSTALLED_APPS:
    app_name = app.split('.')[-2]
   #setattr(Gestio, app_name, property(lambda s: __import__(app)))
    setattr(Gestio, app_name, lambda s: __import__(app))
    # TODO: dynamic URLs

application = Gestio()
