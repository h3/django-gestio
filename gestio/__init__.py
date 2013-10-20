import os

# Use 'final' as the 4th element to indicate
# a full release

VERSION = (0, 0, 1, 'alpha', 0)


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        # Append 3rd digit if > 0
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    elif VERSION[3] != 'final':
        version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version


# Cheeky setting that allows each template to be accessible by two paths.
# Eg: the template 'gestio/templates/gestio/base.html' can be accessed via both
# 'base.html' and 'gestio/base.html'.  This allows Gestio's templates to be
# extended by templates with the same filename
GESTIO_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates/gestio')

GESTIO_CORE_APPS = [
    'gestio',
    'gestio.apps.address',
    'gestio.apps.customer',
   #'gestio.apps.dashboard',
   #'gestio.apps.company',
   #'gestio.apps.project',
   #'gestio.apps.purchaseorder',
]

def get_core_apps(overrides=None):
    """
    Return a list of gestio's apps amended with any passed overrides
    """
    if not overrides:
        return GESTIO_CORE_APPS

    def get_app_label(app_label, overrides):
        pattern = app_label.replace('gestio.apps.', '')
        for override in overrides:
            if override.endswith(pattern):
                if 'dashboard' in override and 'dashboard' not in pattern:
                    continue
                return override
        return app_label

    apps = []
    for app_label in GESTIO_CORE_APPS:
        apps.append(get_app_label(app_label, overrides))
    return apps
