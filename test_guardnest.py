# test_guardnest.py
"""
Tests for GuardNest module.
"""

import unittest
from guardnest import GuardNest

class TestGuardNest(unittest.TestCase):
    """Test cases for GuardNest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GuardNest()
        self.assertIsInstance(instance, GuardNest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GuardNest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
