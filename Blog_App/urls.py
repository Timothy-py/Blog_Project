from django.urls import path
from Blog_App import views
from User_Registration_App import views as user_reg_app_views

app_name =  'Blog_App'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('userpostlist/<str:username>', views.UserPostListView.as_view(), name='user_post_list'),
    path('about/', views.AboutView.as_view(),name="about"),
    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/remove', views.PostDeleteView.as_view(), name='post_remove'),
    path('drafts', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name="add_comment_to_post"),
    # path('comment/<int:pk>/reply', views.add_reply_to_comment, name='reply_comment'),
    path('comment/<int:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove', views.comment_remove, name='comment_remove'),
    path('post/<int:pk>/publish', views.post_publish, name='post_publish'),
    path('comment/<int:pk>/edit', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('profile/<int:pk>', user_reg_app_views.user_profile, name='profile'),
]
