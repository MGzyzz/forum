from django.db.models import Q
from django.contrib.auth import views, login, get_user_model, update_session_auth_hash
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import TemplateView, View, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView, \
    RedirectView
from accounts.models import User, Profile
from forum.forms import SearchForm, ThemeForm, CommentForm
from accounts.models import Profile
from forum.models import Theme, Comment


# Create your views here.
class Home(ListView):
    template_name = 'home.html'
    model = Theme
    context_object_name = 'themes'
    paginate_by = 5


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form

        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})

        return context

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        if self.search_value:
            print('work')
            query = Q(title__icontains=self.search_value)

            qs = qs.filter(query)

        return qs

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get('search')


class DetailTheme(ListView):
    template_name = 'detail.html'
    model = Comment
    context_object_name = 'comments'
    paginate_by = 2

    def get_queryset(self):
        theme_id = self.kwargs.get('id')
        return Comment.objects.filter(themes__id=theme_id).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        theme_id = self.kwargs.get('id')
        theme = Theme.objects.get(pk=theme_id)
        context['theme'] = theme
        return context



class AddTheme(CreateView):
    template_name = 'add.html'
    model = Theme
    form_class = ThemeForm
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'id': self.object.id})


class UploadComments(CreateView):
    template_name = 'detail.html'
    model = Comment
    context_object_name = 'comment'
    form_class = CommentForm
    pk_url_kwarg = 'id'

    def form_valid(self, form):
        user = self.request.user
        comments = form.save(commit=False)
        theme = get_object_or_404(Theme, id=self.kwargs['id'])
        comments.user = user
        comments.save()
        theme.count_answer += 1
        theme.save()

        return redirect('detail', theme.id)

    def form_invalid(self, form):
        return redirect(self.get_success_url())


