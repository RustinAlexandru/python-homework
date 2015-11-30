from django.forms import Form, CharField, Textarea, TextInput


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5}),
        label="Enter your post here")
    author = CharField(widget=TextInput(),
         label="Author")

class UserCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 80, 'rows': 5}),
        label="Enter your comment here")
    author = CharField(widget=TextInput(),
        required=False, label="Author")
