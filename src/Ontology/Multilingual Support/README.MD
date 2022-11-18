## ==================== Multilingual Forms ====================

This app uses 'django-parler' and 'gettext_lazy' to create multilingual support for the ontology. It is however a proof of concept, so it only includes a small subset of the classes and attributes and will need to be extended to the full ontology.
More in detail, django-parler creates additional fields for attributes that are language dependent, for example title, description and url, while gettext_lazy provides translations for labels and templates without requiring duplication.

The app contains templates to a homepage with the list of resources, two forms to upload resources (one with the initial information in one language choice of the user and a second one to add the fields in additional languages), a thank you for your submission page and a page to see the single resource in detail.

For more informations about the design and choices made, please refer to the Multilingual Support section of the README file in Ontology/Design/

The app itself is in the '/forms' folder.
I have also included my settings.py file and '/locale' folder to help in case of confusion.

### Quick start
-----------
1. Copy the '/forms' folder inside the project folder.

2. Add "parler" to your INSTALLED_APPS setting like this:
    ```python
        INSTALLED_APPS = [
            ...
            'parler',
        ]
    ```
        
* Add   "LocaleMiddleware" to MIDDLEWARE right after 'django.contrib.sessions.middleware.SessionMiddleware',
    ```python
        MIDDLEWARE = [
        ....
        'django.middleware.locale.LocaleMiddleware',
        ...
        ]
    ```

3. Add language information to the settings file (list of languages can of course be different). 
   'locale' will be the location where the .po and .mo files are located. Create the 'locale' folder in the project folder.

    ```python
        from django.utils.translation import gettext_lazy as _

        LANGUAGES = (
            ('en', _('English')),
            ('fr', _('French')),
            ('it', _('Italian')),
            ('de', _('German')),
        )

        PARLER_LANGUAGES = {
            None: (
                {'code': 'en',}, # English
                {'code': 'fr',}, # French
                {'code': 'it',}, # Italian
                {'code': 'de',}, # German
            ),
            'default': {
                'fallbacks': ['en'],
                'hide_untranslated': False,
            }
        }


        LOCALE_PATHS = [
            BASE_DIR / 'locale/',
        ]
    ```          

4. Include the forms URLconf in your project urls.py like this::

    ```python
    path('forms/', include('forms.urls')),
    ```

5. Run ``python manage.py migrate`` to create the resource model.

6. Run ``django-admin makemessages --all`` to create the structure in the '/locale' folder as well as the .po files for the translation of the labels and templates. Current ones are available in the /locale folder.
   Once the po files are updated run ``django-admin compilemessages`` to create the .mo files

7. Start the development server and visit http://127.0.0.1:8000/admin/
   to manage the resources (you'll need the Admin app enabled). 
   Visit http://127.0.0.1:8000/newresource/ to add a new resource

8. Visit http://127.0.0.1:8000/ to see the resources. 
