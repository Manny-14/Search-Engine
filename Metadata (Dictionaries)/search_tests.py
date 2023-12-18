from search import keyword_to_titles, title_to_info, search, article_length,key_by_author, filter_to_author, filter_out, articles_from_year
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        dummy_keyword_dict = {
            'cat': ['title1', 'title2', 'title3'],
            'dog': ['title3', 'title4']
        }
        expected_search_results = ['title3', 'title4']
        self.assertEqual(search('dog', dummy_keyword_dict), expected_search_results)

    def test_keyword_to_titles(self):
        #dummy metadata contains a 2D list, mimics the structure from wiki.py
        dummy_metadata = [['Lonely at the top', 'Asake', 1684580361, 1515, ['music', 'amapiano', 'artist', 'afrobeats', 'asake']],
        ['Last Last', 'Burna Boy', 1652439561, 1778, ['afrobeats', 'music', 'artist', 'oluwaburna']]
        ]
        expected_search_results = {
            'music': ['Lonely at the top', 'Last Last'],
            'amapiano': ['Lonely at the top'],
            'artist':  ['Lonely at the top', 'Last Last'],
            'afrobeats': ['Lonely at the top', 'Last Last'],
            'asake': ['Lonely at the top'],
            'oluwaburna': ['Last Last'],
        }
        
        self.assertEqual(keyword_to_titles(dummy_metadata), expected_search_results)
        dummy_metadata = [['No Brainer', 'Jeff Kiney', 1698145161, 15000, ['book', 'greg', 'diary', 'wimpy']]]
        expected_search_results = {
            'book': ['No Brainer'],
            'greg': ['No Brainer'],
            'diary': ['No Brainer'],
            'wimpy': ['No Brainer']
        }
        self.assertEqual(keyword_to_titles(dummy_metadata), expected_search_results)
        self.assertEqual(keyword_to_titles([]), {})
    
    def test_title_to_info(self):
        #create dummy meta data to test the function's functionality
        dummy_metadata = [['Lonely at the top', 'Asake', 1684580361, 1515, ['music', 'amapiano', 'artist', 'afrobeats', 'asake']],
        ['Last Last', 'Burna Boy', 1652439561, 1778, ['afrobeats', 'music', 'artist', 'oluwaburna']]
        ]
        expected_search_results = {
            'Lonely at the top': {'author': 'Asake', 'timestamp': 1684580361, 'length': 1515},
            'Last Last': {'author': 'Burna Boy', 'timestamp':1652439561, 'length': 1778}
        }
        self.assertEqual(title_to_info(dummy_metadata), expected_search_results)
        dummy_metadata = [['No Brainer', 'Jeff Kiney', 1698145161, 15000, ['book', 'greg', 'diary', 'wimpy']]]
        expected_search_results = {'No Brainer': {'author': 'Jeff Kiney', 'timestamp': 1698145161, 'length': 15000 }}
        self.assertEqual(title_to_info(dummy_metadata), expected_search_results)
        self.assertEqual(keyword_to_titles([]), {})
    
    def test_search(self):
        keyword_to_title = {
            'music': ['Lonely at the top', 'Last Last', 'Sunshine', 'City boys'],
            'amapiano': ['Lonely at the top'],
            'artist':  ['Lonely at the top', 'Last Last'],
            'afrobeats': ['Lonely at the top', 'Last Last'],
            'asake': ['Lonely at the top'],
            'oluwaburna': ['Last Last', 'City boys']
        }
        expected_search_results = ['Lonely at the top', 'Last Last', 'Sunshine', 'City boys']
        self.assertEqual(search('music', keyword_to_title), expected_search_results)
        self.assertEqual(search('oluwaburna', keyword_to_title), ['Last Last', 'City boys'])
        self.assertEqual(search('', keyword_to_title), [])
        self.assertEqual(search('soweto', keyword_to_title), [])

    def test_article_length(self):
        keyword_to_titles_dict = keyword_to_titles(article_metadata())
        title_to_info_dict = title_to_info(article_metadata())

        output = article_length(10000, search('music', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = [
            'French pop music', 
            '1986 in music', 
            'Kevin Cadogan', 
            'Lights (musician)', 
            'Tim Arnold (musician)', 
            'Joe Becker (musician)', 
            '1962 in country music', 
            'David Gray (musician)', 
            'Alex Turner (musician)', 
            'List of gospel musicians', 
            'Indian classical music', 
            'Traditional Thai musical instruments', 
            'Tony Kaye (musician)', 
            'Texture (music)'
            ]
        self.assertEqual(output, expected_search_results)

        output = article_length(10000, search('dog', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = ['Mexican dog-faced bat', 'Guide dog']
        self.assertEqual(output, expected_search_results)
        #testing to see the result when the keyword is invalid
        output = article_length(20000, search('', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, [])

        #testing the results when the max length given is bigger than the length of each article
        #Expect each item in the list to get returned
        output = article_length(100000, search('team', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = [
            'USC Trojans volleyball', 
            'Will Johnson (soccer)', 
            '2009 Louisiana Tech Bulldogs football team', 
            'Georgia Bulldogs football', 
            'Spawning (computer gaming)', 
            "Wake Forest Demon Deacons men's soccer"
            ]
        self.assertEqual(output, expected_search_results)

        #testing the result when the max length given is smaller than the length of each article
        #Expect an empty list 
        output = article_length(1000, search('games', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, [])

    def test_key_by_author(self):
        keyword_to_titles_dict = keyword_to_titles(article_metadata())
        title_to_info_dict = title_to_info(article_metadata())
        output = key_by_author(search('dog', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = {
            'Pegship': ['Black dog (ghost)'], 
            'Mack Johnson': ['Mexican dog-faced bat'], 
            'Mr Jake': ['Dalmatian (dog)', 'Sun dog'], 
            'Jack Johnson': ['Guide dog']
            }
        self.assertEqual(output, expected_search_results)

        output = key_by_author(search('soccer', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = {
            'jack johnson': ['Spain national beach soccer team'], 
            'Burna Boy': ['Will Johnson (soccer)'], 
            'Mack Johnson': ['Steven Cohen (soccer)']
            }
        self.assertEqual(output, expected_search_results)

        #test to see output when keyword is invalid
        output = key_by_author(search('Asake', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, {})

    def test_filter_to_author(self):
        keyword_to_titles_dict = keyword_to_titles(article_metadata())
        title_to_info_dict = title_to_info(article_metadata())

        output = filter_to_author('Burna Boy', search('music', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = ['Lights (musician)', 'Indian classical music', 'Tony Kaye (musician)', '2008 in music']
        self.assertEqual(output, expected_search_results)

        output = filter_to_author('Nihonjoe', search('team', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = ['2009 Louisiana Tech Bulldogs football team']
        self.assertEqual(output, expected_search_results)

        #test the result of an invalid author
        output = filter_to_author('Asake', search('music', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, [])

        #test the result of an empty input
        output = filter_to_author('', search('soccer', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, [])
    
    def test_filter_out(self):
        keyword_to_titles_dict = keyword_to_titles(article_metadata())

        output = filter_out('music', search('musician', keyword_to_titles_dict), keyword_to_titles_dict)
        expected_search_results = ['List of overtone musicians']
        self.assertEqual(output, expected_search_results)

        output = filter_out('beach', search('soccer', keyword_to_titles_dict), keyword_to_titles_dict)
        expected_search_results = ['Will Johnson (soccer)', 'Steven Cohen (soccer)']
        self.assertEqual(output, expected_search_results)

        #test to see the result when an invalid keyword is entered
        output = filter_out('Asake', search('musician', keyword_to_titles_dict), keyword_to_titles_dict)
        expected_search_results = search('musician', keyword_to_titles_dict)
        self.assertEqual(output, expected_search_results)

        #test to see when an empty keyword is enterd
        output = filter_out('', search('dog', keyword_to_titles_dict), keyword_to_titles_dict)
        expected_search_results = search('dog', keyword_to_titles_dict)
        self.assertEqual(output, expected_search_results)

    def test_articles_from_year(self):
        keyword_to_titles_dict = keyword_to_titles(article_metadata())
        title_to_info_dict = title_to_info(article_metadata())

        output = articles_from_year(2009, search('music', keyword_to_titles_dict), title_to_info_dict)
        expected_search_results = [
            '1922 in music', 
            '2009 in music', 
            'Rock music', 
            '1936 in music', 
            '1962 in country music', 
            'Steve Perry (musician)'
            ]
        self.assertEqual(output, expected_search_results)

        output = articles_from_year(2007, search('games', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, ['Spawning (computer gaming)'])

        #test to see the result of an invalid year
        output = articles_from_year(2023, search('music', keyword_to_titles_dict), title_to_info_dict)
        self.assertEqual(output, [])
        
    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 5
        advanced_response = 2009

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: ['Spain national beach soccer team', 'Steven Cohen (soccer)']\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_integration_no_advanced(self, input_mock):
        keyword = 'team'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n\nHere are your articles: ['USC Trojans volleyball', 'Will Johnson (soccer)', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Spawning (computer gaming)', \"Wake Forest Demon Deacons men's soccer\"]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option))

        self.maxDiff = None
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_title_length_integration(self, input_mock):
        keyword = 'music'
        advanced_option = 1
        advanced_response = 10000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: ['French pop music', '1986 in music', 'Kevin Cadogan', 'Lights (musician)', 'Tim Arnold (musician)', 'Joe Becker (musician)', '1962 in country music', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Indian classical music', 'Traditional Thai musical instruments', 'Tony Kaye (musician)', 'Texture (music)']\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_search_key_by_author_(self, input_mock):
        keyword = 'games'
        advanced_option = 2

        output = get_print(input_mock, [keyword, advanced_option])
        articles = {'Bearcat': ['List of dystopian music, TV programs, and games'], 'Burna Boy': ['Georgia Bulldogs football'], 'jack johnson': ['Spawning (computer gaming)']}
        expected = "{}{}\n{}{}\n\nHere are your articles: {}\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), articles)

        self.maxDiff = None
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_filter_to_author_integration(self, input_mock):
        keyword = 'music'
        advanced_option = 3
        advanced_response = 'Burna Boy'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: ['Lights (musician)', 'Indian classical music', 'Tony Kaye (musician)', '2008 in music']\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_search_filter_out_integration(self, input_mock):
        keyword = 'soccer'
        advanced_option = 4
        advanced_response = 'beach'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: ['Will Johnson (soccer)', 'Steven Cohen (soccer)']\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)

    #integration test to confirm output when no articles are found
    @patch('builtins.input')
    def test_search_integration_invalid_article(self, input_mock):
        keyword = 'Asake'
        advanced_option = 6

        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n\nNo articles found\n".format(print_basic(), keyword, print_advanced(), str(advanced_option))

        self.maxDiff = None
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
