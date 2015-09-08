# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, absolute_import

import unittest
from ..database import Database
from ...text import Text
from pprint import pprint

# the name of the test index
TEST_INDEX = 'test'


def first():
    text = Text('Mees, keda seal kohtasime, oli tuttav ja teretas meid.')
    text.tag_clauses().tag_named_entities()
    return text


def second():
    text = Text(
        'Üle oja jõele. Läbi oru mäele. Usjas kaslane ründas künklikul maanteel tünjat Tallinnfilmi režissööri.')
    text.tag_clauses().tag_named_entities()
    return text


class InsertTest(unittest.TestCase):

    def setUp(self):
        self.db = Database(TEST_INDEX)
        self.db.delete_index()

    def test_insert_default_ids(self):
        # see pole warningu eemaldamiseks sobiv viis, sest warning lihtsalt peidetakse. Pigem las ta olla nähtav.
        # TODO: delete me: warnings.simplefilter("ignore")
        self.db.refresh()
        db = self.db

        # insert the documents
        id_first = db.insert(first())
        id_second = db.insert(second())

        # check the count
        self.assertEqual(2, db.count())

        # check the document retrieval
        self.assertDictEqual(first(), db.get(id_first))
        self.assertDictEqual(second(), db.get(id_second))


class BulkInsertTest(unittest.TestCase):

    def setUp(self):
        self.db = Database(TEST_INDEX)
        self.db.delete()

    def test_bulk_insert(self):
        db = self.db
        db.refresh()

        # parem on tõsta first ja second InsertTestist lihtsalt välja (tegin juba selle ära).
        # uue instantsi tegemine on ebavajalik.
        # TODO: delete me.
        # insert many (bulk) into db bulk_test
        # it = InsertTest()
        # text_lists = [it.first, it.second]

        text_lists = [first(), second()]
        id_bulk = db.bulk_insert(text_lists)

        # TODO: missing actual assertions


class SearchTest(unittest.TestCase):

    def test_search_keyword_documents(self):
        # TODO: move Database setup and initialization to def setUp() method
        self.db = Database(TEST_INDEX)
        keywords = ["aegna"]
        search = Database.query_documents(self.db, query=keywords)

        # TODO: missing actual assertions


    # TODO: add a test that uses layer argument

