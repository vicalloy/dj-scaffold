import os
from optparse import make_option

import dj_scaffold
from django.core.management.base import CommandError, LabelCommand
from django.utils.importlib import import_module

from dj_scaffold import utils


class Command(LabelCommand):
    option_list = LabelCommand.option_list + (
        make_option('--template', '-t', action='store', dest='app_template', 
            help='The path to the app template'),
        make_option('--parent_path', '-p', action='store', dest='parent_path', 
            help='The parent path of the app to be created'),
    )
    
    help = ("Creates a Django application directory structure based on the specified template directory.")
    args = "[appname]"
    label = 'application name'
    
    requires_model_validation = False
    can_import_settings = True
    
    #def handle_label(self, label, **options):
    def handle_label(self, app_name, directory=None, **options):
        if directory is None:
            directory = os.getcwd()
        #app_name =label
        app_template = options.get('app_template') or os.path.join(dj_scaffold.__path__[0], 'conf', 'app')
        app_dir = os.path.join(options.get('parent_path') or directory, app_name)
                
        if not os.path.exists(app_template):
            raise CommandError("The template path, %r, does not exist." % app_template)

        # Determine the project_name by using the basename of directory,
        # which should be the full path of the project directory (or the
        # current directory if no directory was passed).
        project_name = os.path.basename(directory)
        if app_name == project_name:
            raise CommandError("You cannot create an app with the same name"
                               " (%r) as your project." % app_name)

        # Check that the app_name cannot be imported.
        try:
            import_module(app_name)
        except ImportError:
            pass
        else:
            raise CommandError("%r conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name." % app_name)
        
        # Get any boilerplate replacement variables:
        replace = {}
        utils.copy_template(app_template, app_dir, replace)
