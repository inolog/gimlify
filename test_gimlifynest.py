# test_guardnest.py
"""
Tests for Gimlify module.
"""

import unittest
from guardnest import GuardNest
 
class TestGuardNest(unittest.TestCase):
    """Test cases for Gimlify class."""
    
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
