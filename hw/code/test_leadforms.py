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

    def test_create_leadform(self, create_leadform_fixture_with_teardown: CreateLeadformPage):
        page = create_leadform_fixture_with_teardown
        page.fill_leadform_name(self.leadform_data['leadform_name'])
        page.fill_deco_section(
            self.leadform_data['company_name'],
            self.leadform_data['title'],
            self.leadform_data['description']
        )
        page.click_continue()
        page.fill_question_section(self.leadform_data['questions'])
        page.click_continue()
        page.click_continue()
        page.fill_settings_section()
        page.click_save()

        assert page.has_leadform(self.leadform_data['leadform_name'])

    def test_created_leadform_data(self, create_leadform_fixture_with_teardown: CreateLeadformPage):
        page = create_leadform_fixture_with_teardown
        page.fill_leadform_name(self.leadform_data['leadform_name'])
        page.fill_deco_section(
            self.leadform_data['company_name'],
            self.leadform_data['title'],
            self.leadform_data['description']
        )
        page.click_continue()
        page.fill_question_section(self.leadform_data['questions'])
        page.click_continue()
        page.click_continue()
        page.fill_settings_section()
        page.click_save()

        page.go_to_edit_leadform_page(self.leadform_data['leadform_name'])
        assert page.leadform_name_match(self.leadform_data['leadform_name'])
        assert page.company_name_match(self.leadform_data['company_name'])
        assert page.title_match(self.leadform_data['title'])
        assert page.description_match(self.leadform_data['description'])
        page.click_continue()
        for q in self.leadform_data['questions']:
            assert page.match_question(q['question'])
            assert page.match_answers(q['answers'])
        page.close_window()

    @pytest.fixture
    def edit_leadform_fixture(self):
        return EditLeadformPage(self.driver, self.leadform_data)

    @pytest.fixture
    def edit_leadform_fixture_with_teardown(self, edit_leadform_fixture: EditLeadformPage):
        yield edit_leadform_fixture
        edit_leadform_fixture.archive_leadform(self.leadform_edited_data)

    def test_edit_leadform(
        self,
        edit_leadform_fixture_with_teardown: EditLeadformPage
    ):
        page = edit_leadform_fixture_with_teardown
        page.fill_leadform_name(self.leadform_edited_data['leadform_name'])
        page.fill_deco_section(
            self.leadform_edited_data['company_name'],
            self.leadform_edited_data['title'],
            self.leadform_edited_data['description']
        )
        page.click_continue()
        page.fill_question_section(self.leadform_edited_data['questions'])
        page.click_continue()
        page.click_continue()
        page.fill_settings_section()
        page.click_save()

        assert page.has_leadform(self.leadform_edited_data['leadform_name'])
        page.go_to_edit_leadform_page(self.leadform_edited_data['leadform_name'])
        assert page.leadform_name_match(self.leadform_edited_data['leadform_name'])
        assert page.company_name_match(self.leadform_edited_data['company_name'])
        assert page.title_match(self.leadform_edited_data['title'])
        assert page.description_match(self.leadform_edited_data['description'])
        page.click_continue()
        for q in self.leadform_edited_data['questions']:
            assert page.match_question(q['question'])
            assert page.match_answers(q['answers'])
        page.close_window()

    @pytest.fixture
    def archive_leadform_fixture(self, create_leadform_fixture: CreateLeadformPage):
        create_leadform_fixture.create_leadform(self.leadform_data)
        return create_leadform_fixture

    def test_archive_leadform(self, archive_leadform_fixture: CreateLeadformPage):
        id =  archive_leadform_fixture.get_leadform_id(self.leadform_data)
        archive_leadform_fixture.archive_leadform(self.leadform_data)

        archive_leadform_fixture.go_to_archive_section()
        assert archive_leadform_fixture.has_leadform_by_id(id)
