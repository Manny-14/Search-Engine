from search import search, article_length, unique_authors, most_recent_article, favorite_author, title_and_author, refine_search, display_result
from search_tests_helper import get_print, print_basic, print_advanced, print_advanced_option
from wiki import article_metadata
from unittest.mock import patch
from unittest import TestCase, main

class TestSearch(TestCase):

    ##############
    # UNIT TESTS #
    ##############

    def test_example_unit_test(self):
        expected_search_soccer_results = [
            ['Spain national beach soccer team', 'jack johnson', 1233458894, 1526],
            ['Will Johnson (soccer)', 'Burna Boy', 1218489712, 3562],
            ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]
        ]
        self.assertEqual(search('soccer'), expected_search_soccer_results)

    def test_search(self):
        
        #test the result of the seach query music
        expected_search_music_results = [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], 
            ['French pop music', 'Mack Johnson', 1172208041, 5569], 
            ['Noise (music)', 'jack johnson', 1194207604, 15641], 
            ['1922 in music', 'Gary King', 1242717698, 11576], 
            ['1986 in music', 'jack johnson', 1048918054, 6632], 
            ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], 
            ['2009 in music', 'RussBot', 1235133583, 69451], 
            ['Rock music', 'Mack Johnson', 1258069053, 119498], 
            ['Lights (musician)', 'Burna Boy', 1213914297, 5898], 
            ['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], 
            ['Old-time music', 'Nihonjoe', 1124771619, 12755], 
            ['Arabic music', 'RussBot', 1209417864, 25114], 
            ['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], 
            ['Richard Wright (musician)', 'RussBot', 1189536295, 16185], 
            ['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], 
            ['1936 in music', 'RussBot', 1243745950, 23417], 
            ['1962 in country music', 'Mack Johnson', 1249862464, 7954], 
            ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], 
            ['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], 
            ['David Gray (musician)', 'jack johnson', 1159841492, 7203], 
            ['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], 
            ['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], 
            ['Indian classical music', 'Burna Boy', 1222543238, 9503], 
            ['1996 in music', 'Nihonjoe', 1148585201, 21688], 
            ['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], 
            ['2006 in music', 'Jack Johnson', 1171547747, 105280], 
            ['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], 
            ['Texture (music)', 'Bearcat', 1161070178, 3626], 
            ['2007 in music', 'Bearcat', 1169248845, 45652], 
            ['2008 in music', 'Burna Boy', 1217641857, 107605]
            ]
        self.assertEqual(search('music'), expected_search_music_results)
        #testing the code to see the result of an empty keyword search
        self.assertEqual(search(''), [])
        
        #testing case sensitivity
        expected_results = [
            ['Ken Kennedy (computer scientist)', 'Mack Johnson', 1246308670, 4144], 
            ['Human computer', 'Bearcat', 1248275178, 4750], 
            ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], 
            ['Single-board computer', 'Gary King', 1220260601, 8271], 
            ['Personal computer', 'Pegship', 1220391790, 45663], 
            ['Digital photography', 'Mr Jake', 1095727840, 18093], 
            ['Mode (computer interface)', 'Pegship', 1182732608, 2991]
            ]
        self.assertEqual(search('COMPUTER'), expected_results)

    def test_article_length(self):
        output = article_length(15000, search('dog'))
        expected_results = [
            ['Black dog (ghost)', 'Pegship', 1220471117, 14746], 
            ['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138], 
            ['Guide dog', 'Jack Johnson', 1165601603, 7339]
            ]
        self.assertEqual(output, expected_results)
        #test the results when the max article length exceeds each article length in the meta data
        output = article_length(50000, search('games'))
        expected_results = search('games')
        self.assertEqual(output, expected_results)
        #test to confirm result when max article length is smaller than all article length in metadata
        output = article_length(200, search('music'))
        self.assertEqual(output, [])
    
    def test_unique_authors(self):
        output = unique_authors(5, search('music'))
        expected_results = [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], 
            ['French pop music', 'Mack Johnson', 1172208041, 5569], 
            ['1922 in music', 'Gary King', 1242717698, 11576], 
            ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], 
            ['2009 in music', 'RussBot', 1235133583, 69451]
            ]
        self.assertEqual(output, expected_results)
        #testing result if requested count is more than available unique_authors 
        output = unique_authors(40, search('music'))
        expected_results = [
            ['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], 
            ['French pop music', 'Mack Johnson', 1172208041, 5569], 
            ['1922 in music', 'Gary King', 1242717698, 11576], 
            ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], 
            ['2009 in music', 'RussBot', 1235133583, 69451], 
            ['Lights (musician)', 'Burna Boy', 1213914297, 5898], 
            ['Old-time music', 'Nihonjoe', 1124771619, 12755], 
            ['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]
            ]
        self.assertEqual(output, expected_results)
        #testing the result if the user inputs Zero
        output = unique_authors(0, 'team')
        self.assertEqual(output, [])
    
    def test_most_recent_article(self):
        output = most_recent_article(search('team'))
        expected_results = ["Wake Forest Demon Deacons men's soccer", 'Burna Boy', 1260577388, 26745]
        self.assertEqual(output, expected_results)

        #test to see the result if the parameter is an empty list
        self.assertEqual(search('Asake'), [])

        #test to see what happens if there are more than one most recent article
        #expect the first article that got reiterated over to get returned
        makeshift_metadata = [
            ['Lights (musician)', 'Burna Boy', 1213914297, 5898], 
            ['Old-time music', 'Nihonjoe', 11247716193, 12755], 
            ['List of dystopian music, TV programs, and games', 'Bearcat', 11247716193, 13458]
        ]
        output = most_recent_article(makeshift_metadata)
        expected_results = ['Old-time music', 'Nihonjoe', 11247716193, 12755]
        self.assertEqual(output, expected_results)
        
    def test_favorite_author(self):
        output = favorite_author('Burna Boy', search('music'))
        self.assertEqual(output, True)
        #test case sensitivity
        #expect function to  be case insensitive
        output = favorite_author("BURNA boy", search('music'))
        self.assertEqual(output, True) 

        #test invalid favorite_author
        output = favorite_author('Asake', search('music'))
        self.assertEqual(output, False)
        output = favorite_author('Zuckeberg', search('computer'))
        self.assertEqual(output, False)

        #test result if the user returns an empty string
        output = favorite_author('', search('games'))
        self.assertEqual(output, False)

    def test_title_and_author(self):
        output = title_and_author(search('team'))
        expected_results = [('USC Trojans volleyball', 'jack johnson'), ('Will Johnson (soccer)', 'Burna Boy'), ('2009 Louisiana Tech Bulldogs football team', 'Nihonjoe'), ('Georgia Bulldogs football', 'Burna Boy'), ('Spawning (computer gaming)', 'jack johnson'), ("Wake Forest Demon Deacons men's soccer", 'Burna Boy')]
        self.assertEqual(output, expected_results)

        output = title_and_author(search('games'))
        expected_results = [
            ('List of dystopian music, TV programs, and games', 'Bearcat'), 
            ('Georgia Bulldogs football', 'Burna Boy'), 
            ('Spawning (computer gaming)', 'jack johnson')
            ]
        self.assertEqual(output, expected_results)

        #test to see the result if the parameter is an empty list
        output = title_and_author([])
        expected_results = []
        self.assertEqual(output, expected_results)
    
    def test_refine_search(self):
        output = refine_search('game', search('music'))
        expected_results = [['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458]]
        self.assertEqual(output, expected_results)

        output = refine_search('team', search('game'))
        expected_results = [
            ['Georgia Bulldogs football', 'Burna Boy', 1166567889, 43718], 
            ['Spawning (computer gaming)', 'jack johnson', 1176750529, 3413]
            ]
        self.assertEqual(output, expected_results)

        #test to see the result when the user fails to input a second keyword or an invalid keyword
        output = refine_search('', search('team'))
        self.assertEqual(output, [])
        output = refine_search('Asake', search('music'))
        self.assertEqual(output, [])
        output = refine_search('music', search('afrobeats'))
        self.assertEqual(output, [])

    #####################
    # INTEGRATION TESTS #
    #####################

    @patch('builtins.input')
    def test_example_integration_test(self, input_mock):
        keyword = 'soccer'
        advanced_option = 1
        advanced_response = 3000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = print_basic() + keyword + '\n' + print_advanced() + str(advanced_option) + '\n' + print_advanced_option(advanced_option) + str(advanced_response) + "\n\nHere are your articles: [['Spain national beach soccer team', 'jack johnson', 1233458894, 1526], ['Steven Cohen (soccer)', 'Mack Johnson', 1237669593, 2117]]\n"

        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_search_no_advanced(self, input_mock):
        keyword = 'singles'
        advanced_option = 7

        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n\nHere are your articles: [['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['2006 in music', 'Jack Johnson', 1171547747, 105280]]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_integration_test_article_length(self, input_mock):
        keyword = 'dog'
        advanced_option = 1
        advanced_response = 15000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: [['Black dog (ghost)', 'Pegship', 1220471117, 14746], ['Mexican dog-faced bat', 'Mack Johnson', 1255316429, 1138], ['Guide dog', 'Jack Johnson', 1165601603, 7339]]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_integration_test_unique_authors(self, input_mock):
        keyword = 'music'
        advanced_option = 2
        advanced_response = 5

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: [['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], ['French pop music', 'Mack Johnson', 1172208041, 5569], ['1922 in music', 'Gary King', 1242717698, 11576], ['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], ['2009 in music', 'RussBot', 1235133583, 69451]]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_most_recent_article(self, input_mock):
        keyword = 'team'
        advanced_option = 3

        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n\nHere are your articles: [\"Wake Forest Demon Deacons men's soccer\", 'Burna Boy', 1260577388, 26745]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_integration_test_favorite_author(self, input_mock):
        keyword = 'music'
        advanced_option = 4
        advanced_response = 'burna boy'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: [" \
            "['List of Canadian musicians', 'Jack Johnson', 1181623340, 21023], " \
            "['French pop music', 'Mack Johnson', 1172208041, 5569], " \
            "['Noise (music)', 'jack johnson', 1194207604, 15641], " \
            "['1922 in music', 'Gary King', 1242717698, 11576], " \
            "['1986 in music', 'jack johnson', 1048918054, 6632], " \
            "['Kevin Cadogan', 'Mr Jake', 1144136316, 3917], " \
            "['2009 in music', 'RussBot', 1235133583, 69451], " \
            "['Rock music', 'Mack Johnson', 1258069053, 119498], " \
            "['Lights (musician)', 'Burna Boy', 1213914297, 5898], " \
            "['Tim Arnold (musician)', 'jack johnson', 1181480380, 4551], " \
            "['Old-time music', 'Nihonjoe', 1124771619, 12755], " \
            "['Arabic music', 'RussBot', 1209417864, 25114], " \
            "['Joe Becker (musician)', 'Nihonjoe', 1203234507, 5842], " \
            "['Richard Wright (musician)', 'RussBot', 1189536295, 16185], " \
            "['Voice classification in non-classical music', 'RussBot', 1198092852, 11280], " \
            "['1936 in music', 'RussBot', 1243745950, 23417], " \
            "['1962 in country music', 'Mack Johnson', 1249862464, 7954], " \
            "['List of dystopian music, TV programs, and games', 'Bearcat', 1165317338, 13458], " \
            "['Steve Perry (musician)', 'Nihonjoe', 1254812045, 22204], " \
            "['David Gray (musician)', 'jack johnson', 1159841492, 7203], " \
            "['Alex Turner (musician)', 'jack johnson', 1187010135, 9718], " \
            "['List of gospel musicians', 'Nihonjoe', 1197658845, 3805], " \
            "['Indian classical music', 'Burna Boy', 1222543238, 9503], " \
            "['1996 in music', 'Nihonjoe', 1148585201, 21688], " \
            "['Traditional Thai musical instruments', 'Jack Johnson', 1191830919, 6775], " \
            "['2006 in music', 'Jack Johnson', 1171547747, 105280], " \
            "['Tony Kaye (musician)', 'Burna Boy', 1141489894, 8419], " \
            "['Texture (music)', 'Bearcat', 1161070178, 3626], " \
            "['2007 in music', 'Bearcat', 1169248845, 45652], " \
            "['2008 in music', 'Burna Boy', 1217641857, 107605]" \
            "]\nYour favorite author is in the returned articles!\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_integration_test_title_and_author(self, input_mock):
        keyword = 'dance'
        advanced_option = 5

        output = get_print(input_mock, [keyword, advanced_option])
        expected = "{}{}\n{}{}\n\nHere are your articles: [('List of Canadian musicians', 'Jack Johnson'), ('2009 in music', 'RussBot'), ('Old-time music', 'Nihonjoe'), ('1936 in music', 'RussBot'), ('Indian classical music', 'Burna Boy')]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option))

        self.maxDiff = None
        self.assertEqual(output, expected)
    
    @patch('builtins.input')
    def test_integration_test_refine_search(self, input_mock):
        keyword = 'music'
        advanced_option = 6
        advanced_response = 'singles'

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nHere are your articles: [['2009 in music', 'RussBot', 1235133583, 69451], ['Rock music', 'Mack Johnson', 1258069053, 119498], ['2006 in music', 'Jack Johnson', 1171547747, 105280]]\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_invalid_keyword(self, input_mock):
        keyword = 'Asake'
        advanced_option = 1
        advanced_response = 15000

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nNo articles found\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)

    @patch('builtins.input')
    def test_integration_test_empty_string(self, input_mock):
        keyword = ''
        advanced_option = 2
        advanced_response = 3

        output = get_print(input_mock, [keyword, advanced_option, advanced_response])
        expected = "{}{}\n{}{}\n{}{}\n\nNo articles found\n".format(print_basic(), keyword, print_advanced(), str(advanced_option), print_advanced_option(advanced_option), str(advanced_response))

        self.maxDiff = None
        self.assertEqual(output, expected)



# Write tests above this line. Do not remove.
if __name__ == "__main__":
    main()
