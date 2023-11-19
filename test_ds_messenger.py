'''
Module for testing ds_messenger.py
'''
# test_ds_messenger.py

# Transclude function code for assignment 5 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Helen Chau
# chauh4@uci.edu
# 84334175

import ds_messenger as ds
import unittest

class TestDsMessenger(unittest.TestCase):
    '''
    Runs test using unnittest
    '''
    def test_1_messenger(self):
        '''
        Test 1
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101",
                                         username="assignmentiuahdw5",
                                         password="assignment5")
        sending = direct_test.send("must slee123p", recipient="assignmentiuahdw5")
        assert sending is True

    def test_2_messenger(self):
        '''
        Test 2
        '''
        direct_test = ds.DirectMessenger(dsuserver="16101",
                                         username="assignmentiuahdw5",
                                         password="assignment5")
        sending = direct_test.send("must slee123p", recipient="assignmentiuahdw5")
        assert sending is False

    def test_3_messenger(self):
        '''
        Test 3
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101",
                                         username="assignmentiuahdw5",
                                         password="ssi5")
        sending = direct_test.send("must slee123p", recipient="assignmentiuahdw5")
        assert sending is False

    def test_4_messenger(self):
        '''
        Test 4
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101",
                                         username="assignmentiuahdw5",
                                         password="assignment5")
        sending = direct_test.retrieve_all()
        assert sending is not False

    def test_5_messenger(self):
        '''
        Test 5
        '''
        direct_test = ds.DirectMessenger(dsuserver="16801",
                                         username="assignmentiuahdw5",
                                         password="assignment5")
        sending = direct_test.retrieve_all()
        assert sending is False

    def test_6_messenger(self):
        '''
        Test 6
        '''
        direct_test = ds.DirectMessenger(dsuserver="16801",
                                         username="assignmentiuahdw5",
                                         password="asnt5")
        sending = direct_test.retrieve_all()
        assert sending is False

    def test_7_messenger(self):
        '''
        Test 7
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101", 
                                        username="assignmentiuahdw5",
                                        password="assignment5")
        sending = direct_test.retrieve_new()
        assert sending is not False

    def test_8_messenger(self):
        '''
        Test 8
        '''
        direct_test = ds.DirectMessenger(dsuserver="1681",
                                        username="assignmentiuahdw5",
                                        password="ant5")
        sending = direct_test.retrieve_new()
        assert sending is False

    def test_9_messenger(self):
        '''
        Test 9
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101",
                                         username="assignmentiuahdw5",
                                         password="ant5")
        sending = direct_test.retrieve_new()
        assert sending is False

    def test_10_messenger(self):
        '''
        Test 10
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101")
        sending = direct_test.retrieve_new()
        assert sending is False

    def test_11_messenger(self):
        '''
        Test 11
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101")
        sending = direct_test.retrieve_all()
        assert sending is False

    def test_12_messenger(self):
        '''
        Test 12
        '''
        direct_test = ds.DirectMessenger(dsuserver="168.235.86.101")
        sending = direct_test.send("must slee123p", recipient="assignmentiuahdw5")
        assert sending is False

if __name__ == "__main__":
    unittest.main()
