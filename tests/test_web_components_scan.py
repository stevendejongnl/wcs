from unittest import TestCase



class TestWebComponentsScan(TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.wcs = WebComponentsScan()

    def test_that_file_not_found(self) -> None:
        self.assertRaises(
            FileNotFoundError, self.wcs.get_custom_element_tags, manifest_file_path="./non-existing-manifest-file.json"
        )

    def test_retrieving_manifest_file_list_all_custom_element_tags(self) -> None:
        tags = self.wcs.get_custom_element_tags(manifest_file_path="../custom-elements.json")

        self.assertEqual(['henk-the-men', 'henks-side-chick', 'side-chick-tina'], tags)

    def test_that_path_with_non_html_files_returns_empty_list(self) -> None:
        files = self.wcs.list_html_files(path='./non-existing-directory')

        self.assertEqual([], files)

    def test_that_path_with_html_files_returns_html_paths_in_list(self) -> None:
        files = self.wcs.list_html_files(path='../example-components/implementations')

        self.assertEqual([
            '../example-components/implementations/index.html',
            '../example-components/implementations/henk.html',
            '../example-components/implementations/tina.html',
        ], files)

    def test_searching_a_custom_element_in_html(self) -> None:
        components_dict = self.wcs.search_for_components_in_html_file(
            path='../example-components/implementations/tina.html',
            tags=['side-chick-tina']
        )

        self.assertDictEqual({
            'side-chick-tina': [
                '../example-components/implementations/tina.html:13'
            ]
        }, components_dict)

    def test_full_scan(self) -> None:
        scan_results = self.wcs.scan_html(
            path='../example-components/implementations',
            manifest='../custom-elements.json'
        )

        self.assertEqual([
            '../example-components/implementations/index.html:13',
            '../example-components/implementations/henk.html:13'
        ], scan_results['henk-the-men'])

        self.assertEqual([
            '../example-components/implementations/index.html:14',
            '../example-components/implementations/henk.html:14'
        ], scan_results['henks-side-chick'])

        self.assertEqual([
            '../example-components/implementations/index.html:15',
            '../example-components/implementations/tina.html:13'
        ], scan_results['side-chick-tina'])
