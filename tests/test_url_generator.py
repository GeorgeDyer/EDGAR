"""
This file tests code responsible for generating the EDGAR search URL.

Note that at the time of this writing, EDGAR double-encodes query search
parameters so that %-encoded characters, like a quote ("), are encoded
as %2520 in the browser's URL instead of %20. This is a quirk with the
SEC's search functionality. Local testing indicates that single-encoded
URLs (which is the norm) and double-encoded URLs produce the same
responses.

I.e. this double-encoded URL produced on the SEC's EDGAR search page:
  https://www.sec.gov/edgar/search/#/q=%2522Insider%2520trading%2520report%2522

is functionally equivalent to our generated URL:
  https://www.sec.gov/edgar/search/#/q=%22Insider%20trading%20report%20
"""

import datetime
import pytest

from edgar_tool import url_generator


def test_should_correctly_generate_search_url_for_single_word():
    """Baseline test to assert that querying for a single word
    produces the correct search URL"""
    # GIVEN
    keywords = ["10-K"]
    expected_url = "https://www.sec.gov/edgar/search/#/q=10-K"

    # WHEN
    actual_url = url_generator.generate_search_url_for_kwargs({"keywords": keywords})

    # THEN
    assert actual_url == expected_url


def test_should_correctly_generate_search_url_for_exact_phrase():
    # GIVEN
    keywords = ["Insider trading report"]
    expected_url = (
        "https://www.sec.gov/edgar/search/#/q=%22Insider%20trading%20report%22"
    )

    # WHEN
    actual_url = url_generator.generate_search_url_for_kwargs({"keywords": keywords})

    # THEN
    assert actual_url == expected_url


@pytest.mark.parametrize(
    "test_kwarg",
    [
        {"keywords": []},
        {"entity": []},
    ],
)
def test_should_raise_if_keywords_or_entity_missing(test_kwarg):
    # GIVEN
    expected_error_msg = (
        "Invalid search arguments. You must provide keywords or an entity."
    )

    # WHEN / THEN
    with pytest.raises(ValueError, match=expected_error_msg):
        url_generator.generate_search_url_for_kwargs(test_kwarg)


@pytest.mark.parametrize(
    "date_kwarg",
    [
        {"start_date": datetime.date.today()},
        {"end_date": datetime.date.today()},
    ],
)
def test_should_raise_if_date_range_custom_but_missing_dates(date_kwarg):
    # GIVEN
    expected_error_msg = (
        "Invalid date parameters. "
        "You must provide both a start and end date if searching a custom date range."
    )
    base_kwargs = {"keywords": ["Ford Motor Co"], "date_range_select": "custom"}
    test_kwargs = {**base_kwargs, **date_kwarg}

    # WHEN / THEN
    with pytest.raises(ValueError, match=expected_error_msg):
        url_generator.generate_search_url_for_kwargs(test_kwargs)


def test_should_raise_if_date_range_select_invalid():
    # GIVEN
    expected_error_msg = (
        "Invalid date_range_select. "
        'Value must be one of "all", "10y", "1y", "30d", or "custom"'
    )
    test_kwargs = {"keywords": ["Ford Motor Co"], "date_range_select": "1m"}

    # WHEN / THEN
    with pytest.raises(ValueError, match=expected_error_msg):
        url_generator.generate_search_url_for_kwargs(test_kwargs)


@pytest.mark.parametrize(
    "date_kwargs,url_ending",
    [
        (
            {
                "date_range_select": "custom",
                "start_date": datetime.date.fromisoformat("2024-07-10"),
                "end_date": datetime.date.fromisoformat("2024-07-15"),
            },
            "&dateRange=custom&startdt=2024-07-10&enddt=2024-07-15",
        ),
        ({"date_range_select": "all"}, "&dateRange=all"),
        ({"date_range_select": "10y"}, "&dateRange=10y"),
        ({"date_range_select": "1y"}, "&dateRange=1y"),
        ({"date_range_select": "30d"}, "&dateRange=30d"),
    ],
)
def test_generates_correct_url_for_date(date_kwargs, url_ending):
    # GIVEN
    expected_url = (
        f"https://www.sec.gov/edgar/search/#/q=%22Ford%20Motor%20Co%22{url_ending}"
    )
    test_kwargs = {**{"keywords": ["Ford Motor Co"]}, **date_kwargs}

    # WHEN
    actual_url = url_generator.generate_search_url_for_kwargs(test_kwargs)

    # THEN
    assert actual_url == expected_url
