from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import F, Q, constraints

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                              related_name='posts', blank=True, null=True)

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_author')

    class Meta:
        constraints = [constraints.UniqueConstraint(
            fields=['user', 'following'], name='Subscription_must_be_unique'),
            models.CheckConstraint(
                check=~Q(user=F('following')),
                name='User_and_following_can_not_be_equal'
        )]

    def __str__(self) -> str:
        return f'{self.user} follows {self.following}'
