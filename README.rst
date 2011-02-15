Links (bookmarks)
=================

django-links is the simplest Django app which keeps a list of bookmarks.

Features
--------

* An optional description for each link.
* Links organized into categories.

Installation
------------

Install from github using ``pip``::

    pip install -e git+git://github.com/whiskybar/django-links#egg=django-links

Configuration
-------------

Add ``'links'`` to your ``INSTALLED_APPS`` in ``settings.py`` of your project::

    INSTALLED_APPS = (
        ...
        'links',
    )

Add the following context processor to your ``settings.py``::

    TEMPLATE_CONTEXT_PROCESSORS = (
        ...
        'links.context_processors.categories',
    )

Do not forget to run ``syncdb`` to create the corresponding tables.


Usage
-----

I use the following HTML fragment to list my links in templates::

    {% for category in categories %}
    <li>
        <h2>{{ category }}</h2>
        <ul>
        {% for link in category.link_set.all %}
            <li{% if link.description %} title="{{ link.description }}"{% endif %}>
            {% if link.url %}
                <a href="{{ link.url }}" target="_blank">{{ link }}</a>
            {% else %}
                {{ link }}
            {% endif %}
            </li>
        {% endfor %}
        </ul>
    </li>
    {% endfor %}


