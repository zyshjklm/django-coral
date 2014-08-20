from django.shortcuts import render_to_response, render, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect

from django.contrib import auth

#def login_auth(request):
#	username = request.POST['username']
#	password = request.POST['password']
#	user = auth.authenticate(username=username, password=password)
#	print user,'---'
#	if not user is None:
#		return HttpResponseRedirect('/index')
#	else:
#		return HttpResponseRedirect('/login')

def login_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect("/index")
	else:
		return HttpResponseRedirect("/login")

@csrf_protect
def login(request):
	return render_to_response('login.html', context_instance=RequestContext(request))

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect("/login")

# dashboard
def index(request):
	#print request.user,'---'
	if request.user.is_authenticated():
		username = request.user
		return render_to_response('index.html', {'username': username})
	else:
		return HttpResponseRedirect('/login')

def dashboard(request):
	username = request.user
	return render_to_response('ajax/dashboard.html', {'username': username})


def forgotpassword(request):
	return render_to_response('forgotpassword.html')



# inbox
def inbox(request):
	return render_to_response('ajax/inbox.html')

def email_list(request):
	return render_to_response('ajax/email/email-list.html')

def email_opened(request):
	return render_to_response('ajax/email-opened.html')

def email_compose(request):
	return render_to_response('ajax/email/email-compose.html')

def email_reply(request):
	return render_to_response('ajax/email-reply.html')


# graphs
def flot(request):
	return render_to_response('ajax/flot.html')

def morris(request):
	return render_to_response('ajax/morris.html')

def inline_charts(request):
	return render_to_response('ajax/inline-charts.html')


# table
def table(request):
	return render_to_response('ajax/table.html')

def datatables(request):
	return render_to_response('ajax/datatables.html')


# forms
def form_elements(request):
	return render_to_response('ajax/form-elements.html')

def form_templates(request):
	return render_to_response('ajax/form-templates.html')

def validation(request):
	return render_to_response('ajax/validation.html')

def bootstrap_forms(request):
	return render_to_response('ajax/bootstrap-forms.html')

def plugins(request):
	return render_to_response('ajax/plugins.html')

def wizard(request):
	return render_to_response('ajax/wizard.html')

def other_editors(request):
	return render_to_response('ajax/other-editors.html')

def dropzone(request):
	return render_to_response('ajax/dropzone.html')

# ui elements
def general_elements(request):
	return render_to_response('ajax/general-elements.html')

def buttons(request):
	return render_to_response('ajax/buttons.html')

def fa(request):
	return render_to_response('ajax/fa.html')

def glyph(request):
	return render_to_response('ajax/glyph.html')

def grid(request):
	return render_to_response('ajax/grid.html')

def treeview(request):
	return render_to_response('ajax/treeview.html')

def nestable_list(request):
	return render_to_response('ajax/nestable-list.html')

def jqui(request):
	return render_to_response('ajax/jqui.html')


# calendar
def calendar(request):
	return render_to_response('ajax/calendar.html')


# widgets
def widgets(request):
	return render_to_response('ajax/widgets.html')


# gallery
def gallery(request):
	return render_to_response('ajax/gallery.html')


# google map skins
def gmap_xml(request):
	return render_to_response('ajax/gmap-xml.html')


# miscellaneous
def typography(request):
	return render_to_response('ajax/typography.html')

def pricing_table(request):
	return render_to_response('ajax/pricing-table.html')

def invoice(request):
	return render_to_response('ajax/invoice.html')

#def login(request):
#	return render_to_response('ajax/login.html')

def register(request):
	return render_to_response('register.html')

def lock(request):
	return render_to_response('lock.html')

def error404(request):
	return render_to_response('ajax/error404.html')

def error500(request):
	return render_to_response('ajax/error500.html')

def blank_(request):
	return render_to_response('ajax/blank_.html')

def email_template(request):
	return render_to_response('ajax/email-template.html')

def search(request):
	return render_to_response('ajax/search.html')

def ckeditor(request):
	return render_to_response('ajax/ckeditor.html')


# other pages
def forum(request):
	return render_to_response('ajax/forum.html')

def forum_topic(request):
	return render_to_response('ajax/forum-topic.html')

def profile(request):
	return render_to_response('ajax/profile.html')

def timeline(request):
	return render_to_response('ajax/timeline.html')









