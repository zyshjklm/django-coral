from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT,}),
)


urlpatterns += patterns('coral.views', 
	url(r'^login$', 'login', name='login'),
    url(r'^login_view$', 'login_view', name='login_view'),
    url(r'^logout$', 'logout', name='logout'),

	# dashboard
    url(r'^$', 'index', name='index'),
    url(r'^index$', 'index', name='index'),
    url(r'^dashboard', 'dashboard', name='dashboard'),
    url(r'^forgotpassword$', 'forgotpassword', name='forgotpassword'),

    # inbox
    url(r'^inbox', 'inbox', name='inbox'),
    url(r'^email-list', 'email_list', name='email-list'),
    url(r'^email-opened', 'email_opened', name='email-opened'),
    url(r'^email-compose', 'email_compose', name='email-compose'),
    url(r'^email-reply', 'email_reply', name='email-reply'),

    # graphs
    url(r'^flot', 'flot', name='flot'),
    url(r'^morris', 'morris', name='morris'),
	url(r'^inline-charts', 'inline_charts', name='inline-charts'),

	# table
    url(r'^table', 'table', name='table'),
    url(r'^datatables', 'datatables', name='datatables'),
    url(r'^table', 'table', name='table'),


    # forms
    url(r'^form-elements', 'form_elements', name='form-elements'),
	url(r'^form-templates', 'form_templates', name='form-templates'),
	url(r'^validation', 'validation', name='validation'),
	url(r'^bootstrap-forms', 'bootstrap_forms', name='bootstrap-forms'),
	url(r'^plugins', 'plugins', name='plugins'),
	url(r'^wizard', 'wizard', name='wizard'),
    url(r'^other-editors', 'other_editors', name='other-editors'),
    url(r'^dropzone', 'dropzone', name='dropzone'),

    # ui elements
    url(r'^general-elements', 'general_elements', name='general-elements'),
    url(r'^buttons', 'buttons', name='buttons'),
    url(r'^fa', 'fa', name='fa'),
    url(r'^glyph', 'glyph', name='glyph'),
    url(r'^grid', 'grid', name='grid'),
    url(r'^treeview', 'treeview', name='treeview'),
    url(r'^nestable-list', 'nestable_list', name='nestable-list'),
    url(r'^jqui', 'jqui', name='jqui'),
    url(r'^calendar', 'calendar', name='calendar'),

    # widgets
    url(r'^widgets', 'widgets', name='widgets'),
    
    # gallery
    url(r'^gallery', 'gallery', name='gallery'),

    # google map skins
    url(r'^gmap-xml', 'gmap_xml', name='gmap-xml'),

    # miscellaneous
    url(r'^typography', 'typography', name='typography'),
    url(r'^pricing-table', 'pricing_table', name='pricing-table'),
    url(r'^invoice', 'invoice', name='invoice'),
    #url(r'^login', 'login', name='login'),
    url(r'^register', 'register', name='register'),
    url(r'^lock', 'lock', name='lock'),
    url(r'^error404', 'error404', name='error404'),
    url(r'^error500', 'error500', name='error500'),
    url(r'^blank_', 'blank_', name='blank_'),
    url(r'^email-template', 'email_template', name='email-template'),
    url(r'^search', 'search', name='search'),
    url(r'^ckeditor', 'ckeditor', name='ckeditor'),

    # other pages
    url(r'^forum', 'forum', name='forum'),
    url(r'^forum-topic', 'forum_topic', name='forum-topic'),
    url(r'^profile', 'profile', name='profile'),
    url(r'^timeline', 'timeline', name='timeline'),






)
