import os
import re
from optparse import make_option

import dj_scaffold
from django.core.management.base import CommandError, LabelCommand, _make_writeable

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
    
    def handle_label(self, label, **options):
        project_dir = os.getcwd()
        app_name =label
        app_template = options.get('app_template') or os.path.join(dj_scaffold.__path__[0], 'conf', 'app')
        app_dir = os.path.join(options.get('parent_path') or project_dir, app_name)
                
        if not os.path.exists(app_template):
            raise CommandError("The template path, %r, does not exist." % app_template)
        
        if not re.search(r'^\w+$', label):
            raise CommandError("%r is not a valid application name. Please use only numbers, letters and underscores." % label)
        try:
            os.makedirs(app_dir)
        except OSError, e:
            raise CommandError(e)
        
        # Get any boilerplate replacement variables:
        replace = {}
        utils.copy_template(app_template, app_dir, replace)
