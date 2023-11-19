'''
Module for testing ds_message_protocol
'''
# test_ds_message_protocol.py

# Transclude function code for assignment 5 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

import unittest
import ds_protocol


class DsProtocolTest(unittest.TestCase):
    '''
    Runs test cases using unnittest
    '''
    def test_1_ds_message(self):
        '''
        Test 1
        '''
        test = """{"response": {"type": "ok", "message": "Direct message sent"}}"""
        testing = ds_protocol.directmessage(test)
        assert testing == "Direct message sent"

    def test_2_ds_message(self):
        '''
        Test 2
        '''
        test = """{"response": {"type": "ok", "messages": [{"message": "hi world hi hi", "from": "assignmentiuahdw5", "timestamp": "1679039478.49371"}]}}"""
        testing = ds_protocol.directmessage(test)
        assert testing is not False

    def test_3_ds_message(self):
        '''
        Test 3
        '''
        test = """{"response": {"type": "error", "message": "error"}}"""
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_4_ds_message(self):
        '''
        Test 4
        '''
        test = """{"resppwodakwpo "error"}}"""
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_5_ds_message(self):
        '''
        Test 5
        '''
        test = " "
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_6_ds_message(self):
        '''
        Test 6
        '''
        test = "ok"
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_7_ds_message(self):
        '''
        Test 7
        '''
        test = """{"response": {"type": "ok", "hello": "error"}}"""
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_8_ds_message(self):
        '''
        Test 8
        '''
        test = """{"response": {"type": "ok", "message": }}"""
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_9_ds_message(self):
        '''
        Test 9
        '''
        test = """{"response": {"type": "ok", "message": hi}}"""
        testing = ds_protocol.directmessage(test)
        assert testing is False

    def test_10_ds_message(self):
        '''
        Test 10
        '''
        test = """{"response": {"type": , "message": hi}}"""
        testing = ds_protocol.directmessage(test)
        assert testing is False

if __name__ == "__main__":
    unittest.main()
