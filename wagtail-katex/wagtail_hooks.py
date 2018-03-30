"""
Registers the functions for our plugin.
On loading, Wagtail will find this file and execute the contents.
"""
from __future__ import unicode_literals

# Django imports
from django.conf import settings
from django.utils.html import format_html, format_html_join

# Wagtail core imports
from wagtail.core import hooks


@hooks.register('insert_editor_js')
def editor_js():
    """
    Adds additional JavaScript files or code snippets to the page editor.
    For Draftail plugins, add 'wagtailadmin/js/draftail.js' to the beginning of your js_files array
    """
    print(f"******* Installing the wagtail-katex draftail plugin")
    js_files = [
        'wagtailadmin/js/draftail.js',
        'wagtail-katex.bundle.js',
    ]
    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
        ((settings.STATIC_URL, filename) for filename in js_files)
    )
    return js_includes + format_html(
        """
        <script></script>
        """
    )

print(f"******* Setup hooks for the wagtail-katex draftail plugin")

