from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q, Exists, OuterRef, Count
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import ArticleForm, SearchForm
from webapp.models import Article, ArticleLike


class ArticleListView(ListView):
    model = Article
    template_name = "articles/index.html"
    ordering = ['-created_at']
    context_object_name = "articles"
    paginate_by = 5

    def dispatch(self, request, *args, **kwargs):
        print(request.user.is_authenticated, "is_authenticated")
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        form = self.form
        if form.is_valid():
            self.search_ = form.cleaned_data['search']
            return self.search_

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()

        queryset = queryset.annotate(
            likes_count=Count('articlelike'),
            user_has_liked=Exists(ArticleLike.objects.filter(
                user=user, article_id=OuterRef('pk')
            ))
        )
        if self.search_value:
            queryset = queryset.filter(
                Q(title__contains=self.search_value) | Q(author__contains=self.search_value)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form
        if self.search_value:
            context["search"] = urlencode({"search": self.search_value})
            context["search_value"] = self.search_value
        return context


class CreateArticleView(LoginRequiredMixin, CreateView):
    template_name = "articles/create_article.html"
    form_class = ArticleForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleDetailView(DetailView):
    template_name = "articles/article_detail.html"
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comments.order_by("-created_at")
        return context


class UpdateArticleView(PermissionRequiredMixin, UpdateView):
    template_name = "articles/update_article.html"
    form_class = ArticleForm
    model = Article
    permission_required = "webapp.change_article"

    def has_permission(self):
        # return self.request.user.groups.filter(name="moderators").exists()
        return super().has_permission() or self.request.user == self.get_object().author


class DeleteArticleView(PermissionRequiredMixin, DeleteView):
    template_name = "articles/delete_article.html"
    model = Article
    success_url = reverse_lazy("webapp:articles")
    permission_required = "webapp.delete_article"

    def has_permission(self):
        return super().has_permission() or self.request.user == self.get_object().author
