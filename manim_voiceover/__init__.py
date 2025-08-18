from manim_voiceover.tracker import VoiceoverTracker
from manim_voiceover.voiceover_scene import VoiceoverScene

import pkg_resources

try:
    __version__: str = pkg_resources.get_distribution(__name__).version
except pkg_resources.DistributionNotFound:
    __version__ = "0.0.0"
