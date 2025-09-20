import pytest
import os
import logging
from nanovm_desktop import Sandbox

# Set up timeout and logger
timeout = 60
logger = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def sandbox(debug):
    # Create a new sandbox instance for each test
    sandbox = Sandbox.create(timeout=timeout)

    try:
        yield sandbox
    finally:
        # Ensure proper cleanup
        try:
            sandbox.kill()
        except Exception as e:
            if not debug:
                logger.warning(
                    f"Failed to kill sandbox — this is expected if the test runs with local envd. Error: {e}"
                )


@pytest.fixture
def debug():
    # Determine if debugging is enabled
    return os.getenv("NANOVM_DEBUG") is not None


@pytest.fixture(autouse=True)
def skip_by_debug(request, debug):
    # Skip test if NANOVM_DEBUG is set
    if request.node.get_closest_marker("skip_debug"):
        if debug:
            pytest.skip("skipped because NANOVM_DEBUG is set")
