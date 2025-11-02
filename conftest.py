import pytest


@pytest.fixture(scope="function")
def page(context):
    new_page = context.new_page()
    new_page.set_viewport_size({"width": 1280, "height": 720})
    yield new_page
    new_page.close()