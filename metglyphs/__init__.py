"""A library for converting weather codes to symbols."""

import os.path
from io import BytesIO

import cairosvg
import imageio

from .glyphs import WMO_GLYPH_LOOKUP, DEFAULT_GLYPHS
from .codes import DATAPOINT_TO_WMO_LOOKUP, DARKSKY_TO_WMO_LOOKUP


class GlyphSet():
    """A set of glyphs."""

    def __init__(self, name=None, recolor=None):
        """Load the lookup tables and cache all svgs into memory."""
        self.name = name or DEFAULT_GLYPHS
        self.glyph_set = WMO_GLYPH_LOOKUP[self.name]
        self.recolor = recolor
        self.cache = {}
        for wmo_code in self.glyph_set.keys():
            self._load_svg(wmo_code)

    def _repr_html_(self):
        """Return all the unique glyphs in the set to be used as an inline html object."""
        response = ""
        for _, svg in self.cache.items():
            response += "{}".format(Glyph(svg, recolor=self.recolor)._repr_html_())
        return response

    def _load_svg(self, wmo_code):
        """Load the svg image for a given WMO code to a bytestring from the glyph set."""
        try:
            svg_path = os.path.join(os.path.dirname(__file__), "assets", self.name, self.glyph_set[wmo_code])
        except KeyError:
            svg_path = os.path.join(os.path.dirname(__file__), "assets", "missing.svg")
        if svg_path in self.cache:
            return self.cache[svg_path]
        else:
            with open(svg_path, 'rb') as svg:
                self.cache[svg_path] = svg.read()
                return self.cache[svg_path]

    def datapoint_to_wmo(self, datapoint_code):
        """Convert a datapoint code to a WMO code."""
        return DATAPOINT_TO_WMO_LOOKUP[str(datapoint_code)]

    def darksky_to_wmo(self, darksky_code):
        """Convert a darksky code to a WMO code."""
        return DARKSKY_TO_WMO_LOOKUP[str(darksky_code)]

    def get_glyph(self, wmo_code=None, datapoint_code=None, darksky_code=None, recolor=None):
        """Return a Glyph for a given weather code."""
        if wmo_code is not None:
            return Glyph(self._load_svg(wmo_code), recolor=recolor or self.recolor)

        if datapoint_code is not None:
            return Glyph(self._load_svg(self.datapoint_to_wmo(datapoint_code)), recolor=recolor or self.recolor)

        if darksky_code is not None:
            return Glyph(self._load_svg(self.darksky_to_wmo(darksky_code)), recolor=recolor or self.recolor)

        raise Exception("You must specify a valid type code")


class Glyph():
    """An individual glyph/symbol/icon with methods to convert between types."""

    def __init__(self, svg, recolor=None):
        """The init method."""
        self.svg = svg
        if recolor:
            decoded_svg = self.svg.decode('utf-8')
            for old_color, new_color in recolor.items():
                decoded_svg = decoded_svg.replace(old_color, new_color)
            self.svg = decoded_svg.encode('utf-8')

    def _repr_html_(self):
        """Return the raw svg object so that is can be used as an inline html object."""
        return "<div style='width:40px;display:inline-block;'>{}</div>".format(self.svg.decode("utf-8"))

    def to_svg(self):
        """Return a SVG bytestring."""
        return self.svg

    def to_png(self, scale=1):
        """Convert to a PNG bytestring."""
        return cairosvg.svg2png(bytestring=self.svg,
                                scale=scale)

    def to_np_array(self, scale=1):
        """Convert to a numpy array of RGB values."""
        return imageio.imread(BytesIO(self.to_png(scale=scale)))
