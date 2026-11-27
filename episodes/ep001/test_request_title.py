import unittest

from request_title import normalize_title


class RequestTitleTests(unittest.TestCase):
    def test_trims_outer_spaces(self):
        self.assertEqual(normalize_title("  Reset demo access  "), "Reset demo access")

    def test_rejects_blank_title(self):
        with self.assertRaises(ValueError):
            normalize_title("   ")

    def test_rejects_tab_and_newline(self):
        with self.assertRaises(ValueError):
            normalize_title("\t\n")

    def test_preserves_internal_spaces(self):
        self.assertEqual(normalize_title("Fix  demo link"), "Fix  demo link")
