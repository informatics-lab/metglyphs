import unittest


class TestGlyph(unittest.TestCase):
    """Test the Glpyh class."""

    def setUp(self):
        pass

    def test_construct(self):
        from metglyphs import Glyph
        glyph = Glyph(None)
        self.assertEqual(type(glyph), Glyph)
