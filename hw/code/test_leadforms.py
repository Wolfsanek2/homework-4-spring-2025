from test_vk_ads import BaseCase
from pytest import fixture
from ui.pages.leadforms_page import LeadformsPage, CreateLeadformPage, EditLeadformPage
import time
import pytest

class TestLeadforms(BaseCase):
    leadform_data={
        'company_name': 'Тестовая компания',
        'title': 'Тестовый заголовок',
        'description': 'Тестовое описание',
        'questions': [{
            'question': 'Тестовый вопрос',
            'answers': ['Тестовый ответ 1', 'Тестовый ответ 2']
        }],
        'leadform_name': 'Тестовая лидформа'
    }

    leadform_edited_data={
        'company_name': 'Измененная тестовая компания',
        'title': 'Измененный тестовый заголовок',
        'description': 'Измененное тестовое описание',
        'questions': [{
            'question': 'Измененный тестовый вопрос',
            'answers': ['Измененный тестовый ответ 1', ' Измененный тестовый ответ 2']
        }],
        'leadform_name': 'Измененная тестовая лидформа'
    }

    @fixture(scope='function')
    def leadforms_page(self):
        driver = self.driver
        driver.get(LeadformsPage.url)
        return LeadformsPage(driver)

    @pytest.fixture
    def create_leadform_fixture(self):
        return CreateLeadformPage(self.driver)

    @pytest.fixture
    def create_leadform_fixture_with_teardown(self, create_leadform_fixture: CreateLeadformPage):
        yield create_leadform_fixture
        create_leadform_fixture.archive_leadform(self.leadform_data)

    @pytest.fixture
    def edit_leadform_fixture(self):
        return EditLeadformPage(self.driver, self.leadform_data)

    @pytest.fixture
    def edit_leadform_fixture_with_teardown(self, edit_leadform_fixture: EditLeadformPage):
        yield edit_leadform_fixture
        edit_leadform_fixture.archive_leadform(self.leadform_edited_data)

    def test_create_leadform(self, create_leadform_fixture_with_teardown: CreateLeadformPage):
        create_leadform_fixture_with_teardown.create_leadform(self.leadform_data)
        assert create_leadform_fixture_with_teardown.is_leadform_created(self.leadform_data)

    def test_edit_leadform(
        self,
        edit_leadform_fixture_with_teardown: EditLeadformPage
    ):
        edit_leadform_fixture_with_teardown.edit_leadform(self.leadform_edited_data)
        assert edit_leadform_fixture_with_teardown.is_leadform_edited(self.leadform_edited_data)

    def test_archive_leadform(self, create_leadform_fixture: CreateLeadformPage):
        create_leadform_fixture.create_leadform(self.leadform_data)
        id =  create_leadform_fixture.get_leadform_id(self.leadform_data)
        create_leadform_fixture.archive_leadform(self.leadform_data)
        assert create_leadform_fixture.is_leadform_archived(id)
