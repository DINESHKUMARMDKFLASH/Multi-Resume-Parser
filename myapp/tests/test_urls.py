from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import index, view, update, resume, curview, edit, delete, addmore, welcome


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_view_url_is_resolved(self):
        url = reverse('view')
        self.assertEquals(resolve(url).func, view)

    def test_update_url_is_resolved(self):
        url = reverse('update', args=[1])
        self.assertEquals(resolve(url).func, update)

    def test_resume_url_is_resolved(self):
        url = reverse('resume')
        self.assertEquals(resolve(url).func, resume)

    def test_curview_url_is_resolved(self):
        url = reverse('curview', args=[1])
        self.assertEquals(resolve(url).func, curview)

    def test_edit_url_is_resolved(self):
        url = reverse('edit', args=[1])
        self.assertEquals(resolve(url).func, edit)

    def test_delete_url_is_resolved(self):
        url = reverse('delete', args=[1])
        self.assertEquals(resolve(url).func, delete)

    def test_addmore_url_is_resolved(self):
        url = reverse('addmore')
        self.assertEquals(resolve(url).func, addmore)

    def test_welcome_url_is_resolved(self):
        url = reverse('welcome')
        self.assertEquals(resolve(url).func, welcome)
