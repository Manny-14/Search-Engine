from search import search, title_length, article_count, random_article, favorite_article, multiple_keywords, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_titles
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        # Storing into a variable so don't need to copy and paste long list every time
        # If you want to store search results into a variable like this, make sure you pass a copy of it when
        # calling a function, otherwise the original list (ie the one stored in your variable) might be
        # mutated. To make a copy, you may use the .copy() function for the variable holding your search result.
        expected_dog_search_results = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(search('dog'), expected_dog_search_results)
    
    def test_search(self):
        #check the test result of the search query: music
        expected_music_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', \
        'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        self.assertEqual(search('music'), expected_music_search_results)
        #check the test result of the search query: Musician
        #edge case to confirm the code is case insensitive
        expected_Musician_search_results = ['List of Canadian musicians', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Steve Perry (musician)', 'David Gray (musician)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Joseph Williams (musician)', 'David Levi (musician)', 'George Crum (musician)', 'Charles McPherson (musician)', 'Paul Carr (musician)', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)']
        self.assertEqual(search('Musician'), expected_Musician_search_results)
        #edge case to test an empty query
        expected_empty_search_results = []
        self.assertEqual(search(''), expected_empty_search_results)
        self.assertEqual(search('   '), [])
    def test_title_length(self):
        #check the result of a search query music with a maximum length of 15
        titles = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', \
        'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        expected_search_results = ['Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Aube (musician)', 'Old-time music', 'Arabic music', 'Aco (musician)', '1936 in music', 'Annie (musical)', '1996 in music', '2006 in music', 'Texture (music)', '2007 in music', '2008 in music']
        self.assertEqual(title_length(15, titles), expected_search_results)
        #check what gets returned if all titles in a list have lesser length than the max length
        custom_titles = ['python', 'java', 'C++', 'C*', 'javascript', 'HTML', 'CSS']
        expected_search_results = ['python', 'java', 'C++', 'C*', 'javascript', 'HTML', 'CSS']
        self.assertEqual(title_length(10, custom_titles), expected_search_results)
        #check search result if there is no article less than max length
        titles = ['List of dystopian music, TV programs, and games', 'List of computer role-playing games', 'List of video games with time travel']
        self.assertEqual(title_length(0, titles), [])


    def test_article_count(self):
        #check the test result of music plus an aadvanced search of 10 article_titles
        titles = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', \
        'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        count = 10
        expected_search_results = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)']
        self.assertEqual(article_count(count, titles), expected_search_results)
        #check the test result of team  plus an advanced search of 8 article_titles
        #since article count is greater than articles available. complete list of articles expected
        titles = ['Spain national beach soccer team', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", 'China national soccer team']
        count = 8
        expected_search_results = ['Spain national beach soccer team', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", 'China national soccer team']
        self.assertEqual(article_count(count, titles), expected_search_results)
        #check the test result with an advanced search of 0 article title_length
        titles = search('Games')
        self.assertEqual(article_count(0, titles), [])
    
    def test_random_article(self):
        #check the search result of a random_article, '1',  
        titles = ['List of dystopian music, TV programs, and games', 'List of computer role-playing games', 'List of video games with time travel']
        self.assertEqual(random_article(1, titles), 'List of computer role-playing games')
        #check the search result of a random article, '0'
        titles = ['Spain national beach soccer team', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", 'China national soccer team']
        self.assertEqual(random_article(0, titles), "Spain national beach soccer team")
        #check the return value of an invalid index
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(random_article(20, titles), '')
        titles = ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']
        self.assertEqual(random_article(-1, titles), '')
    
    def test_favorite_article(self):
        #check the return value if the users's favorite title is one of the options
        titles = ['List of Canadian musicians', 'French pop music', 'Noise (music)', '1922 in music', '1986 in music', '2009 in music', 'Rock music', 'Lights (musician)', 'List of soul musicians', 'Aube (musician)', 'List of overtone musicians', 'Tim Arnold (musician)', 'Peter Brown (music industry)', 'Old-time music', 'Arabic music', 'List of Saturday Night Live musical sketches', 'Joe Becker (musician)', 'Aco (musician)', 'Geoff Smith (British musician)', 'Richard Wright (musician)', 'Voice classification in non-classical music', '1936 in music', '1962 in country music', 'List of dystopian music, TV programs, and games', 'Steve Perry (musician)', 'David Gray (musician)', 'Annie (musical)', 'Alex Turner (musician)', 'List of gospel musicians', 'Tom Hooper (musician)', 'Indian classical music', '1996 in music', \
        'Joseph Williams (musician)', 'The Hunchback of Notre Dame (musical)', 'English folk music (1500–1899)', 'David Levi (musician)', 'George Crum (musician)', 'Traditional Thai musical instruments', 'Charles McPherson (musician)', 'Les Cousins (music club)', 'Paul Carr (musician)', '2006 in music', 'Sean Delaney (musician)', 'Tony Kaye (musician)', 'Danja (musician)', 'Texture (music)', 'Register (music)', '2007 in music', '2008 in music']
        self.assertEqual(favorite_article('2009 in music', titles), True)
        #check the return value if the user's favorite is a keyword of one or more of the titles available
        #expect the code to return False
        titles = ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']
        self.assertEqual(favorite_article('computer', titles), False)
        #testing to ensure code is case insensitive
        titles = ['Spain national beach soccer team', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", 'China national soccer team']
        self.assertEqual(favorite_article('2009 LOUISIANA tech BULLDOGS fOoTbAlL team', titles), True)
        #check the return value of a non existent title
        titles = ['Medical value travel', 'Time travel', 'List of video games with time travel']
        self.assertEqual(favorite_article('The boy from Nigeria', titles), False)
    
    def test_multiple_keywords(self):
        #check the return value of keywords games and team
        titles = ['List of dystopian music, TV programs, and games', 'List of computer role-playing games', 'List of video games with time travel']
        expected_search_results = ['List of dystopian music, TV programs, and games', 'List of computer role-playing games', 'List of video games with time travel', 'Spain national beach soccer team', '2009 Louisiana Tech Bulldogs football team', "United States men's national soccer team 2009 results", 'China national soccer team']
        self.assertEqual(multiple_keywords('team', titles), expected_search_results)
        #check to ensure that no title is added if user inputs an empty keyword
        titles = ['Covariance and contravariance (computer science)', 'Solver (computer science)']
        self.assertEqual(multiple_keywords('', titles), titles)
        #check to ensure that no title is added if user inputs an invalid keyword
        titles = ['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']
        self.assertEqual(multiple_keywords('Sunshine', titles), titles)


    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'dog'
        advanced_option = 6

        # Output of calling display_results() with given user input. If a different
        # advanced option is included, append further user input to this list (after `advanced_option`)
        output = get_print(input_mock, [keyword, advanced_option])
        # Expected print outs from running display_results() with above user input
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + "\nHere are your articles: ['Edogawa, Tokyo', 'Kevin Cadogan', 'Endogenous cannabinoid', 'Black dog (ghost)', '2007 Bulldogs RLFC season', 'Mexican dog-faced bat', 'Dalmatian (dog)', 'Guide dog', '2009 Louisiana Tech Bulldogs football team', 'Georgia Bulldogs football', 'Endoglin', 'Sun dog', 'The Mandogs', 'Georgia Bulldogs football under Robert Winston', 'Landseer (dog)']\n"

        # Test whether calling display_results() with given user input equals expected printout
        self.assertEqual(output, expected)
    
    #Testing the integration test without any advanced option
    @patch('builtins.input')
    def test_music_no_advanced(self, input_mock):
        keyword = 'computer'
        advanced_option = 6
        articles = "['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)']"
        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n{}\nHere are your articles: {}\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option), articles)
        self.maxDiff = None
        self.assertEqual(output, expected)
    
    #Testing the code including title length to the search query
    @patch('builtins.input')
    def test_games_advanced_1(self, input_mock):
        keyword = 'games'
        advanced_option = 1
        articles = "['List of computer role-playing games']"
        output = get_print(input_mock, [keyword, advanced_option, 35])
        expected = "{}{}\n{}{}\n{}35\n\nHere are your articles: {}\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option), articles)
        self.maxDiff = None
        self.assertEqual(output, expected)
    
    #Testing the code including article count as a search query
    @patch('builtins.input')
    def test_teams_advanced_2(self, input_mock):
        keyword = 'team'
        advanced_option = 2
        articles = "['Spain national beach soccer team', '2009 Louisiana Tech Bulldogs football team', \"United States men's national soccer team 2009 results\"]"
        output = get_print(input_mock, [keyword, advanced_option, 3])
        expected = "{}{}\n{}{}\n{}3\n\nHere are your articles: {}\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option), articles)
        self.maxDiff = None
        self.assertEqual(output, expected)
    
    #Testing the code to see what random article gets printed
    @patch('builtins.input')
    def test_musician_advanced_3(self, input_mock):
        keyword = 'musician'
        advanced_option = 3
        articles = 'Tim Arnold (musician)'
        output = get_print(input_mock, [keyword, advanced_option, 5])
        expected = "{}{}\n{}{}\n{}5\n\nHere are your articles: {}\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option), articles)
        self.maxDiff = None
        self.assertEqual(output, expected)
    
    #Testing the code to see how the favorite article function works
    @patch('builtins.input')
    def test_soccer_advanced_4(self, input_mock):
        keyword = 'soccer'
        advanced_option = 4
        articles = "['Spain national beach soccer team', 'Will Johnson (soccer)', 'Steven Cohen (soccer)', 'Craig Martin (soccer)', \"United States men's national soccer team 2009 results\", 'China national soccer team', \"Wake Forest Demon Deacons men's soccer\"]"
        output = get_print(input_mock, [keyword, advanced_option, 'Spain national beach soccer team'])
        expected = "{}{}\n{}{}\n{}Spain national beach soccer team\n\nHere are your articles: {}\nYour favorite article is in the returned articles!\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option), articles)
        self.maxDiff = None
        self.assertEqual(output, expected)
   
    @patch('builtins.input')
    def test_computer_advanced_5(self, input_mock):
        keyword = 'computer'
        advanced_option = 5
        articles = "['Ken Kennedy (computer scientist)', 'Human computer', 'Single-board computer', 'Covariance and contravariance (computer science)', 'Personal computer', 'Scores (computer virus)', 'Solver (computer science)', 'Spawning (computer gaming)', 'List of computer role-playing games', 'Mode (computer interface)', 'List of dystopian music, TV programs, and games', 'List of computer role-playing games', 'List of video games with time travel']"
        output = get_print(input_mock, [keyword, advanced_option, 'games'])
        expected = "{}{}\n{}{}\n{}games\n\nHere are your articles: {}\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option), articles)
        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_teams_advanced_6(self, input_mock):
        keyword = 'Nigeria'
        advanced_option = 6
        articles = ''
        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n\nNo articles found\n".format(print_basic(), keyword, print_advanced(), advanced_option, print_advanced_option(advanced_option))
        self.maxDiff = None
        self.assertEqual(output, expected)

# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
