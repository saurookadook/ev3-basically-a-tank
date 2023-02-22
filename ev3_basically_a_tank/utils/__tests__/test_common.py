import io
import sys
from unittest.mock import call, patch

from ...utils import debug_logger, safe_init_port


def test_debug_logger():
    # with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
    with patch("builtins.print") as mock_print:
        debug_logger("can i haz test?", end="\n\n")
        mock_print.assert_has_calls(
            [call("can i haz test?", file=sys.stderr, end="\n\n")]
        )
